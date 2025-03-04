#---------------------- PYTHON LIBRARY -----------------------

import pyttsx3 #Python library used for text-to-speech (TTS) conversion
import datetime #functions to work with dates and times, allowing you to manipulate, format, and perform arithmetic on date and time values easily.
import speech_recognition as sr #Python is a library used for recognizing and processing speech from audio files or a microphone.
import wikipedia 
import webbrowser # this is inbuilt function for webbrowser or opening the web browser
import os #os module interacts with operating system functions.
import random # Import the random module for song selection to play 


#---------------------- INITIALIZATION OF ENGINE -----------------------

engine = pyttsx3.init('sapi5') # window's API for text-to-speech
voices = engine.getProperty('voices') # Get the available voices
# print(voices[1])
engine.setProperty('voice',voices[1].id) # Select a specific voice


#---------------------- SPEAK FUNCTION -----------------------

def speak(audio):
    engine.say(audio) #the text for speech [output as speech]
    engine.runAndWait() #actually process the speech and make the program wait until the speech is completed.
    


#---------------------- SPEECH RECOGNITION FUNCTION -----------------------

def takecommand(): # it takes microphone input[which we will speak to prompt] from the user and the string output
    r = sr.Recognizer() #which initializes the speech recognizer that processes the audio input.
    with sr.Microphone() as source: #This opens the microphone for audio input
       print("Listening. . . . .")
       r.pause_threshold = 1 # Set pause threshold for recognizing speech
       audio = r.listen(source) # Capture audio input
    
    try:
        print("Recognizing. . . .")
        query = r.recognize_google(audio, language='en-in') # Recognize speech [ Google's Web Speech API ]
        print(f"User said : {query}\n") # Output recognized text
    except Exception as e:
        print("Say that again please. . . ")
        return "None" # Return "None" if recognition fails
    return query # Return recognized text




#---------------------- GREETING FUNCTION -----------------------

def greet():
    hour = int(datetime.datetime.now().hour) #gets the current hour (in 24-hour format) by calling datetime.datetime.now() in hours
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Queen. please tell me how may I help you")
    speak("For searching in youtube , say search in youtube")
    speak("For searching in google , say search in google")
    # speak("shivani how are you")





#---------------------- MAIN FUNCTION -----------------------

if __name__ == "__main__":
     greet()
     while True: #Starts an infinite loop to continuously listen for commands.
        query = takecommand().lower() #Captures user input and converts it to lowercase.
        # Logic for executing tasks based on query
        

        if 'wikipedia' in query:  #Checks if the query includes "wikipedia." [import the wikipedia]
            speak('Searching Wikipedia....')
            # print("Searching Wikipedia....")
            query = query.replace("wikipedia","") #Removes "wikipedia" from the query for clarity.
            results = wikipedia.summary(query, sentences=2) #Retrieves a two-sentence summary from Wikipedia based on the topic.
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'search in google' in query:
            query = query.replace("search in google","")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        

        elif 'search in youtube' in query:
            query = query.replace("search in youtube","")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'anime' in query:
            webbrowser.open("https://kaido.to/")

        elif 'movie' in query:
            webbrowser.open("https://iosmirror.cc/")
        
        elif 'play music' in query:
            music_dir = r'D:\Music1'  # Use raw string for the directory
            songs = os.listdir(music_dir)  # List all files in the directory
            print(songs)  # Print the audio files
            selected_song = random.choice(songs) #for the random selection
            os.startfile(os.path.join(music_dir, selected_song))  # Play the first audio file
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        
        elif 'code' in query:
            co = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(co)
        
        
        
        