import requests
import os

headers = {
    'Host': 'image.baidu.com',
    'Cookie': 'BIDUPSID=BCE4E3393F0BA0577F54C303E55A30EA; PSTM=1630501661; __yjs_duid=1_a4fcaca3bce7b874830075fd5876906f1640946247983; BDUSS=C1YdzJmWTdNTkRHOER6VGtnTDJlbzVYc25SVVFKb3ZzVk5WMU0tbVZvY3BacFJqSVFBQUFBJCQAAAAAAQAAAAEAAABhjAxEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACnZbGMp2Wxjd; BDUSS_BFESS=C1YdzJmWTdNTkRHOER6VGtnTDJlbzVYc25SVVFKb3ZzVk5WMU0tbVZvY3BacFJqSVFBQUFBJCQAAAAAAQAAAAEAAABhjAxEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACnZbGMp2Wxjd; BAIDUID=5D110FB2A7DD9E157A606DC5D5C39290:FG=1; H_WISE_SIDS=39668_39663_39682_39690_39676_39679_39713_39740_39751; H_WISE_SIDS_BFESS=39668_39663_39682_39690_39676_39679_39713_39740_39751; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=39668_39676_39713_39740_39751_39791_39787_39704_39683_39662_39679_39818_39664_39783_39843; BAIDUID_BFESS=5D110FB2A7DD9E157A606DC5D5C39290:FG=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BA_HECTOR=848ka0858l00al8005250l8i1imdusu1r; ZFY=fmKYnasmnNuRNxdtVZekwDF4MUy2nlunKGJvUbZzRuE:C; ZD_ENTRY=baidu; PSINO=7; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; userFrom=ala; indexPageSugList=%5B%22%E7%A8%BB%E7%BA%B5%E5%8D%B7%E5%8F%B6%E8%9E%9F%22%2C%22%E5%A4%A7%E8%9E%9F%22%2C%22%E4%B8%9D%E8%8B%97%E7%B1%B3%E7%97%85%E8%99%AB%E5%AE%B3%22%2C%22%E7%A8%BB%E7%BA%B5%E5%8D%B7%E5%8F%B6%E8%9E%9F%E5%B9%BC%E8%99%AB%E6%97%B6%E6%9C%9F%E5%9B%BE%E7%89%87700%E5%BC%A0%22%2C%22%E7%A8%BB%E7%BA%B5%E5%8D%B7%E5%8F%B6%E8%9E%9F%E5%B9%BC%E8%99%AB%E6%97%B6%E6%9C%9F%E5%9B%BE%E7%89%87600%E5%BC%A0%22%2C%22%E7%A8%BB%E7%BA%B5%E5%8D%B7%E5%8F%B6%E8%9E%9F%E8%99%AB%E5%AE%B3%E5%9B%BE%E7%89%87%22%2C%22%E7%A8%BB%E7%BA%B5%E5%8D%B7%E5%8F%B6%E8%9E%9F%E5%B9%BC%E8%99%AB%E6%97%B6%E6%9C%9F%E5%9B%BE%E7%89%87%22%2C%22%E7%A8%BB%E5%8F%B6%E8%9D%89%E5%AF%B9%E6%B0%B4%E7%A8%BB%E7%9A%84%E5%BD%B1%E5%93%8D%22%2C%22%E7%A8%BB%E5%8F%B6%E8%9D%89%22%5D; cleanHistoryStatus=0; ab_sr=1.0.1_MDgzZGQwNDY0NjU2ZTcwOGI2ZmNmZjUxOTg0ZWUwOWU5NTU1NTcwMTZkMzY4YTlhODhhOTAwZWQxNWNiZGE1ZDNiMjUzMjEyYjNiMjIzZjQ0MDEzNjkzMjY1N2ZhODU1ODIzMjRiOTdlMTJmODY2YWMzNDRlM2NmZWQ0ZjM2NTU4NjFlZmE0ZGM0ZjA5N2RkZThkZjZlMGZmNzExM2U1Yw==; BDRCVFR[Txj84yDU4nc]=mk3SLVN4HKm',
    'Referer': 'https://image.baidu.com/search/index?ct=201326592&z=&tn=baiduimage&ipn=r&word=%E7%A8%BB%E7%BA%B5%E5%8D%B7%E5%8F%B6%E8%9E%9F%E5%B9%BC%E8%99%AB&pn=&spn=&istype=2&ie=utf-8&oe=utf-8&cl=2&lm=-1&st=-1&fr=&fmq=1701266423044_R&ic=&se=&sme=&width=&height=&face=0&hd=&latest=&copyright=&cs=&os=&objurl=&di=&gsm=5a&dyTabStr=MCwxLDMsMiw2LDQsNSw4LDcsOQ%3D%3D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'

}
number = 0
for page in range(1, 3):
    url = f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7958352370901162892&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%A8%BB%E7%BA%B5%E5%8D%B7%E5%8F%B6%E8%9E%9F%E5%B9%BC%E8%99%AB&queryWord=%E7%A8%BB%E7%BA%B5%E5%8D%B7%E5%8F%B6%E8%9E%9F%E5%B9%BC%E8%99%AB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=&expermode=&nojc=&isAsync=&pn={page * 30}&rn=30&gsm=1e&1701266431540="
    response = requests.get(url=url, headers=headers)
    json_data = response.json()
    data_list = json_data['data']
    for data in data_list[:-1]:
        number += 1
        file_path = os.path.join("E:/Daiso/稻纵卷叶螟/幼虫/", f'{number}.jpg')
        if os.path.exists(file_path):
            continue
        fromPageTitleEnc = data['fromPageTitleEnc']
        middleURL = data['middleURL']
        print(fromPageTitleEnc, middleURL)
        img_data = requests.get(middleURL).content

        with open(file_path, mode='wb') as f:
            f.write(img_data)





