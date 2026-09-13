from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ToolSpec:
    name: str
    category: str
    packages: tuple[str, ...]
    risk: str
    description: str


_RAW = {
"security": "nmap masscan nikto nuclei zap sqlmap gobuster ffuf wpscan hydra john hashcat aircrack-ng kismet tcpdump tshark wireshark mitmproxy metasploit searchsploit lynis sslscan sslyze testssl testdisk autopsy volatility binwalk foremost sleuthkit ghidra radare2 rizin gdb objdump strings openssl gpg trivy kube-bench kube-hunter adb frida apktool jadx",
"network": "curl wget httpie netcat ncat socat scapy hping3 arping ettercap bettercap dsniff macchanger iodine mtr traceroute iperf3 nmap bind9-dnsutils whois dnsrecon dnsenum fierce amass subfinder assetfinder httpx dnsx naabu theharvester recon-ng",
"web": "dirb wfuzz commix xsstrike dalfox arjun paramspider kiterunner feroxbuster whatweb wafw00f cmseek graphql-cop joomscan droopescan wapiti arachni skipfish w3af cadaver davtest nikto webshell-detector",
"devops": "docker podman kubectl helm minikube terraform ansible packer vagrant git git-lfs gh jq yq tmux screen rsync ssh scp rclone make cmake ninja bazel",
"sysadmin": "htop btop iotop iftop nload ncdu lsof strace ltrace sysstat procps psmisc util-linux coreutils findutils grep sed gawk ripgrep fd fzf tree eza bat man-db",
"desktop": "kdeconnect plasma-workspace dolphin konsole krunner systemsettings xfce4-panel thunar xfce4-terminal gigolo mousepad ristretto gnome-shell nautilus gnome-terminal gnome-control-center dconf-editor gvfs",
"multimedia": "ffmpeg ffplay vlc mpv handbrake imagemagick graphicsmagick sox audacity obs-studio kdenlive blender inkscape krita gimp darktable",
"office": "libreoffice onlyoffice pandoc texlive hunspell aspell okular evince xournalpp pdfarranger wkhtmltopdf",
"disk": "gparted parted fdisk gdisk lsblk smartmontools nvme hdparm ddrescue clonezilla testdisk photorec exfatprogs ntfs-3g btrfs-progs e2fsprogs xfsprogs",
"package": "apt apt-file aptitude nala dpkg snap flatpak discover dnf rpm yum pacman yay paru zypper pipx pip npm pnpm cargo gem",
"monitoring": "prometheus-node-exporter collectd nagios-nrpe zabbix-agent telegraf grafana loki journalctl dstat glances atop sysdig wireshark",
"backup": "restic borgbackup duplicity deja-dup timeshift rsnapshot kopia bacula amanda rdiff-backup tar gzip bzip2 xz zstd zip unzip",
"virtualization": "qemu-system libvirt virt-manager virsh virt-install incus lxc lxd vboxmanage vmware docker-machine",
"database": "sqlite3 psql mysql mariadb mongosh redis-cli redis-server pg_dump mysqldump influx impala",
"build": "gcc g++ clang clangd rustc cargo go openjdk python3 node ruby php perl lua swift dotnet",
}


def _build() -> tuple[ToolSpec, ...]:
    items: list[ToolSpec] = []
    seen: set[str] = set()
    for category, names in _RAW.items():
        for name in names.split():
            if name in seen:
                continue
            seen.add(name)
            risk = "elevated" if category in {"security", "disk", "network"} else "standard"
            items.append(ToolSpec(name, category, (name,), risk, f"Managed {category} capability: {name}"))
    return tuple(items)


TOOLS = _build()
TOOL_INDEX = {tool.name: tool for tool in TOOLS}


def registry_report() -> dict[str, object]:
    categories: dict[str, int] = {}
    for tool in TOOLS:
        categories[tool.category] = categories.get(tool.category, 0) + 1
    return {"count": len(TOOLS), "categories": categories, "tools": [asdict(tool) for tool in TOOLS]}
