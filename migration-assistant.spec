%define name migration-assistant
%define version 0.6.0
%define release %mkrel 1

Summary: Migration Assistant
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://launchpadlibrarian.net/10012930/%{name}_%{version}.tar.gz
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
Patch4: migration-assistant-winnt.patch
# closedir() frees data returned by readdir()
Patch5:	migration-assistant-closedir.patch
# handle win2k migration by not trying to import music if not present
Patch6:	migration-assistant-win2k.patch
# use XDG directories instead of hardcoded english names
Patch7:	migration-assistant-xdg.patch
License: GPL
Group: System/Configuration/Other
Url: https://launchpad.net/migration-assistant
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel

%description
Migration Assistant imports documents and settings from other
operating systems during the install process.

%prep
%setup -q -n %{name}.trunk
%patch0 -p1 -b .extcheck
%patch1 -p1 -b .close
%patch2 -p1 -b .nommap
%patch3 -p1 -b .initmkdir
%patch4 -p1 -b .winnt
%patch5 -p1 -b .closedir
%patch6 -p1 -b .win2k
%patch7 -p1 -b .xdg

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
