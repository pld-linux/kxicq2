Summary:	KXicq2 for KDE2 - An icq clone
Summary(pl):	KXicq2 dla KDE2 - klon ICQ
Name:		kxicq2
Version:	0.0.6
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/kxicq/%{name}-%{version}.tar.gz
# Source0-md5:	4baad94467a624e2f03236a496c94d34
Source1:	http://dl.sourceforge.net/kxicq/GoldBlue.tar.gz
# Source1-md5:	401450e4710aebff4b2edad14c0f4cac
Source2:	http://dl.sourceforge.net/kxicq/blueplanet-0.1.tar.gz
# Source2-md5:	db08ff114c24af4ff185c76820acb04d
Source3:	http://dl.sourceforge.net/kxicq/cyrustheme.tar.gz
# Source3-md5:	0c514e3bdd67f2a2766de43976bc9c2a
Source4:	http://dl.sourceforge.net/kxicq/mauve.tar.gz
# Source4-md5:	f56da80040c4343b7156d0e66f9b8b73
Source5:	http://dl.sourceforge.net/kxicq/ciasa_boark_inc-0.4.tar.gz
# Source5-md5:	b6759abce6e8fd9c69895d28738b63f2
Patch0:		%{name}-glibc.patch
URL:		http://www.kxicq.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	qt-devel >= 2.2
BuildRequires:	kdelibs-devel >= 2.1
Requires:	kdelibs >= 2.1
Obsoletes:	kxicq

%define		_htmldir	%{_datadir}/doc/kde/HTML

%description
This is a CVS release of KXicq2 written by Herwin Jan Steehouwer, it
is still in an early development stage, but it is already stable and
usable. KXicq2 is a program which uses the icq-protocol, which is a
very frequently used protocol for private chats on the Internet.

%description -l pl
To jest KXicq2 napisany przez Herwina Jana Steehouwera, nadal jest we
wczesnym stadium rozwoju, ale jest stabilny i u¿ywalny. KXicq2 jest
programem u¿ywaj±cym protoko³u ICQ, bardzo czêsto u¿ywanego do
prywatnych rozmów przez Internet.

%package skins
Summary:	Kxicq2 skins
Summary(pl):	Skóry do Kxicq2
Group:		X11/Applications/Networking
Requires:	kxicq2

%description skins
Kxicq2 skins.

%description skins -l pl
Skóry do Kxicq2.

%prep
%setup -q -a5
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Internet/kxicq2.desktop \
    $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

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
%{_applnkdir}/Network/Misc/kxicq2.desktop
%{_datadir}/apps/kxicq2/pics

%files skins
%defattr(644,root,root,755)
%{_datadir}/apps/kxicq2/skins
