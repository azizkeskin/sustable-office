#!/usr/bin/env bash
# Ofis iş klasörünü açar ve şablonları kopyalar.
# Kullanım: is_ac.sh <iş-kodu> <kisa-ad>
#   iş-kodu: TECH-512 gibi Linear kodu ya da "-" (IS-yyyymmddSSdd üretilir)
#   kisa-ad: küçük harf, tireli (ör. pcaf-dqs-raporu)
# Çıktı: klasör yolu, dal adı ve worktree kodu (KEY=VALUE satırları).
set -euo pipefail

kok="$(cd "$(dirname "$0")/../../../.." && pwd)"
[ $# -eq 2 ] || { echo "Kullanım: $0 <iş-kodu|-> <kisa-ad>" >&2; exit 1; }

kod="$1"; ad="$2"
[ "$kod" = "-" ] && kod="IS-$(date +%Y%m%d%H%M)"
[[ "$kod" =~ ^[A-Z]+-[0-9]+$ ]] || { echo "Geçersiz iş kodu: $kod (ör. TECH-512)" >&2; exit 1; }
[[ "$ad" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "Geçersiz kısa ad: $ad (küçük harf, rakam ve tire)" >&2; exit 1; }

klasor="$kok/ofis/isler/$kod-$ad"
if [ -e "$klasor" ]; then
  echo "Zaten var: $klasor" >&2; exit 2
fi
mevcut=$(ls -d "$kok/ofis/isler/$kod-"* 2>/dev/null | head -1 || true)
if [ -n "$mevcut" ]; then
  echo "Bu iş kodu için klasör zaten var: $mevcut" >&2; exit 2
fi

mkdir -p "$klasor"
sablon="$kok/ofis/sablonlar"
bugun="$(date +%Y-%m-%d)"
dal="feature/$kod-$ad"
for f in 00-talep 01-analiz; do
  sed -e "s#<İş kodu>#$kod#g" -e "s#<Kısa ad>#$ad#g" -e "s#yyyy-aa-gg#$bugun#g" \
      -e "s#feature/<iş-kodu>-<kisa-ad>#$dal#g" "$sablon/$f.md" > "$klasor/$f.md"
done

echo "KLASOR=$klasor"
echo "DAL=$dal"
echo "WORKTREE_KODU=$(echo "$kod" | tr '[:upper:]' '[:lower:]')"
