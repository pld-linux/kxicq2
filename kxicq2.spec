Summary:	KXicq2 for KDE2 - An icq clone
Name:		kxicq2
Version:	0.0.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
URL:		http://www.kxicq.org
Source0:	%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-glibc.patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	kdebase >= 2.0
Obsoletes:	kxicq

%define		_prefix 	/usr/X11R6

%description
This is a CVS release of KXicq2 written by Herwin Jan Steehouwer, it
is still in an early development stage, but it is already stable and
usable. KXicq2 is a program which uses the icq-protocol, which is a
very frequently used protocol for private chats on the internet.

%prep
%setup -q 
%patch -p1

%build
./configure --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
install -d %{buildroot}/%{_applnkdir}/Network/Communications
install %{SOURCE1} %{buildroot}/%{_applnkdir}/Network/Communications

%clean
rm -rf %{buildroot}

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/kxicq2/pics/*
%{_applnkdir}/Network/Communications/kxicq2.desktop
%doc ChangeLog
