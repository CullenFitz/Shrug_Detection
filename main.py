import cv2

from Utils import putTextRect
from PoseDetector import PoseDetector

def main():
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
        if bboxInfo:
            center = bboxInfo["center"]
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        left_shoulder = lmList[11][2]
        right_shoulder = lmList[12][2]
        if left_shoulder < 540 or right_shoulder < 540:
            putTextRect(img,"Shrug detected",[300,300])
        #print(left_shoulder,right_shoulder)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
