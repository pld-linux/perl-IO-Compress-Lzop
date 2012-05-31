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
Version:	2.052
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81b06adec5e9dbd6f36bd5b5f34cb8d6
URL:		http://search.cpan.org/dist/IO-Compress-Lzop/
BuildRequires:	perl-ExtUtils-MakeMaker >= 5.16
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Compress-LZO
BuildRequires:	perl-IO-Compress >= %{version}
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
%{_mandir}/man3/IO::Compress::Lzop.3pm*
%{_mandir}/man3/IO::Uncompress::UnLzop.3pm*
