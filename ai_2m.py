import pyttsx3
import pywhatkit
import os
import shutil
import calories_calculator 

engine = pyttsx3.init("sapi5")

def speak(text):
    if not isinstance(text, str):
        text = str(text)
    engine.say(text)
    engine.runAndWait()

def show_help():
    help_text = """
    Here are the commands you can use:
    1. play <song name> - Plays a song on YouTube.
    2. open - Opens an application or file (provide full path).
    3. make - Creates folders with files inside them.
    4. remove or delete - Deletes a specified file or folder.
    5. calori - Opens the calories calculator.
    6. read - Reads content from a specified text file.
    7. add - Appends text to a specified text file.
    8. help - Shows this help section.
    9. exit or quit - Closes the assistant.
    """
    print(help_text)
    speak("Here are the commands you can use. Check the console for details.")

def filemaker():
    ask_user_for_folder_name = input("Enter folder name: ")
    file_name = input("Enter file name (without extension): ")
    file_extension = input("Enter file extension (e.g., txt, py, html, json): ")
    file_quantity = int(input("Enter number of folders to create: "))

    for i in range(1, file_quantity + 1):
        folder_name = f"{ask_user_for_folder_name} {i}"
        os.makedirs(folder_name, exist_ok=True)  

        full_file_path = os.path.join(folder_name, f"{file_name}.{file_extension}")
        with open(full_file_path, 'w') as file:
            content = input(f"Enter content for {full_file_path} (leave blank for empty file): ")
            file.write(content)
        
        print(f"Created {full_file_path}")

    speak("File making complete!")

def fileremover():
    speak("Enter the file or folder name")
    ask_name = input("Enter the file or folder name: ")
    current_directory = os.getcwd()
    path = os.path.join(current_directory, ask_name)

    if os.path.isfile(path):
        os.remove(path)
        speak(f"File '{ask_name}' has been deleted.")
        print(f"File '{ask_name}' has been deleted.")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Folder '{ask_name}' has been deleted.") 
        speak(f"Folder '{ask_name}' has been deleted.")   
    else:
        print(f"'{ask_name}' not found in the current directory.")
        speak(f"'{ask_name}' not found in the current directory.")

def applicationopener():
    ask_user_for_application_name = input("Enter application name or file path: ")
    try:
        os.startfile(ask_user_for_application_name)
    except Exception as e:
        print("Error opening application:", e)
        speak("Unable to open the application.")

def read_file():
    file_name = input("Enter the file name to read: ")
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            text = f.read()
            print(text)
            speak("Reading the file.")
    else:
        print("File not found.")
        speak("File not found.")

def add_to_file():
    file_name = input("Enter the file name to add content to: ")
    text_type = input("Enter your text here: ")
    with open(file_name, "a") as f:
        f.write(f"{text_type}\n")
        print("Info added to the file.")
        speak("Information added to the file.")

def run_ai():
    speak("How can I assist you?")
    print("Type 'help' to see all the avaliable commands")
    while True:
        try:
            command = input("How can I assist you? : ").lower().strip()
            if not command:
                continue 
            print("Command received:", command)

            if "play" in command:
                song = command.replace("play", "").strip()
                speak("Playing" + song)
                pywhatkit.playonyt(song)

            elif "open" in command:
                applicationopener()
            
            elif "make" in command:
                filemaker()

            elif "remove" in command or "delete" in command:
                fileremover()
            
            elif "calori" in command:
                calories_calculator.calo_calc()
            
            elif "read" in command:
                read_file()

            elif "add" in command:
                add_to_file()

            elif "help" in command:
                show_help()

            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                print("Exiting...")
                break

            else:
                speak("I didn't understand that command.")
        
        except Exception as e:
            print("An error occurred:", e)
            speak("An error occurred. Please try again.")
               

run_ai()
