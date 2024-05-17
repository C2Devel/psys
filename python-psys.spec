%define project_name psys
%global project_description %{expand:
A Python module with a set of basic tools for writing system utilities}

Name:    python-%project_name
Version: 0.4
Release: 3.ROCKIT3%{?dist}
Summary: A Python module with a set of basic tools for writing system utilities

Group:   Development/Languages
License: MIT
URL:     http://github.com/KonishchevDmitry/%project_name
Source:  http://pypi.python.org/packages/source/p/%project_name/%project_name-%{version}.tar.gz

BuildArch:     noarch

%description %{project_description}


%package -n python%{python3_pkgversion}-%project_name
Summary: %{summary}
Requires: python%{python3_pkgversion}-pcore
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
Obsoletes: python36-%project_name
Conflicts: python36-%project_name

%description -n python%{python3_pkgversion}-%project_name %{project_description}


%prep
%setup -n %project_name-%version -q


%build
%{py3_build}

%install
%{py3_install}


%files -n python%{python3_pkgversion}-%project_name
%defattr(-,root,root,-)
%{python3_sitelib}/psys
%{python3_sitelib}/psys-*.egg-info
%doc ChangeLog README INSTALL

%clean
[ "%buildroot" = "/" ] || rm -rf "%buildroot"


%changelog
* Tue Jan 23 2023 Andrey Kulaev <adkulaev@gmail.com> - 0.4-3
- Add centos 8.4 support

* Sun Jan 13 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.4-2
- Add python3 package build for EPEL

* Thu Apr 28 2016 Dmitry Konishchev <konishchev@gmail.com> - 0.4-1
- Add psys.pipe module
- Add psys.process module
- Add psys.daemon.write_pidfile() and psys.daemonize() functions

* Mon Nov 18 2013 Dmitry Konishchev <konishchev@gmail.com> - 0.3-1
- New version

* Wed Nov 13 2013 Dmitry Konishchev <konishchev@gmail.com> - 0.2-1
- New version

* Fri Jun 28 2013 Dmitry Konishchev <konishchev@gmail.com> - 0.1.1-2
- Don't remove *.egg-info to make setup.py with entry_points work
- Provide python-pcore

* Thu Jun 27 2013 Dmitry Konishchev <konishchev@gmail.com> - 0.1.1-1
- New version

* Thu Dec 20 2012 Dmitry Konishchev <konishchev@gmail.com> - 0.1-1
- New package
