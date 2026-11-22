# GHG Protokolü — Kurumsal Envanter, Kapsam 1/2/3

> Kendi özetimizdir; standart metni değildir. "doğrulanmalı" işaretli maddeler kullanılmadan önce
> GHG Protokolü'nün güncel yayınlarından kontrol edilmelidir. Son gözden geçirme: 2026-11-22 (ilk sürüm).

## 1. Kapsam
- **Standartlar ailesi (WRI ve WBCSD ortak girişimi):**
  - **Kurumsal Standart** (Corporate Accounting and Reporting Standard, gözden geçirilmiş baskı 2004): şirket
    düzeyinde envanter ilkeleri (ilgililik, eksiksizlik, tutarlılık, şeffaflık, doğruluk), sınırlar, Kapsam 1 ve 2'nin
    zorunlu raporlanması, baz yıl.
  - **Kapsam 2 Rehberi** (Scope 2 Guidance, 2015): satın alınan elektrik, buhar, ısı ve soğutma için iki yöntem —
    **konum bazlı** (şebeke ortalaması faktörü) ve **piyasa bazlı** (sözleşmeye dayalı araçlar ve kalıntı karışım).
    Rehberin "ikili raporlama" kuralı: iki sonuç da raporlanır.
  - **Kapsam 3 Standardı** (Corporate Value Chain (Scope 3) Standard, 2011): değer zincirindeki 15 kategori.
- **Kimler kullanır:** her sektörden şirketler, kamu kurumları; CDP, SBTi, PCAF (bkz. `pcaf.md`) gibi çerçeveler
  GHG Protokolü'nü temel alır.
- **TSRS 2 ilişkisi:** TSRS 2 (IFRS S2), sera gazı emisyonlarının GHG Protokolü Kurumsal Standardı'na göre
  ölçülmesini ister (yerel otorite başka yöntem öngörmedikçe); Kapsam 2 için konum bazlı sonuç ve sözleşmeye dayalı
  araçlar hakkında bilgi, Kapsam 3 için kategori kırılımı istenir (bkz. `tsrs.md`). Geçiş muafiyetleri ve ayrıntı
  **doğrulanmalı** — `tsrs.md` ile tutarlı tutulmalı.
- **ISO 14064-1 ilişkisi:** ISO 14064-1:2018 aynı mantığı altı kategoriye (doğrudan; enerji dolaylı; ulaşım;
  kullanılan ürünler; kuruluşun ürünlerinin kullanımı; diğer) böler ve doğrulama için uygundur. Kapsam ↔ kategori
  eşlemesi birebir değildir (bkz. `iso14064.md`).

## 2. Kontrol listesi

### 2.1 Sınırlar
- [ ] **Organizasyonel sınır** yaklaşımı seçildi ve açıklandı; tüm envanterde tutarlı:
  - **Özkaynak payı:** emisyon ortaklık payı oranında alınır.
  - **Finansal kontrol:** finansal ve işletme politikalarını yönlendiren kuruluş %100 alır.
  - **Operasyonel kontrol:** işletme politikalarını uygulama yetkisi olan kuruluş %100 alır (en yaygın tercih).
- [ ] Ortak girişimler, kiralanan varlıklar ve iştirakler seçilen yaklaşıma göre sınıflandırıldı.
- [ ] **Operasyonel sınır:** hangi kaynakların Kapsam 1, 2, 3 olduğu belirlendi; hariç tutulan kaynaklar ve gerekçe yazıldı.

### 2.2 Kapsam 1 (doğrudan)
- [ ] **Sabit yanma:** kazan, fırın, jeneratör, türbin.
- [ ] **Mobil yanma:** şirkete ait/kontrol edilen araç, iş makinesi, gemi, uçak.
- [ ] **Proses emisyonları:** kimyasal/fiziksel süreçler (çimento klinkeri, kireç, metal üretimi vb.).
- [ ] **Kaçak (sızıntı) emisyonları:** soğutucu akışkanlar, yangın söndürücüler, SF6'lı şalt, metan kaçakları.

### 2.3 Kapsam 2 (enerji dolaylı)
- [ ] **Konum bazlı** sonuç: tüketim × şebeke ortalama emisyon faktörü (ülke/bölge, ilgili yıl).
- [ ] **Piyasa bazlı** sonuç: sözleşmeye dayalı araçlar (YEK-G/I-REC/GO sertifikaları, PPA, tedarikçiye özgü faktör);
      kalmayan tüketim için **kalıntı karışım** (residual mix) faktörü — yoksa şebeke ortalaması kullanıldığı açıklanır.
