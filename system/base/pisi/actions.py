# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules

def build():
    #pisitools.dosed("pisi/__init__.py", "2.4", "2.6")
    #pisitools.dosed("pisi/db/lazydb.py", "2.4", "2.6")
    pythonmodules.compile()

def install():
    # Install into /usr/lib/pardus so we can protect ourself from python updates
    pythonmodules.install()

    pisitools.dosym("pisi-cli", "/usr/bin/pisi")

    pisitools.insinto("/etc/pisi", "pisi.conf-%s" % get.ARCH(), "pisi.conf")
