%define name migration-assistant
%define version 0.6.4
%define release %mkrel 2

Summary: Migration Assistant
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://archive.ubuntu.com/ubuntu/pool/main/m/%{name}/%{name}_%{version}.tar.gz
Patch0:	migration-assistant-xdg.patch
Patch1:	migration-assistant-0.6.2-fix-str-fmt.patch
License: GPLv2+
Group: System/Configuration/Other
Url: https://launchpad.net/migration-assistant
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel

%description
Migration Assistant imports documents and settings from other
operating systems during the install process.

%prep
%setup -q -n %{name}.trunk
%patch0 -p1 -b .xdg
%patch1 -p0

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
