import cv2


def resize(i):
    dir = "./images/kimchichigae/"
    newDir = "./images/kimchichigae/new/"
    imgname = str(i) + ".jpg"
    print(imgname)
    image = cv2.imread(dir + imgname)
    small = cv2.resize(image, (0,0), fx=0.4, fy=0.4)

    cv2.imwrite(newDir+imgname,small)
    cv2.waitKey(0)


for i in range(99,120):
    try:
        resize(i)
    except:
        pass