from language import language
key = 3
plain_text = input("暗号化したいテキストをひらがなで入力してください。")
secret_text = ""
language_size = len(language)
for char in plain_text:
    if char in language:
        index = language.index(char)
        secret_text += language[(index+key)%language_size]
    else:
        secret_text += char

print("暗号化されたテキストは「",secret_text,"」となりました。")

# もし、あまりの考え方が難しそうなら以下のような方法をとってください。
# for char in plain_text:
#     if char in language:
#         index = language.index(char)
#         if index != language_size:
#             secret_text += language[(index+1)%language_size]
#         else:
#             secret_text += language[0]
#     else:
#         secret_text += char