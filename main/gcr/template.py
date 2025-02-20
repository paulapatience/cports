pkgname = "gcr"
pkgver = "4.2.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgpg_path=/usr/bin/gpg",
    "-Dsystemd=disabled",
    "-Dssh_agent=false",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gtk-doc-tools",
    "gettext-devel",
    "gobject-introspection",
    "vala",
    "openssh",
]
makedepends = [
    "gtk4-devel",
    "libgcrypt-devel",
    "libsecret-devel",
    "p11-kit-devel",
    "libxslt-devel",
    "vala",
]
pkgdesc = "GNOME crypto package"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gcr"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ed783b5c80373cd058c02ea9e3e2a64e558599ca190a5abd598122e479967de5"
# getpass
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# FIXME int (crashes gnome-keyring suite)
hardening = ["!int"]
# needs x11
options = ["!check"]


def post_install(self):
    self.install_file(
        self.files_path / "10-gcr-memlock.conf", "etc/security/limits.d"
    )


@subpackage("gcr-devel")
def _devel(self):
    return self.default_devel()


@subpackage("gcr-progs")
def _progs(self):
    return self.default_progs()
