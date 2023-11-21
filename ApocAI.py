import pyttsx3
import speech_recognition as sr
import time
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openai

# Your Python functions from before...

# Set up the engine and other necessary configurations
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
openai.api_key='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'

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

speak("I am apoc sir! Please tell me how can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def ask_jarvis(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response['choices'][0]['text']
    except Exception as e:
        print(f"Error from OpenAI: {e}")
        return "Sorry, I encountered an issue with OpenAI."

def fill_form():
    speak("Welcome! Let's fill out the form.")
    time.sleep(1)
    
    speak("Please state your name.")
    user_name = takeCommand()
    print(user_name)
    speak(f"Thank you, {user_name}.")

    speak("What is your address?")
    user_address = takeCommand()
    print(user_address)
    speak("Got it.")

    speak("Which city do you live in?")
    user_city = takeCommand()
    print(user_city)
    speak("Noted.")

    speak("Please state your state.")
    user_state = takeCommand()
    print(user_state)
    speak("Understood.")

    speak("Lastly, what is your zip code?")
    user_zip = takeCommand()
    print(user_zip)
    speak("Thank you for providing the information.")

    # Display collected information
    speak(f"Here is the information you provided: {user_name}, {user_address}, {user_city}, {user_state}, {user_zip}.")
    print(user_name)
    print(user_address)
    print(user_city)
    print(user_state)
    print(user_zip)
    speak("Thank you for giving your details. Details Successfully stored")

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('ironmanonlineminecraft@gmail.com', 'uuhuigiyfftfuhhyt')
        server.sendmail('ironmanonlineminecraft@gmail.com', to, content)
        server.close()

if __name__=="__main__" :
    wishme()
    if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'apply PAN card' in query:
            webbrowser.open("https://incometaxindia.gov.in/Pages/default.aspx")

        elif 'chat' in query:
            speak("Sure, let's chat. What would you like to talk about?")
            if 2:
                user_input = takeCommand()
                response = ask_jarvis(user_input)
                print(response)
                speak(response)
    
        elif 'play music' in query:
            music_dir = 'C:\\Users\\abina\\Skct ags\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "abinavgs27@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'form' in query:
            fill_form()
