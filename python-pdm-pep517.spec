Name:		python-pdm-pep517
Version:	1.1.4
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/pdm-pep517/pdm-pep517-%{version}.tar.gz
Summary:	A PEP 517 backend for PDM that supports PEP 621 metadata
URL:		https://pypi.org/project/pdm-pep517/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A PEP 517 backend for PDM that supports PEP 621 metadata

%prep
%autosetup -p1 -n pdm-pep517-%{version}

%files
%{py_sitedir}/pdm/pep517
%{py_sitedir}/pdm_pep517-*.*-info
