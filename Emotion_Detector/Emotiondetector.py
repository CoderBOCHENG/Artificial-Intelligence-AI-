from fer import FER
import matplotlib.pyplot as plt
emo_detector = FER(mtcnn=True)


test_image_one = plt.imread("Image-One.jpeg")

captured_emotions = emo_detector.detect_emotions(test_image_one)
print(captured_emotions)

plt.imshow(test_image_one)

dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
print(dominant_emotion, emotion_score)


test_image_two = plt.imread("Image-Two.jpg")
captured_emotions_two = emo_detector.detect_emotions(test_image_two)
print(captured_emotions_two)
plt.imshow(test_image_two)
dominant_emotion_two, emotion_score_two = emo_detector.top_emotion(test_image_two)
print(dominant_emotion_two, emotion_score_two)

test_image_three = plt.imread("Image-Three.jpg")
captured_emotions_three = emo_detector.detect_emotions(test_image_three)
print(captured_emotions_three)
plt.imshow(test_image_three)
dominant_emotion_three, emotion_score_three = emo_detector.top_emotion(test_image_three)
print(dominant_emotion_three, emotion_score_three)

test_image_four = plt.imread("Image-Four.jpg")
captured_emotions_four = emo_detector.detect_emotions(test_image_four)
print(captured_emotions_four)
plt.imshow(test_image_four)
dominant_emotion_four, emotion_score_four = emo_detector.top_emotion(test_image_four)
print(dominant_emotion_four, emotion_score_four)

test_image_five = plt.imread("Image-Five.png")
captured_emotions = emo_detector.detect_emotions(test_image_five)
print(captured_emotions)
plt.imshow(test_image_five)
dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_five)
print(dominant_emotion, emotion_score)
