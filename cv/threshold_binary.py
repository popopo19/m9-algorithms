import cv2 as cv
import numpy as np
import time

# Colors
BLUE = (255, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)

# Conditions
NONE = -1
ENCLOSING_LETTERS = 5
LETTERS = 10
MIN_RECT_AREA = 40

threshold = 240

def count_children(child, hierarchy):
    if child[0] == -1:
        return 0
    else:
        return count_children(hierarchy[child[0]], hierarchy) + 1


def find_text(image):
    global threshold

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    (thresh, threshold_image) = cv.threshold(gray_image, threshold, 255, cv.THRESH_BINARY)

    # threshold_image = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 2)

    contours, hierarchy = cv.findContours(threshold_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return image

    hierarchy = hierarchy[0]

    text_location_index = 0

    for i in range(len(contours)):

        relations = hierarchy[i]
        child_index = relations[2]
        parent = relations[3]
        has_child = child_index != NONE
        has_parent = parent != NONE

        is_rect = False
        x, y, w, h = cv.boundingRect(contours[i])
        correct_scale = w > h and w > h * 3
        big_area = cv.contourArea(contours[i]) > MIN_RECT_AREA

        if correct_scale and has_child and not has_parent and big_area:
            is_rect = True

        if is_rect:
            child = hierarchy[child_index]
            child_count = count_children(child, hierarchy)

            if child_count > 0:

                cv.rectangle(image, (x, y), (x + w, y + h), RED, 2)
                print("Child Count: " + str(child_count))
                # cv.drawContours(image, contours, child_index, RED, 3, cv.LINE_8)
            else:
                return image

    return image


def trackbar_cb(value):
    global threshold
    threshold = value


def video():

    cap = cv.VideoCapture('./test_images/testing_vid.mp4')
    cv.namedWindow("Inspector")
    cv.createTrackbar('Threshold', 'Inspector', 243, 255, lambda v: trackbar_cb(v))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        image = find_text(frame)

        cv.imshow('frame', image)

        if cv.waitKey(3) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

def images():
    image1 = cv.imread("./test_images/test1.PNG")
    image2 = cv.imread("./test_images/test2.PNG")

    cv.namedWindow("Inspector")
    cv.createTrackbar('Threshold', 'Inspector', 255, 255, lambda v: trackbar_cb(v))

    while True:

        image = find_text(image1)

        cv.imshow("New Image", image)

        if cv.waitKey() & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

video()