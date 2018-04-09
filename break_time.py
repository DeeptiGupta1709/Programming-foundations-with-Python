import webbrowser
import time

for i in range (0, 3):
    time.sleep(10)
    print("This program started at"+time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=zYoum2gQip8")
