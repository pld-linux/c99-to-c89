Summary:	Tool to convert C99 code to MSVC-compatible C89
Summary(pl.UTF-8):	Narzędzie do konwersji kodu C99 do C89 zgodnego z MSVC
Name:		c99-to-c89
Version:	1.0.3
Release:	1
License:	Apache v2.0
Group:		Development/Tools
#Source0Download: https://github.com/libav/c99-to-c89/releases
Source0:	https://github.com/libav/c99-to-c89/archive/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	17634d419ff1019d5b5f2fa5912fdc60
URL:		https://github.com/libav/c99-to-c89
BuildRequires:	clang-devel >= 3.1
Requires:	clang-libs >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to convert C99 code to MSVC-compatible C89.

%description -l pl.UTF-8
Narzędzie do konwersji kodu C99 do C89 zgodnego z MSVC.

%prep
%setup -q -n %{name}-release-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install c99conv c99wrap $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/c99conv
%attr(755,root,root) %{_bindir}/c99wrap
