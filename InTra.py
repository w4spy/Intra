import subprocess
import shlex
import keyboard
from googletrans import Translator

###sudo apt-get --reinstall install libnotify-bin notify-osd
#start the script 
#highlite the word u wanna translate
#press Ctrl key
#u will get popup notification with the translation
#refer to https://github.com/w4spy/Intra for updates

print('''
           _
       .--' |
      /___^ |     .--.
          ) |    /    \\
         /  |  /`      '.
        |   '-'    /     \\
        \\         |      |\\
         \\    /   \\      /\\|
          \\  /'----`\\   /
          |||       \\ |
          ((|        ((|
          |||        |||
         //_(       //_( Instance Translator v1.0 by waspy
''')
try:
    subprocess.Popen(['/usr/lib/notification-daemon/notification-daemon']) #start notification daemon
    print("[+] notification-daemon started ")
except Exception:
    pass
  
print("-----history will be logged here-----")

while True:
    keyboard.wait("Ctrl")
    selected_text = subprocess.check_output((shlex.split('xclip -out -selection')))
    selected_text = selected_text.decode("utf-8") 

    translator = Translator()
    translations = translator.translate(selected_text, dest='ar')
    print(translations.text)
    subprocess.call(['notify-send', translations.text])