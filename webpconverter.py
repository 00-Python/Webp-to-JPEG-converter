from PIL import Image
import os

os.system("mkdir jpgs")

while True:
    img = input("Enter Name of img to convert: \n")
    tst = img[-5:]
    
    if ".jpeg" in tst:
        print("Already a JPEG!")
        exit()
    elif ".jpg" in tst:
        print("Already a JPEG!")
        exit()
    elif ".webp" not in tst:
        img = img+".webp"
        
    noext = img[:-5]
    im = Image.open(img).convert("RGB")
    im.save("jpgs/"+noext+".jpg", "jpeg")
    os.system("del /f "+img)
