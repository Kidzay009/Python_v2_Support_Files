import os

print("Your current directory is:", os.getcwd())

for text_file in os.listdir():
    if text_file.endswith('.txt'):
        print(text_file)

os.rename('313-message.txt','OLD313-message.txt')

