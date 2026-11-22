#!/usr/bin/env python3
"""Ofis panosu: ofis/isler/* iş dosyalarından kanban görünümü üretir.

Kullanım: python3 ofis/pano/pano.py [--port 4320]
Yalnız 127.0.0.1'de dinler, salt okunurdur. Bağımlılık yok (standart kütüphane).

Veri kaynakları (her istekte yeniden okunur):
- 00-talep.md   → başlık, tür, dal, "Akış durumu" tablosu
- 01-analiz.md  → kabul kriteri (KK) sayısı
- 06-test-raporu.md → KK bazında son test sonucu
- 07-inceleme.md → inceleme sonucu
- ofis/.canli.json → şu an çalışan ajanlar (.claude/hooks/ofis_canli.py yazar)
"""
import argparse
import json
import re
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

KOK = Path(__file__).resolve().parents[2]
ISLER = KOK / "ofis" / "isler"
CANLI = KOK / "ofis" / ".canli.json"
SAYFA = Path(__file__).with_name("pano.html")

# Pano sütunları ve her sütuna düşen akış adımları (00-talep.md tablosundaki adım adları).
SUTUNLAR = [
    ("analiz", "Analiz", ["Analiz", "İş Birimi incelemesi"]),
    ("onay1", "◆ Onay 1", ["◆ Onay 1"]),
    ("tasarim", "Tasarım", ["Tasarım"]),
    ("gorev", "Görev dağılımı", ["Görev dağılımı"]),
    ("gelistirme", "Geliştirme", ["Geliştirme"]),
    ("test", "Test", ["Test"]),
    ("inceleme", "İnceleme", ["İnceleme"]),
    ("onay2", "◆ Onay 2", ["◆ Onay 2"]),
    ("kapanis", "Kapanış", ["Kapanış"]),
]
BITMIS = {"tamam", "gerekmiyor"}
CANLI_SINIR = 3 * 3600  # sn


def satir_hucreleri(satir):
    return [h.strip() for h in satir.strip().strip("|").split("|")]


def akis_tablosu(metin):
    """'## Akış durumu' altındaki tabloyu [(adım, durum, not)] olarak döner."""
    bolum = re.split(r"^## Akış durumu\s*$", metin, flags=re.M)
    if len(bolum) < 2:
        return []
    adimlar = []
    for satir in bolum[1].splitlines():
        if satir.startswith("## "):
            break
        if not satir.startswith("|") or set(satir.replace("|", "").strip()) <= set("-: "):
            continue
        h = satir_hucreleri(satir)
        if len(h) < 2 or h[0] == "Adım":
            continue
        adimlar.append((h[0], h[1].lower(), h[2] if len(h) > 2 else ""))
    return adimlar


def alan(metin, ad):
    m = re.search(rf"\*\*{re.escape(ad)}:\*\*\s*(.+)", metin)
    return m.group(1).strip() if m else ""


def kk_sayisi(klasor):
    try:
        metin = (klasor / "01-analiz.md").read_text()
    except OSError:
        return 0
    return sum(
        1
        for s in metin.splitlines()
        if re.match(r"\s*-\s*\*\*KK-\d+:\*\*", s) and "iptal" not in s.lower() and "<kriter>" not in s
    )


def test_sonuclari(klasor):
    """KK başına son sonuç: {'KK-1': 'geçti', ...}"""
    try:
        metin = (klasor / "06-test-raporu.md").read_text()
    except OSError:
        return {}
    sonuc = {}
    for s in metin.splitlines():
        if not s.startswith("|"):
            continue
        h = satir_hucreleri(s)
        if h and re.fullmatch(r"KK-\d+", h[0]):
            durum = next((x.lower() for x in h if x.lower() in ("geçti", "kaldı")), None)
            if durum:
                sonuc[h[0]] = durum
    return sonuc


def inceleme_sonucu(klasor):
    try:
        metin = (klasor / "07-inceleme.md").read_text()
    except OSError:
        return ""
    bolum = re.split(r"^## Sonuç\s*$", metin, flags=re.M)
    if len(bolum) < 2:
        return ""
    for s in bolum[1].splitlines():
        s = s.strip()
        if s in ("onaylandı", "düzeltme gerekli"):
            return s
    return ""


