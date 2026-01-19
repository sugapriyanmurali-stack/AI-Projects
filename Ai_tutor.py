import random
import time

face_emotions = ["Happy", "Confused", "Bored", "Neutral"]
voice_emotions = ["neutral", "sad", "excited"]

def detect_face_emotion():
    return random.choice(face_emotions)

def detect_voice_emotion():
    return random.choice(voice_emotions)

def ai_tutor(question, emotion):
    if emotion == "Confused":
        return "Let's go slowly . Machine learning means teaching computers using examples."
    elif emotion == "Bored":
        return "Let me explain in a simple real-life way..."
    else:
        return "Here is a clear explanation of your topic."

print("=== AI Emotion-Aware Study Coach ===")

while True:
    face = detect_face_emotion()
    voice = detect_voice_emotion()

    print("\nDetected Face Emotion:", face)
    print("Detected Voice Emotion:", voice)

    if face == "Bored":
        print("AI Coach: You look tired ... Take a 2 minute break.")
    elif face == "Confused":
        q = input("AI Coach: What topic is confusing you? ")
        print("AI Tutor:", ai_tutor(q, face))
    else:
        print("AI Coach: Keep going! You're doing well ")

    time.sleep(2)

    if input("\nExit? (y/n): ") == "y":
        break
