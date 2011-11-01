Name:		texlive-cmpj
Version:	1.17
Release:	1
Summary:	Style for the journal Condensed Matter Physics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmpj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpj.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmpj.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package contains macros and some documentation for
typesetting papers for submission to the Condensed Matter
Physics journal published by the Institute for Condensed Matter
Physics of the National Academy of Sciences of Ukraine.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/cmpj/cmpj.bst
%{_texmfdistdir}/tex/latex/cmpj/cmp-logo.eps
%{_texmfdistdir}/tex/latex/cmpj/cmp-logo.pdf
%{_texmfdistdir}/tex/latex/cmpj/cmpj.sty
%doc %{_texmfdistdir}/doc/latex/cmpj/README
%doc %{_texmfdistdir}/doc/latex/cmpj/eps_demo.eps
%doc %{_texmfdistdir}/doc/latex/cmpj/eps_demo.pdf
%doc %{_texmfdistdir}/doc/latex/cmpj/icmphome.eps
%doc %{_texmfdistdir}/doc/latex/cmpj/icmphome.pdf
%doc %{_texmfdistdir}/doc/latex/cmpj/template.pdf
%doc %{_texmfdistdir}/doc/latex/cmpj/template.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
