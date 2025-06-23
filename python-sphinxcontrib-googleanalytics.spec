#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension googleanalytics
Summary(pl.UTF-8):	Rozszerzenie Sphinksa googleanalytics
Name:		python-sphinxcontrib-googleanalytics
Version:	0.4
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-googleanalytics/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-googleanalytics/sphinxcontrib-googleanalytics-%{version}.tar.gz
# Source0-md5:	a267c20096c4006bef6605e64cb3a4d3
URL:		https://pypi.org/project/sphinxcontrib-googleanalytics/
%if %{with python2}
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules
Requires:	python-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extensions allows tracking generated HTML files with Google
Analytics web service.

%description -l pl.UTF-8
To rozszerzenie pozwala na śledzenie wygenerowanych plików HTML przy
użyciu usługi WWW Google Analytics.

%package -n python3-sphinxcontrib-googleanalytics
Summary:	Sphinx extension googleanalytics
Summary(pl.UTF-8):	Rozszerzenie Sphinksa googleanalytics
Group:		Libraries/Python
Requires:	python3-modules
Requires:	python3-sphinxcontrib

%description -n python3-sphinxcontrib-googleanalytics
This extensions allows tracking generated html files with Google
Analytics web service.

%description -n python3-sphinxcontrib-googleanalytics -l pl.UTF-8
To rozszerzenie pozwala na śledzenie wygenerowanych plików HTML przy
użyciu usługi WWW Google Analytics.

%prep
%setup -q -n sphinxcontrib-googleanalytics-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/sphinxcontrib/googleanalytics.py[co]
%{py_sitescriptdir}/sphinxcontrib_googleanalytics-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_googleanalytics-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-googleanalytics
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/sphinxcontrib/googleanalytics.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/googleanalytics.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_googleanalytics-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_googleanalytics-%{version}-py*-nspkg.pth
%endif
