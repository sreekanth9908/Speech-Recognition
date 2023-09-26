import speech_recognition as sr

def main():
    r = sr.Recognizer()  # Note the correct spelling: Recognizer with a capital R

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now.... ")

        # Recognize using Google
        try:
            recognized_text = r.recognize_google(audio)
            print("You Have Said:\n", recognized_text)
            print("Audio Recorded successfully\n")

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        # Write audio to a file
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

if __name__ == "__main__":
    main()
