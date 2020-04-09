import os
#import autolip
import maya.cmds as cmds
import librarywindow

libraryWindow = None
lipWindow = None

# def autolipShow():
# 	global lipWindow
# 	try:
# 		cmds.deleteUI("AUTOLIPWINDOWWorkspaceControl")
# 		cmds.deleteUI("AUTOLIPWINDOWW")
# 	except:
# 		pass
# 	lipWindow = autolip.autoLipWindow()
# 	lipWindow.show()


def libraryShow():
	global libraryWindow

	if libraryWindow:
		libraryWindow.show()
	else:
		if cmds.window(librarywindow.LIBRARYWINDOWNAME,q=True,ex=True):
			cmds.deleteUI(librarywindow.LIBRARYWINDOWNAME)

		libraryWindow = librarywindow.libraryMainWindow()
		#print libraryWindow.objectName()
		libraryWindow.show()