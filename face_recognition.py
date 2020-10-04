import cv2
import os
from skimage import io


def face_detector(url):
    # 读取图片,注意这里是RGB
    image = io.imread(url)
    # 转成BGR
    img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    global face_cascade, eye_cascade, nose_cascade, mouth_cascade
    # 获取cv2安装路径
    path_dirname = os.path.dirname(cv2.__file__)
    # 获取安装路径下的所有文件夹
    path_dirs = os.listdir(path_dirname)
    # 获取识别模型文件夹
    path_models = os.path.join(path_dirname, 'data')
    # 获取所有的模型
    modes_list = os.listdir(path_models)
    for model in modes_list:
        if model == 'haarcascade_frontalface_alt.xml':
            path_face_model = os.path.join(path_models, model)
            # 脸分类器
            face_cascade = cv2.CascadeClassifier()
            # 加载模型数据
            face_cascade.load(path_face_model)
            continue
        if model == 'haarcascade_eye_tree_eyeglasses.xml':
            path_eye_model = os.path.join(path_models, model)
            # 眼睛分类器
            eye_cascade = cv2.CascadeClassifier()
            # 加载眼睛模型数据
            eye_cascade.load(path_eye_model)
            continue
        if model == 'haarcascade_mcs_nose.xml':
            path_nose_model = os.path.join(path_models, model)
            # 鼻子分类器
            nose_cascade = cv2.CascadeClassifier()
            nose_cascade.load(path_nose_model)
            continue
        if model == 'haarcascade_mcs_mouth.xml':
            path_mouth_model = os.path.join(path_models, model)
            # 嘴巴分类器
            mouth_cascade = cv2.CascadeClassifier()
            mouth_cascade.load(path_mouth_model)
            continue
    # 脸
    faces = face_cascade.detectMultiScale(gray, 1.2, 3,minSize = (30, 30))
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        # 眼睛
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        # 鼻子
        nose = nose_cascade.detectMultiScale(roi_gray, 1.2, 5)
        for (nx, ny, nw, nh) in nose:
            cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (0, 0, 255), 2)
        # 嘴巴
        mouth = mouth_cascade.detectMultiScale(roi_gray, 1.5, 2)
        for (mx, my, mw, mh) in mouth:
            cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (255, 0, 0), 2)

    # cv2.imwrite('switched_img1.jpg',img)
    result='faces:{},eyes:{},nose:{},mouth:{}'.format(faces,eyes,nose,mouth)
    # print(result)
    # cv2.imshow('img', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return result



# if __name__ == "__main__":
#     url='http://json119.com/images/img/2020/10/03/23b1cbda-d58f-4fe1-ba23-3673d94ea1bb.jpg'
#     res=face_detector(url)
