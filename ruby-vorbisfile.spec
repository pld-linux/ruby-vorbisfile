Summary:	Ogg Vorbis module for Ruby
Summary(pl):	Modu³ Ogg Vorbis dla Ruby
Name:		ruby-vorbisfile
Version:	0.2
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://rikkus.info/arch/%{name}-%{version}.tar.gz
# Source0-md5:	1772ca1c368c527b8809803fb4996b3e
URL:		http://rikkus.info/ruby_vorbisfile.html
BuildRequires:	libvorbis-devel
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ogg Vorbis module for Ruby.

%description -l pl
Modu³ Ogg Vorbis dla Ruby.

%prep
%setup -q

%build
# not autoconf-generated
./configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_sitearchdir}

install vorbisfile.so $RPM_BUILD_ROOT%{ruby_sitearchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{ruby_sitearchdir}/*.so
