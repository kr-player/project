from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 열고 NumPy 배열로 변환
img = Image.open('cat.jpg')

# 이미지 지정한 좌표에서 자르기
box = (300, 300, 700, 700)
region = img.crop(box)

# 이미지 크기 크게 변경
new_size = (800, 800)
img = img.resize(new_size)

# 이미지를 90도 회전
region = region.transpose(Image.ROTATE_90)

# 이미지 좌우 대칭
region = region.transpose(Image.FLIP_LEFT_RIGHT)

# 원래 이미지를 흐리게 만들기
blurred_img = img.filter(ImageFilter.BLUR)

# 원래 이미지와 조작된 이미지 병합하며 (위치는 0,0,400,400에 병합함)
blurred_img.paste(region, (0, 0, 400, 400))

# 이미지를 넘파이 배열로 변환
img_np = np.array(blurred_img)

# 이미지를 시각화
plt.imshow(np.array(blurred_img))
plt.show()

# 이미지를 바이트 배열로 변환하여 출력
img_byte_array = blurred_img.tobytes()
print("바이트 배열:")
print(img_byte_array)

# 넘파이 배열 출력
print("넘파이 배열:")
print(img_np)

# 이미지를 파일로 저장 (예: saved_image.jpg)
blurred_img.save("new cat.jpg", "JPEG")
