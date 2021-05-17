#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Path
%define		pnam	Tiny
Summary:	Path::Tiny - File path utility
Summary(pl.UTF-8):	Path::Tiny - narzędzia do ścieżek plików
Name:		perl-Path-Tiny
Version:	0.118
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cb34fd356725ec12b78e88ddac37db08
URL:		https://metacpan.org/release/Path-Tiny
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.17
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Path) >= 2.07
BuildRequires:	perl(File::Spec) >= 0.86
BuildRequires:	perl-Digest >= 1.03
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-Digest-SHA >= 5.45
BuildRequires:	perl-Encode
BuildRequires:	perl-File-Temp >= 0.19
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a small, fast utility for working with file
paths. It is friendlier to use than File::Spec and provides easy
access to functions from several other core file handling modules. It
aims to be smaller and faster than many alternatives on CPAN, while
helping people do many common things in consistent and less
error-prone ways.

%description -l pl.UTF-8
Ten moduł zawiera małe, szybkie narzędzie do pracy ze ścieżkami
plików. Jest bardziej przyjazny w użyciu niż File::Spec i daje łatwy
dostęp do funkcji z kilku innych głównych modułów obsługujących pliki.
Moduł ma za zadanie być mniejszym i szybszym od alternatyw z CPAN-u,
pomagając ludziom wykonywać wiele popularnych zadań w spójny i
bardziej błędoodporny sposób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Path/Tiny.pm
%{_mandir}/man3/Path::Tiny.3pm*
