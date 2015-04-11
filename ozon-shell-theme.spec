%global theme	Ozon
%global daterev	20150327git92e1e8

Summary:	%{theme} theme for Gnome Shell
Name:		ozon-shell-theme
Version:	0.3
Release:	0.1.%{?daterev}%{?dist}

License:	GPLv3
Group:		User Interface/Desktops
URL:		http://ozonos.github.io
Source0:	%{name}-%{version}-%{?daterev}.tar.xz
Patch0:		ozon-shell-theme-0.3-cantarell.patch

Requires:	gnome-shell >= 3.12.0

BuildArch:	noarch

%description
%{theme} is the official Gnome Shell theme for Ozon OS.


%prep
%setup -q
%patch0 -p1

%build

%install
install -d -m755 %{buildroot}%{_datadir}/themes/%{theme}
cp -pr gnome-shell %{buildroot}%{_datadir}/themes/%{theme}


%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_datadir}/themes/%{theme}


%changelog
* Sat Apr 11 2015 Arkady L. Shane <ashejn@russianfedora.ru> 0.3-0.1.20150327git92e1e8.R
- initial build
