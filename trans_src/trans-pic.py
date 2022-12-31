import cv2
import argparse
import os
ap = argparse.ArgumentParser()
ap.add_argument('-p', '--pic_path', type=str, help='path to input picture',
                default="../img/2.png")
ap.add_argument('-op', '--operation', type=int,
                help='operation: 1 for light sketch; 2 for Chinese painting; '
                     '3 for line drawing; 4 for western painting;'
                     ' 5 for grey sketch; 6 for colorful sketch')
ap.add_argument('-sp', '--save_path',  type=str, help='path to saved picture',
                default=os.path.join(os.getcwd(), "out.jpg"))
args = vars(ap.parse_args())
op = args['operation']
img = cv2.imread(args['pic_path'])
save_path = args['save_path']
print(save_path)
# cv2.imshow('original', img)
if op == 1:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image using Gaussian Blur
    # 高斯核服从正态分布，核数越大，越模糊
    gray_blur = cv2.GaussianBlur(gray, (75, 75), 0)
    # Convert the image into pencil sketch
    cartoon = cv2.divide(gray, gray_blur, scale=250.0)
    cv2.imwrite(save_path, cartoon)
    # cv2.imshow('cartoon.jpg', cartoon)
    cv2.waitKey()
    cv2.destroyAllWindows()
elif op == 2:
    # convert the image into grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the grayscale image with median blur中值滤波
    gray_blur = cv2.medianBlur(gray, 3)
    # Apply adaptive thresholding to detect edges检测图像边缘
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)  # 自适应均值滤波
    # Sharpen the image锐化图像
    color = cv2.detailEnhance(img, sigma_s=5, sigma_r=0.5)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite(save_path, cartoon)
    # cv2.imshow('cartoon.jpg', cartoon)
    cv2.waitKey()
    cv2.destroyAllWindows()
elif op == 3:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    edges = cv2.Laplacian(gray, -1, ksize=5)
    edges_inv = 255 - edges
    dummy, cartoon = cv2.threshold(edges_inv, 0, 255, cv2.THRESH_BINARY)
    cv2.imwrite(save_path, cartoon)
    # cv2.imshow('cartoon.jpg', cartoon)
    cv2.waitKey()
    cv2.destroyAllWindows()
elif op == 4:
    mix_pixel = int(img.shape[0]/300)
    cartoon = cv2.xphoto.oilPainting(img, mix_pixel, 1)
    cv2.imwrite(save_path, cartoon)
    # cv2.imshow('cartoon.jpg', cartoon)
    cv2.waitKey()
    cv2.destroyAllWindows()
elif op == 5 or op == 6:
    grey, color = cv2.pencilSketch(img, sigma_s=20, sigma_r=0.15, shade_factor=0.04)
    if op == 5:
        cv2.imwrite(save_path, grey)
        # cv2.imshow('grey.jpg', grey)
    else:
        cv2.imwrite(save_path, color)
        # cv2.imshow('color.jpg', color)
    cv2.waitKey()
    cv2.destroyAllWindows()