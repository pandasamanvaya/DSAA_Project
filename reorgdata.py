import os
from math import inf
import sys
from shutil import copyfile

my= "/home/atrophy98/Desktop/DSAA/Project/drive-download-20190501T190905Z-001/Dataset"

for dirname in os.listdir(my):
	for filename in os.listdir(my+"/"+dirname):
		if filename.endswith((".jpg",".png",".jpeg")):
			if "ppt" in filename:
				copyfile(my+"/"+dirname+"/"+filename, "./slides/"+dirname+"_"+filename)
			else:
				copyfile(my+"/"+dirname+"/"+filename, "./frames/"+dirname+"_"+filename)
