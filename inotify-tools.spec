Name:           inotify-tools
Version:        3.13
Release:        3%{?dist}
Summary:        Command line utilities for inotify

Group:          Applications/System
License:        GPLv2
URL:		 http://inotify-tools.sourceforge.net/
Source0:        http://download.sf.net/inotify-tools/inotify-tools-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  autoconf
BuildRequires:  doxygen

%description
inotify-tools is a set of command-line programs for Linux providing
a simple interface to inotify. These programs can be used to monitor
and act upon filesystem events.

%package        devel
Summary:        Headers and libraries for building apps that use libinotifytools
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains headers and libraries required to build applications
that use the libinotifytools library.

%prep
%setup -q


%build
%configure \
        --disable-dependency-tracking \
        --disable-static \
        --enable-doxygen
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
# We'll install documentation in the proper place
rm -rf %{buildroot}/%{_datadir}/doc/


%check
make check


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/inotifywait
%{_bindir}/inotifywatch
%{_libdir}/libinotifytools.so.*
%{_mandir}/man1/inotifywait.1*
%{_mandir}/man1/inotifywatch.1*

%files devel
%defattr(-,root,root,-)
%doc libinotifytools/src/doc/html/*
%dir %{_includedir}/inotifytools/
%{_includedir}/inotifytools/inotify.h
%{_includedir}/inotifytools/inotify-nosys.h
%{_includedir}/inotifytools/inotifytools.h
%{_libdir}/libinotifytools.so


%changelog
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 11 2008 Adel Gadllah <adel.gadllah@gmail.com> 3.13-1
- Update to 3.13

* Mon Sep 24 2007 Dawid Gajownik <gajownik[AT]gmail.com> - 3.11-1
- Update to 3.11 (CVE-2007-5037, #299771)
- Fix License tag

* Sun Dec 17 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 3.6-1
- Update to 3.6

* Tue Oct 31 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 3.3-1
- Update to 3.3
- Add %%check stage

* Sat Oct 28 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 3.1-1
- Update to 3.1
- Add -devel subpackage

* Tue Oct  3 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.6-1
- Update to 2.6

* Mon Oct  2 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.5-1
- Update to 2.5

* Sat Sep  9 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.4-1
- Update to 2.4

* Tue Aug 15 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.3-1
- Update to 2.3
- Drop implicit_syscall patch (fixed upstream)

* Mon Jul 31 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.2-3
- Fix URL

* Thu Jul  6 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.2-2
- Fix compilation warnings

* Thu Jul  6 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.2-1
- New version 2.2
- Update URL and description
- Add man pages

* Wed Jul  5 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.1-1
- Initial RPM release.
