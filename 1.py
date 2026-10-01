import time
import webbrowser
from urllib.parse import quote_plus

password = (input('Enter the Name: '))
time.sleep(1)
print("good morning " + password + ", how may i help you?")
answer = str(input())
time.sleep(1)
print("let me check if i can help you with that")
time.sleep(1)
print("please wait for a moment")
time.sleep(1)
print("I have checked and I can help you with that")
time.sleep(3)
search_url = f"https://www.google.com/search?q={quote_plus(answer)}"
webbrowser.open(search_url)