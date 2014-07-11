# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cmdstring
# catalog-date 2008-08-18 10:38:42 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-cmdstring
Version:	1.1
Release:	8
Summary:	Get command name reliably
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmdstring
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdstring.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdstring.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 750264
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 718078
- texlive-cmdstring
- texlive-cmdstring
- texlive-cmdstring
- texlive-cmdstring
- texlive-cmdstring

