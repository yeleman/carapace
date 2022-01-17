#!/urs/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

from __future__ import unicode_literals, absolute_import, division, print_function

import sys

from PyQt5.QtWidgets import QApplication
from database import setup

from ui.mainwindow import MainWindow

app = QApplication(sys.argv)


def main():

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
