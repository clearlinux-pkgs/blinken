#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: 250a666
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : blinken
Version  : 23.08.3
Release  : 59
URL      : https://download.kde.org/stable/release-service/23.08.3/src/blinken-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/blinken-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/blinken-23.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GFDL-1.2 GPL-2.0
Requires: blinken-bin = %{version}-%{release}
Requires: blinken-data = %{version}-%{release}
Requires: blinken-license = %{version}-%{release}
Requires: blinken-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : phonon-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Blinken uses a special handwriting font called Steve that is in the
fonts directory to show the status text. If this font is not currently installed
on the target system, on first run Blinken uses the fonts:/ ioslave to copy it
to the user's fonts location.

%package bin
Summary: bin components for the blinken package.
Group: Binaries
Requires: blinken-data = %{version}-%{release}
Requires: blinken-license = %{version}-%{release}

%description bin
bin components for the blinken package.


%package data
Summary: data components for the blinken package.
Group: Data

%description data
data components for the blinken package.


%package doc
Summary: doc components for the blinken package.
Group: Documentation

%description doc
doc components for the blinken package.


%package license
Summary: license components for the blinken package.
Group: Default

%description license
license components for the blinken package.


%package locales
Summary: locales components for the blinken package.
Group: Default

%description locales
locales components for the blinken package.


%prep
%setup -q -n blinken-23.08.3
cd %{_builddir}/blinken-23.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699559479
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1699559479
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/blinken
cp %{_builddir}/blinken-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/blinken/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/blinken-%{version}/LICENSES/GFDL-1.2-only.txt %{buildroot}/usr/share/package-licenses/blinken/7b300def279cc0c38b84d3351f68d558cc01ad61 || :
cp %{_builddir}/blinken-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/blinken/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/blinken-%{version}/LICENSES/LicenseRef-SJFonts.txt %{buildroot}/usr/share/package-licenses/blinken/0018a9a18b50c9dcea23b1178ba98063b5a9b018 || :
cp %{_builddir}/blinken-%{version}/LICENSES/LicenseRef-SJFonts.txt %{buildroot}/usr/share/package-licenses/blinken/0018a9a18b50c9dcea23b1178ba98063b5a9b018 || :
cp %{_builddir}/blinken-%{version}/fonts/steve.ttf.license %{buildroot}/usr/share/package-licenses/blinken/67bc81af1c395d6bd93b6687ff4eb1c15fe8a6f9 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang blinken
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/blinken
/usr/bin/blinken

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.blinken.desktop
/usr/share/blinken/README.packagers
/usr/share/blinken/fonts/steve.ttf
/usr/share/blinken/images/blinken.svg
/usr/share/blinken/sounds/1.wav
/usr/share/blinken/sounds/2.wav
/usr/share/blinken/sounds/3.wav
/usr/share/blinken/sounds/4.wav
/usr/share/blinken/sounds/lose.wav
/usr/share/config.kcfg/blinken.kcfg
/usr/share/icons/hicolor/128x128/apps/blinken.png
/usr/share/icons/hicolor/16x16/apps/blinken.png
/usr/share/icons/hicolor/22x22/apps/blinken.png
/usr/share/icons/hicolor/32x32/apps/blinken.png
/usr/share/icons/hicolor/48x48/apps/blinken.png
/usr/share/icons/hicolor/64x64/apps/blinken.png
/usr/share/icons/hicolor/scalable/apps/blinken.svgz
/usr/share/metainfo/org.kde.blinken.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/blinken/blinken1.png
/usr/share/doc/HTML/ca/blinken/blinken2.png
/usr/share/doc/HTML/ca/blinken/blinken_accesskeys.png
/usr/share/doc/HTML/ca/blinken/blinken_helpbutton.png
/usr/share/doc/HTML/ca/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/ca/blinken/index.cache.bz2
/usr/share/doc/HTML/ca/blinken/index.docbook
/usr/share/doc/HTML/de/blinken/blinken1.png
/usr/share/doc/HTML/de/blinken/blinken2.png
/usr/share/doc/HTML/de/blinken/blinken_accesskeys.png
/usr/share/doc/HTML/de/blinken/blinken_helpbutton.png
/usr/share/doc/HTML/de/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/de/blinken/blinken_quitbutton.png
/usr/share/doc/HTML/de/blinken/index.cache.bz2
/usr/share/doc/HTML/de/blinken/index.docbook
/usr/share/doc/HTML/en/blinken/blinken1.png
/usr/share/doc/HTML/en/blinken/blinken2.png
/usr/share/doc/HTML/en/blinken/blinken_accesskeys.png
/usr/share/doc/HTML/en/blinken/blinken_helpbutton.png
/usr/share/doc/HTML/en/blinken/blinken_highscoresbutton.png
/usr/share/doc/HTML/en/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/en/blinken/blinken_quitbutton.png
/usr/share/doc/HTML/en/blinken/index.cache.bz2
/usr/share/doc/HTML/en/blinken/index.docbook
/usr/share/doc/HTML/es/blinken/index.cache.bz2
/usr/share/doc/HTML/es/blinken/index.docbook
/usr/share/doc/HTML/et/blinken/index.cache.bz2
/usr/share/doc/HTML/et/blinken/index.docbook
/usr/share/doc/HTML/fr/blinken/blinken1.png
/usr/share/doc/HTML/fr/blinken/blinken2.png
/usr/share/doc/HTML/fr/blinken/blinken_accesskeys.png
/usr/share/doc/HTML/fr/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/fr/blinken/index.cache.bz2
/usr/share/doc/HTML/fr/blinken/index.docbook
/usr/share/doc/HTML/it/blinken/index.cache.bz2
/usr/share/doc/HTML/it/blinken/index.docbook
/usr/share/doc/HTML/nl/blinken/index.cache.bz2
/usr/share/doc/HTML/nl/blinken/index.docbook
/usr/share/doc/HTML/pt/blinken/index.cache.bz2
/usr/share/doc/HTML/pt/blinken/index.docbook
/usr/share/doc/HTML/pt_BR/blinken/blinken1.png
/usr/share/doc/HTML/pt_BR/blinken/blinken2.png
/usr/share/doc/HTML/pt_BR/blinken/blinken_accesskeys.png
/usr/share/doc/HTML/pt_BR/blinken/blinken_helpbutton.png
/usr/share/doc/HTML/pt_BR/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/pt_BR/blinken/index.cache.bz2
/usr/share/doc/HTML/pt_BR/blinken/index.docbook
/usr/share/doc/HTML/sv/blinken/blinken1.png
/usr/share/doc/HTML/sv/blinken/blinken2.png
/usr/share/doc/HTML/sv/blinken/blinken_accesskeys.png
/usr/share/doc/HTML/sv/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/sv/blinken/index.cache.bz2
/usr/share/doc/HTML/sv/blinken/index.docbook
/usr/share/doc/HTML/uk/blinken/blinken1.png
/usr/share/doc/HTML/uk/blinken/blinken2.png
/usr/share/doc/HTML/uk/blinken/blinken_accesskeys.png
/usr/share/doc/HTML/uk/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/uk/blinken/index.cache.bz2
/usr/share/doc/HTML/uk/blinken/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/blinken/0018a9a18b50c9dcea23b1178ba98063b5a9b018
/usr/share/package-licenses/blinken/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/blinken/67bc81af1c395d6bd93b6687ff4eb1c15fe8a6f9
/usr/share/package-licenses/blinken/7b300def279cc0c38b84d3351f68d558cc01ad61
/usr/share/package-licenses/blinken/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f blinken.lang
%defattr(-,root,root,-)

