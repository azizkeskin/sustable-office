# Sustable Agent Ofisi

Bu klasör (`app/sustable/`) Sustable ürünü için agent ofisinin köküdür. Ofis deposu (`sustable-ofis`)
yalnız ofis dosyalarını izler; ürün kodu aşağıdaki ayrı git depolarındadır.

| Depo | Yol | Teknoloji | Ayrıntı |
|---|---|---|---|
| Backend | `sustable-backend/` | Java 17, Spring Boot | `sustable-backend/AGENTS.md`, `CLAUDE.md`, `.claude/rules/*.md` |
| Frontend | `sustable-frontend/` | Nx + Next.js (`platform/*`) | `sustable-frontend/AGENTS.md`, `platform/<app>/CLAUDE.md`, `libs/CLAUDE.md` |
| Admin paneli | `sustable-admin/` | Next.js + MUI (port 4100) | `sustable-admin/src/` |
| AI servisi | `sustable-ai/` | Java, Spring Boot | `sustable-ai/README.md` (AGENTS.md / CLAUDE.md henüz yok) |
| Medya sunucusu | `media-sustable/` | Node 22, Express (statik yayın, `media.sustable.com`) | `media-sustable/README.md` |

Bir depoda çalışmadan önce o deponun `AGENTS.md` ve `CLAUDE.md` dosyalarını oku; depo kuralları bu
dosyadaki kuralların üstündedir.

## Dil

Ofis içindeki tüm metinler (iş dosyaları, raporlar, ajan özetleri) Türkçe yazılır. Kod tanımlayıcıları,
komutlar ve dosya yolları olduğu gibi kalır; commit mesajları ilgili deponun alışkanlığına uyar.

## Roller

| Rol | Biçim | Görev |
|---|---|---|
| IT Direktörü | Ana oturum, `/ofis` skill'i | Triyaj, akışı yürütme, ajanları çağırma, onay kapıları, kapanış |
| Proje Yöneticisi | `proje-yoneticisi` ajanı | Görev dağılımı ve API sözleşmesi; kod yazmaz |
| İş Birimi | `is-birimi` ajanı | GRI, TSRS, PCAF, ISO 14064, GHG Protokolü, çevre yönetimi açısından inceleme ve öneri |
| İş Analisti | `is-analisti` ajanı | İş kuralları, kabul kriterleri, iş planı |
| UI/UX | `ui-ux` ajanı | Ekran tasarımı; Excel, PDF, Word çıktı düzeni |
| Backend Developer | `backend-developer` ajanı | `sustable-backend` ve `media-sustable` geliştirmesi |
| AI Developer | `ai-developer` ajanı | `sustable-ai` geliştirmesi, istem ve çıktı doğrulama |
| Frontend Developer | `frontend-developer` ajanı | `sustable-frontend` ve `sustable-admin` geliştirmesi |
| QA Developer | `qa-developer` ajanı | Kabul kriterlerine göre uçtan uca test; kodu düzeltmez, geri bildirir |
| Kod İnceleyici | `kod-inceleyici` ajanı | Diff incelemesi; backend'de `yetki-denetcisi`'ni de çalıştırır |

Alt ajanlar başka alt ajan çağıramaz. Bütün çağrıları IT Direktörü (ana oturum) yapar.

## Akış

1. **Triyaj (Direktör):** Talep sohbetten ya da Linear issue'sundan (`TECH-xxx`) gelir. İş klasörü açılır,
   `00-talep.md` yazılır, iş türü belirlenir:
   - **Hata / küçük iş → hızlı yol:** analiz ve UI/UX atlanır; kısa bir `01-analiz.md` (yalnız KK listesi)
     yeterlidir, doğrudan ilgili geliştiriciye gider.
   - **Özellik:** tam akış.
2. **Analiz:** İş Analisti `01-analiz.md` taslağını yazar → İş Birimi `02-is-birimi.md` ile inceler →
   İş Analisti düzeltmeleri `01-analiz.md`'ye işler.
3. **◆ Onay kapısı 1:** Kullanıcı analizi onaylar. Onaysız geliştirmeye geçilmez.
4. **Tasarım:** Ekran ya da Excel/PDF/Word çıktısı varsa UI/UX `03-tasarim.md`'yi yazar.
5. **Görev dağılımı:** Proje Yöneticisi `04-gorev-dagilimi.md`'yi yazar (depo bazında görevler, sıra,
   API sözleşmesi).
