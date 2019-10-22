import cv2

image = cv2.imread("Testing/Sidecar-21689150_173486586555782_7058856979510329344_n-20170913-18h-04m.jpg")
hist = cv2.calcHist(image,[0,1,2], None, (256,256,256), [0,256,0,256,0,256])

color_count = 0
for i in hist:
	for j in i:
		for k in j:
			if k:
				color_count += 1

print(color_count)