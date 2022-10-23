%global optflags %{optflags} -fcommon

Summary:	Migration Assistant
Name:		migration-assistant
Version:	0.6.13
Release:	1
License:	GPLv2+
Group:		System/Configuration/Other
Url:		https://launchpad.net/migration-assistant
Source0:	https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/migration-assistant/%{version}/migration-assistant_%{version}.tar.gz
Patch0:		migration-assistant-xdg.patch
BuildRequires:	pkgconfig(libxml-2.0)

%description
Migration Assistant imports documents and settings from other
operating systems during the install process.

%prep
%setup -q
%autopatch -p1

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

