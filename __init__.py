import os
import sys
import tempfile


__MAINPATH = os.path.dirname(__file__)
__ICONPATH = os.path.join(__MAINPATH, "icons")
__BINPATH = os.path.join(__MAINPATH, "bin")
__SCRIPTPATH = os.path.join(__MAINPATH, "scripts")
__PACKAGEPATH = os.path.join(__MAINPATH, "packages")


sys.path.append(__SCRIPTPATH)
sys.path.append(__PACKAGEPATH)



def getMainPath():
    return __MAINPATH
def GetIcon(name):

    iconfile = os.path.join(__ICONPATH, name)
    if os.path.isfile(iconfile):
        return iconfile
def makeTempIconFile():
    folder = makeTempDir()
    imagename = os.path.join(folder,"perviewImage.jpg")
    return imagename

def makeTempDir():
    tmp = tempfile.mktemp(prefix="capute")
    os.makedirs(tmp)
    return tmp
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