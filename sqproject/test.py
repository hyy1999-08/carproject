from aip import AipImageClassify

APP_ID='17061516'
Type_client_id = '0aAPIpeYX7RbtFsEhSkzaFcY'
Type_client_secret = 'W1jSIHOSa7zwVYnGyA2H4pmG3Y1tOpb1'
client=AipImageClassify(APP_ID,Type_client_id,Type_client_secret)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image_path = 'E:\\大学\\大学~学习\\实习培训\\车牌识别代码①\\License-Plate-Recognition-master\\test\\cAA662F.jpg'
image=get_file_content(image_path)
print(client.carDetect(image, options={"top_num":1})["result"][0]["name"])