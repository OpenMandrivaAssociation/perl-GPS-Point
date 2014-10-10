%define upstream_name    GPS-Point
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.20
Release:	2

Summary:	Provides an object interface for a GPS point
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/GPS/GPS-Point-0.20.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.180.0-2mdv2011.0
+ Revision: 654332
- rebuild for updated spec-helper

* Sun Oct 31 2010 Olivier Thauvin <nanardon@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 590777
- import perl-GPS-Point


