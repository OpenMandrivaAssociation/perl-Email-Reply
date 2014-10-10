%define upstream_name    Email-Reply
%define upstream_version 1.203

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Reply to a Message
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/Email-Reply-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl(Email::Simple::Creator)
BuildRequires:	perl(Email::Abstract)
BuildRequires:	perl(Email::MIME)
BuildRequires:	perl(Email::MIME::Creator)
BuildRequires:	perl(Email::Date)
BuildArch:	noarch

%description
This software takes the hard out of generating replies to email messages.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.202.0-1mdv2010.0
+ Revision: 403158
- rebuild using %%perl_convert_version

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.20.2-4mdv2009.0
+ Revision: 290409
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.2-1mdv2008.0
+ Revision: 56076
- update to new version 1.20.2


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.1-1mdv2007.1
+ Revision: 138830
- new version

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.0-1mdv2007.1
+ Revision: 111591
- fix build dependencies
- fix build dependencies
- fix build dependencies
- fix build dependencies
- Import perl-Email-Reply

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.20.0-1mdv2007.1
- first mdv release


