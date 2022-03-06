#lex_auth_01269363490743091290

def display(num):
    message=""
    #write your logic here
    if(num%3==0 and num%5==0):
        message=message+"Zoom"
    elif(num%3==0):
        message=message+"Zip"
    elif(num%5==0):
        message=message + "Zap"
    else:
        message=message+"Invalid"
    
    return message

#Provide different values for num and test your program
message=display(15)
print(message)