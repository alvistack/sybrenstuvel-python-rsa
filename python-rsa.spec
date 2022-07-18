%global debug_package %{nil}

Name: python-rsa
Epoch: 100
Version: 4.7.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Pure-Python RSA implementation
License: Apache-2.0
URL: https://github.com/sybrenstuvel/python-rsa/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the command-line.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
%if 0%{?centos_version} == 700
mv %{buildroot}%{_bindir}/pyrsa-keygen %{buildroot}%{_bindir}/pyrsa-keygen-3
mv %{buildroot}%{_bindir}/pyrsa-verify %{buildroot}%{_bindir}/pyrsa-verify-3
mv %{buildroot}%{_bindir}/pyrsa-priv2pub %{buildroot}%{_bindir}/pyrsa-priv2pub-3
mv %{buildroot}%{_bindir}/pyrsa-decrypt %{buildroot}%{_bindir}/pyrsa-decrypt-3
mv %{buildroot}%{_bindir}/pyrsa-encrypt %{buildroot}%{_bindir}/pyrsa-encrypt-3
mv %{buildroot}%{_bindir}/pyrsa-sign %{buildroot}%{_bindir}/pyrsa-sign-3
%endif
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-rsa
Summary: Pure-Python RSA implementation
Requires: python3
Requires: python3-pyasn1 >= 0.1.3
Provides: python3-rsa = %{epoch}:%{version}-%{release}
Provides: python3dist(rsa) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rsa = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rsa) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rsa = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rsa) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-rsa
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the command-line.

%files -n python%{python3_version_nodots}-rsa
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-rsa
Summary: Pure-Python RSA implementation
Requires: python3
Requires: python3-pyasn1 >= 0.1.3
Provides: python3-rsa = %{epoch}:%{version}-%{release}
Provides: python3dist(rsa) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-rsa = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(rsa) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-rsa = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(rsa) = %{epoch}:%{version}-%{release}

%description -n python3-rsa
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the command-line.

%files -n python3-rsa
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
