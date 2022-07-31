import mediapipe as mp
import cv2
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
cam = cv2.VideoCapture("Video 2.mp4")#Capture Video
output=cv2.VideoWriter("Output2.mp4",cv2.VideoWriter_fourcc(*'mp4v'),30,(1280,720))
while(cam.isOpened()):
    _,frame = cam.read()

    if _ == True:
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        # print(results.pose_landmarks)
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        frame = cv2.resize(frame,(1280,720))
        cv2.imshow("video",frame)
        output.write(frame)
        key=cv2.waitKey(1)&0xFF
        if key==ord('q'):
            break
    else:
        break
cam.release()
output.release()
cv2.destroyAllWindows()