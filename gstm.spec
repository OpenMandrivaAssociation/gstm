Name:		gstm
Version:	1.2
Release:	10
Summary:	A front-end to ssh tunneling

Group:		Networking/Remote access
License:	GPL
URL:		http://gstm.sourceforge.net
Source0:	http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libgnomeui-2.0)
Requires: openssh-clients

%description
gSTM, short for Gnome SSH Tunnel Manager, is a graphical front-end for 
managing ssh tunneled portredirects.

%package -n gaskpass
Group:	Networking/Remote access
Summary: A Gnome X11 passphrase dialog for OpenSSH
%description -n gaskpass
%{summary}.

%prep
%setup -q

%build
export LIBS="-lX11 -lxml2"
%configure
%make

%install
%makeinstall


%files 
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%files -n gaskpass
%{_bindir}/gaskpass



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-10mdv2011.0
+ Revision: 619267
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2-9mdv2010.0
+ Revision: 429331
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2-8mdv2009.0
+ Revision: 246663
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2-6mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import gstm


* Sat Sep 16 2006 Stefan van der Eijk <stefan@mandriva.org> 1.2-6
- initial Mandriva package

* Thu Sep 05 2006 Damien Durand <splinux@fedoraproject.org> - 1.2-5
- Fixed %%description and %%datadir/pixmpaps

* Thu Aug 26 2006 Damien Durand <splinux@fedoraproject.org> - 1.2-4
- Added patch from Laurent Rineau

* Thu Aug 19 2006 Damien Durand <splinux@fedoraproject.org> - 1.2-3
- Added openssh in Requires

* Thu Aug 12 2006 Damien Durand <splinux@fedoraproject.org> - 1.2-2
- Removed openssh in BuildRequires

* Thu Aug 08 2006 Damien Durand <splinux@fedoraproject.org> - 1.2-1
- Initial package
