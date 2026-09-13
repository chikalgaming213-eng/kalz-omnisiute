# Kalz OmniSuite

Kalz OmniSuite adalah blueprint dan foundation untuk aplikasi desktop native Linux berbasis Python, PySide6/QML/QSS. Fokusnya adalah otomasi workstation yang dapat diaudit: deteksi distro dan desktop environment, tool registry, konfigurasi, backup, scheduling, reporting, dan integrasi KDE Plasma, XFCE, GNOME, serta fallback generic.

## Prinsip operasi

Semua perubahan sistem bersifat **preview-first** dan **consent-gated**. Operasi dijalankan melalui argv terstruktur tanpa shell interpolation, dicatat dalam audit hash-chain, dapat dihentikan melalui panic control, dan ketika gagal hanya melakukan abort, diagnosis, serta recovery plan. Tidak ada perilaku merusak atau penghapusan data otomatis.

## Struktur

Paket `kalz/automation` mengelola deteksi dan health workflows. `kalz/de_integration` berisi adapter per DE. `kalz/tools` menyimpan registry 200+ tool yang dikelompokkan ke security, system, devops, multimedia, office, disk, package, monitoring, backup, virtualization, dan kategori lain. `kalz/ui` adalah shell native PySide6/QML/QSS. `kalz/system` menampung service definitions, sedangkan `packaging` dan `scripts` memuat pipeline distribusi.

## Roadmap

| Versi | Sasaran |
|---|---|
| v0.1 | scaffold, detector, registry, audit, dry-run planner, CLI headless |
| v0.2 | apt/dnf/pacman/zypper/flatpak/snap adapters dengan consent |
| v0.3 | PySide6/QML dashboard, QSS auto-theme, task monitor |
| v0.5 | automation install/config/heal/update/backup/report/scope |
| v0.7 | KDE/XFCE/GNOME adapters, plugin API, scheduler, DB migrations |
| v1.0 | 200+ tool workflows, deb/rpm/AppImage/Flatpak/Snap packaging |
| v1.3 | DE service integrations, accessibility, offline catalogs |
| v1.5 | headless fleet inventory dan encrypted exports |
| v2.0 | plugin marketplace design, reproducible lab profiles |
| v2.5 | digital twin workstation/lab model dan policy simulation |

## Development

```bash
python -m kalz --doctor
python -m kalz --plan curl git
pytest -q
```
