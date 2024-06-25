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
    cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    return img



# import pdf
filepath = "/Users/arhan.sheth/Documents/Codes/DX/cv_projects/empty-receivables-6-20pm.pdf"

#convert into image and add contours
page_img = pdf_to_img(filepath)
img_table = tables(page_img)
cv.imshow("img", img_table)
cv.waitKey(0)
cv.destroyAllWindows()


