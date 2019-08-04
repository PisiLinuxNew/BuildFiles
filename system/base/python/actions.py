#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pisitools.flags.add("-fwrapv")

    pisitools.dosed("Lib/cgi.py","^#.* /usr/local/bin/python","#!/usr/bin/python")
    # Speed up LTO
    pisitools.dosed("configure","-flto","-flto=4")

    for dir in ["expat","_ctypes/libffi_msvc", "_ctypes/libffi_osx","_ctypes/darwin"]:
        shelltools.unlinkDir("Modules/%s" % dir)

    autotools.rawConfigure("\
                            --prefix=/usr \
                            --enable-shared \
                            --with-computed-gotos \
                            --enable-ipv6 \
                            --with-system-expat \
                            --with-dbmliborder=gdbm:ndbm \
                            --with-system-ffi \
                            --enable-loadable-sqlite-extensions \
                            --without-ensurepip")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.insinto("/usr/lib/python3.6/Tools","Tools/i18n")
    pisitools.insinto("/usr/lib/python3.6/Tools","Tools/scripts")

    # pisitools.remove("/usr/bin/2to3")
    # pisitools.remove("/usr/bin/2to3-3.6")

    # remove tcltk files
    pisitools.remove("/usr/bin/idle3")
    pisitools.remove("/usr/bin/idle3.6")

    for dir in ["/usr/lib/python3.6/tkinter", "/usr/lib/python3.6/idlelib","/usr/lib/python3.6/turtledemo", "/usr/lib/python3.6/test/test_tk*"]:
        pisitools.removeDir("%s" % dir)

    pisitools.dodoc("LICENSE", "README.*")
    