from gtts import gTTS  
 
s = input("Enter the File name: ") 
 
f = open(s)
text = f.read()
 
obj = gTTS(text= text, lang= 'en' ,slow= False) # en -- english || You can change slow value into True..
 
f1 = input("Enter the Audio name to be saved : ")  
 
obj.save(f1)  
