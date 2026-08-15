import cv2 
import mediapipe as mp
from Finger_counter import FingerCounter
from gesture_detector import GestureDetector

print("\n===== HAND TRACKING PROJECT =====")
print("1 - Finger Counter")
print("2 - Gesture Recognition")

choice = input("\nSelect mode: ")

if choice == "1":
    mode = "count"

elif choice == "2":
    mode = "gesture"

else:
    print("Invalid option")
    exit()


# camera input 
cap= cv2.VideoCapture(0)

# MediaPipe Hand Landmarker
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=2
)

# Create hand detector
detector = HandLandmarker.create_from_options(options)

# Window
window_name= "camera"
cv2.namedWindow(window_name)

frame_timestamp = 0

counter=FingerCounter()
gesture_detector = GestureDetector()


while True:
    success, frame=cap.read()

    if not success:
        print("Could not access camera ")
        break

    # OpenCV to RGB
    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

  # Convert to MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )
       # Detect hands
    result = detector.detect_for_video(
        mp_image,
        frame_timestamp
    )
    

    
    frame_timestamp += 1

   
    if result.hand_landmarks:

       for i, hand in enumerate(result.hand_landmarks):

 
      
            # Get Left / Right
            handedness = result.handedness[i][0].category_name


            # Count fingers
            finger_states = counter.get_finger_states(
                hand,
                handedness
)

            finger_count = sum(finger_states)

            gesture = gesture_detector.detect_gesture(
                finger_states
)

 # Draw landmarks
            for landmark in hand:

                # Convert normalized coordinates
                x = int(landmark.x * frame.shape[1])
                y = int(landmark.y * frame.shape[0])
                cv2.circle(
                    frame,
                    (x, y),
                    3,
                    (0, 255, 0),
                    -1
                )


            # Display finger count
            if mode == "count":

                cv2.putText(
                    frame,
                    f"{handedness} Hand: {finger_count}",
                    (50, 100 + i * 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,
                    (0, 255, 0),
                    3
    )

            elif mode == "gesture":

                cv2.putText(
                    frame,
                    gesture,
                    (50, 100 + i * 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,
                    (255, 0, 255),
                    3)
                
       



    #the borders 
    cv2.imshow(window_name, frame)
    cv2.putText(
    frame,
    f"MODE: {mode.upper()}",
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

    # closing using the "q"
    if cv2.waitKey(1)& 0xFF == ord("q"):
        break;

    
    #close it using the x button 
    if cv2.getWindowProperty(window_name,cv2.WND_PROP_VISIBLE)<1:
      break  


cap.release()
detector.close()
cv2.destroyAllWindows()
