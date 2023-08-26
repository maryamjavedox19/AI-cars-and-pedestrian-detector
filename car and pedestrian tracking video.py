import cv2

video_file='Cars and Pedestrians_Trim.mp4'

video=cv2.VideoCapture(video_file)

classifier_file='cars.xml'

car_tracker=cv2.CascadeClassifier(classifier_file)


while True:
    success, frame=video.read()

    if not success:
        break

    # grayscale video
    grayscaled_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars_coordinates=car_tracker.detectMultiScale(grayscaled_frame)

    for (x,y,w,h) in cars_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    cv2.imshow('showing video', frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break


video.release()






