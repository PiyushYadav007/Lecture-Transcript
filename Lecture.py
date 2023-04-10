import speech_recognition as sr
import pyttsx3

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
        r.pause_threshold = 1
        audio = r.listen(source)
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

    return query


if __name__ == '__main__':
    while True:

        query = myCommand()
        query = query.lower()

        if 'hello' in query:
            print("hello sir")

        elif 'exit code' in query:
            break

    
