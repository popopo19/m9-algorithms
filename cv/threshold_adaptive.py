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
LETTERS = 13
MIN_CHILDREN = 1
MIN_RECT_AREA = 10
CENTER_BOX_SIZE = 200

test_image = cv.imread("./test_images/test1.PNG")
block_size = 9
constant = 1

# 0 - image
# 1 - video

test_type = 1


def count_children(child, hierarchy):
    if child[0] == -1:
        return 0
    else:
        return count_children(hierarchy[child[0]], hierarchy) + 1


def find_blue_squ(img):

    image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    img_height, img_width, channels = img.shape

    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    hsv_image[..., 2] = hsv_image[..., 2] * 0.5

    lower_bound = (90, 40, 100)
    upper_bound = (150, 255, 255)

    mask = cv.inRange(hsv_image, lower_bound, upper_bound)

    threshold_image = cv.adaptiveThreshold(mask, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size, constant)
    contours, hierarchy = cv.findContours(threshold_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return image

    hierarchy = hierarchy[0]

    for i in range(len(contours)):
        relations = hierarchy[i]
        child_index = relations[2]
        parent = relations[3]
        has_child = child_index != NONE
        has_parent = parent != NONE

        x, y, w, h = cv.boundingRect(contours[i])

        big_area = cv.contourArea(contours[i]) > 1000
        x_in_box = img_width // 2 + CENTER_BOX_SIZE > x > img_width // 2 - CENTER_BOX_SIZE
        c = 130
        y_in_box = img_height // 2 + CENTER_BOX_SIZE - c > y > img_height // 2 - CENTER_BOX_SIZE + c
        in_box = x_in_box and y_in_box

        a = 100
        correct_scale = w + a > h > w - a and h + a > w > h - a

        if big_area and has_child and in_box:
            cv.rectangle(image, (x, y), (x + w, y + h), RED, 2)

    return image


def find_text(img):
    image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    img_height, img_width, channels = img.shape

    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

    lower_bound = (0, 0, 200)
    upper_bound = (180, 5, 255)

    mask = cv.inRange(hsv_image, lower_bound, upper_bound)

    threshold_image = cv.adaptiveThreshold(mask, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size, constant)

    contours, hierarchy = cv.findContours(threshold_image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cv.rectangle(image, (img_width // 2 + CENTER_BOX_SIZE*2, img_height // 2 + CENTER_BOX_SIZE), (img_width // 2 - CENTER_BOX_SIZE*2, img_height // 2 - CENTER_BOX_SIZE), BLUE, 2)

    if len(contours) == 0:
        return image

    hierarchy = hierarchy[0]

    for i in range(len(contours)):

        relations = hierarchy[i]
        child_index = relations[2]
        parent = relations[3]
        has_child = child_index != NONE
        has_parent = parent != NONE

        is_rect = False
        x, y, w, h = cv.boundingRect(contours[i])
        correct_scale = w > h and h * 4 > w > h * 3
        big_area = cv.contourArea(contours[i]) > MIN_RECT_AREA
        x_in_box = img_width // 2 + CENTER_BOX_SIZE > x > img_width // 2 - CENTER_BOX_SIZE
        y_in_box = img_height // 2 + CENTER_BOX_SIZE > y > img_height // 2 - CENTER_BOX_SIZE
        in_box = x_in_box and y_in_box

        if correct_scale and has_child and big_area and in_box:
            is_rect = True

        if is_rect:
            child = hierarchy[child_index]
            child_count = count_children(child, hierarchy)

            if LETTERS > child_count >= MIN_CHILDREN:

                print("Child Count: " + str(child_count))
                # cv.drawContours(image, contours, child_index, RED, 3, cv.LINE_8)
                cv.rectangle(image, (x, y), (x + w, y + h), RED, 2)
            else:
                return image

    return image


def image_cb(v):
    global test_image

    if v == 0:
        test_image = cv.imread("./test_images/test1.PNG")
    elif v == 1:
        test_image = cv.imread("./test_images/test2.PNG")


def block_size_cb(v):
    global block_size

    if v % 2 != 0 and v > 0:
        block_size = v


def constant_cb(v):
    global constant

    if v > 0:
        constant = v


def video():

    cap = cv.VideoCapture('./test_images/testing_vid.mp4')

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        image = find_blue_squ(frame)

        cv.imshow('frame', image)

        if cv.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


def images():

    cv.namedWindow("Inspector")
    cv.createTrackbar('Image', 'Inspector', 0, 1, lambda v: image_cb(v))
    cv.createTrackbar('Block Size', 'Inspector', 19, 30, lambda v: block_size_cb(v))
    cv.createTrackbar('Constant', 'Inspector', 12, 30, lambda v: constant_cb(v))

    while True:
        image = find_blue_squ(test_image)

        cv.imshow("New Image", image)

        if cv.waitKey(3) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

def main():
    if test_type == 0:
        images()
    elif test_type == 1:
        video()

main()