from language import language
key = 3
secret_text = input("解読したいテキストをひらがなで入力してください。")
plain_text = ""
language_size = len(language)
for char in secret_text:
    if char in language:
        index = language.index(char)
        plain_text += language[(index-key)%language_size]
    else:
        plain_text += char
    
print("解読すると、「",plain_text,"」と書いていました。")
