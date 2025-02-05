"""
/***************************************************************************
 SpatialFilter
                                 A QGIS plugin
 This plugin applies spatial filters to layers for performance and efficiency.

 Base was generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-10-16
        copyright            : (C) 2022 Wheregroup GmbH
        email                : info@wheregroup.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QLocale, QSettings, QTranslator, QCoreApplication

import os.path

from .controller import FilterController
from .widgets import FilterToolbar


class SpatialFilter:

    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale', QLocale().name())[0:2]
        locale_path = os.path.join(self.plugin_dir, 'i18n', f'spatial_filter_{locale}.qm')

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        self.toolbar = FilterToolbar(FilterController(), self.iface.mainWindow())
        self.iface.mainWindow().addToolBar(self.toolbar)

    def unload(self):
        self.toolbar.hideFilterGeom()
        self.toolbar.controller.removeFilter()
        self.toolbar.controller.disconnectSignals()
        self.toolbar.deleteLater()
