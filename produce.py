from detecto import core, utils, visualize
import cv2
import torch
import numpy as np

model = core.Model.load('mm.pth',
 ['Ladder','Hand','Feet'])

def img(f):
    im = cv2.imread(f)
    im = cv2.resize(im,(224,224))
    return im

img1 = img(input('image path here: '))

pred = model.predict(img1)

labels, boxes, scores = pred

label1, box1 = [], []

for i in labels:
    label1.append(i)

for i in boxes:
    box1.append(i)

ladder = []

for i in range(len(labels)):
    if labels[i] == 'Ladder':
        ladder.append(i)
    else:
        pass

ladder = ladder[1:]

for i in ladder:
    del box1[i]
    del label1[i]

lad = []

for i in range(len(label1)):
    if label1[i] == 'Ladder':
        lad = box1[i]

target = []

for i in range(1, len(box1), 1):
    a1 = lad[0]
    b1 = lad[2]
    a2 = box1[i][0]
    b2 = box1[i][2]
    if a2 > a1 and b2 < b1:
        pass
    elif a2 < a1 and b2 > b1:
        pass
    elif a2 < a1 and b2 < b1:
        target.append(i)
    elif a2 > a1 and b2 > b1:
        target.append(i)

if len(target) > 0:
    for i in target:
        del box1[i]
        del label1[i]

foot = []
hands = []

for g in range(len(label1)):
    if label1[g] == 'Feet':
        foot.append(g)
    elif label1[g] == 'Hand':
        hands.append(g)

if len(foot) <= 2:
    del foot

try:
    if len(foot) > 2:
        foot = foot[2:]

except:
    pass

if len(hands) <= 2:
    del hands

try:
    if len(hands) > 2:
        hands = hands[2:]

except:
    pass

for i in range(len(box1)):
    box1[i] = box1[i].numpy()

try:
    for i in range(len(foot)):
        box1.pop(foot[i])
        label1.pop(foot[i])

except:
    pass

try:
    for i in range(len(hands)):
        box1.pop(hands[i])
        label1.pop(hands[i])

except:
    pass

for i in range(len(box1)):
    box1[i] = torch.from_numpy(box1[i])

box1 = torch.stack(box1)

h = 0
f = 0

for i in range(len(label1)):
    if label1[i] == 'Hand':
        h += 1
    elif label1[i] == 'Feet':
        f += 1
    else:
        pass

if (h+f) >= 3:
    print('safe')
elif (h+f) < 3:
    print('dangerous')

visualize.show_labeled_image(img1,box1,label1)

















