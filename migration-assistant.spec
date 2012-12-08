Summary: Migration Assistant
Name:    migration-assistant
Version: 0.6.12
Release: 1
Source0: http://archive.ubuntu.com/ubuntu/pool/main/m/%{name}/%{name}_%{version}.tar.gz
Patch0:	migration-assistant-xdg.patch
Patch1:	migration-assistant-0.6.2-fix-str-fmt.patch
License: GPLv2+
Group: System/Configuration/Other
Url: https://launchpad.net/migration-assistant
BuildRequires: libxml2-devel

%description
Migration Assistant imports documents and settings from other
operating systems during the install process.

%prep
%setup -q
%patch0 -p1 -b .xdg
%patch1 -p0

%build
export CC="gcc %{optflags} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
%make

%install
%makeinstall_std
install -m755 ma-search-users %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/ma-import
%{_bindir}/ma-search-items
%{_bindir}/ma-search-users


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-4mdv2011.0
+ Revision: 666423
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-3mdv2011.0
+ Revision: 606641
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.4-2mdv2010.1
+ Revision: 523306
- rebuilt for 2010.1

* Sun Jul 26 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.4-1mdv2010.0
+ Revision: 400416
- New version 0.6.4

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 0.6.2-2mdv2009.1
+ Revision: 352762
- diff p1 to fix string format not literal

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 25 2008 Funda Wang <fwang@mandriva.org> 0.6.2-1mdv2009.0
+ Revision: 228851
- New version 0.6.2
- drop patch0,1,2,3,4,5,6,8,9,10 (merged upstream)
- rediff xdg dir patch

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-3mdv2009.0
+ Revision: 223258
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - make profilesdir error message more generic

* Thu Mar 13 2008 Olivier Blin <oblin@mandriva.com> 0.6.0-2mdv2008.1
+ Revision: 187496
- filter Public and Default users for Vista (from registry keys)
- filter "Default User" key in Vista (it is a junction to Default)
- do not segfault if keys are missing
- get profiles directory from registry for ma-search-items and
  ma-import as well ("Documents and Settings" is not correct in Vista)
- fix segfault by zeroing buffers for strcat
- improve WINNT patch to factorize user registry location as well
- update source URL

* Mon Mar 10 2008 Olivier Blin <oblin@mandriva.com> 0.6.0-1mdv2008.1
+ Revision: 183547
- 0.6.0
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 0.5.4-1mdv2008.1
+ Revision: 101036
- New version 0.5.4

* Wed Oct 03 2007 Olivier Blin <oblin@mandriva.com> 0.5.1-3mdv2008.0
+ Revision: 95185
- use XDG directories instead of hardcoded english names (#34381)

* Wed Oct 03 2007 Olivier Blin <oblin@mandriva.com> 0.5.1-2mdv2008.0
+ Revision: 95020
- handle win2k migration by not trying to import music if not present
- fix get_insensitive_path(), since closedir() frees data returned by readdir()
- fix WINNT handling in ma-search-users

* Mon Oct 01 2007 Olivier Blin <oblin@mandriva.com> 0.5.1-1mdv2008.0
+ Revision: 94319
- 0.5.1

* Fri Aug 10 2007 Olivier Blin <oblin@mandriva.com> 0.4.5-5mdv2008.0
+ Revision: 61566
- do not uselessly create directories with uninitialized names
- fix my fd leak fix /o\

* Fri Aug 10 2007 Olivier Blin <oblin@mandriva.com> 0.4.5-4mdv2008.0
+ Revision: 61272
- fix more file descriptor leaks (to migrate a big number of files)

* Thu Aug 09 2007 Olivier Blin <oblin@mandriva.com> 0.4.5-3mdv2008.0
+ Revision: 60880
- fix again segfault when file has no extension (upstream copy-paste rox)

* Wed Aug 01 2007 Olivier Blin <oblin@mandriva.com> 0.4.5-1mdv2008.0
+ Revision: 57543
- buildrequire libxml2-devel
- reimplement copy to handle large files
- fix file descriptor leaks to be able to import a big number of files
- fix segfault when file has no extension
- initial release
- Create migration-assistant

