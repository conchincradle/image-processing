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
