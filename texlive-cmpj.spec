Name:		texlive-cmpj
Version:	3.01
Release:	1
Summary:	Style for the journal Condensed Matter Physics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmpj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpj.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpj.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains macros and some documentation for
typesetting papers for submission to the Condensed Matter
Physics journal published by the Institute for Condensed Matter
Physics of the National Academy of Sciences of Ukraine.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/cmpj
%{_texmfdistdir}/tex/latex/cmpj
%doc %{_texmfdistdir}/doc/latex/cmpj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
