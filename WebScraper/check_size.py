import os

f = open("seedly-forum/link-names.txt","r")
contents = ""
if f.mode == "r":
    contents = f.read()
   
content_list = contents.split(",")

print(len(content_list))