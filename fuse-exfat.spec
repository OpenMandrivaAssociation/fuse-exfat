Summary:	Free exFAT file system implementation
Name:		fuse-exfat
Version:	1.3.0
Release:	5
License:	GPLv3+
Group:		System/Kernel and hardware
Url:		https://github.com/relan/exfat
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
#Patch0:		fuse-exfat-1.3.0-fuse3.patch
#BuildRequires:	pkgconfig(fuse3)
#Requires:	fuse >= 3.0
BuildRequires:	pkgconfig(fuse)
Requires:	fuse >= 2.6

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%files
/sbin/*
%{_sbindir}/*
%{_mandir}/man8/*.8.*

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

install -d %{buildroot}/sbin
ln -sr %{buildroot}%{_sbindir}/mount.exfat %{buildroot}/sbin/mount.exfat
ln -sr %{buildroot}%{_sbindir}/mount.exfat-fuse %{buildroot}/sbin/mount.exfat-fuse

# (tpg) install man
mkdir -p %{buildroot}%{_mandir}/man8
install -m644 fuse/mount.exfat-fuse.8 %{buildroot}%{_mandir}/man8/
