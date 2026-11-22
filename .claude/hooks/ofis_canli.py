#!/usr/bin/env python3
"""Ofis panosu için canlı ajan durumu hook'u.

Olaylar:
- PreToolUse (Agent|Task): istemde "İş klasörü: <yol>" geçen bir ofis ajanı çağrısını "bekleyen" listesine yazar.
- SubagentStart: aynı türdeki en eski bekleyen kaydı agent_id ile "aktif" yapar.
- SubagentStop: aktif kaydı kaldırır ve işin `.canli-gecmis.jsonl` dosyasına ekler.

Durum dosyası: <ofis kökü>/ofis/.canli.json (git'e girmez). Hook hiçbir zaman Claude'u durdurmaz:
her hata sessizce yutulur ve çıkış kodu 0'dır.
"""
import fcntl
import json
import os
import re
import sys
import time
from pathlib import Path

KOK = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
DURUM = KOK / "ofis" / ".canli.json"
KILIT = KOK / "ofis" / ".canli.lock"
IS_KLASORU = re.compile(r"İş klasörü:\s*`?([^\s`]+)`?")
BEKLEME_SINIRI = 120  # sn: SubagentStart bu sürede gelmezse bekleyen kayıt eşleştirilmez
ESKIME = 6 * 3600  # sn: bu süreyi aşan kayıtlar temizlenir


def is_klasoru(prompt):
    m = IS_KLASORU.search(prompt or "")
    if not m:
        return None
    yol = Path(m.group(1).rstrip("/.,"))
    if not yol.is_absolute():
        yol = KOK / yol
    try:
        yol = yol.resolve()
        yol.relative_to((KOK / "ofis" / "isler").resolve())
    except (ValueError, OSError):
        return None
    return yol if yol.is_dir() else None


def oku():
    try:
        d = json.loads(DURUM.read_text())
    except (OSError, ValueError):
        d = {}
    d.setdefault("bekleyen", [])
    d.setdefault("aktif", {})
    simdi = time.time()
    d["bekleyen"] = [b for b in d["bekleyen"] if simdi - b.get("zaman", 0) < ESKIME]
    d["aktif"] = {k: v for k, v in d["aktif"].items() if simdi - v.get("basladi", 0) < ESKIME}
    return d


def yaz(d):
    gecici = DURUM.with_suffix(".tmp")
    gecici.write_text(json.dumps(d, ensure_ascii=False, indent=1))
    gecici.replace(DURUM)


def gecmise_ekle(kayit, bitti):
    try:
        dosya = Path(kayit["is"]) / ".canli-gecmis.jsonl"
        satir = {"ajan": kayit["ajan"], "basladi": kayit.get("basladi"), "bitti": bitti}
        with dosya.open("a") as f:
            f.write(json.dumps(satir, ensure_ascii=False) + "\n")
    except (OSError, KeyError):
        pass


def isle(p):
    olay = p.get("hook_event_name") or ""
    simdi = time.time()

    if olay == "PreToolUse":
        girdi = p.get("tool_input") or {}
        ajan = girdi.get("subagent_type") or ""
        yol = is_klasoru(girdi.get("prompt"))
        if not ajan or not yol:
            return
        d = oku()
        d["bekleyen"].append({"ajan": ajan, "is": str(yol), "zaman": simdi})
        yaz(d)

    elif olay == "SubagentStart":
        ajan = p.get("agent_type") or ""
        kimlik = p.get("agent_id") or ""
        if not ajan or not kimlik:
            return
        d = oku()
        for i, b in enumerate(d["bekleyen"]):
            if b["ajan"] == ajan and simdi - b["zaman"] < BEKLEME_SINIRI:
                d["bekleyen"].pop(i)
                d["aktif"][kimlik] = {"ajan": ajan, "is": b["is"], "basladi": simdi}
                yaz(d)
                return

    elif olay == "SubagentStop":
        kimlik = p.get("agent_id") or ""
        ajan = p.get("agent_type") or ""
        d = oku()
        kayit = d["aktif"].pop(kimlik, None)
        if kayit is None and ajan:
            # SubagentStart gelmediyse (eski sürüm) bekleyen listesindeki en eski eşleşmeyi kapat.
            for i, b in enumerate(d["bekleyen"]):
                if b["ajan"] == ajan:
                    b = d["bekleyen"].pop(i)
                    kayit = {"ajan": ajan, "is": b["is"], "basladi": b["zaman"]}
                    break
        if kayit is None:
            return
        yaz(d)
        gecmise_ekle(kayit, simdi)


def main():
    try:
        p = json.load(sys.stdin)
    except ValueError:
        return 0
    try:
        DURUM.parent.mkdir(parents=True, exist_ok=True)
        with open(KILIT, "w") as kilit:
            fcntl.flock(kilit, fcntl.LOCK_EX)
            isle(p)
    except Exception:  # noqa: BLE001 — hook asla oturumu bozmamalı
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
