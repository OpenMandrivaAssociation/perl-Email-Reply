%define module      Email-Reply
%define name        perl-%{module}
%define version     1.20.2
%define up_version  1.202
%define release     %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Reply to a Message
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Email::Simple::Creator)
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::MIME::Creator)
BuildRequires:  perl(Email::Date)
BuildArch:      noarch

%description
This software takes the hard out of generating replies to email messages.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