- [ ] Sözleşmeye dayalı araçların kalite kriterleri (Kapsam 2 Rehberi):
  - araç, enerjinin emisyon oranını taşır;
  - tek bir talep (çift sayım yok), raporlayan adına iptal/itfa edilmiş;
  - tüketim dönemine yakın üretilmiş ve itfa edilmiş;
  - tüketimle aynı piyasada (şebeke sınırı) üretilmiş;
  - tedarikçiye özgü faktörlerde aynı enerji iki kez talep edilmemiş; kalıntı karışım bu talepleri dışlıyor.
- [ ] Buhar, ısı, soğutma da Kapsam 2'de; iki yöntemle de raporlandı.

### 2.4 Kapsam 3 (diğer dolaylı) — 15 kategori
Yukarı akış (1–8):
1. **Satın alınan mal ve hizmetler** — tedarikçide beşikten kapıya emisyon.
2. **Sermaye malları** — makine, bina, ekipman; satın alındığı yıl tamamı raporlanır.
3. **Yakıt ve enerjiyle ilgili faaliyetler** (Kapsam 1–2 dışı) — yakıtların kuyudan tanka (WTT) payı, iletim/dağıtım kayıpları.
4. **Yukarı akış taşıma ve dağıtım** — satın alınan lojistik, tedarikçiden gelen taşıma.
5. **Operasyonlarda oluşan atık** — üçüncü tarafça bertaraf/arıtma.
6. **İş seyahatleri** — uçak, tren, otobüs, kiralık araç; isteğe bağlı otel konaklaması.
7. **Çalışanların işe gidiş gelişi** — isteğe bağlı uzaktan çalışma.
8. **Yukarı akış kiralanan varlıklar** — kiracı olunan, Kapsam 1–2'de sayılmayan varlıklar.

Aşağı akış (9–15):
9. **Aşağı akış taşıma ve dağıtım** — satılan ürünün şirketçe ödenmeyen taşıması, depolama, perakende.
10. **Satılan ürünlerin işlenmesi** — ara ürünün üçüncü tarafça işlenmesi.
11. **Satılan ürünlerin kullanımı** — doğrudan kullanım fazı emisyonu (yakıt, enerji tüketen ürün).
12. **Satılan ürünlerin ömür sonu işlemleri** — bertaraf ve arıtma.
13. **Aşağı akış kiralanan varlıklar** — kiraya verilen varlıklar.
14. **Franchise'lar** — franchise verenin raporladığı franchise işletme emisyonu.
15. **Yatırımlar** — hisse, borç, proje finansmanı (finans sektöründe PCAF; bkz. `pcaf.md`).

- [ ] Her kategori için dahil/hariç kararı ve gerekçe; önemlilik taraması yapıldı.
- [ ] Hesap yöntemi (tedarikçiye özgü, ortalama veri, harcama bazlı, mesafe bazlı vb.) kategori bazında açıklandı.
- [ ] Kapsam 3 ayrı raporlanır; Kapsam 1–2 ile çift sayım yok.

### 2.5 Gazlar ve GWP
- [ ] Kyoto gazları: **CO2, CH4, N2O, HFC'ler, PFC'ler, SF6, NF3** (NF3 sonradan eklendi; yedi gaz).
- [ ] Sonuç tCO2e; kullanılan **GWP seti** (100 yıllık) ve IPCC değerlendirme raporu açıklandı.
  - **AR5:** CH4 28, N2O 265.
  - **AR6:** CH4 fosil 29,8, fosil olmayan 27,0 (genel 27,9 da kullanılır); N2O 273 — değerler **doğrulanmalı**.
  - GHG Protokolü en güncel IPCC raporunu önerir; TSRS 2 de raporlama tarihindeki en güncel IPCC GWP'lerini ister
    (**doğrulanmalı**). GWP seti değiştiğinde baz yıl ve karşılaştırmalı yıllar aynı setle yeniden hesaplanmalıdır.
- [ ] Emisyon faktörü veritabanının kendi GWP'si gömülü mü (ör. DEFRA CO2e faktörleri)? Çifte GWP uygulanmadı.

