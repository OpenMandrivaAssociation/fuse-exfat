Summary:	Free exFAT file system implementation
Name:		fuse-exfat
Version:	1.0.1
Release:	4
License:	GPLv3+
Group:		System/Kernel and hardware
Url:		http://code.google.com/p/exfat/
Source0:	http://exfat.googlecode.com/files/fuse-exfat-%{version}.tar.gz

BuildRequires:	scons
BuildRequires:	pkgconfig(fuse)
Requires:	fuse >= 2.6

%description
This driver is the first free exFAT file system implementation with write
support. exFAT is a simple file system created by Microsoft. It is intended
to replace FAT32 removing some of it's limitations. exFAT is a standard FS
for SDXC memory cards.

%prep
%setup -q

%build
%scons

%install
scons install DESTDIR=%{buildroot}/sbin
mkdir -p %{buildroot}%{_mandir}/man8
install -m644 fuse/mount.exfat-fuse.8 %{buildroot}%{_mandir}/man8/

%files
/sbin/*
%{_mandir}/man8/*

