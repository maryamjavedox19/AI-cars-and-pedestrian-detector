import cv2
img_file='car.jpg'

# pretained car classifier
classifier_file='cars.xml'

# creating open cv img
img=cv2.imread(img_file)

# create car classifier
car_tracker=cv2.CascadeClassifier(classifier_file)

# coverting to grey scaled
black_n_white=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect cars
cars_coordinates=car_tracker.detectMultiScale(black_n_white)

# for 1 car (first)
# car1=cars_coordinates[0]

# looping through cars
for (x,y,w,h) in cars_coordinates:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)


cv2.imshow('car detector', img)
cv2.waitKey()
# waits till you press a key before it disappears

print(cars_coordinates)

print("completed")