# PCAF — Finanse Edilen Emisyonlar

> Kendi özetimizdir; standart metni değildir. "doğrulanmalı" işaretli maddeler kullanılmadan önce
> PCAF'ın güncel standardından kontrol edilmelidir. Son gözden geçirme: 2026-11-22 (ilk sürüm).

## 1. Kapsam
- **Standart:** PCAF (Partnership for Carbon Accounting Financials) — Finans Sektörü için Küresel Sera Gazı
  Muhasebesi ve Raporlama Standardı.
  - **Kısım A:** Finanse edilen emisyonlar (krediler ve yatırımlar) — Sustable'ın `platform/bank` kapsamı.
  - **Kısım B:** Kolaylaştırılan emisyonlar (sermaye piyasası işlemleri).
  - **Kısım C:** Sigortayla ilişkili emisyonlar.
- **Konum:** GHG Protokolü Kapsam 3, **Kategori 15 (Yatırımlar)**'ın finans sektörüne uygulanması.
- **Kimler kullanır:** bankalar, varlık yöneticileri, sigortacılar. TSRS 2 finansal kuruluşlardan finanse edilen
  emisyonların açıklanmasını ister (bkz. `tsrs.md`); PCAF bunun fiilî hesap yöntemidir.
- **Sürüm:** Kısım A'nın son sürümü varlık sınıfı listesini genişletti (fon kullanımına dayalı yapılar, menkul
  kıymetleştirme, alt egemen borç) — sürüm numarası ve tarihi **doğrulanmalı**.

## 2. Temel formül
**Finanse edilen emisyon = Atıf faktörü × Müşterinin (ya da varlığın) emisyonu**

Atıf faktörü = Kuruluşun bakiye tutarı / Müşterinin (ya da varlığın) toplam değeri. Payda varlık sınıfına göre değişir:

| Varlık sınıfı | Payda (atıf faktörü) |
|---|---|
| Borsada işlem gören hisse ve kurumsal tahviller | EVIC (nakit dahil işletme değeri) |
| Ticari krediler ve borsada işlem görmeyen hisse | Borsada işlem görüyorsa EVIC; değilse toplam özkaynak + borç |
| Proje finansmanı | Başlangıçtaki toplam proje özkaynak + borç |
| Ticari gayrimenkul | Başlangıçtaki mülk değeri |
| Konut kredileri | Başlangıçtaki mülk değeri |
| Motorlu taşıt kredileri | Başlangıçtaki araç değeri |
| Devlet borçlanma araçları | Satın alma gücü paritesine göre düzeltilmiş GSYH |
| Alt egemen borç, fon kullanımı, menkul kıymetleştirme | Sınıfa özgü kurallar — **doğrulanmalı** |

- "Paranın izini sür": yalnız bilançodaki tutar sayılır; bakiye tutarı dönem sonu değeridir.
- Atıf faktörü 1'i aşamaz.

## 3. Veri kalitesi puanı (1 en iyi – 5 en zayıf)
Ticari krediler ve hisseler için genel mantık (ayrıntılar varlık sınıfına göre değişir — **doğrulanmalı**):

| Puan | Emisyon verisinin kaynağı |
|---|---|
| 1 | Müşterinin raporladığı, doğrulanmış emisyon |
| 2 | Müşterinin raporladığı doğrulanmamış emisyon, ya da birincil fiziksel faaliyet verisiyle (enerji tüketimi) hesap |
| 3 | Fiziksel faaliyet verisi (üretim miktarı vb.) × emisyon faktörü |
| 4 | Ekonomik faaliyet verisi: ciro × sektörel emisyon yoğunluğu |
| 5 | Varlık/bakiye tutarı × sektörel emisyon yoğunluğu (tahmin) |

- Puan, varlık sınıfı bazında **bakiye ağırlıklı** olarak raporlanır.
- Zamanla puanın iyileşmesi beklenir; kuruluş iyileştirme planını açıklar.

