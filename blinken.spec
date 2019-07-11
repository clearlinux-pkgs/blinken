#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : blinken
Version  : 19.04.3
Release  : 10
URL      : https://download.kde.org/stable/applications/19.04.3/src/blinken-19.04.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.3/src/blinken-19.04.3.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.3/src/blinken-19.04.3.tar.xz.sig
Summary  : Memory Enhancement Game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: blinken-bin = %{version}-%{release}
Requires: blinken-data = %{version}-%{release}
Requires: blinken-license = %{version}-%{release}
Requires: blinken-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : phonon-dev

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
%setup -q -n blinken-19.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562852197
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1562852197
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/blinken
cp COPYING %{buildroot}/usr/share/package-licenses/blinken/COPYING
cp COPYING-sjfonts %{buildroot}/usr/share/package-licenses/blinken/COPYING-sjfonts
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/blinken/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang blinken

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/doc/HTML/ca/blinken/blinken_highscoresbutton.png
/usr/share/doc/HTML/ca/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/ca/blinken/blinken_quitbutton.png
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
/usr/share/doc/HTML/pt_BR/blinken/blinken_highscoresbutton.png
/usr/share/doc/HTML/pt_BR/blinken/blinken_nickprompt.png
/usr/share/doc/HTML/pt_BR/blinken/blinken_quitbutton.png
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
/usr/share/package-licenses/blinken/COPYING
/usr/share/package-licenses/blinken/COPYING-sjfonts
/usr/share/package-licenses/blinken/COPYING.DOC

%files locales -f blinken.lang
%defattr(-,root,root,-)

