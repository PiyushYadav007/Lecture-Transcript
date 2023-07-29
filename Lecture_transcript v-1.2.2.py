import speech_recognition as sr
import pyttsx3
from pydub import AudioSegment

audio_files = []


f = open("n.txt", "r")
n = f.readline()
print(n)
f.close()

val = int(n)
val = val+1
print(val)

f = open("n.txt", "w")
f.write(str(val))
f.close()

lec = "lecture_no_"+str(val)

print(lec)


def WriteLec():
    f = open(lec+".txt", "a")
    f.write(query+"\n")
    f.close()


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.record(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        f = open(lec+".txt", "a")
        f.write(query)
        f.close()

    except sr.UnknownValueError:
        print('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    except KeyboardInterrupt:
        pass

    

    # Save audio to file
    filename = "audio_{0}.wav".format(len(audio_files) + 1)
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())
    audio_files.append(filename)

    # Save text to file
    text_filename = "text_{0}.txt".format(len(audio_files))
    with open(text_filename, "w") as f:
        f.write(query)
    
    return query

def Save():
    # Merge all generated audio files into a single file
    audio_segments = [AudioSegment.from_file(f) for f in audio_files]
    audio_combined = audio_segments[0]
    for segment in audio_segments[1:]:
      audio_combined += segment
    audio_combined.export(lec+".wav", format="wav")


if __name__ == '__main__':
    while True:

        query = myCommand()
        query = query.lower()

        if 'hello' in query:
            print("hello sir")

        elif 'exit code' in query:
            break

    Save()
    

    
