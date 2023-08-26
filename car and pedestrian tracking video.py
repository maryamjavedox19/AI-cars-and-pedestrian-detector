import cv2
video_file='Cars and Pedestrians_Trim.mp4'

video=cv2.VideoCapture(video_file)


while True:
    success, frame=video.read()

    if not success:
        break

    cv2.imshow('showing video', frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break


video.release()






