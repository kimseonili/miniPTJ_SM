from PIL import Image
import face_recognition
import os

imagePath ='/Users/babywalnut/새달껌/T2b/Project#Big#pytorch/AI_hub/part3/part3/KETI_MULTIMODAL_0000001004/KETI_MULTIMODAL_0000001004/'
file_list2=os.listdir(imagePath)
print(file_list2)
for i in range(len(file_list2)):
    cnt = 0
    file_list = os.listdir(imagePath+file_list2[i])
    print(file_list)
    for j in range(len(file_list)):
        이 부분에 알파포즈입히는 코드나 함수 호출
        # image = face_recognition.load_image_file(imagePath+file_list2[i]+'/'+file_list[j])
        # face_locations = face_recognition.face_locations(image)
        # for face_location in face_locations:
        #     top, right, bottom, left = face_location

        #     face_image=image[top:bottom, left:right]
        #     pil_image = Image.fromarray(face_image)
        #     #cv2.resize(pil_image)
            pil_image.save(f'/Users/babywalnut/PycharmProject/Find_Face/Destroy_image/{file_list2[i]}_{cnt}.jpg')
            cnt+=1

