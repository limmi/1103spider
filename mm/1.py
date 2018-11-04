import requests


wd=input('请输入关键字：')
parse={'wd':wd}
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
url='https://www.baidu.com/s?'
response=requests.get(url,params=parse,headers=headers)
print(response.url)
with open(wd+'.html','wb') as f:
    f.write(response.content)