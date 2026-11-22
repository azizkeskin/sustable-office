# TSRS — Türkiye Sürdürülebilirlik Raporlama Standartları

> Kendi özetimizdir; standart metni değildir. "doğrulanmalı" işaretli maddeler kullanılmadan önce
> güncel KGK metninden kontrol edilmelidir. Son gözden geçirme: 2026-11-22 (ilk sürüm, İş Birimi ajanı ile genişletilecek).

## 1. Kapsam
- **Yayımlayan:** Kamu Gözetimi, Muhasebe ve Denetim Standartları Kurumu (KGK).
- **Kaynak:** IFRS S1 ve IFRS S2'nin (ISSB) Türkiye uyarlaması.
  - **TSRS 1** — Sürdürülebilirlikle ilgili finansal bilgilerin açıklanmasına ilişkin genel hükümler.
  - **TSRS 2** — İklimle ilgili açıklamalar.
- **Yürürlük:** 1 Ocak 2024 ve sonrasında başlayan raporlama dönemleri, kapsamdaki işletmeler için.
- **Kimler zorunlu:** KGK kararıyla belirlenen işletmeler (aktif büyüklüğü, net satış hasılatı ve çalışan sayısı
  eşiklerinden ikisini art arda iki dönem aşanlar; bankalar ve bazı kamu yararını ilgilendiren kuruluşlar ayrıca).
  Eşikler ve kapsam sonradan güncellendi — **doğrulanmalı** (güncel KGK kurul kararı).
- **Önemlilik yaklaşımı:** **Finansal önemlilik** — işletmenin nakit akışlarını, finansmana erişimini ya da sermaye
  maliyetini kısa, orta ya da uzun vadede etkilemesi makul olarak beklenen bilgiler. (GRI'nin etki önemliliğinden farklıdır.)

## 2. Kontrol listesi

### 2.1 Genel hükümler (TSRS 1)
- [ ] Raporlama dönemi ve raporlayan işletme **finansal tablolarla aynı** mı?
- [ ] Rapor finansal tablolarla birlikte yayımlanıyor mu (ilk yıl için geçiş kolaylığı var — **doğrulanmalı**)?
- [ ] Dört temel alan kapsanıyor mu: **Yönetişim, Strateji, Risk Yönetimi, Metrikler ve Hedefler**.
- [ ] Riskler ve fırsatlar **değer zinciri** boyunca değerlendiriliyor mu?
- [ ] **Kısa / orta / uzun vade** tanımları yapılmış ve işletmenin planlama ufkuyla ilişkilendirilmiş mi?
- [ ] Finansal tablolarla **bağlantılılık**: kullanılan varsayımlar ve veriler finansal tablolarla tutarlı mı?
- [ ] Karşılaştırmalı bilgi (önceki dönem) veriliyor mu (ilk yıl muafiyeti — **doğrulanmalı**)?
- [ ] Tahmin ve ölçüm belirsizliği açıklanıyor mu; önceki dönem hataları düzeltiliyor mu?

### 2.2 İklimle ilgili açıklamalar (TSRS 2)
- **Yönetişim:** iklim risk/fırsatlarının gözetiminden sorumlu yönetim organı, yetkinliği, yönetimin rolü,
  hedeflerin ücretlendirmeyle ilişkisi.
- **Strateji:**
  - [ ] Fiziksel riskler (akut / kronik) ve geçiş riskleri (politika, teknoloji, piyasa, itibar) ayrı mı?
  - [ ] İş modeli ve değer zinciri üzerindeki etkiler; geçiş planı varsa açıklanıyor mu?
  - [ ] Finansal durum, performans ve nakit akışlarına mevcut ve beklenen etkiler.
  - [ ] **İklim direnci**: senaryo analizi (işletmenin koşullarıyla orantılı yaklaşım).
- **Risk yönetimi:** riskleri belirleme, değerlendirme, önceliklendirme ve izleme süreçleri; genel risk yönetimine entegrasyon.
- **Metrikler ve hedefler:**
  - [ ] **Sera gazı emisyonları:** Kapsam 1, Kapsam 2 (konum bazlı ve sözleşmeye dayalı yöntem bilgisi), Kapsam 3;
        GHG Protokolü Kurumsal Standardı ile ölçüm; mutlak brüt tCO2e.
  - [ ] Kapsam 3'te dahil edilen kategoriler (GHG Protokolü'nün 15 kategorisi) ve ölçüm yaklaşımı.
  - [ ] **Finansal kuruluşlar:** finanse edilen emisyonlar (varlık yönetimi, ticari bankacılık, sigorta) — bkz. `pcaf.md`.
  - [ ] Sektörler arası metrikler: geçiş ve fiziksel risklere açık varlık/faaliyet tutarı ve oranı, iklim fırsatları,
        sermaye kullanımı, içsel karbon fiyatı, ücretlendirme.
  - [ ] Sektöre özgü metrikler (SASB kökenli uygulama rehberi).
  - [ ] İklim hedefleri: metrik, kapsam, baz yıl, ara hedefler, karbon kredisi kullanımı, ilerleme.
- **Geçiş kolaylıkları (ilk yıl):** yalnız iklim konusunda raporlama ve Kapsam 3'ü açıklamama gibi muafiyetler var — **doğrulanmalı**.

## 3. Sık yapılan hatalar
- Finansal önemlilik yerine etki önemliliği (GRI mantığı) kullanmak; TSRS raporunu GRI raporunun kopyası yapmak.
- Raporlama dönemi ya da konsolidasyon sınırını finansal tablolardan farklı almak.
- Kapsam 2'yi yalnız bir yöntemle vermek ve yöntemi belirtmemek.
- Vade tanımlarını yapmadan risk/fırsatı "kısa/orta/uzun" diye sınıflamak.
- Senaryo analizini yalnız nitel bırakmak ve varsayımları açıklamamak.
- Hedefi baz yıl, kapsam ve metrik olmadan vermek.
- Bankalarda finanse edilen emisyonları TSRS'de hiç açıklamamak ya da PCAF veri kalitesini belirtmemek.

## 4. Sustable karşılığı
| TSRS konusu | Ekran (`sustable-frontend/platform/esg`) | Backend |
|---|---|---|
| Dört temel alan soruları | `tsrs/home/[[...slug]]` (strateji, risk yönetimi, metrik ve hedefler, özel kategori) | `service/tsrs/TsrsOrchestrator`, `TsrsFormConfigService` |
| Risk ve fırsat değerlendirmesi | `tsrs/risk-and-opportunity`, `tsrs/scenario/[id]` | `service/tsrs/TsrsRiskAssessmentService`, `TsrsAssessmentAiOrchestrator` |
| Değer zinciri, vade tanımları | `tsrs/tanimlamalar/{deger-zinciri,vade-tanimlari}` | `service/tsrs` |
| Hedefler | `tsrs/target` | `service/tsrs` |
| Metrik tabloları ve grafikler | `tsrs/tsrs-table/*`, `tsrs/tsrs-chart` | ortak ızgara motoru `service/table/*`, `service/tsrs/ai/TsrsTableGrid*` |
| AI TSRS raporu (Word) | `ai/tsrs/[[...slug]]` | `service/tsrs/ai/TsrsAiOrchestrator`, `util/TsrsAiReportWordUtil` |
| Paydaş verisi | `tsrs/share-holders/*` | `service/shareholder/*` |
| Kapsam 1/2/3 emisyonları | `platform/carbon` | emisyon domain'i (`emission-calculator.md`) |

Kod kuralları: `sustable-backend/.claude/rules/esg-tsrs.md`.
