import cv2
import os

link = input('enter the name of the video file here >> ')

video = cv2.VideoCapture(link)

try: 
    if not os.path.exists('data'): 
        os.makedirs('data') 

except OSError: 
    print ('Error: Creating directory of data') 
  
currentframe = 0

print(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(video.get(cv2.CAP_PROP_FPS))

n = input('enter the frame number >> ')
n = int(n)

counter = 0
 
while(True): 

    ret,frame = video.read() 
  
    if ret: 
        name = './data/frame' + str(counter) + link.split('.')[0] +'.jpg'
        print ('Creating...' + name) 
  
        cv2.imwrite(name, frame) 

        currentframe += n
        counter += 1
        video.set(1, currentframe)

    else: 
        break
  
video.release() 
cv2.destroyAllWindows() 