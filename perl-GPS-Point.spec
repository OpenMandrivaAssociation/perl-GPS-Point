%define upstream_name    GPS-Point
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Provides an object interface for a GPS point
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/GPS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Number::Delta)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a re-write of the Net::GPSD::Point manpage with a goal of being
more re-usable.

GPS::Point - Provides an object interface for a GPS fix (e.g. Position,
Velocity and Time).

  Note: Please use Geo::Point, if you want 2D or projection support.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


