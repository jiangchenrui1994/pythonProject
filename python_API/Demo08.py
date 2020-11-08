# 下载保存图片
#https://static.veer.com/veer/static/resources/Titles/2020-10-09/655024ef6fde46d7813dc76796447a9a.gif
import requests
from io import BytesIO
from PIL import Image
response = requests.get(url = 'https://static.veer.com/veer/static/resources/Titles/2020-10-09/655024ef6fde46d7813dc76796447a9a.gif')
img = Image.open(BytesIO(response.content))
img.save('../data/a.gif')