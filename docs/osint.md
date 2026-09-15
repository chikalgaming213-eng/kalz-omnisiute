# OSINT Catalog, Installation, and Safe Execution Policy

Kalz OmniSuite mencatat repository OSINT yang diminta sebagai **catalog terverifikasi**, bukan sebagai instalasi otomatis. Setiap tool pihak ketiga harus dipasang secara terpisah oleh operator pada environment yang sesuai. Kalz hanya menghasilkan metadata, scope-safe plan, dan audit boundary; Kalz tidak menjalankan pemindaian atau pengumpulan data terhadap target nyata secara otomatis.

> Gunakan tool hanya terhadap aset yang Anda miliki atau yang secara eksplisit Anda diberi wewenang untuk uji. Publicly reachable tidak sama dengan authorized.

## Prasyarat Umum

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip pipx curl jq
pipx ensurepath
```

Tambahan umum untuk tool Go:

```bash
sudo apt install -y golang-go
export GOPATH="$HOME/go"
export PATH="$PATH:$GOPATH/bin"
```

Tambahan umum untuk containerized platform:

```bash
sudo apt install -y docker.io docker-compose-plugin
sudo usermod -aG docker "$USER"
```

Logout/login diperlukan setelah perubahan group Docker. Jangan menjalankan Docker socket yang terekspos ke jaringan publik tanpa hardening.

Semua command instalasi di bawah ini adalah **operator-run commands**. Jalankan setelah meninjau license, release, checksum, kebutuhan credential, dan policy organisasi.

## Installation Matrix

| Entry | Upstream | Metode utama | Credential/API | Verifikasi |
|---|---|---|---|---|
| Awesome OSINT | [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | `git clone` curated list | tidak diperlukan | cek `README.md` |
| Awesome OSINT Tools | [oryon-osint/awesome-osint-tools](https://github.com/oryon-osint/awesome-osint-tools) | `git clone` curated list | tidak diperlukan | cek `README.md` |
| awesome_osint | [NCols/awesome_osint](https://github.com/NCols/awesome_osint) | `git clone` curated list | tidak diperlukan | cek `README.md` |
| Sherlock | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | `pipx` atau Docker | umumnya tidak; rate limits berlaku | `sherlock --help` |
| Maigret | [soxoj/maigret](https://github.com/soxoj/maigret) | `pipx` | umumnya tidak | `maigret --help` |
| GHunt | [mxrch/GHunt](https://github.com/mxrch/GHunt) | `pipx`/source sesuai upstream | Google session/cookies dapat diperlukan; jangan masukkan ke Kalz | `ghunt --help` |
| PhoneInfoga | [sundowndev/phoneinfoga](https://github.com/sundowndev/phoneinfoga) | release binary atau Docker | provider API opsional | `phoneinfoga version` |
| OWASP Amass | [OWASP/Amass](https://github.com/OWASP/Amass) | binary release atau Go | data sources opsional | `amass -h` |
| Subfinder | [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) | binary release atau Go | banyak passive source memerlukan API key | `subfinder -h` |
| theHarvester | [laramies/theHarvester](https://github.com/laramies/theHarvester) | `pipx` atau source | search/API providers opsional | `theHarvester --help` |
| SpiderFoot | [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) | source + requirements atau release | module API keys opsional | `sf.py -h` |
| Recon-ng | [lanmaster53/recon-ng](https://github.com/lanmaster53/recon-ng) | source + requirements | marketplace modules dapat memerlukan keys | `recon-ng --help` |
| BBOT | [blacklanternsecurity/bbot](https://github.com/blacklanternsecurity/bbot) | `pipx` | module/provider keys opsional | `bbot --help` |
| Photon | [s0md3v/Photon](https://github.com/s0md3v/Photon) | source atau Docker | API keys tidak selalu diperlukan | `python photon.py -h` |
| Crawl4AI | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) | `pip` + browser setup atau Docker | LLM provider opsional | `crawl4ai-setup` |
| Firecrawl | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | self-host Docker Compose atau hosted service | hosted API key; self-host config | health endpoint/docs |
| MISP | [MISP/MISP](https://github.com/MISP/MISP) | Docker Compose atau deployment guide | instance auth dan feeds | health/login check |
| OpenCTI | [OpenCTI-Platform/opencti](https://github.com/OpenCTI-Platform/opencti) | Docker Compose | app secrets, connector config | health/API check |
| Awesome Threat Intelligence | [hslatman/awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence) | `git clone` curated list | tidak diperlukan | cek `README.md` |

## 1. Curated Lists

Curated lists berisi referensi, bukan executable tools. Clone ke direktori terpisah:

```bash
mkdir -p "$HOME/opt/kalz-osint/sources"
cd "$HOME/opt/kalz-osint/sources"
git clone https://github.com/jivoi/awesome-osint.git
git clone https://github.com/oryon-osint/awesome-osint-tools.git
git clone https://github.com/NCols/awesome_osint.git
git clone https://github.com/hslatman/awesome-threat-intelligence.git
```

Verifikasi:

```bash
for d in awesome-osint awesome-osint-tools awesome_osint awesome-threat-intelligence; do
  test -s "$d/README.md" && printf '%s: ok\n' "$d"
