import os
import subprocess
def analis(text): 2 usages
    text = text.lower()
    print(text)
    if text == "запусти калькулятор":
        subprocess.call(['gnome-calculator'])
    elif text == "открой консоль" :
        subprocess.call(['gnome-terminal'])
    return "выполнено"