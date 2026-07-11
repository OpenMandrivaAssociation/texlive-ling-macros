%global tl_name ling-macros
%global tl_revision 42268

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros for typesetting formal linguistics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ling-macros
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ling-macros.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ling-macros.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains macros for typesetting glosses and formal
expressions. It covers a range of subfields in formal linguistics.

