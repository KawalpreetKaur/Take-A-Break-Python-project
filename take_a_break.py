import time
import webbrowser
breaks=3
print("program started on" +time.ctime())
for i in range(breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=D9KfGLP30BE")
