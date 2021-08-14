import cv2

'''
  读取图片

# 图片的地址
img_path = r'D:\yuyanbiancheng\PyCharm\QQpicture20200430203406.jpg'

# 读取图片
img = cv2.imread(img_path)

# 显示图片，Output是窗体名
cv2.imshow("Output", img)

# 窗体关闭等待时长 0：一直等待
cv2.waitKey(0)
'''
'''
  读取视频

# 视频地址
video_path = r'D:\yuyanbiancheng\PyCharm\Grand Theft Auto V 2021.04.23 - 22.44.39.01_Trim.mp4'
cap = cv2.VideoCapture(video_path)

# 一帧一帧的读取，
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''
'''
  读取摄像头
'''
cam = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
cam.set(10, 100)

# 一帧一帧的读取，
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


