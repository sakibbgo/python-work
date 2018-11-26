import ftplib
import time
import sys
import os


def main():
	version = str(sys.argv[1])
	product = str(sys.argv[2])
	print(version)
	print(product)
	versionnameconstantdict = {'Pilot':'VizPilot-', 'PDS':'VizrtPilotDataServer-x64-'}

	requiredfilename = []
	installernamelist = []
	productdict = {'Pilot':'/latest_builds_for_testing_only/VCP/', 'PDS':'/latest_builds_for_testing_only/VCP/Services/'}
	
	versionlength = len(versionnameconstantdict[product])+3
	print(versionlength)
	installernamelist = getListOfInstallerNameFromBunny(installernamelist, productdict, product)
	
	requiredfilename = getRequiredInstallerFilename(version, versionnameconstantdict, requiredfilename, installernamelist, versionlength, product)
	
	
	downloadTheRequiredInstaller(requiredfilename, productdict, product)
	
	os.system('msiexec /qb /i '+requiredfilename+' INSTALLDESKTOPSHORTCUTS=1')





		

def getListOfInstallerNameFromBunny(installernamelist, productdict, product):
	try:
		ftp = ftplib.FTP("bunny.vizrt.internal")
		ftp.connect("bunny.vizrt.internal")
		ftp.login("anonymous", "")
	except:
		print("Can't connect to the server!")
		
	try:
		print(productdict[product])
		ftp.cwd(productdict[product])
		installernamelist = ftp.nlst()
		return installernamelist
	except:
		print("Can't get the list of installer name!")




		
		
def getRequiredInstallerFilename(version, versionnameconstantdict, requiredfilename, installernamelist, versionlength, product):
	try:
		for filename in installernamelist:
			if (filename[0:versionlength] == versionnameconstantdict[product]+version):
				requiredfilename = filename
			else:
				continue
		return requiredfilename
	except:
		print("Can't get the requred installer name!")
		
		
		
		
def downloadTheRequiredInstaller(requiredfilename, productdict, product):
	try:
		ftp = ftplib.FTP("bunny.vizrt.internal")
		ftp.login("anonymous", "")
		ftp.cwd(productdict[product])
	except:
		print("Can't connect to the Bunny server!")
	
	try:
		localfile = open(requiredfilename, 'wb')
		ftp.retrbinary('RETR ' + requiredfilename, localfile.write, 1024)
		time.sleep(5)	
	except:
		print("Can't download the installer!")
	
		
		
	
		
main()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	