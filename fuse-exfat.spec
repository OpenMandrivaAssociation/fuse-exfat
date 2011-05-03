Name: fuse-exfat
Summary: Free exFAT file system implementation
Version: 0.9.2
Release: %mkrel 2
License: GPLv3+
Group: System/Kernel and hardware
Source0: http://exfat.googlecode.com/files/fuse-exfat-%{version}.tar.gz
URL: http://code.google.com/p/exfat/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: fuse-devel >= 2.6
BuildRequires: scons
Requires: fuse >= 2.6

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
rm -rf %buildroot
DESTDIR=%buildroot/sbin scons install
mkdir -p %buildroot%_mandir/man8
install -m644 fuse/mount.exfat-fuse.8 %buildroot%_mandir/man8/

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
/sbin/*
%{_mandir}/man8/*
