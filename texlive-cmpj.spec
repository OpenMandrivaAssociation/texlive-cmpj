%global tl_name cmpj
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.04a
Release:	%{tl_revision}.1
Summary:	Style for the journal Condensed Matter Physics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cmpj
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpj.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpj.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains macros and some documentation for typesetting
papers for submission to the Condensed Matter Physics journal published
by the Yukhnovskii Institute for Condensed Matter Physics of the
National Academy of Sciences of Ukraine.

