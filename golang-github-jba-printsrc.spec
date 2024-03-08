# Run tests in check section
# (fail on ABF)
%bcond_with check

# https://github.com/jba/printsrc
%global goipath		github.com/jba/printsrc
%global forgeurl	https://github.com/jba/printsrc
Version:		0.2.2

%gometa

Summary:	Print Go values as Go source
Name:		golang-github-jba-printsrc

Release:	1
Source0:	https://github.com/jba/printsrc/archive/v%{version}/printsrc-%{version}.tar.gz
URL:		https://github.com/jba/printsrc
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
This package prints Go values so the Go compiler can
read them. It is intended for use in code generators.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n printsrc-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

