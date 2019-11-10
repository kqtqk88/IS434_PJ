import os
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", type=str,
	help="path to input folder", default=0)
args = vars(ap.parse_args())

if args["folder"]:

	# outfolder = os.getcwd()+"/Text_"+args["folder"]
	destination = "Text_"+args["folder"]

	if not os.path.exists(destination):
		os.makedirs(destination)

	for root, dirs, files in os.walk(args["folder"]):
		for file in files:
			if file.endswith(".jpg"):
				path = os.path.join(root, file)
				outputfile = path.replace(args['folder'], destination)


				outfolder = os.path.dirname(outputfile)
				if not os.path.exists(outfolder):
				    os.makedirs(outfolder)

				cmd = "python text_detection.py --image " + path + " --east frozen_east_text_detection.pb --out " + outputfile
				os.system(cmd)