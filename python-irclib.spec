
%define		module	irclib

Summary:	A set of Python modules for IRC support
Summary(pl):	Zestaw modu³ów Pythona do obs³ugi IRC-a
Name:		python-%{module}
Version:	0.4.1
Release:	0.1
License:	BSD
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	7efae7ada5fc9d4c06c71dcbc45f118d
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
Ta biblioteka ma za zadanie obudowywaæ protokó³ IRC na dosyæ niskim
poziomie. Dostarcza szkielet klienta IRC sterowany zdarzeniami. Ma
w miarê gruntown± obs³ugê dla podstaw protoko³u IRC i po³±czeñ CTCP i
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
