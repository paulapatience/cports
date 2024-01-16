pkgname = "clasp"  # TODO: Name clasp-cl instead?
pkgver = "2.5.0"
pkgrel = 0
# archs = ["aarch64", "x86_64"]  # TODO: check
hostmakedepends = [
    "ninja",
    "pkgconf",
    "sbcl",
]
makedepends = [
    "boost-devel",
    "clang-devel",
    "elfutils-devel",
    "fmt-devel",
    "gmpxx-devel",
    "libucontext-devel",
    "libunwind-devel",
    "llvm-devel",
]
pkgdesc = "Common Lisp implementation"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "LGPL-2.1-or-later AND custom:mps"
url = "https://github.com/clasp-developers/clasp"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/clasp-developers/ansi-test/archive/9f47f89de3a84017f6103e1309f4f07838b74b7f.tar.gz",
    "https://github.com/clasp-developers/cl-bench/archive/7d184b4ef2a6272f0e3de88f6c243edb20f7071a.tar.gz",
    "https://github.com/edicl/cl-who/archive/07dafe9b351c32326ce20b5804e798f10d4f273d.tar.gz",
    "https://github.com/quicklisp/quicklisp-client/archive/refs/tags/version-2021-02-13.tar.gz",
    "https://github.com/yitzchak/shasht/archive/27ba0a8842e103f2d575b3c8bbcfc19bd172d9ea.tar.gz",
    "https://github.com/yitzchak/trivial-do/archive/a19f93227cb80a6bec8846655ebcc7998020bd7e.tar.gz",
    "https://github.com/trivial-gray-streams/trivial-gray-streams/archive/f873865e192d43d2b29b595b9a75bc54a6b68107.tar.gz",
    "https://github.com/robert-strandh/Acclimation/archive/dd15c86b0866fc5d8b474be0da15c58a3c04c45c.tar.gz",
    "https://github.com/clasp-developers/alexandria/archive/refs/tags/v1.4.tar.gz",
    "https://github.com/s-expressionists/Cleavir/archive/30af5977ef44cbf535c61dd696a2c866ba1dbe58.tar.gz",
    "https://github.com/pcostanza/closer-mop/archive/d4d1c7aa6aba9b4ac8b7bb78ff4902a52126633f.tar.gz",
    "https://github.com/s-expressionists/Concrete-Syntax-Tree/archive/37291727196a3bc88a7be67c1427c52078d4b82c.tar.gz",
    "https://github.com/s-expressionists/Eclector/archive/refs/tags/0.9.0.tar.gz",
    "https://github.com/scymtym/esrap/archive/7588b430ad7c52f91a119b4b1c9a549d584b7064.tar.gz",
    "https://github.com/sharplispers/split-sequence/archive/89a10b4d697f03eb32ade3c373c4fd69800a841a.tar.gz",
    "https://github.com/trivial-features/trivial-features/archive/d249a62aaf022902398a7141ae17217251fc61db.tar.gz",
    "https://github.com/hraban/trivial-http/archive/ca45656587f36378305de1a4499c308acc7a03af.tar.gz",
    "https://github.com/scymtym/trivial-with-current-source-form/archive/3898e09f8047ef89113df265574ae8de8afa31ac.tar.gz",
    "https://github.com/usocket/usocket/archive/7ad6582cc1ce9e7fa5931a10e73b7d2f2688fa81.tar.gz",
    "https://github.com/clasp-developers/asdf/archive/refs/heads/add-clasp-bytecode-support.tar.gz",
    "https://github.com/Ravenbrook/mps/archive/b8a05a3846430bc36c8200f24d248c8293801503.tar.gz",
    "https://github.com/ivmai/bdwgc/archive/refs/tags/v8.2.0.tar.gz",
    "https://github.com/ivmai/libatomic_ops/archive/refs/tags/v7.6.12.tar.gz",
]
source_paths = [
    ".",
    "dependencies/ansi-test",
    "dependencies/cl-bench",
    "dependencies/cl-who",
    "dependencies/quicklisp-client",
    "dependencies/shasht",
    "dependencies/trivial-do",
    "src/lisp/kernel/contrib/trivial-gray-streams",
    "src/lisp/kernel/contrib/Acclimation",
    "src/lisp/kernel/contrib/alexandria",
    "src/lisp/kernel/contrib/Cleavir",
    "src/lisp/kernel/contrib/closer-mop",
    "src/lisp/kernel/contrib/Concrete-Syntax-Tree",
    "src/lisp/kernel/contrib/Eclector",
    "src/lisp/kernel/contrib/esrap",
    "src/lisp/kernel/contrib/split-sequence",
    "src/lisp/kernel/contrib/trivial-features",
    "src/lisp/kernel/contrib/trivial-http",
    "src/lisp/kernel/contrib/trivial-with-current-source-form",
    "src/lisp/kernel/contrib/usocket",
    "src/lisp/modules/asdf",
    "src/mps",
    "src/bdwgc",
    "src/libatomic_ops",
]
sha256 = [
    "35b5125d9bbcce2d8e3c8e5d71e034b88ec12cdf2abd062ad744eb0702c045e1",
    "a79b901b0c650c45acf710247c7593793616ffd19b36256ab40f5424e1727014",
    "54bad2d9c2a47f622816cec18520cc17dcdadf233ae0cc18a295684c1c2ac8e1",
    "d1560dc36662d9430630e69a6ae17d8849767512fc1c801fd9b669b683839ab4",
    "b0606eb7da7d98111430342a5cd6c7a3f7e2a86bdc4b0350e095d8dc06a995a2",
    "82779b813ba2c1a34039ff4cd4a84929831762356b220ef61d704e202bfdbe4a",
    "ca4916c6bd8d38ff368bee166b7c9088bf1ddca21cbdb7eadcbbfea1e9725922",
    "6523bfdf8d76c9a4c75c5ef17533b5d9bdf1ad476bffd2e69c990d7cda696f61",
    "5a47b38d6da651405c9101fe0ea891376de00c6c9f077453d1005fff6762decc",
    "698377912deedb56e653e50a3352108473c1571d8252cb99bb13929bf81ff489",
    "e250398c84159695c595cb9f75c0fa1b8ae4c40b905ff746a44db695cc500b33",
    "94c9d09da3be53f4b944b0a6ec65e176228b2674534efd437f5e87623d9276f7",
    "e004380f313e43e34060b2b28559836892328f7e2e9422d7b354d68b4d90dd07",
    "abf30f5456861080333902af89b7297ad61b1e822454e3902f1610b5cda28907",
    "8d4fbc9f008fa0b0710a8e6dabe70c93b921737fe72b3344222c06ba3c8dab29",
    "fb87f03b93a93101d02c09be50ee2ac32d66d11d296d71474b53c52a1d192317",
    "4d6f12754866ba948c018d93bd2badfc5ef10abbe11175dc5a2781743bec566d",
    "6819802e27f4c36df7c6548c47330e6a5a808ea1ae7399cff4c8a5dabc0a111a",
    "7130853322d5fb36903ea2504a71e66847647c60ee9aeadd0fed01466e524feb",
    "2c8a51a305cc275f7a1e2974e94a523437fc78e67e3b3812d3722b29009e1ae1",
    "a42a1b61bca90ef71406a09c9211e5995074c9c772b18c30169d2d20255dd9b7",
    "342cf564fa014a9c19a08ddb733c437065d54ed8810e18c4931089abe40fc673",
    "c7f03093f72190cf5ed427886006b72ab8ca1f45b509c0cb9c8f97cee497d7d3",
    "18091d5f3cb7008b0432016390ff437b9d1d76c10b92c8e63ff63f0c1331b030",
]
# env = {"ASDF_OUTPUT_TRANSLATIONS": "/:/tmp/cache/"}
options = [
    "!cross",
    # "!strip",
]  # TODO: !strip? Arch package has it, may not be necessary


