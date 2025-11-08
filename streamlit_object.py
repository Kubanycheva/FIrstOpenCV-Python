import streamlit as st
import cv2
import datetime

st.title("Добро пожаловать🎥")

video_type = st.radio(
    "Choose filter",
    [1, 2, 3, 4],
    format_func=lambda x: {1:"Оригинал",2:"ч/б",3:"Размытие",4:"Контур"}[x]
)

run = st.checkbox("Start camera")
frame_placeholder = st.empty()

cap = None
out = None

if run:
    cap = cv2.VideoCapture(0)

    # get frame size and fps
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_fps = float(cap.get(cv2.CAP_PROP_FPS))
    if frame_fps == 0:
        frame_fps = 30.0

    # video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('test_video.mp4', fourcc, frame_fps, (frame_width, frame_height))

while run:
    ret, frame = cap.read()
    if not ret:
        st.write("No camera frame 😕")
        break

    text = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cv2.putText(frame, text, (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,255), 2)

    if video_type == 2:
        frame_filtered = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif video_type == 3:
        frame_filtered = cv2.GaussianBlur(frame, (35, 35), 0)
    elif video_type == 4:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 100)
        frame_filtered = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # fix here ✅
    else:
        frame_filtered = frame

    # If grayscale, convert for display
    if len(frame_filtered.shape) == 2:  # means single channel
        frame_show = cv2.cvtColor(frame_filtered, cv2.COLOR_GRAY2BGR)
    else:
        frame_show = frame_filtered

    frame_placeholder.image(frame_show, channels="BGR")