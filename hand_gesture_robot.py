import cv2
import mediapipe as mp
import RPi.GPIO as GPIO
import time

# GPIO Setup
GPIO.setmode(GPIO.BCM)

# Motor Pins
IN1 = 17
IN2 = 18
IN3 = 22
IN4 = 23

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

finger_tips = [8, 12, 16, 20]

def count_fingers(hand):
    fingers = []

    # Thumb
    fingers.append(
        1 if hand.landmark[4].x < hand.landmark[3].x else 0
    )

    # Other fingers
    for tip in finger_tips:
        fingers.append(
            1 if hand.landmark[tip].y < hand.landmark[tip - 2].y else 0
        )

    return fingers.count(1)

try:
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                fingers = count_fingers(hand_landmarks)

                if fingers == 1:
                    forward()
                    text = "FORWARD"
                elif fingers == 2:
                    backward()
                    text = "BACKWARD"
                elif fingers == 3:
                    left()
                    text = "LEFT"
                elif fingers == 4:
                    right()
                    text = "RIGHT"
                else:
                    stop()
                    text = "STOP"

                cv2.putText(img, text, (20, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (0, 255, 0), 2)
        else:
            stop()

        cv2.imshow("Hand Gesture Robot - Raspberry Pi", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    stop()
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
