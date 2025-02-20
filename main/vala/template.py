pkgname = "vala"
pkgver = "0.56.15"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "flex",
    "bison",
    "xsltproc",
    "pkgconf",
    "automake",
    "libtool",
    "docbook-xml",
]
makedepends = ["libfl-devel-static", "glib-devel", "graphviz-devel"]
checkdepends = ["dbus", "libgirepository-devel", "bash"]
provides = ["so:libvalaccodegen.so=0"]
pkgdesc = "Programming language based on the GObject type system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Vala"
source = f"$(GNOME_SITE)/vala/{pkgver[0:pkgver.rfind('.')]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "535b6452ed310fd5fb5c7dd6794b6213dac3b48e645e5bff3173741ec2cb3f2b"


@subpackage("libvala")
def _lib(self):
    self.pkgdesc = f"{pkgname} (shared library)"

    return ["usr/lib/libvala-*.so.*"]


@subpackage("valadoc")
def _valadoc(self):
    self.pkgdesc = "Vala documentation tool"

    return [
        "usr/bin/valadoc*",
        "usr/share/man/man1/valadoc.1",
    ]


@subpackage("libvaladoc")
def _libdoc(self):
    self.pkgdesc = "Vala documentation tool (shared library)"

    return [
        "usr/lib/libvaladoc-*.so.*",
        "usr/lib/valadoc-*",
        "usr/share/valadoc-*",
    ]


@subpackage("valadoc-devel")
def _develdoc(self):
    self.pkgdesc = "Vala documentation tool (development files)"

    return [
        "usr/include/valadoc-*",
        "usr/lib/libvaladoc-*.so",
        "usr/lib/pkgconfig/valadoc-*.pc",
        "usr/share/vala/vapi/valadoc*",
    ]


@subpackage("vala-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    # do not pick up vapigen.pc etc
    return [
        "usr/lib/libvala-*.so",
        "usr/lib/pkgconfig/libvala*.pc",
        "usr/include/vala-*",
        "usr/share/vala/vapi/libvala-*.*",
        "usr/share/aclocal",
    ]