## 4. Kontrol listesi
- [ ] Her kayıt doğru varlık sınıfında mı; atıf faktörü paydası o sınıfa uygun mu?
- [ ] Müşterinin Kapsam 1 ve 2 emisyonları dahil mi; Kapsam 3 sektöre göre aşamalı mı (petrol-gaz, madencilik
      gibi sektörlerde öncelikli — **doğrulanmalı**)?
- [ ] Her emisyon değerinin veri kalitesi puanı ve kaynağı (raporlanan / fiziksel / ciro / varlık) izlenebilir mi?
- [ ] Tahmin kullanılan kayıtlarda kullanılan parametre (sektör yoğunluğu, finansal oran, döviz kuru, yıl) kayıtlı mı?
- [ ] Döviz: bakiye tutarı ile payda aynı para biriminde ve aynı tarihte mi?
- [ ] Müşteri verisinin yılı ile raporlama yılı arasındaki fark (zaman gecikmesi) açıklanıyor mu?
- [ ] Raporlanan metrikler: mutlak finanse edilen emisyon (tCO2e), ekonomik yoğunluk (tCO2e / yatırılan milyon),
      gerekiyorsa fiziksel yoğunluk ve WACI; varlık sınıfı ve sektör kırılımı.
- [ ] Hesaplama yeniden yapıldığında (veri ya da yöntem değişikliği) önceki sonuçlar korunuyor, fark açıklanıyor mu?

## 5. Sık yapılan hatalar
- Borsada işlem görmeyen müşteride EVIC yerine yalnız borç ya da yalnız özkaynakla pay hesaplamak.
- Başlangıç değeri yerine güncel mülk/araç değerini kullanmak (konut, taşıt, ticari gayrimenkul).
- Veri kalitesi puanını kayıt bazında saklamayıp portföy ortalamasını uydurmak.
- Ciro bazlı tahminde ciro ile sektör yoğunluğunun para birimi ve yılını eşleştirmemek.
- Kapsam 2'yi müşteri enerji verisinden hesaplarken yılın emisyon faktörü yerine sabit faktör kullanmak.
- Aynı müşteriyi iki varlık sınıfında saymak (çift sayım).

## 6. Sustable karşılığı
| PCAF konusu | Ekran (`sustable-frontend/platform/bank`) | Backend (`src/main/java/io/sustable/api/`) |
|---|---|---|
| Kredi müşterisi ve varlık sınıfı | Kredi müşterileri diyaloğu | `service/fnetwork/FNetworkCompanyService`, `service/pcaf/financial/PcafCustomerAssetClass` |
| Finansal kayıtlar (bakiye, payda) ve atıf faktörü | `/data-entry/financial`, `/data-entry/financial/[assetClass]` | `service/pcaf/financial`, `PcafAttributionCalculator`, `model/pcaf/financial/PcafAttributionMethod` |
| Varlık sınıfları (10 sınıf) | aynı | `model/pcaf/financial/PcafAssetClassType` |
| Emisyon verisi: şirket emisyonu, ciro, enerji, üretim, araç | `/data-entry/emission-data/*` | `service/pcaf/emission` |
| Tahmin parametreleri (finansal oran, emisyon oranı, sektör yoğunluğu, döviz kuru, taşıt göstergesi, NACE eşlemesi) | parametre ekranları | `service/pcaf/parameter` |
| Hesaplama ve veri kalitesi puanı | `/calculate/runs`, `/calculate/runs/[id]` | `service/pcaf/calculation/PcafFinancedEmissionEngine` |
| Dashboard ve portföy raporu | `/home`, `/report/pcaf` | `service/pcaf/calculation` |

Kod kuralları: `sustable-backend/.claude/rules/pcaf.md` (veri kilidi, platform varsayılanı + banka üzerine yazması,
hesaplama, Excel yükleme tuzakları).
