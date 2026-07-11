%global tl_name cmdstring
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Get command name reliably
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cmdstring
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdstring.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdstring.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Extracts the letters of a command's name (e.g., foo for command \foo),
in a reliable way.

