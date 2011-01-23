
%define		module	irclib

Summary:	A set of Python modules for IRC support
Summary(pl.UTF-8):	Zestaw modułów Pythona do obsługi IRC-a
Name:		python-%{module}
Version:	0.4.5
Release:	3
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	141b7cd26723b337ef277ff5eb56bb5e
Patch0:		%{name}-CR.patch
URL:		http://python-irclib.sourceforge.net/
BuildRequires:	python >= 2.2.1
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildArch:	noarch
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is intended to encapsulate the IRC protocol at a quite
low level. It provides an event-driven IRC client framework. It has a
fairly thorough support for the basic IRC protocol, CTCP and DCC
connections.

%description -l pl.UTF-8
Ta biblioteka ma za zadanie obudowywać protokół IRC na dosyć niskim
poziomie. Dostarcza szkielet klienta IRC sterowany zdarzeniami. Ma
w miarę gruntowną obsługę dla podstaw protokołu IRC i połączeń CTCP i
DCC.

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README irccat irccat2 servermap testbot.py dccsend dccreceive
%{py_sitescriptdir}/*.py[co]
