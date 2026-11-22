# 04 — Görev Dağılımı: <İş kodu> <Kısa ad>

Yazan: Proje Yöneticisi · Dayanak: `01-analiz.md`, `03-tasarim.md`

## Dal
`feature/<iş-kodu>-<kisa-ad>` — her depoda yerel `develmaster`'dan.

## API sözleşmesi
### `<METOT> /api/v1/<yol>`
- **Yetki:** rol sabiti, `hasAccess*` kontrolü
- **İstek:** (DTO alanları ve türleri)
- **Yanıt:** (`RestResponse` içindeki gövde)
- **Hata kodları:**
- **KK:**

## Görevler
| # | Ajan | Depo | Görev | Bağımlılık | KK |
|---|---|---|---|---|---|
| G-1 | backend-developer | sustable-backend | | — | |
| G-2 | frontend-developer | sustable-frontend | | G-1 sözleşmesi | |

## Paralel çalışma
<Hangi görevler aynı anda yürüyebilir, hangileri bekler.>

## Riskler
- <ör. migration sırası, mevcut veriye etki, performans>
