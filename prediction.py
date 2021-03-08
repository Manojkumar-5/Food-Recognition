import cv2
import label_image

def load_image(image):
    text = label_image.main(image)
    img = cv2.imread(image)
    return img, text
	
img,text = load_image('/sample.jpg')
cv2.putText(img,'Predicted food is :'+text,(40,20),cv2.FONT_HERSHEY_SIMPLEX)
cv2.imshow('prediction',img)
cv2.waitKey(0)
