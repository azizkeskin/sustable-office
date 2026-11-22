# Sustable Agent Ofisi — İnceleme ve Kurulum Planı

Tarih: 2026-11-22

## 1. Mevcut durum (inceleme bulguları)

| Konu | Bulgu | Ofise etkisi |
|---|---|---|
| Depolar | `sustable-backend` (Java 17 / Spring Boot), `sustable-frontend` (Nx + Next.js, `platform/*` uygulamaları), `sustable-admin` (ayrı Next.js, port 4100), `sustable-ai` (ayrı Java servis, backend'den Feign ile çağrılıyor) ve `media-sustable` (Node/Express statik medya sunucusu). Her biri ayrı git deposu; üst klasör (`app/sustable`) başlangıçta git deposu değildi. | Ofis tek bir depoda yaşayamaz; depolar üstü bir "ofis kökü" gerekir. |
| Mevcut Claude yapılandırması | Backend'de: `yetki-denetcisi` agent'ı, 5 hook (bash koruma, flyway kilidi, spotless, derleme, TR kontrol), domain kuralları (`rules/pcaf.md`, `esg-tsrs.md`, `iso14064.md`, `emission-calculator.md`, `ems-waste.md`, `water.md`), skill'ler (`api-dokumani`, `entegrasyon-testi`, `flyway-migration`, `hata-kodu-ekle`). Frontend'de domain haritası `CLAUDE.md`'leri ve `libs/CLAUDE.md` bileşen kataloğu. Kullanıcı düzeyinde `lokal-e2e`, `capraz-inceleme`, `vakifbank-teslim`, `efr-test-ortami` skill'leri. | Sıfırdan başlamıyoruz: agent'lar bu kuralları ve skill'leri **yeniden yazmadan referans almalı**. |
| Çalışma kuralları | Dal her zaman yerel `develmaster`'dan açılır; `tasks/todo.md` + `tasks/lessons.md` akışı; plan önce, doğrulama zorunlu. | Ofis akışı bu kurallara uymalı (worktree + aynı dal adı tüm depolarda). |
| İş kaynağı | Linear bağlantısı açık; iş kodları `TECH-xxx` biçiminde. | Direktör işi doğrudan Linear issue'sundan okuyabilir. |
| Test altyapısı | Backend'de entegrasyon testi skill'i var. Frontend/admin'de Playwright bağımlılığı yok; uçtan uca deneme `lokal-e2e` skill'i + tarayıcı (Playwright MCP / tarayıcı paneli) ile yapılıyor. | QA ajanı başlangıçta tarayıcı ile doğrulama yapar; kalıcı e2e test paketi ayrı bir karar. |

## 2. Önerilen yapıya tavsiyeler

### 2.1 Teknik kısıt: alt ajan, alt ajan çağıramaz
Claude Code'da bir subagent başka bir subagent başlatamaz. "IT Direktörü → Proje Yöneticisi → Geliştirici"
zincirini iç içe subagent olarak kurmak çalışmaz. Bu yüzden:

- **IT Direktörü bir subagent değil, ana oturumun kendisi olmalı.** Bir skill (`/ofis`) olarak yazılır;
  ana oturum bu skill'i yükleyince direktör rolüne girer ve diğer tüm ajanları **kendisi** sırayla/paralel çağırır.
- **Proje Yöneticisi bir "planlayıcı" ajan olur:** görev dağılım planını (hangi depo, hangi ajan, hangi sıra,
  API sözleşmesi) dosyaya yazar ve döner; dağıtımı Direktör yapar.

### 2.2 Akış sırası değişikliği
Önerilen sırada Proje Yöneticisi analizden önce geliyor; ama işin FE/BE/AI/Admin kırılımı ancak analiz
bittiğinde netleşir. Önerilen akış:

```
Kullanıcı / Linear issue
   │
   ▼
IT Direktörü (ana oturum, /ofis) ── triyaj: hata mı, küçük iş mi, özellik mi?
   │                                   └─ küçük iş/hata → hızlı yol (analiz ve UI/UX atlanır)
   ▼
İş Analisti ──taslak──► İş Birimi (sürdürülebilirlik uzmanı) ──düzeltme/öneri──► İş Analisti (son hâl)
   │
   ▼  ◆ ONAY KAPISI 1: kullanıcı analizi onaylar
   ▼
UI/UX (yalnız ekran / Excel / PDF / Word çıktısı varsa)
   │
   ▼
Proje Yöneticisi ── görev dağılımı + API sözleşmesi
   │
   ├──► Backend Developer ─┐
   ├──► AI Developer      ─┤  (sözleşme sabit olduğu için paralel)
   ├──► Frontend Developer ┤  (platform/* ve/veya sustable-admin)
   ▼                        ▼
QA Developer ── kabul kriterlerine göre uçtan uca test; hata varsa ilgili geliştiriciye geri
   │
   ▼
Kod İnceleyici (+ backend'de mevcut yetki-denetcisi)
   │
   ▼  ◆ ONAY KAPISI 2: kullanıcı commit / merge'ü onaylar
   ▼
IT Direktörü: özet, Linear güncellemesi, tasks/lessons.md
```

### 2.3 Eklenmesi önerilen roller
| Rol | Neden |
|---|---|
| **Kod İnceleyici** | Geliştiricinin kendi işini onaylaması zayıf bir kontrol. Ayrı bağlamda bakan bir inceleyici, QA'nın yakalayamadığı kod kalitesi/güvenlik sorunlarını yakalar. Backend tarafında mevcut `yetki-denetcisi` bu rolün parçası olarak çağrılır. |
| **AI Developer** | Proje Yöneticisinin dağıttığı alanlardan biri "AI modülü", ama ekipte karşılığı yok. `sustable-ai` ayrı bir servis; istem (prompt) tasarımı, çıktı doğrulama (`AiOutputValidator`, `AiPromptNumbers` vb.) ve Feign sözleşmesi ayrı uzmanlık. İş azsa Backend Developer'a bir "AI kipi" olarak da eklenebilir. |
| DevOps / Teslim (opsiyonel, şimdilik ajan değil) | `helm/`, `k8s/`, `vakifbank-teslim` ve `efr-test-ortami` skill'leri zaten var. Ajan yerine Direktör bu skill'leri gerektiğinde çağırır. |

### 2.4 Rol birleştirme / sadeleştirme önerileri
- Frontend Developer hem `sustable-frontend` hem `sustable-admin`'i kapsayabilir (ikisi de Next.js + MUI);
  admin işleri artarsa ayrı ajan yapılır. Ajan tanımında iki deponun farkları (Nx monorepo vs tek uygulama) yazılmalı.
- UI/UX'in Excel/PDF/Word çıktı tasarımları **backend'de** üretiliyor (`util/excel`, `TableGridWordWriter` vb.).
  UI/UX'in çıktı tasarımı bu yüzden Backend Developer'a da girdi olmalı (yalnız Frontend'e değil).

### 2.5 Ajanlar arası iletişim: dosya tabanlı sözleşme
Subagent'lar birbirini görmez; Direktör'e yalnızca kısa özet döner. Ortak hafıza dosyalar olmalı.
Her iş için bir klasör:

```
ofis/isler/<TECH-xxx>-<kisa-ad>/
  00-talep.md            Direktör: ham talep, triyaj kararı, kapsam
  01-analiz.md           İş Analisti: iş kuralları (IK-1..n), kabul kriterleri (KK-1..n), veri/rol/yetki etkisi
  02-is-birimi.md        İş Birimi: standart uyumu (GRI/TSRS/PCAF/ISO 14064/GHG), düzeltme ve öneriler
  03-tasarim.md          UI/UX: ekran akışı, alanlar, durumlar (boş/hata/yükleniyor), Excel/PDF/Word düzeni
  04-gorev-dagilimi.md   Proje Yöneticisi: depo bazında görevler, sıra, API sözleşmesi (uç, DTO, hata kodları)
  05-gelistirme-<alan>.md Geliştiriciler: yapılanlar, değişen dosyalar, dal adı, açık noktalar
  06-test-raporu.md      QA: KK bazında geçti/kaldı, kanıt (ekran görüntüsü, istek/yanıt)
  07-inceleme.md         Kod İnceleyici: bulgular
```

Numaralı **kabul kriterleri (KK-n)** tüm zincirin bağlantı noktasıdır: UI/UX tasarımı, geliştirme ve QA testi
aynı KK numaralarına referans verir.

### 2.6 Ofisin konumu
- Ofis kökü: `app/sustable/` (üç depoyu kapsayan klasör). Burada `git init` ile küçük bir **`sustable-ofis`**
  deposu açılması önerilir (yalnız `.claude/`, `CLAUDE.md`, `ofis/` izlenir; alt depolar `.gitignore`'a girer).
- Analiz/tasarım/planlama ajanları ofis kökünde çalışır.
- Geliştiriciler, her depoda yerel `develmaster`'dan açılmış **worktree**'lerde, tüm depolarda **aynı dal adıyla**
  çalışır (ör. `feature/TECH-512-...`).
- Dikkat: Backend'in hook'ları (`.claude/settings.json`) ofis kökünden açılan oturumda otomatik devreye girmez.
  İki seçenek: (a) Backend Developer ajanının tanımına aynı hook'lar eklenir, (b) geliştirme adımı backend
  deposunda açılan ayrı bir oturumda yapılır. Önerim (a); hook betikleri backend deposundan referans alınır, kopyalanmaz.

## 3. Ajan tanımları (özet)

| Ajan (dosya adı) | Model | Araçlar | Okur | Yazar | Not |
|---|---|---|---|---|---|
| IT Direktörü (`/ofis` skill, ana oturum) | oturum modeli | hepsi + Agent | her şey | `00-talep.md`, özet | Triyaj, akış, onay kapıları, Linear |
| `proje-yoneticisi` | opus | Read, Grep, Glob, Write (yalnız `ofis/`) | 01–03, AGENTS.md domain haritaları | `04-gorev-dagilimi.md` | Kod yazmaz |
| `is-birimi` | opus | Read, Grep, Glob, WebSearch, Write (yalnız `ofis/`) | 01, backend `rules/*.md`, ofis domain bilgi tabanı | `02-is-birimi.md` | GRI, TSRS 1/2, PCAF, ISO 14064, GHG Protokolü, EMS/atık/su |
| `is-analisti` | opus | Read, Grep, Glob, Write (yalnız `ofis/`) | talep, mevcut kod/domain haritası | `01-analiz.md` | Mevcut davranışı koddan doğrular |
| `ui-ux` | sonnet/opus | Read, Grep, Glob, Write | 01, 02, `libs/CLAUDE.md` bileşen kataloğu | `03-tasarim.md` (+ istenirse HTML maket) | Var olan bileşenleri önce kullanır |
| `backend-developer` | opus | hepsi | 01, 03, 04 | kod + `05-gelistirme-backend.md` | Flyway, hata kodu, API dokümanı skill'lerini kullanır |
| `ai-developer` | opus | hepsi | 01, 04 | `sustable-ai` kodu + rapor | İstem ve çıktı doğrulama |
| `frontend-developer` | sonnet/opus | hepsi | 01, 03, 04, frontend/admin CLAUDE.md'leri | kod + rapor | Barrel kuralı, i18n (tr/en), Prettier |
| `qa-developer` | sonnet | Read, Bash, Playwright MCP, Write (yalnız `ofis/`) | 01 (KK listesi), 04, 05 | `06-test-raporu.md` | `lokal-e2e` + `entegrasyon-testi` skill'leri |
| `kod-inceleyici` | opus | Read, Grep, Glob, Bash (salt okuma) | diff, 01, 04 | `07-inceleme.md` | Backend'de `yetki-denetcisi`'ni de çağırtır |

Her ajan dosyasında olması gerekenler: rol, girdi dosyaları, çıktı dosyası ve şablonu, "yapmayacakların"
(ör. analist kod yazmaz, QA kodu düzeltmez — geri bildirir), bitiş ölçütü ve Direktör'e döneceği kısa özet biçimi.
Tüm metinler Türkçe.

### İş Birimi için bilgi tabanı
- `ofis/bilgi/` altında standart başına **özet kontrol listeleri** (ör. `tsrs.md`, `gri.md`, `pcaf.md`,
  `iso14064.md`, `ghg-kapsam3.md`): hangi açıklama zorunlu, hangi hesap yöntemi, sık yapılan hatalar,
  Sustable'da karşılığı olan ekran/servis. Standart metinleri kopyalanmaz; kendi özetimiz tutulur.
- Backend'deki `rules/*.md` dosyaları kod tarafını anlatır; bilgi tabanı iş tarafını. İkisi birbirine bağlantı verir.

## 4. Kurulum planı

### Faz 0 — Kararlar (kurulumdan önce)
1. Ofis kökü `app/sustable/` olsun mu ve `sustable-ofis` adıyla git deposu açılsın mı?
2. AI Developer ayrı ajan mı, Backend Developer'ın bir kipi mi?
3. İş girişi: yalnız sohbet mi, yoksa Linear issue (`TECH-xxx`) da mı?
4. Onay kapıları: analiz sonrası ve merge öncesi (önerilen iki kapı) yeterli mi?

### Faz 1 — İskelet (yarım gün)
- `app/sustable/.claude/{agents,skills}/`, `app/sustable/CLAUDE.md` (ofis anayasası: roller, akış,
  dosya sözleşmesi, dal kuralı, dil kuralı), `ofis/sablonlar/` (00–07 şablonları), `ofis/isler/`, `ofis/bilgi/`.
- `.gitignore`: `sustable-backend/`, `sustable-frontend/`, `sustable-admin/`.

### Faz 2 — Analiz katmanı ajanları
- `is-analisti`, `is-birimi`, `ui-ux`, `proje-yoneticisi` tanımları + İş Birimi bilgi tabanının ilk sürümü
  (önce TSRS ve PCAF; en çok iş gelen alanlar).
- Deneme: geçmiş bir işi (ör. kapanmış bir TECH işi) yalnız analiz katmanından geçirip çıktıyı gerçek işle karşılaştırmak.

### Faz 3 — Geliştirme ve kalite katmanı
- `backend-developer`, `frontend-developer`, `ai-developer`, `qa-developer`, `kod-inceleyici` tanımları.
- Backend Developer'a backend hook'larının bağlanması; mevcut skill'lerin (flyway, hata kodu, API dokümanı,
  entegrasyon testi, lokal-e2e) ajan tanımlarında referanslanması.

### Faz 4 — Direktör skill'i (`/ofis`)
- Triyaj kuralları (hata / küçük iş / özellik), hızlı yol, ajan çağırma sırası, paralel adımlar,
  onay kapıları, QA'dan geri dönüş döngüsü (en fazla 2 tur, sonra kullanıcıya sor), kapanışta
  `tasks/lessons.md` ve Linear güncellemesi.

### Faz 5 — Pilot ve ayar
- Gerçek, küçük-orta boy bir işle uçtan uca pilot (ör. tek ekran + tek uç).
- Her adımda: çıktı yeterli mi, gereksiz adım var mı, token maliyeti. Ajan tanımları buna göre sıkılaştırılır.

### Faz 6 — Genişletme (opsiyonel)
- Kalıcı e2e test paketi (frontend/admin'e Playwright projesi) — QA'nın testlerinin depoya girmesi için.
- Akış oturmuşsa, tekrarlanan zinciri Workflow betiğine dönüştürmek (paralel geliştirme + doğrulama).
- Admin işi artarsa ayrı `admin-developer`.

## 5. Riskler
- **Maliyet:** Her iş için 6–9 ajan çağrısı. Hızlı yol ve triyaj zorunlu; küçük iş tüm ofisten geçmemeli.
- **Bağlam kaybı:** Ajanlar yalnız dosyalardan beslenir; şablonlar zayıfsa zincir kopar. KK numaraları bu yüzden zorunlu.
- **Paralel çakışma:** FE ve BE paralel çalışırken API sözleşmesi değişirse iki taraf ayrışır. Sözleşme
  `04-gorev-dagilimi.md`'de sabitlenir; değişiklik yalnız Proje Yöneticisi üzerinden.
- **Hook'lar:** Ofis kökünden çalışırken depo hook'larının devre dışı kalması (bkz. 2.6).
