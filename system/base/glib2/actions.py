#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.makedirs("build")

    shelltools.cd("build")
    options = "meson --prefix=/usr \
                     -Dinternal_pcre=false \
                     -Dlibmount=false \
                     -Dgtk_doc=false \
                     -Dfam=false \
                     -Dsystemtap=false \
                     -Dinstalled_tests=false \
                     -Dselinux=disabled"


    if get.buildTYPE() == "_emul32":
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")
        options += " --libdir=lib32 \
                     --bindir=/usr/_emul32/bin \
                     --sbindir=/usr/_emul32/sbin \
                     -DG_DISABLE_CAST_CHECKS=true \
                     -Ddtrace=false .."

    shelltools.system(options)

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.cd("build")
    shelltools.system("DESTDIR=%s ninja install" % get.installDIR())

    if get.buildTYPE() == "_emul32":
        pisitools.domove("/usr/_emul32/bin/gio-querymodules", "/usr/bin/32/")
        pisitools.removeDir("/usr/_emul32")
        pisitools.dosed("%s/usr/lib32/pkgconfig/*.pc" % get.installDIR(), "_emul32", "usr")
        pisitools.removeDir("/usr/share/gdb")
        return

    pisitools.removeDir("/usr/share/gdb")
    
    shelltools.cd("..")
    pisitools.dodoc("AUTHORS", "README*", "NEWS")
