Name:		texlive-infwarerr
Version:	53023
Release:	2
Summary:	Complete set of information/warning/error message macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/infwarerr
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/infwarerr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/infwarerr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/infwarerr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a complete set of macros for information,
warning and error messages. Under LaTeX, the commands are
wrappers for the corresponding LaTeX commands; under Plain TeX
they are available as complete implementations.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/infwarerr
%{_texmfdistdir}/tex/generic/infwarerr
%doc %{_texmfdistdir}/doc/latex/infwarerr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
