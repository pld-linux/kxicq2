%define _cvs   	cvs
Summary:	KXicq2 for KDE3 - An icq clone
Summary(pl.UTF-8):   KXicq2 dla KDE3 - klon ICQ
Name:		kxicq2
Version:	0.7.8
Release:	0.%{_cvs}
License:	GPL
Group:		X11/Applications/Networking
Source0:	%{name}-%{version}-%{_cvs}-kde3.tgz
Source1:	ftp://ftp.sourceforge.net/pub/sourceforge/kxicq/GoldBlue.tar.gz
Source2:	ftp://ftp.sourceforge.net/pub/sourceforge/kxicq/blueplanet-0.1.tar.gz
Source3:	ftp://ftp.sourceforge.net/pub/sourceforge/kxicq/cyrustheme.tar.gz
Source4:	ftp://ftp.sourceforge.net/pub/sourceforge/kxicq/mauve.tar.gz
Source5:	ftp://ftp.sourceforge.net/pub/sourceforge/kxicq/ciasa_boark_inc-0.4.tar.gz
Patch0:		%{name}-glibc.patch
URL:		http://www.kxicq.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	qt-devel >= 3.0.3
BuildRequires:	kdelibs-devel >= 3.0
Requires:	kdelibs >= 3.0
Obsoletes:	kxicq

%define         _prefix		/usr/X11R6
%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
This is a CVS release of KXicq2 written by Herwin Jan Steehouwer, it
is still in an early development stage, but it is already stable and
usable. KXicq2 is a program which uses the icq-protocol, which is a
very frequently used protocol for private chats on the Internet.

%description -l pl.UTF-8
To jest KXicq2 napisany przez Herwina Jana Steehouwera, nadal jest we
wczesnym stadium rozwoju, ale jest stabilny i używalny. KXicq2 jest
programem używającym protokołu ICQ, bardzo często używanego do
prywatnych rozmów przez Internet.

%package skins
Summary:	Kxicq2 skins
Summary(pl.UTF-8):   Skóry do Kxicq2
Group:		X11/Applications/Networking
Requires:	kxicq2

%description skins
Kxicq2 skins.

%description skins -l pl.UTF-8
Skóry do Kxicq2.

%prep
%setup -q -a5 -n %{name}
%patch -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

export QTDIR=/usr/X11R6/lib
make -f Makefile.cvs
%configure --with-qt-dir=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Internet/kxicq2.desktop \
    $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kxicq2/skins
tar zxvf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/apps/kxicq2/skins
tar zxvf %{SOURCE2} -C $RPM_BUILD_ROOT%{_datadir}/apps/kxicq2/skins
tar zxvf %{SOURCE3} -C $RPM_BUILD_ROOT%{_datadir}/apps/kxicq2/skins
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kxicq2/skins/mauve
tar zxvf %{SOURCE4} -C $RPM_BUILD_ROOT%{_datadir}/apps/kxicq2/skins/mauve
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kxicq2/skins/ciasa
tar zxvf ciasa_boark_inc-0.4.tar.gz -C $RPM_BUILD_ROOT%{_datadir}/apps/kxicq2/skins/ciasa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxicq
%{_applnkdir}/Network/Communications/kxicq2.desktop
%{_datadir}/apps/kxicq2/pics

%files skins
%defattr(644,root,root,755)
%{_datadir}/apps/kxicq2/skins