### 2.6 Baz yıl ve yeniden hesaplama
- [ ] Doğrulanabilir verisi olan bir baz yıl (ya da birkaç yılın ortalaması) seçildi ve gerekçesi yazıldı.
- [ ] **Yeniden hesaplama politikası** yazılı: tetikleyiciler
  - **yapısal değişiklik** (birleşme, satın alma, elden çıkarma, dış kaynak kullanımı/içe alma);
  - **yöntem değişikliği** (hesap yöntemi, emisyon faktörü, GWP seti);
  - **önemli hata** ya da birikmiş küçük hataların önemli toplamı.
- [ ] **Önemlilik eşiği** tanımlı (yaygın uygulama baz yıl emisyonunun %5'i; standart sabit eşik vermez — **doğrulanmalı**).
- [ ] Organik büyüme/küçülme yeniden hesaplama gerektirmez.

### 2.7 Diğer zorunlu ayrımlar
- [ ] **Biyojenik CO2** (biyokütle yanması) kapsamların dışında, ayrı satırda raporlanır; biyokütleden CH4 ve N2O Kapsam 1'de kalır.
- [ ] **Karbon denkleştirme** (offset) ve satın alınan karbon kredileri envantere dahil edilmez, brüt emisyondan düşülmez;
      ayrı bilgi olarak raporlanır. (Kapsam 2 piyasa bazlı sözleşmeye dayalı araçlar denkleştirme değildir.)
- [ ] **Veri kalitesi ve belirsizlik:** faaliyet verisi ve faktör kaynakları, tahminler, veri boşlukları, belirsizlik
      değerlendirmesi (niteliksel ya da niceliksel, ör. GHG Protokolü belirsizlik aracı veya Monte Carlo) açıklandı.
- [ ] Raporlama dönemi (genellikle takvim yılı) ve tesis kırılımı tutarlı.

### 2.8 Uçuş emisyonları (kısa not)
- İş amaçlı uçuşlar **Kapsam 3 Kategori 6**; şirketin kendi uçağı ise Kapsam 1 mobil yanma.
- **ICAO Karbon Emisyon Hesaplayıcısı** yolcu başına CO2'yi rota, uçak tipi ve doluluk verisiyle verir; yalnız CO2
  içerir, ışınım zorlaması (RF/uplift) çarpanı içermez (**doğrulanmalı**). DEFRA mesafe bazlı faktörleri ise sınıf ve
  mesafe bandına göre CO2e verir; hangi yöntemin seçildiği ve RF uygulanıp uygulanmadığı açıklanmalı.

## 3. Sık yapılan hatalar
- Organizasyonel sınır yaklaşımını açıklamamak ya da tesisler arasında karışık uygulamak.
- Kapsam 2'yi yalnız tek yöntemle raporlamak; piyasa bazlıda sertifikası olmayan tüketime kalıntı karışım yerine şebeke
  ortalamasını gerekçesiz uygulamak.
- Sertifikanın tüketim yılı, piyasası veya itfa kaydı ile eşleşmemesi; aynı sertifikayı birden fazla tesiste saymak.
- Proses ve kaçak emisyonları (soğutucu akışkan dolumu) atlamak.
- Kategori 3'ü (WTT, iletim kayıpları) unutmak ya da Kapsam 1/2 ile çift saymak.
- Karbon kredilerini toplam emisyondan düşmek; biyojenik CO2'yi Kapsam 1 toplamına katmak.
- GWP setini değiştirip baz yılı yeniden hesaplamamak; DEFRA CO2e faktörüne ikinci kez GWP uygulamak.
- Baz yıl yeniden hesaplama politikası ve önemlilik eşiği olmadan baz yılı değiştirmek.
- Kapsam 3'te hariç tutulan kategorileri gerekçesiz bırakmak.

## 4. Sustable karşılığı
| GHG Protokolü konusu | Ekran (`sustable-frontend/platform/carbon`, `src/app/[lang]/`) | Backend (`sustable-backend/src/main/java/io/sustable/api/`) |
|---|---|---|
| GHG kaynak tanımı (kapsam, kategori, faktör zinciri, Kapsam 3 önemlilik ve belirsizlik derecesi) | `ghg-source/*` | `service/ghgsource/EmissionGhgSourceService`, `GhgSourceMaterialityService`; `/emission-ghg-source` |
| Faaliyet verisi girişi ve hesap (Kapsam 1/2/3) | `calculate`, `calculate/source/[id]`, `calculate/list`, `calculate/results` | `service/calculator/orchestrator/EmissionCalculateOrchestrator`, `service/calculator/emission/*`; `/emission-calculator`, `/company-emission` |
| Onay kuyruğu, veri kilidi | `admin/pending-approvals`, `pending-approvals`, `admin/data-lock` | `service/calculator/emission/PendingEmissionApprovalService`, `DataLockService`; `/pending-emission`, `/data-lock` |
| GHG Protokolü raporu (Kapsam 1/2/3 kırılımı, konum/piyasa bazlı, Word, rapor metinleri) | `ghg-report/[[...slug]]` | `service/calculator/GhgProtocolOrchestrator`, `model/enums/GhgProtocol{Scope,Category}`, `util/GhgProtocolWordUtil`, `util/GhgProtocolSettingConstants`; `controller/emission/GhgProtocolController` (`/ghg-protocol`) |
| Analiz ve dashboard (kapsam/kategori/kaynak) | `home`, `analytics/[[...slug]]` | `service/real/CorporateEmission{Dashboard,Analytic}Service`, `service/dasboard/`; `/analytic`, `/dashboard`, `/emission/inventory` |
| Emisyon geçmişi (önceki yıllar, baz yıl karşılaştırması) | `custom-inventory/emission-history` | `service/history/EmissionHistoryService`; `controller/history/EmissionHistoryController` (`/emission/history`) |
| Uçuş emisyonu (ICAO, Kategori 6) | `custom-inventory/icao` | `service/calculator/IcaoService` (Jsoup ile ICAO sitesi); `controller/icao/IcaoCalculatorController` (`/icao`) |
| Emisyon yoğunluğu | `custom-inventory/emission-density` | `service/density`; `/emission-density` |
| GWP ve faktör değişikliği sonrası yeniden hesaplama | (admin talebi) | `service/GwpConstantService`, `model/entity/GwpConstant`, `util/GwpSnapshotUtil`, `service/calculator/recalculation/`; `/emission-recalculation` |
| Belirsizlik değerlendirmesi | — | `service/uncertainty/`, `controller/uncertainty/` |
| Sözleşmeye dayalı araçlar (yenilenebilir sertifika), denkleştirme | `cfi`, `cfi/create` | `service/cfi` (`sumRenewableCertificate`); `/cfi` |
| Kuruluş bilgisi, baz yıl, nicelleştirilmiş envanter | `iso-report/[[...slug]]` | `CorporateController` (`/corporation`), `service/CompanyQuantifiedInventoryService` (`/company/quantified/inventory`) |
| ISO 14064-1 raporu (aynı veri, kategori 1–6) | `iso-report/[[...slug]]` | `service/iso`, `util/Iso14064ReportUtils`, `service/calculator/orchestrator/CorporateEmissionReportOrchestrator`; `/iso-14064-1/*` |

Kod kuralları: `sustable-backend/.claude/rules/emission-calculator.md` (hesap akışı, veri kilidi, onay, GWP snapshot,
yeniden hesaplama), `sustable-backend/.claude/rules/iso14064.md`. Akış: `sustable-backend/docs/architecture/calculation.md`.

### Sustable'da mevcut durum (koddan, 2026-11-22)
- **GWP:** tek global set, AR6 olarak adlandırılıyor (`GwpConstant`): CO2 1, CH4 **27,0** (V21_52 göçüyle 27,9'dan
  indirildi; AR6 fosil olmayan CH4 değerine karşılık geliyor), N2O **273**. Fosil CH4 (29,8) ayrımı yok. Yalnız CO2, CH4,
  N2O ve doğrudan CO2e (`GreenhouseGas`) modellenmiş; HFC/PFC/SF6/NF3 ayrı gaz olarak değil, faktör CO2e olarak giriyor
  (**doğrulanmalı**). DEFRA veritabanında GWP uygulanmıyor. Kullanılan GWP kayıt anında `emission.gwp_ch4/gwp_n2o`
  alanlarına damgalanıyor; değişiklikte otomatik yeniden hesaplama yok, admin talebiyle iş çalışıyor.
- **Kapsam 2:** GHG raporunda konum bazlı ve piyasa bazlı iki satır var (elektrik + buhar/ısı). Piyasa bazlı değer
  `GhgProtocolOrchestrator.enrichMarketBased` içinde yalnız **elektrik** için hesaplanıyor: toplam tüketimden CFI'daki
  yenilenebilir sertifika miktarı (MWh × 1000) düşülüyor, kalan tüketim **aynı (şebeke) faktörüyle** çarpılıyor.
  Kalıntı karışım faktörü, PPA ve tedarikçiye özgü faktör desteği görünmüyor; buhar/ısı için piyasa bazlı ayrı hesap yok.
  Belirsizlik modülü de `SCOPE2_LOCATION_BASED_ONLY` sınırlamasını kaydediyor.
- **Kapsam 1:** GHG rapor eşlemesinde (`GhgProtocolScope.SCOPE_1`) sabit, mobil ve kaçak var; `EmissionCategory.PROCESS_EMISSION`
  tanımlı olduğu hâlde GHG Protokolü raporundaki Kapsam 1'e eşlenmemiş (**doğrulanmalı**: raporda proses emisyonu
  görünüyor mu?). Biyokütle (`BIOMASS_EMISSION`) sabit yanma satırına dahil; biyojenik CO2'nin ayrı satırda
  raporlanması GHG raporunda görünmüyor (ISO raporu biyokütleyi ayrı filtreliyor) — **doğrulanmalı**.