def canli_ajanlar():
    try:
        d = json.loads(CANLI.read_text())
    except (OSError, ValueError):
        return []
    simdi = time.time()
    ajanlar = [
        {"ajan": v["ajan"], "is": v["is"], "basladi": v["basladi"], "kesin": True}
        for v in d.get("aktif", {}).values()
        if simdi - v.get("basladi", 0) < CANLI_SINIR
    ]
    ajanlar += [
        {"ajan": b["ajan"], "is": b["is"], "basladi": b["zaman"], "kesin": False}
        for b in d.get("bekleyen", [])
        if simdi - b.get("zaman", 0) < CANLI_SINIR
    ]
    return ajanlar


def is_karti(klasor, canli):
    try:
        metin = (klasor / "00-talep.md").read_text()
    except OSError:
        return None
    adimlar = akis_tablosu(metin)
    durumlar = {a: d for a, d, _ in adimlar}
    notlar = {a: n for a, _, n in adimlar}

    sutun, adim, adim_durum = "kapanis", "Kapanış", "tamam"
    bitti = True
    for anahtar, _, sutun_adimlari in SUTUNLAR:
        for a in sutun_adimlari:
            d = durumlar.get(a)
            if d is not None and d not in BITMIS:
                sutun, adim, adim_durum, bitti = anahtar, a, d, False
                break
        if not bitti:
            break

    kod_ad = klasor.name
    baslik = re.search(r"^# 00 — Talep:\s*(.+)$", metin, flags=re.M)
    tur = alan(metin, "İş türü").split("|")[0].strip()
    if "|" in alan(metin, "İş türü"):
        tur = ""  # şablon değiştirilmemiş
    testler = test_sonuclari(klasor)
    gecen = sum(1 for v in testler.values() if v == "geçti")
    kalan = sum(1 for v in testler.values() if v == "kaldı")
    son_degisiklik = max((f.stat().st_mtime for f in klasor.glob("*.md")), default=0)

    return {
        "kod": kod_ad,
        "baslik": baslik.group(1).strip() if baslik else kod_ad,
        "tur": tur,
        "yol": alan(metin, "Yol"),
        "dal": alan(metin, "Dal adı").strip("`"),
        "sutun": sutun,
        "adim": adim,
        "durum": "tamam" if bitti else adim_durum,
        "not": "" if bitti else notlar.get(adim, ""),
        "onay_bekliyor": (not bitti) and adim.startswith("◆") and adim_durum in ("bekliyor", "sürüyor"),
        "kk": kk_sayisi(klasor),
        "kk_gecen": gecen,
        "kk_kalan": kalan,
        "inceleme": inceleme_sonucu(klasor),
        "son_degisiklik": son_degisiklik,
        "dosya": str(klasor / "00-talep.md"),
        "canli": [a for a in canli if Path(a["is"]).name == klasor.name],
    }


def pano_verisi():
    canli = canli_ajanlar()
    kartlar = []
    if ISLER.is_dir():
        for klasor in sorted(ISLER.iterdir()):
            if klasor.is_dir() and (klasor / "00-talep.md").exists():
                kart = is_karti(klasor, canli)
                if kart:
                    kartlar.append(kart)
    return {
        "zaman": time.time(),
        "sutunlar": [{"anahtar": a, "ad": ad} for a, ad, _ in SUTUNLAR],
        "kartlar": kartlar,
        "canli_sayisi": len(canli),
    }


class Isleyici(BaseHTTPRequestHandler):
    def gonder(self, kod, tur, govde):
        self.send_response(kod)
        self.send_header("Content-Type", tur)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(govde)))
        self.end_headers()
        self.wfile.write(govde)

    def do_GET(self):  # noqa: N802
        if self.path in ("/", "/index.html"):
            self.gonder(200, "text/html; charset=utf-8", SAYFA.read_bytes())
        elif self.path == "/api/pano":
            govde = json.dumps(pano_verisi(), ensure_ascii=False).encode()
            self.gonder(200, "application/json; charset=utf-8", govde)
        elif self.path == "/saglik":
            self.gonder(200, "text/plain; charset=utf-8", b"ok")
        else:
            self.gonder(404, "text/plain; charset=utf-8", b"bulunamadi")

    def log_message(self, *args):
        pass


def main():
    ap = argparse.ArgumentParser(description="Sustable ofis panosu")
    ap.add_argument("--port", type=int, default=4320)
    args = ap.parse_args()
    sunucu = ThreadingHTTPServer(("127.0.0.1", args.port), Isleyici)
    print(f"Ofis panosu: http://127.0.0.1:{args.port}/", flush=True)
    sunucu.serve_forever()


if __name__ == "__main__":
    main()
