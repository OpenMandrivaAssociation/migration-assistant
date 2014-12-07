Summary:	Migration Assistant
Name:		migration-assistant
Version:	0.6.12
Release:	9
License:	GPLv2+
Group:		System/Configuration/Other
Url:		https://launchpad.net/migration-assistant
Source0:	http://archive.ubuntu.com/ubuntu/pool/main/m/%{name}/%{name}_%{version}.tar.gz
Patch0:		migration-assistant-xdg.patch
Patch1:		migration-assistant-0.6.2-fix-str-fmt.patch
BuildRequires:	pkgconfig(libxml-2.0)

%description
Migration Assistant imports documents and settings from other
operating systems during the install process.

%prep
%setup -q
%apply_patches

%build
export CC="gcc %{optflags} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
%make

%install
%makeinstall_std
install -m755 ma-search-users %{buildroot}%{_bindir}

%files
%doc README
%{_bindir}/ma-import
%{_bindir}/ma-search-items
%{_bindir}/ma-search-users

