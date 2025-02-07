#
# spec file for package python-copr_gui
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-copr_gui
Version:        0.0.6
Release:        0
Summary:        Copr package build gui tools
License:        GPL-3.0-only
URL:            https://pagure.io/matrix/python-copr-wx
Source:         copr_gui-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-bidict
Requires:       python-copr
Requires:       python-json5
BuildArch:      noarch
%python_subpackages

%description
Copr package build gui tools

%prep
%autosetup -p1 -n copr_gui-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%{python_sitelib}/**/*

%changelog
