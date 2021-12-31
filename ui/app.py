# Form implementation generated from reading ui file 'f:\2. Programming\3. VS Code Project\Python\music_player_qt\ui\app.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(App)
        self.gridLayout.setObjectName("gridLayout")
        self.search_button = QtWidgets.QPushButton(App)
        self.search_button.setMinimumSize(QtCore.QSize(0, 30))
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 0, 0, 1, 1)
        self.search_bar = QtWidgets.QLineEdit(App)
        self.search_bar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_bar.setFont(font)
        self.search_bar.setObjectName("search_bar")
        self.gridLayout.addWidget(self.search_bar, 0, 1, 1, 1)
        self.playback_control = QtWidgets.QWidget(App)
        self.playback_control.setMinimumSize(QtCore.QSize(0, 90))
        self.playback_control.setMaximumSize(QtCore.QSize(16777215, 80))
        self.playback_control.setStyleSheet("QWidget {\n"
"\n"
"}")
        self.playback_control.setObjectName("playback_control")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.playback_control)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backward_button = QtWidgets.QToolButton(self.playback_control)
        self.backward_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.backward_button.setToolTipDuration(-1)
        self.backward_button.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.backward_button.setIconSize(QtCore.QSize(40, 40))
        self.backward_button.setObjectName("backward_button")
        self.horizontalLayout.addWidget(self.backward_button)
        self.pause_button = QtWidgets.QToolButton(self.playback_control)
        self.pause_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pause_button.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.pause_button.setIconSize(QtCore.QSize(48, 48))
        self.pause_button.setObjectName("pause_button")
        self.horizontalLayout.addWidget(self.pause_button)
        self.resume_button = QtWidgets.QToolButton(self.playback_control)
        self.resume_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.resume_button.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.resume_button.setIconSize(QtCore.QSize(48, 48))
        self.resume_button.setObjectName("resume_button")
        self.horizontalLayout.addWidget(self.resume_button)
        self.forward_button = QtWidgets.QToolButton(self.playback_control)
        self.forward_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.forward_button.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.forward_button.setIconSize(QtCore.QSize(40, 40))
        self.forward_button.setObjectName("forward_button")
        self.horizontalLayout.addWidget(self.forward_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.duration_passed = QtWidgets.QLabel(self.playback_control)
        self.duration_passed.setObjectName("duration_passed")
        self.horizontalLayout.addWidget(self.duration_passed)
        self.progress_bar = QtWidgets.QSlider(self.playback_control)
        self.progress_bar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progress_bar.setObjectName("progress_bar")
        self.horizontalLayout.addWidget(self.progress_bar)
        self.total_duration = QtWidgets.QLabel(self.playback_control)
        self.total_duration.setObjectName("total_duration")
        self.horizontalLayout.addWidget(self.total_duration)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.playback_control)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.volume_bar = QtWidgets.QSlider(self.playback_control)
        self.volume_bar.setMaximumSize(QtCore.QSize(150, 16777215))
        self.volume_bar.setMaximum(100)
        self.volume_bar.setSingleStep(5)
        self.volume_bar.setProperty("value", 30)
        self.volume_bar.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_bar.setObjectName("volume_bar")
        self.horizontalLayout.addWidget(self.volume_bar)
        self.playbackmode_loop = QtWidgets.QToolButton(self.playback_control)
        self.playbackmode_loop.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.playbackmode_loop.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.playbackmode_loop.setIconSize(QtCore.QSize(48, 48))
        self.playbackmode_loop.setObjectName("playbackmode_loop")
        self.horizontalLayout.addWidget(self.playbackmode_loop)
        self.playbackmode_sequential = QtWidgets.QToolButton(self.playback_control)
        self.playbackmode_sequential.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.playbackmode_sequential.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.playbackmode_sequential.setIconSize(QtCore.QSize(48, 48))
        self.playbackmode_sequential.setObjectName("playbackmode_sequential")
        self.horizontalLayout.addWidget(self.playbackmode_sequential)
        self.playbackmode_looponce = QtWidgets.QToolButton(self.playback_control)
        self.playbackmode_looponce.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.playbackmode_looponce.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.playbackmode_looponce.setIconSize(QtCore.QSize(48, 48))
        self.playbackmode_looponce.setObjectName("playbackmode_looponce")
        self.horizontalLayout.addWidget(self.playbackmode_looponce)
        self.playbackmode_random = QtWidgets.QToolButton(self.playback_control)
        self.playbackmode_random.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.playbackmode_random.setStyleSheet("QToolButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.playbackmode_random.setIconSize(QtCore.QSize(48, 48))
        self.playbackmode_random.setObjectName("playbackmode_random")
        self.horizontalLayout.addWidget(self.playbackmode_random)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addWidget(self.playback_control, 3, 0, 1, 2)
        self.main_menu = QtWidgets.QWidget(App)
        self.main_menu.setObjectName("main_menu")
        self.gridLayout.addWidget(self.main_menu, 2, 1, 1, 1)
        self.other_menu = QtWidgets.QWidget(App)
        self.other_menu.setMinimumSize(QtCore.QSize(160, 0))
        self.other_menu.setMaximumSize(QtCore.QSize(160, 16777215))
        self.other_menu.setStyleSheet("QWidget {\n"
"}")
        self.other_menu.setObjectName("other_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.other_menu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.home_button = QtWidgets.QPushButton(self.other_menu)
        self.home_button.setObjectName("home_button")
        self.verticalLayout.addWidget(self.home_button)
        self.line_2 = QtWidgets.QFrame(self.other_menu)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.download_from_url_button = QtWidgets.QPushButton(self.other_menu)
        self.download_from_url_button.setObjectName("download_from_url_button")
        self.verticalLayout.addWidget(self.download_from_url_button)
        self.setting_button = QtWidgets.QPushButton(self.other_menu)
        self.setting_button.setObjectName("setting_button")
        self.verticalLayout.addWidget(self.setting_button)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.playlist_button = QtWidgets.QPushButton(self.other_menu)
        self.playlist_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.playlist_button.setStyleSheet("QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    color: rgb(115, 115, 115);\n"
"}")
        self.playlist_button.setObjectName("playlist_button")
        self.verticalLayout.addWidget(self.playlist_button)
        self.line = QtWidgets.QFrame(self.other_menu)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.listWidget = QtWidgets.QListWidget(self.other_menu)
        self.listWidget.setMaximumSize(QtCore.QSize(160, 16777215))
        self.listWidget.setStyleSheet("QListWidget {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"}")
        self.listWidget.setItemAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout.addWidget(self.other_menu, 2, 0, 1, 1)

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Music Player"))
        self.search_button.setToolTip(_translate("App", "Search"))
        self.search_button.setText(_translate("App", "Search"))
        self.search_bar.setToolTip(_translate("App", "Search songs here..."))
        self.search_bar.setPlaceholderText(_translate("App", "Search songs here...."))
        self.backward_button.setText(_translate("App", "..."))
        self.pause_button.setText(_translate("App", "..."))
        self.pause_button.setShortcut(_translate("App", "Space"))
        self.resume_button.setText(_translate("App", "..."))
        self.resume_button.setShortcut(_translate("App", "Space"))
        self.forward_button.setText(_translate("App", "..."))
        self.duration_passed.setText(_translate("App", "0:00"))
        self.total_duration.setText(_translate("App", "0:00"))
        self.label.setText(_translate("App", "Volume"))
        self.playbackmode_loop.setText(_translate("App", "..."))
        self.playbackmode_sequential.setText(_translate("App", "..."))
        self.playbackmode_looponce.setText(_translate("App", "..."))
        self.playbackmode_random.setText(_translate("App", "..."))
        self.home_button.setText(_translate("App", "Home"))
        self.download_from_url_button.setToolTip(_translate("App", "Download something directly from a given link"))
        self.download_from_url_button.setText(_translate("App", "Download from URL"))
        self.setting_button.setToolTip(_translate("App", "Settings"))
        self.setting_button.setText(_translate("App", "Settings"))
        self.playlist_button.setToolTip(_translate("App", "All the downloaded audio are stored in here"))
        self.playlist_button.setText(_translate("App", "Downloads"))
