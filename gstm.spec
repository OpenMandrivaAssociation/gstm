Name:		gstm
Version:	1.2
Release:	%mkrel 6
Summary:	A front-end to ssh tunneling

Group:		Networking/Remote access
License:	GPL
URL:		http://gstm.sourceforge.net
Source0:	http://heanet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	desktop-file-utils
#BuildRequires:	gettext
BuildRequires:	gnomeui2-devel
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
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files 
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%files -n gaskpass
%{_bindir}/gaskpass