- **Kapsam 3:** raporda 14 kategori var; **Kategori 14 (Franchise'lar) yok**.
- **Baz yıl:** şirket detayında `baseYear` alanı ve rapor metni var; yapısal değişiklik/önemlilik eşiğine dayalı baz yıl
  yeniden hesaplama iş akışı görünmüyor (**doğrulanmalı**).
- Rapor metni şablonu (`GhgProtocolSettingConstants`) varsayılan olarak "operasyonel kontrol" yaklaşımını ve Kurumsal
  Standart (2004) atfını kullanıyor; şirket metni ekrandan değiştirebiliyor (`/ghg-protocol/setting`).

## Kaynaklar
- GHG Protocol, *A Corporate Accounting and Reporting Standard*, gözden geçirilmiş baskı, 2004 —
  https://ghgprotocol.org/corporate-standard
- GHG Protocol, *Scope 2 Guidance*, 2015 — https://ghgprotocol.org/scope-2-guidance
- GHG Protocol, *Corporate Value Chain (Scope 3) Accounting and Reporting Standard*, 2011 —
  https://ghgprotocol.org/corporate-value-chain-scope-3-standard
- GHG Protocol, *Technical Guidance for Calculating Scope 3 Emissions*, 2013 — https://ghgprotocol.org/scope-3-calculation-guidance-2
  (URL **doğrulanmalı**)
- GHG Protocol, *Required Greenhouse Gases in Inventories* (NF3 eki), 2013 — https://ghgprotocol.org/standards (**doğrulanmalı**)
- IPCC AR6 WG1, Bölüm 7, Tablo 7.15 (GWP-100), 2021 — https://www.ipcc.ch/report/ar6/wg1/
- IPCC AR5 WG1, Bölüm 8, Tablo 8.A.1, 2013 — https://www.ipcc.ch/report/ar5/wg1/
- ICAO Carbon Emissions Calculator — https://www.icao.int/environmental-protection/CarbonOffset
- GHG Protocol, kamuoyu danışmaları sayfası — https://ghgprotocol.org/ghg-protocol-public-consultations
- GHG Protocol, Kapsam 2 danışması geri bildirim özeti (2026-07-29, güncelleme 2026-08-25) ve piyasa bazlı yöntem
  güncellemesi (2026-10-06) — https://ghgprotocol.org/sites/default/files/2026-10/S2-Market-Based-Method-Update-20261006.pdf

**Revizyon süreci (web, 2026-11-22):** GHG Protokolü, Bağımsız Standartlar Kurulu (ISB) ve teknik çalışma grupları
(TWG) eliyle Kurumsal Standart, Kapsam 2 ve Kapsam 3'ü güncelliyor. Kapsam 2 ilk kamuoyu danışması 20 Ekim 2025 –
31 Ocak 2026 arasında yapıldı (saatlik eşleştirme ve teslim edilebilirlik gibi piyasa bazlı yöntem değişiklikleri
tartışıldı); geri bildirim özeti Temmuz–Ağustos 2026'da yayımlandı, Ekim 2026 güncellemesine göre piyasa bazlı yöntemde
iki ana görüş var ve TWG çalışması sürüyor. İkinci Kapsam 2 danışmasının açılıp açılmadığı teyit edilemedi; yeni
standardın 2027'de, birleştirilmiş Kurumsal Standart taslağının 2027 2. çeyrekte danışmaya çıkması bekleniyor —
**doğrulanmalı**. Yayımlanana kadar 2004/2011/2015 metinleri geçerlidir.
