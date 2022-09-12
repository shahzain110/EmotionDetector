import cv2
import pandas as pd
from deepface import DeepFace

dicList = []


def emotion_analyzer(filePath):
    excelSheet_name = filePath[7:-4]
    cap = cv2.VideoCapture(filePath)
    success, img = cap.read()
    frames_counter = 0
    while success:
        mainDic = {}
        cap.set(cv2.CAP_PROP_POS_MSEC, ((frames_counter * 1000) + 100))
        success, image = cap.read()
        predictions = DeepFace.analyze(img_path=img)
        mainDic['Time (s)'] = frames_counter
        mainDic['Emotion'] = predictions['dominant_emotion']
        dicList.append(mainDic)
        frames_counter += 1
        cv2.waitKey(1)

    df_to_csv(excelSheet_name, )


def df_to_csv(csv_name):
    df = pd.DataFrame.from_dict(dicList)
    root = f"output/{csv_name}.csv"
    df.to_csv(root, index=False)


#

def main():
    # .mp4 format is recommended
    # Set your file path here
    filePath = 'videos/00056_pos.mov'
    emotion_analyzer(filePath)


if __name__ == "__main__":
    main()
