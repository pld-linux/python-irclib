
%define		module	irclib

Summary:	A set of Python modules for IRC support
Summary(pl):	Zestaw modu��w Pythona do obs�ugi IRC-a
Name:		python-%{module}
Version:	0.4.4
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	08cac5978df640aaa24d3a4a47274b90
URL:		http://python-irclib.sourceforge.net/
BuildRequires:	python >= 2.2.1
BuildRequires:	rpm-pythonprov >= 4.0.2-50
%pyrequires_eq	python
BuildArch:	noarch
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is intended to encapsulate the IRC protocol at a quite
low level. It provides an event-driven IRC client framework. It has a
fairly thorough support for the basic IRC protocol, CTCP and DCC
connections.

%description -l pl
Ta biblioteka ma za zadanie obudowywa� protok� IRC na dosy� niskim
poziomie. Dostarcza szkielet klienta IRC sterowany zdarzeniami. Ma
w miar� gruntown� obs�ug� dla podstaw protoko�u IRC i po��cze� CTCP i
DCC.

%prep
%setup -q

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
