pkgname = "evolution"
pkgver = "3.50.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_OPENLDAP=OFF",
    "-DENABLE_TEXT_HIGHLIGHT=OFF",
    "-DENABLE_PST_IMPORT=OFF",
    "-DENABLE_MARKDOWN=OFF",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
    "intltool",
    "itstool",
    "ninja",
    "pkgconf",
]
makedepends = [
    "at-spi2-core-devel",
    "cairo-devel",
    "enchant-devel",
    "evolution-data-server-devel",
    "gdk-pixbuf-devel",
    "geocode-glib-devel",
    "glib-devel",
    "gnome-autoar-devel",
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "gspell-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libgweather-devel",
    "libnotify-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libxml2-devel",
    "nspr-devel",
    "nss-devel",
    "shared-mime-info",
    "sqlite-devel",
    "webkitgtk-devel",
    "xorgproto",
    "ytnef-devel",
]
pkgdesc = "Mail, calendar and address book suite"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Apps/Evolution"
source = f"https://download.gnome.org/sources/evolution/{pkgver[:-2]}/evolution-{pkgver}.tar.xz"
sha256 = "e0f955ca14dfb1b2e1682fcfa1816a03c114b8161998f96cf9d681a6a3842698"


@subpackage("evolution-devel")
def _devel(self):
    return self.default_devel()
