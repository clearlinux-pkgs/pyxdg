#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyxdg
Version  : 0.26
Release  : 23
URL      : http://pypi.debian.net/pyxdg/pyxdg-0.26.tar.gz
Source0  : http://pypi.debian.net/pyxdg/pyxdg-0.26.tar.gz
Summary  : PyXDG contains implementations of freedesktop.org standards in python.
Group    : Development/Tools
License  : LGPL-2.0
Requires: pyxdg-license = %{version}-%{release}
Requires: pyxdg-python = %{version}-%{release}
Requires: pyxdg-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
The XDG Package contains:
- Implementation of the XDG-Base-Directory Standard
http://standards.freedesktop.org/basedir-spec/

%package license
Summary: license components for the pyxdg package.
Group: Default

%description license
license components for the pyxdg package.


%package python
Summary: python components for the pyxdg package.
Group: Default
Requires: pyxdg-python3 = %{version}-%{release}

%description python
python components for the pyxdg package.


%package python3
Summary: python3 components for the pyxdg package.
Group: Default
Requires: python3-core
Provides: pypi(pyxdg)

%description python3
python3 components for the pyxdg package.


%prep
%setup -q -n pyxdg-0.26
cd %{_builddir}/pyxdg-0.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603402938
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyxdg
cp %{_builddir}/pyxdg-0.26/COPYING %{buildroot}/usr/share/package-licenses/pyxdg/44f7289042b71631acac29b2f143330d2da2479e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyxdg/44f7289042b71631acac29b2f143330d2da2479e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
