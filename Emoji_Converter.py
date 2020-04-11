def emoji_function(message):
    words = message.split(" ")
    emojis = {
        ':)': '😊',
        ':(': '😢'
    }
    out_put = ''
    for word in words:
        out_put += emojis.get(word, word) + " "
    return out_put


message = input("> ")
out = emoji_function(message)
print(out)

