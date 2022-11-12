Name:		texlive-cmdstring
Version:	15878
Release:	1
Summary:	Get command name reliably
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmdstring
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdstring.r15878.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdstring.doc.r15878.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Extracts the letters of a command's name (e.g., foo for command
\foo), in a reliable way.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cmdstring/cmdstring.sty
%doc %{_texmfdistdir}/doc/latex/cmdstring/README
%doc %{_texmfdistdir}/doc/latex/cmdstring/cmdstring.pdf
%doc %{_texmfdistdir}/doc/latex/cmdstring/cmdstring.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
