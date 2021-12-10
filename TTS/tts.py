from gtts import gTTS
import os
from pathlib import Path
import glob
import ntpath
import playsound
import time

PATH = Path(__file__).parent
INPUT = PATH.joinpath("Input")
OUTPUT = PATH.joinpath("Output")

class main:
    def __init__(self) -> None:
        while True:
            os.system("cls")
            print("For list of commands type help")
            command = input("Command: ").lower()

            if command == "close":
                os.system("cls")
                exit()
            
            if command == "tts":
                self.tts()

            if command == "play":
                self.speak()

            if command == "play all":
                self.speak_all()
            
            if command == "del" or command == "delete":
                self.delete()
                
            if command == "del all" or command =="delete all":
                self.delete_all()
            
            if command == "?" or command == "help" or command == "/?":
                self.help()

    def speak_all(self):
        files = glob.glob(str(OUTPUT)+"/*.mp3")
        if files == []:
            print("no files")
        else:
            for fil in files:
                name_ext = ntpath.basename(fil)
                print(f"playing: {name_ext}")
                playsound.playsound(f"Output/{name_ext}")
                os.system("pause")
    
    def speak(self):
        name = input("Name of file(without extension): ") + ".mp3"
        name_ext = f"Output/{name}"
        print(f"playing: {name}")
        playsound.playsound(name_ext)

    def tts(self):
        files = glob.glob(str(INPUT)+"/*.txt")
        if files == []:
            print("no files")
        else:
            items = files
            l = len(items)

            # Initial call to print 0% progress
            self.printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            for i, item in enumerate(items):
                # Do stuff...
                with open(item, 'r', encoding="utf8") as f:
                    text = f.read()
                name_ext = ntpath.basename(item)
                name = name_ext.replace(".txt", '.mp3')

                tts = gTTS(text= text, lang ="en")

                tts.save(f"{OUTPUT}/{name}")

                time.sleep(0.1)
                # Update Progress Bar
                self.printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
        
            choise = input("Delete .txt's [Y/N]: ").lower()

            if choise == 'y':
                for fil in files:
                    os.remove(fil)
        os.system("pause")

    def delete(self):
        name = input("Name of file(without extension): ") + ".mp3"
        name_ext = f"{OUTPUT}/{name}"   
        try:
            os.remove(name_ext)
        except Exception as e:
            print(e)
        else:
            print(f"Deleted {name}")
        
        os.system("pause")
    
    def delete_all(self):
        choise = input("Are you sure you want to delete everything\n[Y/N]: ").lower()

        if choise == 'y':
            files = glob.glob(str(OUTPUT)+"/*.mp3")

            if files == []:
                print("no files")
            else:
                for fil in files:
                    os.remove(fil)
                    name = ntpath.basename(fil)
                    print(f"{fil} has been deleted")
        
        os.system("pause")
    
    def printProgressBar (self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()
    
    def help(self):
        print("tts:\t\tTakes the .txt files in Input and converts to .mp3 in output\n\t\tNote: Input has to be .txt")
        print("play:\t\tPlays the .mp3 files")
        print("play all:\tPlays all .mp3 files")
        print("del:\t\tDeletes .mp3")
        print("del all:\tDeletes all .mp3")

        os.system("pause")

if __name__ == "__main__":
    main()