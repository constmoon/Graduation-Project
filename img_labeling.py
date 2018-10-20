import cv2

cropping = False

x_start, y_start, x_end, y_end = 0, 0, 0, 0
dir = "./images/rice/"
classname = "rice"
imgname = "1.jpg"
image = cv2.imread(dir+imgname)
oriImage = image.copy()
txtfile = "dir.txt"
output_txt = open(txtfile, 'r')


def mouse_crop(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, cropping

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False  # cropping is finished

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2:  # when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)
            cv2.imwrite(imgname, roi)
            string = roi.imline
            # filepath,x1,y1,x2,y2,class_name
            #string = dir + " " + roi.x1 + " " + roi.y1 + " " + roi.x2 + " " + roi.y2 + " " + classname
            output_txt.write(string)
            print(string)
            output_txt.close()


cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)

while True:
    i = image.copy()

    if not cropping:
        cv2.imshow("image", image)

    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow("image", i)

    cv2.waitKey(1)

# close all open windows
cv2.destroyAllWindows()
