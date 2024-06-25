import cv2 as cv
import numpy as np
from pdf2image import convert_from_path

def pdf_to_img(pdf_path):
    return convert_from_path(pdf_path, 300)[0]

def tables(image):
    #convert img to array
    img = np.array(image)
    #convert into grayscale
    gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    #apply threshold
    _, thresh = cv.threshold(gray_img, 150, 255, cv.THRESH_BINARY_INV)
    # find contours
    contours, heirarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cropped_images = []
    for c in contours:
        x, y, w, h = cv.boundingRect(c)
        if h >= 120 and w >= 2066:
            cv.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
            crop_img = img[y:y+h, x:x+w]
            cropped_images.append(crop_img)
    return cropped_images
    #return img


# import pdf
filepath = "/Users/arhan.sheth/Documents/Codes/DX/cv_projects/split2/empty-receivables-6-24pm.pdf"

#convert into image and add contours
page_img = pdf_to_img(filepath)
img_table = tables(page_img)
#cv.imshow("Image", img_table)
#cv.waitKey(0)
#cv.destroyAllWindows()
#save each file 
for i, table in enumerate(img_table):
    img_path = f"/Users/arhan.sheth/Documents/Codes/DX/cv_projects/split2/cropped_table{i}.jpeg"
    cv.imwrite(img_path, table)
    print(f"Table{i} cropped and saved")

#cv.putText(img, str(w), (x,y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
#cv.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 1)