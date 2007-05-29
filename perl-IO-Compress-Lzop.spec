#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Compress-Lzop
Summary:	Modules to read/write lzop files/buffers
Summary(pl.UTF-8):	Moduły do odczytu/zapisu plików/buforów lzop
Name:		perl-IO-Compress-Lzop
Version:	2.004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c9401b0007f7b8f1dbd6b80fe9075f3
URL:		http://search.cpan.org/dist/IO-Compress-Lzop/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Compress-LZO
BuildRequires:	perl-IO-Compress-Base >= %{version}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IO::Compress::Lzop and IO::Uncompress::UnLzop modules provide a Perl
interface that allows reading and writing lzop compressed data from/to
files or buffer.

%description -l pl.UTF-8
Moduły IO::Compress::Lzop i IO::Uncompress::UnLzop udostępniają
perlowy interfejs umożliwiający odczyt i zapis danych skompresowanych
algorytmem lzop z/do plików lub buforów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Compress/Adapter/LZO.pm
%{perl_vendorlib}/IO/Compress/Lzop.pm
%{perl_vendorlib}/IO/Compress/Lzop
%{perl_vendorlib}/IO/Uncompress/Adapter/LZO.pm
%{perl_vendorlib}/IO/Uncompress/UnLzop.pm
%{_mandir}/man3/IO::*
