import cv2        
import threading   
import playsound  

  

fire_cascade = cv2.CascadeClassifier('fire_detection.xml') 

vid = cv2.VideoCapture(0) 
runOnce = False 

def play_alarm_sound_function():
    playsound.playsound('FOM.mp3',True) 
    print("Fire alarm end") 


    
		
while(True):
    Alarm_Status = False
    ret, Forest = vid.read() 
    gray = cv2.cvtColor(Forest, cv2.COLOR_BGR2GRAY) 
    fire = fire_cascade.detectMultiScale(Forest, 1.2, 5) 

    
    for (x,y,w,h) in fire:
        cv2.rectangle(Forest,(x-20,y-20),(x+w+20,y+h+20),(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = Forest[y:y+h, x:x+w]

        print("Fire alarm initiated")
        threading.Thread(target=play_alarm_sound_function).start()  # To call alarm thread

      

    cv2.imshow('Forest', Forest)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release
cv2.destroyAllWindows    