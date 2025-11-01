import cv2
import datetime

cap = cv2.VideoCapture(0)

if not cap:
    print('Camera not found')
    exit()

video_type = 1
print('1 - оригинал')
print('2 - ч/б')
print('3 - размытие')
print('4 - контур')
print('q - выйти')

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_fps = float(cap.get(cv2.CAP_PROP_FPS))

if frame_fps == 0:
    frame_fps = 30.0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('test_video.mp4', fourcc, frame_fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        print('Frame not found')
        break

    text = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cv2.putText(frame, text, (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2, cv2.LINE_AA)

    if video_type == 2:
        filter_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif video_type == 3:
        filter_frame = cv2.GaussianBlur(frame, (35, 35), 0)
    elif video_type == 4:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filter_frame = cv2.Canny(gray, 50, 100)
    else:
        filter_frame = frame


    cv2.imshow('Video', filter_frame)

    out.write(frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('2'):
        video_type = 2
    elif key == ord('3'):
        video_type = 3
    elif key == ord('4'):
        video_type = 4

cap.release() #камераны тазалап коебуз
out.release()
cv2.destroyAllWindows() #Экрандарды жаап коет