def init_configure(self):
    # TODO: Better place for this? Also, better location for the translations?
    self.env["ASDF_OUTPUT_TRANSLATIONS"] = f"/:{self.chroot_cwd}/cache/"


def do_configure(self):
    self.do(
        "./koga",
        "--skip-sync",
        "--build-mode=bytecode-faso",
        "--reproducible-build",
        "--bin-path=/usr/bin",
        "--lib-path=/usr/lib/clasp",
        "--share-path=/usr/share/clasp",
        f"--package-path={self.chroot_destdir}",
        "--ld=lld",
    )


def init_build(self):
    self.env["ASDF_OUTPUT_TRANSLATIONS"] = f"/:{self.chroot_cwd}/cache/"


def do_build(self):
    self.do("ninja", "-C", "build")


def do_check(self):
    self.do("ninja", "-C", "build", "test")
    self.do("ninja", "-C", "build", "ansi-test")


def do_install(self):
    self.do("ninja", "-C", "build", "install")

    self.install_license("licenses/clasp_Copyright")
    self.install_license("licenses/ecl_Copyright")
    self.install_license("licenses/mps_license.txt")


@subpackage("clasp-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/clasp/*.a",
            # TODO: fasls go into main package?
            # In ECL they are left in the -libs package.
            "usr/lib/clasp/images/*.fasl",
            "usr/lib/clasp/modules/*.fasl",
            # TODO: Contains all the source
            # code; seems excessive.
            "usr/share/clasp",
        ]
    )
