import random
from google.colab.patches import cv2_imshow
new_crop = crops.copy()
random.shuffle(new_crop)
#print(new_crop)

img = [0]*n
for i in range(n):
  path = new_crop[n*i]
  
  img[i] = cv2.imread(path)
for i in range(n):
  for j in range(1,n):
    path = new_crop[n*i+j]
    img[i] = np.concatenate((img[i],cv2.imread(path)),axis=1)
  #cv2_imshow(img[i])
final = img[0]   
for i in range(1,n):
  final = np.concatenate((final,img[i]),axis=0)
cv2_imshow(final)
# SEE puzzle_4.jpg


cv2.imwrite("final.jpg",final)
# final.jpg renamed to puzzle_128.jpg
# below is to do image blending of the concatenated lines
img = cv2.imread("puzzle_128.jpg")
n = 128
for i in range(1,n):
  mid = i*256//n
  a = img[mid-3].copy()
  b = img[mid+2].copy()
  for i in range(5):
    img[mid-3+i] = (1-0.2*i)*a+0.2*i*b
for i in range(1,n):
  mid = i*256//n
  a = img[:,mid-3].copy()
  b = img[:,mid+2].copy()
  for i in range(5):
    img[:,mid-3+i] = (1-0.2*i)*a+0.2*i*b

cv2.imwrite("128.jpg",img)

# SEE blending_puzzle_4.jpg
