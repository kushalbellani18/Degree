import random 

def encryptData(msg): 
    global data 
    str = "" 

    for c in msg: 
        if(c == " "): 
            str += " " 
        else: 
            str += data[c] 

    return str 

if __name__ == "__main__": 
    data = {} 

    i = 0 
    while(i < 26): 
        l = [v for k, v in data.items()] 

        while(True): 
            hmm = chr(random.randint(97, 122)) 
            if(hmm not in l): 
                data[chr(i+97)] = hmm 
                break 

        i += 1 

    msg = input("Enter: ") 
    msg = msg.lower() 
    msg2 = encryptData(msg) 

    print(msg2) 
