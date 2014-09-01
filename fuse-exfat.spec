Summary:	Free exFAT file system implementation
Name:		fuse-exfat
Version:	1.0.1
Release:	3.1
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
# (tpg) nothing to do here as builds are started twice

%install
export CCFLAGS="%{optflags} -std=c99"
export LDFLAGS="%{ldflags}"
# (tpg) fix for https://issues.openmandriva.org/show_bug.cgi?id=834
export CC="%{__cc} -fuse-ld=bfd"
export CXX="%{__cxx} -fuse-ld=bfd"
mkdir -p BFD
ln -sf /usr/bin/ld.bfd BFD/ld
export PATH=$PWD/BFD:$PATH

%scons_install DESTDIR=%{buildroot}/sbin
mkdir -p %{buildroot}%{_mandir}/man8
install -m644 fuse/mount.exfat-fuse.8 %{buildroot}%{_mandir}/man8/

%files
/sbin/*
%{_mandir}/man8/*

