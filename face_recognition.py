import cv2
import face_recognition as fr
from PIL import Image

#load image file- used to load image in an array
img1= fr.load_image_file(""path\\1.png"") 
img2= fr.load_image_file(""path\\2.png"")

img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB);   #changes color format
img2=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB);

#face encoding function - returns an array of 128 dimensions face encodings for each face in the image
img1=fr.face_encodings(img1)[0]    #image encoding
img1=fr.face_encodings(img1)[0]


#comare faces=it returns an array of true false showing which encoding matches it
res=fr.compare_faces([enc1],enc2, tolerance=0.5) #
print(res)

location=fr.face_locations(img1)[0]
print(location) #gives 4 coordinates of face- top, right, bottom, left

top, right, bottom, left=location
face= img1[top:bottom, left:right]  #gets face from image

finalImage=Image.fromarray(face)  #converts array to image
finalImage.show()  

landmarks= fr.face_landmarks(img1)[0]
print(landmarks)

img= Image.fromarray(img1)
img_draw= ImageDraw(img)  #image_draw- a module that enables us to draw on image using draw function

img_draw.line(landmarks["left_eye"])
img_draw.line(landmarks["right_eye"])

img.show()
