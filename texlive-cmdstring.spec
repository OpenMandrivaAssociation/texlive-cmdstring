Name:		texlive-cmdstring
Version:	1.1
Release:	1
Summary:	Get command name reliably
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmdstring
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdstring.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdstring.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Extracts the letters of a command's name (e.g., foo for command
\foo), in a reliable way.

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
%{_texmfdistdir}/tex/latex/cmdstring/cmdstring.sty
%doc %{_texmfdistdir}/doc/latex/cmdstring/README
%doc %{_texmfdistdir}/doc/latex/cmdstring/cmdstring.pdf
%doc %{_texmfdistdir}/doc/latex/cmdstring/cmdstring.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