6. **Geliştirme:** Sözleşme sabitse Backend, AI ve Frontend paralel çalışır; her biri
   `05-gelistirme-<alan>.md` raporunu yazar.
7. **Test:** QA `06-test-raporu.md`'yi yazar. Kalan KK varsa ilgili geliştiriciye geri döner.
   En fazla 2 tur; sonra kullanıcıya sorulur.
8. **İnceleme:** Kod İnceleyici `07-inceleme.md`'yi yazar; önemli bulgular geliştiriciye döner.
9. **◆ Onay kapısı 2:** Commit, push ve merge yalnız kullanıcı onayıyla yapılır.
10. **Kapanış (Direktör):** Kullanıcıya özet, gerekirse Linear güncellemesi, öğrenilen ders varsa ilgili
    deponun `tasks/lessons.md` dosyası.

## İş dosyası sözleşmesi

Her iş `ofis/isler/<TECH-xxx>-<kisa-ad>/` klasöründe yürür (Linear kodu yoksa `IS-<yyyymmddSSdd>-<kisa-ad>`).
Dosyalar `ofis/sablonlar/` altındaki şablonlardan kopyalanır.

| Dosya | Yazan | İçerik |
|---|---|---|
| `00-talep.md` | Direktör | Ham talep, triyaj kararı, kapsam, dal adı |
| `01-analiz.md` | İş Analisti | İş kuralları (IK-n), kabul kriterleri (KK-n), rol/yetki ve veri etkisi |
| `02-is-birimi.md` | İş Birimi | Standart uyumu, düzeltmeler, öneriler |
| `03-tasarim.md` | UI/UX | Ekran akışı, alanlar, durumlar, çıktı düzeni |
| `04-gorev-dagilimi.md` | Proje Yöneticisi | Görevler, sıra, API sözleşmesi |
| `05-gelistirme-<alan>.md` | Geliştirici | Yapılanlar, değişen dosyalar, doğrulama, açık noktalar |
| `06-test-raporu.md` | QA | KK bazında sonuç ve kanıt |
| `07-inceleme.md` | Kod İnceleyici | Bulgular ve önem derecesi |

Kurallar:
- **KK numaraları bağlayıcıdır.** Tasarım, geliştirme raporu ve test raporu aynı KK numaralarına atıf yapar.
  KK eklemek ya da değiştirmek yalnız İş Analisti üzerinden olur.
- **API sözleşmesi** `04-gorev-dagilimi.md`'de sabitlenir; değişiklik yalnız Proje Yöneticisi üzerinden.
- Her ajan yalnız kendi dosyasını yazar; diğerlerini okur.
- Ajan, Direktör'e en fazla 10 satırlık bir özet döner: ne yaptı, hangi dosyayı yazdı, açık soru var mı.

## Dal ve worktree kuralı

- İşin dokunduğu tüm depolarda **aynı dal adı** kullanılır (ör. `feature/TECH-512-kisa-ad`). Dal, deponun
  **yerel** taban dalından açılır (`origin/...` taban alınmaz):

  | Depo | Taban dalı | İş dalı açılmayacak dallar |
  |---|---|---|
  | `sustable-backend` | `develmaster` | `test`, `main` |
  | `sustable-frontend` | `develmaster` | `develop`, `main` |
  | `sustable-admin` | `main` (doğrulanmalı) | `test` |
  | `sustable-ai` | `master` | — |
  | `media-sustable` | `main` | — |

- Geliştirme her depoda ayrı bir worktree'de yapılır: `<depo>/.claude/worktrees/<iş-kodu-küçük-harf>`.
  Açma: `git -C <depo> worktree add .claude/worktrees/<kod> -b <dal> <taban-dalı>` (dal varsa `-b`'siz).
  Ana çalışma kopyasının dalı değiştirilmez.

## Bilgi tabanı

`ofis/bilgi/` İş Birimi'nin standart özetlerini tutar (iş tarafı). Kod tarafı bilgisi
`sustable-backend/.claude/rules/*.md` dosyalarındadır; iki taraf birbirine bağlantı verir, içerik kopyalanmaz.
Standart metinleri olduğu gibi aktarılmaz; yalnız kendi özetlerimiz ve kontrol listelerimiz tutulur.
