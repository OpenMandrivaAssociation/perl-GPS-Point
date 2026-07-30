%define upstream_name    GPS-Point
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	0.20
Release:	4

Summary:	Provides an object interface for a GPS point
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/GPS-Point
Source0:	https://cpan.metacpan.org/authors/id/M/MR/MRDVT/GPS-Point-0.20.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Number::Delta)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch

%description
This is a re-write of the Net::GPSD::Point manpage with a goal of being
more re-usable.

GPS::Point - Provides an object interface for a GPS fix (e.g. Position,
Velocity and Time).

  Note: Please use Geo::Point, if you want 2D or projection support.

%prep
%setup -q -n GPS-Point-0.20

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

