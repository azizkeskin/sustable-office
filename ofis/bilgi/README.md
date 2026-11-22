# İş Birimi Bilgi Tabanı

İş Birimi ajanının başvurduğu standart özetleri ve kontrol listeleri. Standart metinleri kopyalanmaz;
yalnız kendi özetlerimiz, kontrol listelerimiz ve Sustable'daki karşılıkları tutulur.

Her dosyanın yapısı:
1. Kapsam: standart neyi düzenler, kimler için zorunlu.
2. Kontrol listesi: zorunlu açıklamalar, hesap yöntemi, birimler, dönem.
3. Sık yapılan hatalar.
4. Sustable karşılığı: ilgili ekran (`platform/<app>`), uç ve kod kuralı (`sustable-backend/.claude/rules/<dosya>.md`).

| Dosya | Konu | Kod kuralı | Durum |
|---|---|---|---|
| `tsrs.md` | TSRS 1 ve TSRS 2 (iklimle ilgili açıklamalar) | `esg-tsrs.md` | kaynaklarla teyitli (2026-11-22) |
| `pcaf.md` | PCAF finanse edilen emisyonlar, veri kalitesi puanı | `pcaf.md` | kaynaklarla teyitli (2026-11-22) |
| `gri.md` | GRI standartları (GRI 101/102/103, sektör V1.1) | `esg-tsrs.md` | ilk sürüm, 11 madde doğrulanmalı |
| `iso14064.md` | ISO 14064-1 kurumsal sera gazı envanteri | `iso14064.md` | ilk sürüm, lisanslı metinle teyit gerekir |
| `ghg-protokolu.md` | GHG Protokolü, Kapsam 1/2/3 | `emission-calculator.md` | ilk sürüm, 12 madde doğrulanmalı |
| `cevre-yonetimi.md` | Atık, su, EMS | `ems-waste.md`, `water.md` | sonra |

## Bakım

- Her dosyanın üst notunda "Son gözden geçirme" tarihi, sonunda kaynaklar ve sürümleri bulunur.
- İş Birimi bir işte eksik ya da eskimiş bilgi görürse `02-is-birimi.md` sonuna "Bilgi tabanı notu" yazar; Direktör kapanışta bunları kullanıcıya güncelleme önerisi olarak getirir.
- "doğrulanmalı" işaretli maddeler kullanılmadan önce resmî kaynaktan teyit edilir; teyit edilince işaret kaldırılır ve kaynak eklenir.
