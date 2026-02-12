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

# メッセージ鍵ありバージョン
# from language import language
# secret_text = input("解読したいテキストをひらがなで入力してください。")
# plain_text = ""
# language_size = len(language)

# # 鍵である一文字目を取り出す
# message_key = secret_text[0]
# key = language.index(message_key)

# #鍵である一文字目以外を一文字づつずらして復号していく
# for char in secret_text[1:]:
#     if char in language:
#         index = language.index(char)
#         plain_text += language[(index-key)%language_size]
#     else:
#         plain_text += char
    
# print("解読すると、「",plain_text,"」と書いていました。")
