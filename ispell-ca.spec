Summary:	Catalan dictionary for ispell
Summary(ca):	Diccionari català per a ispell
Summary(es):	Diccionario catalan para ispell
Summary(pl):	Kataloñski s³ownik dla ispella
Name:		ispell-ca
Version:	20041027
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.jmoratinos.com/ispell/catalan.rar
# Source0-md5:	936bfcef39f32e131d595f4cc32c7b21
URL:		http://www.jmoratinos.com/cgi-bin/index.php
BuildRequires:	ispell >= 3.2.06
BuildRequires:	unrar
Requires:	ispell >= 3.2.06
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Catalan dictionary for ispell.

%description -l ca
Diccionari català per a ispell.

%description -l es
Diccionario catalan para ispell.

%description -l pl
Kataloñski s³ownik dla programu ispell.

%prep
%setup -q -c -T
unrar -inul x %{SOURCE0}

%build
buildhash catalan_i.dic catalan_i.aff catalan.hash

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ispell

install catalan_i.aff $RPM_BUILD_ROOT%{_libdir}/ispell/catalan.aff
install catalan.hash $RPM_BUILD_ROOT%{_libdir}/ispell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/ispell/*
