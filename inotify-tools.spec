Name:           inotify-tools
Version:        2.6
Release:        1%{?dist}
Summary:        Command line utilities for inotify

Group:          Applications/System
License:        GPL
URL:            http://inotify-tools.sourceforge.net/
Source0:        http://download.sf.net/inotify-tools/inotify-tools-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
inotify-tools is a set of command-line programs for Linux providing
a simple interface to inotify. These programs can be used to monitor
and act upon filesystem events.


%prep
%setup -q


%build
%configure --disable-dependency-tracking
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/inotifywait
%{_bindir}/inotifywatch
%{_mandir}/man1/inotifywait.1*
%{_mandir}/man1/inotifywatch.1*


%changelog
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
