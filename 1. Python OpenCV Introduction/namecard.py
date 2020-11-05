import sys
import cv2

src = cv2.imread('namecard1.jpg')

if src is None:
    print('image load failed')
    sys.exit()

# (810, 1080, 3) -> (480, 640, 3)
cv2.resize(src, (0, 0), fx = 0.5, fy = 0.5) # src = cv2.resize(src, (640, 480))

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# histogram에 따라서 T=130으로 이진화 적용 결과 다르게 나옴 (수동 이진화)
_, src_bin = cv2.threshold(src_gray, 130, 255, cv2.THRESH_BINARY) # _ : 첫번째 return값은 받지만 안쓸 것

# Otsu : 자동 임계값 결정 방법
th, src_otsu = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 0이든 130이든 Otsu에서는 무시
print(th) # Otsu로 구해진 임계값 (133)

cv2.imshow('src', src)
cv2.imshow('src_gray', src_gray)
cv2.imshow('src_bin', src_bin)
cv2.waitKey()
cv2.destroyAllWindows()