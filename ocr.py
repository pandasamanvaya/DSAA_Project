from PIL import Image
import pytesseract
import editdistance
import os
from math import inf
import sys

if len(sys.argv) < 3:
	print("USAGE {} images_path ppt_path".format(sys.argv[0]))
	sys.exit(1)

images_dir = sys.argv[1]
ppt_dir = sys.argv[2]



ppt_text = {}

for filename in os.listdir(ppt_dir):
	if filename.endswith((".jpg",".png",".jpeg")):
		text = pytesseract.image_to_string(Image.open(ppt_dir+'/'+filename))
		ppt_text[filename] = ' '.join(text.split())

rollnum = "2018121002"
with open(rollnum+".txt","w") as f:
	for filename in os.listdir(images_dir):
		if filename.endswith((".jpg",".png",".jpeg")):
			text = pytesseract.image_to_string(Image.open(images_dir+'/'+filename))
			text = ' '.join(text.split())
			best = inf
			bestfile = ""
			for fname in ppt_text.keys():
				edist = editdistance.eval(text,ppt_text[fname])
				if edist < best:
					best = edist
					bestfile = fname

			f.write(filename+" "+bestfile+'\n')

