Summary:	KXicq2 for KDE2 - An icq clone
Name:		kxicq2
Version:	0.0.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
URL:		http://www.kxicq.org
Source0:	http://prdownload.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	http://prdownload.sourceforge.net/%{name}/GoldBlue.tar.gz
Source2:	http://prdownload.sourceforge.net/%{name}/blueplanet-0.1.tar.gz
Source3:	http://prdownload.sourceforge.net/%{name}/cyrustheme.tar.gz
Source4:	http://prdownload.sourceforge.net/%{name}/mauve.tar.gz
Source5:	http://prdownload.sourceforge.net/%{name}/ciasa_boark_inc-0.4.tar.gz
Patch0:		%{name}-glibc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	qt-devel >= 2.2
BuildRequires:	kdelibs >= 2.1
Requires:	kdelibs >= 2.1
Obsoletes:	kxicq

%define         _prefix		/usr/X11R6
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
This is a CVS release of KXicq2 written by Herwin Jan Steehouwer, it
is still in an early development stage, but it is already stable and
usable. KXicq2 is a program which uses the icq-protocol, which is a
very frequently used protocol for private chats on the internet.


%package skins
Summary:	Kxicq2 skins
Group:		X11/KDE/Applications
Group(de):	X11/KDE/Applikationen
Group(pl):	X11/KDE/Aplikacje
Requires:	kxicq2

%description skins
Kxicq2 skins.

%prep
%setup -q -a5
%patch -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT/%{_applnkdir}/Network/Misc
mv -f $RPM_BUILD_ROOT/%{_applnkdir}/Internet/kxicq2.desktop \
    $RPM_BUILD_ROOT/%{_applnkdir}/Network/Misc

install -d $RPM_BUILD_ROOT/%{_datadir}/apps/kxicq2/skins
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT/%{_datadir}/apps/kxicq2/skins
tar zxvf %{SOURCE2} -C $RPM_BUILD_ROOT/%{_datadir}/apps/kxicq2/skins
tar zxvf %{SOURCE3} -C $RPM_BUILD_ROOT/%{_datadir}/apps/kxicq2/skins
install -d $RPM_BUILD_ROOT/%{_datadir}/apps/kxicq2/skins/mauve
tar zxvf %{SOURCE4} -C $RPM_BUILD_ROOT/%{_datadir}/apps/kxicq2/skins/mauve
install -d $RPM_BUILD_ROOT/%{_datadir}/apps/kxicq2/skins/ciasa
tar zxvf ciasa_boark_inc-0.4.tar.gz -C $RPM_BUILD_ROOT/%{_datadir}/apps/kxicq2/skins/ciasa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxicq
%{_applnkdir}/Network/Misc/kxicq2.desktop
%{_datadir}/apps/kxicq2/pics

%files skins
%defattr(644,root,root,755)
%{_datadir}/apps/kxicq2/skins
