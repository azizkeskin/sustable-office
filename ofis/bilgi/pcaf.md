# PCAF — Finanse Edilen Emisyonlar

> Kendi özetimizdir; standart metni değildir. "doğrulanmalı" işaretli maddeler kullanılmadan önce
> PCAF'ın güncel standardından kontrol edilmelidir. Son gözden geçirme: 2026-11-22 (kaynaklarla teyit edildi:
> PCAF Kısım A, Üçüncü Baskı, Aralık 2025; bkz. "Kaynaklar").

## 1. Kapsam
- **Standart:** PCAF (Partnership for Carbon Accounting Financials) — Finans Sektörü için Küresel Sera Gazı
  Muhasebesi ve Raporlama Standardı.
  - **Kısım A:** Finanse edilen emisyonlar (krediler ve yatırımlar) — Sustable'ın `platform/bank` kapsamı.
  - **Kısım B:** Kolaylaştırılan emisyonlar (sermaye piyasası işlemleri).
  - **Kısım C:** Sigortayla ilişkili emisyonlar.
- **Konum:** GHG Protokolü Kapsam 3, **Kategori 15 (Yatırımlar)**'ın finans sektörüne uygulanması.
- **Kimler kullanır:** bankalar, varlık yöneticileri, sigortacılar. TSRS 2 finansal kuruluşlardan finanse edilen
  emisyonların açıklanmasını ister (bkz. `tsrs.md`); PCAF bunun fiilî hesap yöntemidir.
- **Sürüm:** Kısım A'nın en güncel sürümü **Üçüncü Baskı (Aralık 2025)**; 2 Aralık 2025'te yayımlandı. Önceki
  baskılar: birinci (Kasım 2020, 6 varlık sınıfı), ikinci (Aralık 2023, egemen borç eklendi). Üçüncü baskı dört yeni
  yöntem getirdi: fon kullanımına dayalı yapılar (use of proceeds), menkul kıymetleştirme ve yapılandırılmış ürünler,
  alt egemen borç ve IFRS S1/S2'ye göre kullandırılmamış kredi taahhütlerinin isteğe bağlı raporlanması. Toplam
  **10 varlık sınıfı:** borsada işlem gören hisse ve kurumsal tahviller; ticari krediler ve borsada işlem görmeyen hisse;
  proje finansmanı; ticari gayrimenkul; konut kredileri; motorlu taşıt kredileri; fon kullanımına dayalı yapılar;
  menkul kıymetleştirme ve yapılandırılmış ürünler; devlet borçlanma araçları; alt egemen borç.
  - İkinci baskının eklemeleri ve üçüncü baskının yeni yöntemleri henüz GHG Protokolü incelemesinden geçmemiştir.

## 2. Temel formül
**Finanse edilen emisyon = Atıf faktörü × Müşterinin (ya da varlığın) emisyonu**

Atıf faktörü = Kuruluşun bakiye tutarı / Müşterinin (ya da varlığın) toplam değeri. Payda varlık sınıfına göre değişir:

| Varlık sınıfı | Payda (atıf faktörü) |
|---|---|
| Borsada işlem gören hisse ve kurumsal tahviller | EVIC (nakit dahil işletme değeri) |
| Ticari krediler ve borsada işlem görmeyen hisse | Borsada işlem görüyorsa EVIC; değilse toplam özkaynak + borç |
| Proje finansmanı | Projenin toplam özkaynak + borcu (başlangıçta toplam finansman, sonraki yıllarda proje bilançosu); ayrı bilançosu olmayan projede başlangıçtaki proje değeri sabitlenir |
| Ticari gayrimenkul | Başlangıçtaki mülk değeri |
| Konut kredileri | Başlangıçtaki mülk değeri |
| Motorlu taşıt kredileri | Başlangıçtaki araç değeri |
| Devlet borçlanma araçları | Satın alma gücü paritesine göre düzeltilmiş GSYH |
| Fon kullanımına dayalı yapılar | Çift atıf: yatırımcının bakiyesi / yapının toplam özkaynak + borcu, çarpı her dayanak varlığın kendi sınıfına göre atıf faktörü. Ayrı yapılarda (fonlar, SPV) yalnız tahsis edilmiş tutar; ihraççının bilançosundaki entegre yapılarda (yeşil tahvil/kredi) tahsis edilmemiş tutar ihraççı düzeyinde hesaplanır |
| Menkul kıymetleştirme ve yapılandırılmış ürünler | Üç katman: teminat atıf faktörü (güncel bakiye / dayanak varlığın başlangıç değeri ya da kurumsal borçluda özkaynak + borç veya EVIC), kredi atıf faktörü (havuzdaki kredi payı) ve dilim atıf faktörü (dilim bakiyesi / işlemin toplam bakiyesi; kıdem sırası etkilemez) |
| Alt egemen borç | Bölge/il/belediyenin satın alma gücü paritesine göre düzeltilmiş GSYH'si (ülkenin SGP katsayısı yerel nominal GSYH'ye uygulanır); bölgesel yaklaşım. Şirket benzeri alt egemen ihraççılar ticari krediler yöntemiyle hesaplanır |

- "Paranın izini sür": yalnız bilançodaki tutar sayılır; bakiye tutarı takvim ya da mali yıl sonu değeridir (seçim
  açıklanır ve tutarlı uygulanır).
