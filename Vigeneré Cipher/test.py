plaintext = "JAVAHUNGRYBLOG"
keyword = "LEMON"

msg = [char for char in plaintext]
msgLen = len(msg)
i = msgLen
j = 0

key = [msgLen]
encryptedMsg = [msgLen]
decryptedMsg = [msgLen]

for i, j in msgLen:
    if j == len(keyword):
        j = 0
    key[i] = keyword[j]


for i in msgLen:
    encryptedMsg[i] = chr( % 26) + ord('A')))