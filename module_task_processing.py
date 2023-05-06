import requests

def CTt():
    try:
        gets = requests.get("https://api.modrinth.com/")
    except requests.exceptions.ConnectionError:
        return "请检查你的网络设置！"
    getsj = gets.json()
    
    if gets.status_code == 200:
        info = "连接成功！modrinth api版本：{0}".format(getsj['version'])
    else:
        info = "连接出现错误。状态码：{0}".format(gets.status_code)
    
    return info

def URLc(url):
    pass
        
    
    return url