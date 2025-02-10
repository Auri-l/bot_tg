import requests
import wget
from pathlib import Path
from shutil import rmtree
def vk():
    access_token = 'c1e1dbd9c1e1dbd9c1e1dbd98cc2c6238fcc1e1c1e1dbd9a6711c99c0af284316c12dda'
    url=f"https://api.vk.com/method/board.getComments?group_id=158830121&topic_id=37235959&access_token={access_token}&v=5.1999"
    response = requests.get(url)
    mass = response.json()['response']['items'][response.json()['response']['count']-1]
    if "заочного" in mass['text']:
        mass = response.json()['response']['items'][response.json()['response']['count']-2]
        if "заочного" in mass['text']:
            mass = response.json()['response']['items'][response.json()['response']['count']-3]
    print(mass)
    result=[]
    len_obj = len(mass['attachments'])

    for path in Path('/home/Student/PycharmProjects/PythonProject/pdf').glob('*'):
        if path.is_dir():
            rmtree(path)
        else:
            path.unlink()

    for i in range(0,len_obj):
        url = mass['attachments'][i]['doc']['url']
        wget.download(url, f'pdf/pdf_v2{i}.pdf')
        result.append({'title':mass['attachments'][i]['doc']['title'],'url':mass['attachments'][i]['doc']['url'],'name':f'pdf/pdf_v2{i}.pdf'})
    return result


























#c1e1dbd9c1e1dbd9c1e1dbd98cc2c6238fcc1e1c1e1dbd9a6711c99c0af284316c12dda
