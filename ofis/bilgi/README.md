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
| `tsrs.md` | TSRS 1 ve TSRS 2 (iklimle ilgili açıklamalar) | `esg-tsrs.md` | ilk sürüm |
| `pcaf.md` | PCAF finanse edilen emisyonlar, veri kalitesi puanı | `pcaf.md` | ilk sürüm |
| `gri.md` | GRI standartları | `esg-tsrs.md` | sonra |
| `iso14064.md` | ISO 14064-1 kurumsal sera gazı envanteri | `iso14064.md` | sonra |
| `ghg-protokolu.md` | GHG Protokolü, Kapsam 1/2/3 | `emission-calculator.md` | sonra |
| `cevre-yonetimi.md` | Atık, su, EMS | `ems-waste.md`, `water.md` | sonra |