done
```

Jangan menganggap link di curated list aman atau aktif. Review setiap destination sebelum mengunjunginya.

## 2. Identity and Username Tools

### Sherlock

Dengan isolated pipx environment:

```bash
pipx install sherlock-project
sherlock --help
```

Alternatif Docker sesuai dokumentasi upstream:

```bash
docker run --rm -it sherlock/sherlock --help
```

### Maigret

```bash
pipx install maigret
maigret --help
```

### GHunt

```bash
pipx install ghunt
ghunt --help
```

GHunt dapat membutuhkan session atau cookies untuk capability tertentu. Jangan menyalin cookies ke `.env`, audit log, issue, atau output Kalz. Gunakan account dan target yang authorized.

### PhoneInfoga

Gunakan release resmi atau container resmi upstream. Contoh verifikasi container:

```bash
docker pull sundowndev/phoneinfoga:latest
docker run --rm sundowndev/phoneinfoga:latest version
```

Tag `latest` tidak ideal untuk production. Untuk release tetap, gunakan digest atau version tag yang sudah direview.

## 3. Domain, IP, and Recon Tools

### OWASP Amass

Binary release upstream adalah pilihan paling sederhana. Jika memakai Go, sesuaikan path dengan versi upstream:

```bash
go install -v github.com/owasp-amass/amass/v4/...@latest
amass -h
```

### Subfinder

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
subfinder -h
```

Sebagian passive providers memerlukan API key. Konfigurasikan key hanya pada config directory permission-restricted dan jangan menaruhnya pada command history.

### theHarvester

```bash
pipx install theHarvester
theHarvester --help
```

Jika package tidak tersedia pada distro Anda, gunakan source checkout dan requirements upstream pada virtual environment terpisah.

### SpiderFoot

```bash
git clone https://github.com/smicallef/spiderfoot.git "$HOME/opt/kalz-osint/spiderfoot"
cd "$HOME/opt/kalz-osint/spiderfoot"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python sf.py -h
```

SpiderFoot memiliki banyak module provider. API keys module bukan bagian dari Kalz secret store dan harus dikelola terpisah.

### Recon-ng

```bash
git clone https://github.com/lanmaster53/recon-ng.git "$HOME/opt/kalz-osint/recon-ng"
cd "$HOME/opt/kalz-osint/recon-ng"
python3 -m venv .venv
source .venv/bin/activate
pip install -r REQUIREMENTS
recon-ng --help
```

Marketplace modules dapat memiliki license, credential, dan rate-limit sendiri. Review sebelum instalasi.

### BBOT

```bash
pipx install bbot
bbot --help
```

BBOT adalah scanner recursive yang dapat menghasilkan traffic signifikan. Mulai dari configuration review dan passive scope, bukan active enumeration.

## 4. Web Crawling

### Photon

```bash
git clone https://github.com/s0md3v/Photon.git "$HOME/opt/kalz-osint/Photon"
cd "$HOME/opt/kalz-osint/Photon"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python photon.py -h
```

Photon juga menyediakan Docker workflow pada upstream. Gunakan volume terisolasi dan target authorized saja.

### Crawl4AI

```bash
python3 -m venv "$HOME/opt/kalz-osint/crawl4ai-venv"
source "$HOME/opt/kalz-osint/crawl4ai-venv/bin/activate"
pip install crawl4ai
crawl4ai-setup
python -c 'import crawl4ai; print("crawl4ai import ok")'
```

Browser setup dapat mengunduh browser binaries. Review storage dan network policy sebelum menjalankannya.

### Firecrawl

Firecrawl dapat digunakan sebagai hosted service atau self-hosted. Untuk self-hosting, gunakan Compose dan environment template dari upstream:

```bash
git clone https://github.com/firecrawl/firecrawl.git "$HOME/opt/kalz-osint/firecrawl"
cd "$HOME/opt/kalz-osint/firecrawl"
# Review .env.example dan docker-compose files terlebih dahulu.
docker compose config
docker compose up -d
```

Jangan mengekspos service ke internet sebelum menambahkan authentication, TLS, rate limits, secret rotation, dan network isolation.

## 5. Threat Intelligence Platforms