- Payda finanse edilen tarafın toplam değerini temsil ettiğinden atıf faktörü normalde 1'den küçüktür; menkul
  kıymetleştirmede teminat atıf faktörü ve egemen/alt egemen borçta oran açıkça en fazla 1 alınır.
- Alt egemen borçta borçlunun Kapsam 1'i (arazi kullanımı hariç) zorunlu, Kapsam 2 ve 3 önerilir.

## 3. Veri kalitesi puanı (1 en iyi – 5 en zayıf)
Ticari krediler / borsada işlem görmeyen hisse ile borsada işlem gören hisse / kurumsal tahviller için aynı yapı
(Kısım A üçüncü baskı, Tablo 5.1-2 ve 5.2-1; diğer sınıfların tabloları farklıdır, bkz. standardın Ek 10.1'i):

| Puan | Seçenek | Emisyon verisinin kaynağı |
|---|---|---|
| 1 | 1a — raporlanan | Müşterinin raporladığı, **doğrulanmış** emisyon; bakiye ve payda (özkaynak + borç ya da EVIC) biliniyor |
| 2 | 1b — raporlanan | Müşterinin hesapladığı **doğrulanmamış** emisyon |
| 2 | 2a — fiziksel faaliyet | Müşterinin birincil **enerji tüketimi** verisi × o veriye özgü faktör (+ ilgili proses emisyonları); yalnız Kapsam 1–2 için |
| 3 | 2b — fiziksel faaliyet | Müşterinin birincil **üretim** verisi × o veriye özgü faktör |
| 4 | 3a — ekonomik faaliyet | Müşterinin **cirosu** × sektörün ciro başına emisyon faktörü (payda biliniyor) |
| 5 | 3b — ekonomik faaliyet | Yalnız bakiye biliniyor: bakiye × sektörün **varlık başına** emisyon faktörü |
| 5 | 3c — ekonomik faaliyet | Yalnız bakiye biliniyor: sektörün ciro başına faktörü × sektörün **varlık devir hızı** |

- Ciro uygun gösterge değilse başka bir finansal gösterge kullanılabilir (gerekçesi açıklanır, puan değişmez).

- Puan, varlık sınıfı bazında **bakiye ağırlıklı** olarak raporlanır.
- Zamanla puanın iyileşmesi beklenir; kuruluş iyileştirme planını açıklar.

## 4. Kontrol listesi
- [ ] Her kayıt doğru varlık sınıfında mı; atıf faktörü paydası o sınıfa uygun mu?
- [ ] Müşterinin Kapsam 1, 2 **ve 3** emisyonları dahil mi; Kapsam 3, Kapsam 1–2'den ayrı açıklanıyor mu? Sektörel
      aşamalı geçiş tamamlandı: 2021'den itibaren yayımlanan raporlarda en az petrol-gaz ve madencilik (NACE 05–09,
      19, 20), 2023'ten itibaren ulaşım, inşaat, binalar, malzeme ve sanayi, **2025'ten itibaren yayımlanan raporlarda
      tüm sektörler** (finans sektörü dahil; finans sektörüne verilen kredilerin ayrı raporlanması önerilir). Veri
      yetersizliğinde Kapsam 3'ün neden raporlanamadığı açıklanmalıdır.
- [ ] Her emisyon değerinin veri kalitesi puanı ve kaynağı (raporlanan / fiziksel / ciro / varlık) izlenebilir mi?
- [ ] Tahmin kullanılan kayıtlarda kullanılan parametre (sektör yoğunluğu, finansal oran, döviz kuru, yıl) kayıtlı mı?
- [ ] Döviz: bakiye tutarı ile payda aynı para biriminde ve aynı tarihte mi?
- [ ] Müşteri verisinin yılı ile raporlama yılı arasındaki fark (zaman gecikmesi) açıklanıyor mu?
- [ ] Raporlanan metrikler: mutlak finanse edilen emisyon (tCO2e), ekonomik yoğunluk (tCO2e / yatırılan milyon),
      gerekiyorsa fiziksel yoğunluk ve WACI; varlık sınıfı ve sektör kırılımı.
- [ ] Hesaplama yeniden yapıldığında (veri ya da yöntem değişikliği) önceki sonuçlar korunuyor, fark açıklanıyor mu?

## 5. Sık yapılan hatalar
- Borsada işlem görmeyen müşteride toplam özkaynak + borç (işlem görende EVIC) yerine yalnız borç ya da yalnız özkaynakla pay hesaplamak.
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

## Kaynaklar
| Başlık | Kurum | Tarih / sürüm | URL |
|---|---|---|---|
| The Global GHG Accounting and Reporting Standard Part A: Financed Emissions | PCAF | Üçüncü Baskı, Aralık 2025 | https://carbonaccountingfinancials.com/files/standard-launch-2025/PCAF-PartA-2025-V3-December.pdf |
| Part A 2025 Yönetici Özeti | PCAF | Aralık 2025 | https://carbonaccountingfinancials.com/files/standard-launch-2025/PCAF-PartA-2025-Executive-Summary-Clean.pdf |
| PCAF launches updated GHG accounting standard (yayım duyurusu) | PCAF | 2 Aralık 2025 | https://www.carbonaccountingfinancials.com/en/newsitem/pcaf-launches-updated-ghg-accounting-standard-2025 |
| PCAF updates financed emissions standards (ikincil teyit) | EY | Aralık 2025 | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/technical/ifrs-technical-resources/documents/ey-gl-ghg-susdev-2-pcaf-updates-emissions-standards-12-2025.pdf |
