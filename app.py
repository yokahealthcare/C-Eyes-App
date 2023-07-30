import streamlit as st
import cv2

video = cv2.VideoCapture("video.mp4")
frame_placeholder = st.empty()
stop_button_pressed = st.button("Stop")

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while video.isOpened() and not stop_button_pressed:
    ret, frame = video.read()

    if not ret:
        st.write("The video has ended!")
        break

    faces = cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 3)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    frame_placeholder.image(frame, channels="BGR")

    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
        break

video.release()
cv2.destroyAllWindows()
