Name:		texlive-ling-macros
Version:	42268
Release:	1
Summary:	Macros for typesetting formal linguistics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ling-macros
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ling-macros.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ling-macros.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains macros for typesetting glosses and formal
expressions. It covers a range of subfields in formal
linguistics.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ling-macros
%doc %{_texmfdistdir}/doc/latex/ling-macros

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
