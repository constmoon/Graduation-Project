import cv2

if __name__ == '__main__':
    dir = "./images/bulgogi/"    # Read image
    classname = "bulgogi"        # set class name
    imgname = "0.jpg"
    image = cv2.imread(dir + imgname)
    oriImage = image.copy()
    txtfile = "./dir/dir_bulgogi.txt"
    output_txt = open(txtfile, 'a')

    im = cv2.imread(dir+imgname)
    r = cv2.selectROI(im)    # Select ROI
    imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]    # Crop image

    # Display cropped image
    cv2.imshow("Image", imCrop)

    # Save ROI image
    newDir = "./edit/bulgogi/"
    newImgname = newDir + imgname
    cv2.imwrite(newImgname, imCrop)

    string = dir + imgname + " " + str(int(r[0])) + " " + str(int(r[1])) + " " + str(int(r[2])) + " " + str(int(r[3])) + " " + classname + "\n"
    print(string)
    output_txt.write(string)
    output_txt.close()
    cv2.waitKey(0)