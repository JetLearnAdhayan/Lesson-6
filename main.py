import cv2
import os
from PIL import Image

os.chdir("C:/Users/Adhay/OneDrive/Desktop/Open CV/Lesson 6/Photos")

path = "C:/Users//Adhay/OneDrive/Desktop/Open CV/Lesson 6/Photos"



mean_width = 0

mean_height = 0

num_of_images = len(os.listdir("."))

for file in os.listdir("."):
    img=Image.open(os.path.join(path,file))
    width,height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height


mean_width = mean_width//num_of_images
mean_height = mean_height//num_of_images
print(mean_width,mean_height)

for file in os.listdir("."):
    img=Image.open(os.path.join(path,file))
    image_resize = img.resize((mean_width,mean_height))
    image_resize.save(file,"JPEG", quality = 100)
    print("images have resized sucsessfully")


def videoGenerator():
   os.chdir("C:/Users/Adhay/OneDrive/Desktop/Open CV/Lesson 6/Photos")
   video_name = "MyFirstVideo.avi" 
   images = []
   for img in os.listdir("."):
    images.append(img)
   frame = cv2.imread(os.path.join(".",images[0]))
   height, width,layer =frame.shape
   video = cv2.VideoWriter(video_name, 0, 1,(width,height))
   for image in images:
      video.write(cv2.imread(os.path.join(".",image)))

    
   cv2.destroyAllWindows()
   video.release()
    

videoGenerator()

