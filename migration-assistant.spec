%define name migration-assistant
%define version 0.4.5
%define release %mkrel 5

Summary: Migration Assistant
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://launchpadlibrarian.net/7154726/%{name}_%{version}.tar.bz2
# fix segfault when file has no extension
Patch0: migration-assistant-extcheck.patch
# close file descriptors
# the fd leaks made impossible to migrate a big number of files
# an additional fix would be to msync() and munmap()
# http://marc.info/?l=linux-nfs&m=110061860303322&w=2
Patch1: migration-assistant-close.patch
# reimplement copy using read/write (like cp) to handle large files
# we can't mmap() (twice) large files in memory
Patch2: migration-assistant-nommap.patch
# do not uselessly create directories with uninitialized names
Patch3: migration-assistant-initmkdir.patch
License: GPL
Group: System/Configuration/Other
Url: https://launchpad.net/migration-assistant
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel

%description
Migration Assistant imports documents and settings from other
operating systems during the install process.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .extcheck
%patch1 -p1 -b .close
%patch2 -p1 -b .nommap
%patch3 -p1 -b .initmkdir

%build
export CC="gcc $RPM_OPT_FLAGS -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -m755 ma-search-users %{buildroot}%{_bindir}
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/ma-import
%{_bindir}/ma-search-items
%{_bindir}/ma-search-users
