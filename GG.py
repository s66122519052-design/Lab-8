import cv2
import numpy as np
import time
import itertools

WINDOW_NAME = "Driver Monitoring (Dummy Zero2W)"


states = ["SafeDriving", "Distracted", "Drowsy", "Smartphone"]
colors = {
    "SafeDriving": (0, 255, 0),
    "Distracted": (0, 255, 255),
    "Drowsy": (0, 128, 255),
    "Smartphone": (0, 0, 255),
}

def main():

    frame_h, frame_w = 320, 480


    for state in itertools.cycle(states):

        frame = np.zeros((frame_h, frame_w, 3), dtype=np.uint8)


        color = colors.get(state, (255, 255, 255))
        cv2.putText(frame, f"STATE: {state}",
                    (30, frame_h // 2), cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, color, 2, cv2.LINE_AA)


        cv2.putText(frame, "FPS: 10.0", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)


        cv2.imshow(WINDOW_NAME, frame)


        key = cv2.waitKey(1000) & 0xFF
        if key in (27, ord('q')):  
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