### MISP

```bash
git clone https://github.com/MISP/MISP.git "$HOME/opt/kalz-osint/MISP"
cd "$HOME/opt/kalz-osint/MISP"
# Pilih deployment method resmi yang sesuai distro dan review compose/config.
docker compose config
```

MISP adalah platform server, bukan sekadar CLI. Siapkan persistent storage, database, instance secret, feed governance, backup, dan access control sebelum `docker compose up`.

### OpenCTI

```bash
git clone https://github.com/OpenCTI-Platform/opencti.git "$HOME/opt/kalz-osint/opencti"
cd "$HOME/opt/kalz-osint/opencti"
docker compose config
```

OpenCTI umumnya bergantung pada service pendukung dan connector. Ikuti deployment matrix upstream; jangan menjalankan default compose tanpa meninjau secret, ports, volumes, dan connector egress.

## Kalz Integration Boundary

Kalz menyimpan metadata tool melalui:

```bash
python -m kalz --osint
```

Kalz planner hanya membuat plan:

```python
from kalz.osint.planner import OSINTPlanner
plan = OSINTPlanner().plan("Sherlock", "example.org")
print(plan.to_dict())
```

Plan mencakup:

1. validasi consent dan authorized scope;
2. public-source-only collection boundary;
3. audit record untuk request, target, dan tool;
4. explicit operator approval sebelum future execution adapter;
5. redaction sebelum storage.

Tidak ada entrypoint Kalz yang menjalankan `sherlock`, `amass`, `bbot`, `misp`, `opencti`, atau tool lain pada target hanya karena tool tersebut ada di catalog.

## Credential Matrix

| Credential | Disimpan di | Jangan dilakukan |
|---|---|---|
| Search/provider API key | secret manager atau config mode 0600 | jangan taruh di CLI args atau Git |
| GHunt session/cookies | isolated user profile | jangan masukkan ke Kalz audit/log |
| MISP auth | instance secret manager | jangan expose port/API publik |
| OpenCTI connector secret | protected `.env`/secret manager | jangan commit Compose `.env` |
| Firecrawl hosted key | environment secret | jangan embed di frontend/QML |
| LLM provider key | `OPENAI_API_KEY` atau secret manager | jangan paste ke chat/source |

## Verification Checklist

```bash
python -m kalz --osint
python -m compileall -q kalz tests scripts
pytest -q tests/integration/test_osint_catalog.py
git diff --check
```

Untuk setiap tool yang benar-benar dipasang:

- pin version atau digest;
- simpan install log di luar source tree;
- jalankan `--help`, `version`, atau health check;
- cek executable path dengan `command -v`;
- review permissions dan outbound network;
- gunakan target test yang Anda miliki;
- simpan output ter-redact;
- catat approval dan scope pada audit chain.

## Troubleshooting

### `pipx: command not found`

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Buka shell baru setelah PATH berubah.

### `go: command not found`

Pasang Go dari package manager distro, lalu pastikan `$GOPATH/bin` ada di PATH.

### Docker permission denied

Gunakan rootless Docker atau konfigurasi group secara sadar. Jangan mengatasi error dengan mengekspos Docker daemon TCP.

### API key provider gagal

Periksa nama environment/config yang diwajibkan upstream. Jangan menyalin key ke issue atau log. Mulai dengan module/provider yang tidak membutuhkan key.

### Browser automation gagal

Untuk Crawl4AI/Firecrawl, cek browser dependency, sandbox policy, storage, dan egress. Jangan menonaktifkan sandbox sebagai shortcut pada host production.

## References

- [Awesome OSINT](https://github.com/jivoi/awesome-osint)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [Maigret](https://github.com/soxoj/maigret)
- [GHunt](https://github.com/mxrch/GHunt)
- [PhoneInfoga](https://github.com/sundowndev/phoneinfoga)
- [OWASP Amass](https://github.com/OWASP/Amass)
- [Subfinder](https://github.com/projectdiscovery/subfinder)
- [theHarvester](https://github.com/laramies/theHarvester)
- [SpiderFoot](https://github.com/smicallef/spiderfoot)
- [Recon-ng](https://github.com/lanmaster53/recon-ng)
- [BBOT](https://github.com/blacklanternsecurity/bbot)
- [Photon](https://github.com/s0md3v/Photon)
- [Crawl4AI](https://github.com/unclecode/crawl4ai)
- [Firecrawl](https://github.com/firecrawl/firecrawl)
- [MISP](https://github.com/MISP/MISP)
- [OpenCTI](https://github.com/OpenCTI-Platform/opencti)
- [Awesome Threat Intelligence](https://github.com/hslatman/awesome-threat-intelligence)
