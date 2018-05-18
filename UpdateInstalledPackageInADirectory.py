
import os, shutil

import win32serviceutil

import urllib.request

import time

import zipfile

serviceName = "Vizrt Pilot Data Server"
win32serviceutil.StopService(serviceName)

time.sleep(5)
print("Vizrt Pilot Data Server service stopped..")

folder = "C:/Program Files/Vizrt/Pilot Data Server/app/pilotedge"

'Code to remove all folders and files from a directory'
for the_file in os.listdir(folder):
	file_path = os.path.join(folder, the_file)
	try:
		if os.path.isfile(file_path):
			os.unlink(file_path)
		elif os.path.isdir(file_path): 
			shutil.rmtree(file_path)
	except Exception as e:
		print(e)

time.sleep(5)
print("Pilor Edge installed directory cleaned up..")

test = urllib.request.URLopener()
test.retrieve("http://component.vizrt.internal/packages/PilotEdge-latest.zip", "C:/Program Files/Vizrt/Pilot Data Server/app/pilotedge/PilotEdge-latest.zip")

time.sleep(5)
print("Latest Pilot Edge zip has been downloaded..")

with zipfile.ZipFile("C:/Program Files/Vizrt/Pilot Data Server/app/pilotedge/PilotEdge-latest.zip","r") as zip_ref:
    zip_ref.extractall("C:/Program Files/Vizrt/Pilot Data Server/app/pilotedge")

time.sleep(5)
print("The zip file is unzipped..")

serviceName = "Vizrt Pilot Data Server"
win32serviceutil.StartService(serviceName)
time.sleep(2)
print("Vizrt Pilot Data Server service started..")		
		
#"D:/BGO/2018/February 2018/February 23/Python work/New folder"
#"C:/Program Files/Vizrt/Pilot Data Server/app/pilotedge"
