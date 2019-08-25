#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #pisitools.domove("/usr/lib/libisl.so.21.0.0-gdb.py", "/usr/share/gdb/auto-load")

    pisitools.dodoc("AUTHORS","ChangeLog","doc/manual.pdf")
