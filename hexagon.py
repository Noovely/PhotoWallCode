import cv2
import numpy


def hexagonImg(img):
    #GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows, cols, channels = img.shape
    size = min(rows, cols)
    mask = numpy.zeros((rows, cols))
    # 六边形六个端点坐标（逆时针）
    """A = [int(size * 5.9 / 23.6), int(size * 1.3 / 23.6)]
    B = [int(size * 0 / 23.6), int(size * 11.8 / 23.6)]
    C = [int(size * 5.9 / 23.6), int(size * 22.3 / 23.6)]
    D = [int(size * 17.7 / 23.6), int(size * 22.3 / 23.6)]
    E = [int(size * 23.6 / 23.6), int(size * 11.8 / 23.6)]
    F = [int(size * 17.7 / 23.6), int(size * 1.3 / 23.6)]"""
    A = [int(cols/2-size*5.9/23.6), int(rows/2-size*10.5/23.6)]
    B = [int(cols/2-size*11.8/23.6), int(rows/2)]
    C = [int(cols/2-size*5.9/23.6), int(rows/2+size*10.5/23.6)]
    D = [int(cols/2+size*5.9/23.6), int(rows/2+size*10.5/23.6)]
    E = [int(cols/2+size*11.8/23.6), int(rows/2)]
    F = [int(cols/2+size*5.9/23.6), int(rows/2-size*10.5/23.6)]

    # 创建蒙版
    triangle1 = numpy.array([A, B, C, D, E, F], numpy.int32)
    cv2.fillPoly(mask, [triangle1, ], 1)
    mask = numpy.uint8(mask)
    ret, mask = cv2.threshold(mask, 0.5, 1, cv2.THRESH_BINARY)

    img = cv2.bitwise_and(img, img, mask=mask)
    return img


if __name__ == "__main__":
    img = cv2.imread("image/size.png")
    proImg = hexagonImg(img)
    cv2.imshow("HEXAGON", proImg)
    cv2.imwrite("image/h_lena.jpg", proImg)
    cv2.waitKey(0)
