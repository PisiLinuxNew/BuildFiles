#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

multilib = "--enable-multilib" if get.ARCH() == "x86_64" else ""

# WorkDir = "binutils-2.20.51"

def setup():
    # Build binutils with LD_SYMBOLIC_FUNCTIONS=1 and reduce PLT relocations in libfd.so by 84%.
    #shelltools.export("LD_SYMBOLIC_FUNCTIONS", "1")
    shelltools.system('sed -i "/ac_cpp=/s/\$CPPFLAGS/\$CPPFLAGS -O2/" libiberty/configure')

    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system('../configure \
                         --prefix=/usr \
                         --enable-shared \
                         --build=%s \
                         --enable-threads \
                         --enable-ld=default \
                         --enable-gold \
                         --enable-plugins \
                         --disable-gdb \
                         --with-pkgversion="Pisi Linux" \
                         --with-bugurl=http://bugs.pisilinux.org/ \
                         %s \
                         --with-pic \
                         --disable-nls \
                         --with-system-zlib \
                         --disable-werror' % (get.HOST(), multilib))
                         #--enable-targets="i386-linux" \

def build():
    # autotools.make("configure-host")
    shelltools.cd("build")

    autotools.make()

# check fails because of LD_LIBRARY_PATH
#def check():
#    autotools.make("check -j1")

def install():
    shelltools.cd("build")

    autotools.rawInstall("DESTDIR=%s tooldir=/usr" % get.installDIR())

    # Remove unneded man , info
    unneeded_man={"dlltool.1","windres.1","windmc.1"}
    for i in unneeded_man:
        pisitools.remove("/usr/share/man/man1/%s" %i)

