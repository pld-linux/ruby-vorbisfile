%define	ruby_sitearchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitearchdir"]')
Summary:	OGG Vorbis module for Ruby
Summary(pl):	Modu³ OGG Vorbis dla Ruby
Name:		ruby-vorbisfile
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rikkus.info/arch/%{name}-%{version}.tar.gz
# Source0-md5:	1772ca1c368c527b8809803fb4996b3e
URL:		http://rikkus.info/ruby_vorbisfile.html
BuildRequires:	ruby
BuildRequires:	libvorbis-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OGG Vorbis module for Ruby.

%description -l pl
Modu³ OGG Vorbis dla Ruby.

%prep
%setup -q 

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitearchdir}

install vorbisfile.so $RPM_BUILD_ROOT%{ruby_sitearchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{ruby_sitearchdir}/*
