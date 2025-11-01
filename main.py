import cv2
import datetime

cap = cv2.VideoCapture(0)

if not cap:
    print('Камера не работает')
    exit()

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
        print('Кадр жок')
        break

    time_text = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    cv2.putText(frame, time_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Image', frame)

    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
