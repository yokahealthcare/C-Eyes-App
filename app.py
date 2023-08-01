import streamlit as st
import cv2

video = cv2.VideoCapture("video16fps.mp4")
# frame_placeholder = st.empty()
stop_button_pressed = False

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



# Get video properties (width, height, frames per second, etc.)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))
print(f"Current Video FPS: {fps}")


# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("processed_video.avi", fourcc, fps, (frame_width, frame_height))


number_of_frame = 0
while video.isOpened() and not stop_button_pressed:
    ret, frame = video.read()

    if not ret:
        st.write("The video has ended!")
        break

    faces = cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 3)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    out.write(frame)
    # frame_placeholder.image(frame, channels="BGR")
    number_of_frame += 1
    if number_of_frame % 100 == 0:
        print(f"Frame : {number_of_frame}")

    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
        break



video.release()
cv2.destroyAllWindows()
