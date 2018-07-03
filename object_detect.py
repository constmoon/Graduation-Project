import cv2

# multi-thread를 이용해 최적화, speed-up
cv2.setUseOptimized(True);
cv2.setNumThreads(4);

# read image
im = cv2.imread("images/lunch.jpg")

# resize image
newHeight = 200
newWidth = int(im.shape[1] * 200 / im.shape[0])
im = cv2.resize(im, (newWidth, newHeight))

# create Selective Search Segmentation Object using default parameters
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

# set input image on which we will run segmentation
ss.setBaseImage(im)

ss.switchToSelectiveSearchFast()    # 빠른 속도 보장
#ss.switchToSelectiveSearchQuality()


# run selective search segmentation on input image
rects = ss.process()
print('Total Number of Region Proposals: {}'.format(len(rects)))

# number of region proposals to show
numShowRects = 100
# increment to increase/decrease total number
# of reason proposals to be shown
increment = 50

cv2.imshow("Output", im)
while True:
    # create a copy of original image
    imOut = im.copy()

    # itereate over all the region proposals
    for i, rect in enumerate(rects):
        # draw rectangle for region proposal till numShowRects
        if (i < numShowRects):
            x, y, w, h = rect
            cv2.rectangle(imOut, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)
        else:
            break

    # show output
    cv2.imshow("Output", imOut)

    # record key press
    k = cv2.waitKey(0)

# close image show window
cv2.destroyAllWindows()