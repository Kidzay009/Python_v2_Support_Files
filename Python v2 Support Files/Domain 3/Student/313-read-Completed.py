message = open('313-message.txt','w')
message.write('Testing file for player configuration\n')
message.write('Testing file for player score')
message.close()

message_test = open('313-message.txt','r')
content = message_test.read()
print(content)
message_test.close()