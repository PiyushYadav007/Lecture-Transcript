import speech_recognition as sr
import pyttsx3

# Reading the lecture number from the file
f = open("n.txt", "r")
n = f.readline()
print(n)
f.close()

# Converting the string to integer
val = int(n)
val = val+1
print(val)

# Writing the new lecture number to the file
f = open("n.txt", "w")
f.write(str(val))
f.close()

# Creating the lecture file name
lec = "lecture_no_"+str(val)

# Creating the lecture file
print(lec)

# Function to write the lecture
def WriteLec():
    f = open(lec+".txt", "a")
    f.write(query+"\n")
    f.close()

# Function to read and converting the lecture into string
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
        f.write(query) #calling the function to write the lecture
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

    
