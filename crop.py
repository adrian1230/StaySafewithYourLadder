import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from gxml import generate
from pathlib import Path

try:
    if not os.path.exists('annotation'):
        os.makedirs('annotation')

except OSError:
    print('Error: Creating directory of annotation')

try:
    if not os.path.exists('annotation/hands'):
        os.makedirs('annotation/hands')

except OSError:
    print('Error: Creating directory of hands')

try:
    if not os.path.exists('annotation/humanhands'):
        os.makedirs('annotation/humanhands')

except OSError:
    print('Error: Creating directory of human hands')

try:
    if not os.path.exists('annotation/ladder'):
        os.makedirs('annotation/ladder')

except OSError:
    print('Error: Creating directory of ladder')

try:
    if not os.path.exists('annotation/ladderwooden'):
        os.makedirs('annotation/ladderwooden')

except OSError:
    print('Error: Creating directory of ladder wooden')

try:
    if not os.path.exists('annotation/shoes'):
        os.makedirs('annotation/shoes')

except OSError:
    print('Error: Creating directory of shoes')

try:
    if not os.path.exists('annotation/trainershoes'):
        os.makedirs('annotation/trainershoes')

except OSError:
    print('Error: Creating directory of trainer shoes')

try:
    if not os.path.exists('annotation/4'):
        os.makedirs('annotation/4')

except OSError:
    print('Error: Creating directory of 4')

try:
    if not os.path.exists('annotation/5'):
        os.makedirs('annotation/5')

except OSError:
    print('Error: Creating directory of 5')

try:
    if not os.path.exists('annotation/6'):
        os.makedirs('annotation/6')

except OSError:
    print('Error: Creating directory of 6')

container = os.listdir('data')

container = container[1:]

docker = []

for i in range(len(container)):
    if container[i].endswith('mp4') != True:
        docker.append(container[i])

print('all data folder for this task:\n{}'.format(
    docker
))

path = input('input the folder you want to annotate here >>> ')

image_folder = 'data' + '/' + path
savedir = 'annotation'
tl_list = []
br_list = []
object_list = []
img = None
obj = 'Ladder'

def line_select_callback(clk, rls):
    global tl_list
    global br_list
    
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)
    print(f'Recorded: \n{object_list}\n')
    print(f'Top Left: \n{tl_list}\n')
    print(f'Bottom Right: \n{br_list}\n')

def change_object(event):
    global obj
    if event.key == 'c':
        print('[Changed to Ladder]\n')
        obj = 'Ladder'

    if event.key == 'h':
        print('[Changed to Hand]\n')
        obj = 'Hand'
    
    if event.key == 'e':
        print('[Changed to Feet]\n')
        obj = 'Feet'

    if event.key == 'r':
        del tl_list[-1]
        del br_list[-1]
        del object_list[-1]
        print('[Deleted Previous Object]\n')
        print(f'Recorded: \n{object_list}\n')
        print(f'Top Left: \n{tl_list}\n')
        print(f'Bottom Right: \n{br_list}\n')

def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 's':
        generate(image_folder, img, object_list,
         tl_list, br_list, savedir)
        print(f'[Final] \n{tl_list}\n{br_list}\n{object_list}\n')
        tl_list = []
        br_list = []
        img = None
        object_list = []
        plt.close()

    if event.key == 'd':
        os.remove(img)
        print('[Deleted the image]\n')
        plt.close()

def toggle_selector(event):
    toggle_selector.RS.set_active(True)

if __name__ == '__main__':
    for image_file in sorted(Path(image_folder).glob('*.jpg')):
        img = image_file
        fig, ax = plt.subplots(1)
        image = cv2.imread(str(img))
        print(image_file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype = 'box', useblit = True,
            button = [1], minspanx = 3, minspany = 3,
            spancoords = 'pixels', interactive = True
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        obj_changed = plt.connect('key_press_event', change_object)
        key = plt.connect('key_press_event', onkeypress)
        plt.tight_layout()
        plt.show()