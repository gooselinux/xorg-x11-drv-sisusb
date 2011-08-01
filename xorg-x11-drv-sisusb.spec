%define tarball xf86-video-sisusb
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 sisusb video driver
Name:      xorg-x11-drv-sisusb
Version:   0.9.3
Release:   1.1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6

Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6

%description 
X.Org X11 sisusb video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
# FIXME: This should be using makeinstall macro instead.  Please test
# makeinstall with this driver, and if it works, check it into CVS. If
# it fails, fix it in upstream sources and file a patch upstream.
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/sisusb_drv.so
%{_mandir}/man4/*.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.9.3-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 0.9.3-1
- sisusb 0.9.3

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 0.9.2-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 0.9.2-1
- sisusb 0.9.2

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 24 2009 Adam Jackson <ajax@redhat.com> 0.9.1-1
- sisusb 0.9.1

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 0.9.0-1
- Latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.1-10
- Autorebuild for GCC 4.3

* Thu Sep 06 2007 Adam Jackson <ajax@redhat.com> 0.8.1-9
- Disown the manual directory. (#226622)

* Thu Aug 23 2007 Adam Jackson <ajax@redhat.com> - 0.8.1-8
- sisusb-0.8.1-open-is-not-fopen.patch: Despite the similarity, you can not
  pass character literals to open that match the string literals you'd pass
  to fopen.

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 0.8.1-7
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 0.8.1-6
- Update Requires and BuildRequires.  Disown the module directories.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 0.8.1-5
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Thu Jun 29 2006 Adam Jackson <ajackson@redhat.com> 0.8.1-4
- Add builds for ppc and ia64 to satisfy xorg-x11-drivers
  dependencies.  Highly untested.

* Wed Jun 28 2006 Mike A. Harris <mharris@redhat.com> 0.8.1-3
- Remove system owned directories from file manifest.

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 0.8.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr 09 2006 Adam Jackson <ajackson@redhat.com> 0.8.1-1
- Update to 0.8.1 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> 0.7.1.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> 0.7.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 0.7.1.3-1
- Updated xorg-x11-drv-sisusb to version 0.7.1.3 from X11R7.0
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 0.7.1.2-1
- Updated xorg-x11-drv-sisusb to version 0.7.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 0.7.1-1
- Updated xorg-x11-drv-sisusb to version 0.7.1 from X11R7 RC2

* Fri Nov 04 2005 Mike A. Harris <mharris@redhat.com> 0.7.0.1-1
- Updated xorg-x11-drv-sisusb to version 0.7.0.1 from X11R7 RC1
- Fix *.la file removal.

* Fri Sep 02 2005 Mike A. Harris <mharris@redhat.com> 0.7.0-0
- Initial spec file for sisusb video driver generated automatically
  by my xorg-driverspecgen script.
