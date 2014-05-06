import os
import shutil
import sys

def createFolderFunction(path):
	#print path
	FolderPath = os.path.dirname(path)
	newPath = FolderPath + "\MailingFolder"
	if not os.path.isdir(newPath):
		os.mkdir(newPath)
	if(os.path.isdir(path) and os.path.isfile(newPath+"\\" +os.path.basename(path)) == False):
		shutil.copytree(path,newPath +"\\" +os.path.basename(path))
		FolderName = os.path.basename(path)
		#print "%s is copied" %FolderName

	if(os.path.isfile(path) and os.path.isfile(newPath+"\\" +os.path.basename(path)) == False):
		FileName = os.path.basename(path)
		shutil.copy(path,newPath)
		#print "%s is copied" %FileName
path = sys.argv[1]
createFolderFunction(path)
