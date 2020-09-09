import json
import os
cnt=0
st_path='/Users/babywalnut/PycharmProject/Find_Face/age_classifier/'
file_list = os.listdir(st_path)
ab=[]
for i in range(len(file_list)):
    file_list2 = os.listdir(os.path.join(st_path,file_list[i]))
    for j in range(len(file_list2)):
        ms_json='''
        image : {file_name}
        age : {age} 
        gender : {gender}'''.format(file_name=file_list2[j], age=file_list[i][-3::], gender=file_list[i][11:-4])
        ms_json2= [k for k in ms_json.split('\n') if len(k)>3]
        ms_json2= {k.split(':')[0].strip():k.split(':')[1].strip() for k in ms_json2}
        ab.append(ms_json2)
        cnt+=1


s=json.dumps(ab, indent=2)
print(s)
print(type(s))
print(cnt)
filename="ms_image_information.txt"

file = open(filename, 'a')
file.write(s)
file.close()