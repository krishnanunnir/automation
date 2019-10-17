#!/usr/bin/python
import sys
import os

def printUsageMsg(e):
	print(e)
	print("Usage:\tpython updateJar.py [filename] [jarname] [classpath dependency 1] [classpath dependency 2]...............")
	quit()
args = sys.argv

if(len(args)<=2):
	printUsageMsg("The program expects atleast two arguments.")
filename = args[1]
jarname = args[2]
currentDirectory = os.getcwd()
classpath = "\":" + currentDirectory + "/*:"
for i in args[3:]:
        classpath += currentDirectory + "/" +i +"/*:"
classpath += "\"" 
f = open(filename,'r')
for lines in f:
	try:
		if(lines.split()[0] == "package"):
			name = lines.split()[1][:-1]
			name = name.split('.')
			folderName = name[0]
			packageName = '/'.join(name)
			classNameList = filename.split('.')
			className = classNameList[0] + ".class"
			os.system("jar xf "+ jarname)
			os.system("javac -cp  " + classpath + " " + filename)
			os.system("mkdir -p " + packageName)
			os.system("cp " + className +" " + packageName)
			os.system("rm " + className)
			os.system("jar -uf " +jarname + " " + packageName + "/" +className)
			os.system("rm -rf " + folderName)
			break
	except Exception as e:
		printUsageMsg(e)