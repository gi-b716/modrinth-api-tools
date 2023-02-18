import requests

def CTt():
    gets = requests.get("https://api.modrinth.com/")
    getsj = gets.json()
    
    if gets.status_code == 200:
        print("连接成功！modrinth api版本：{0}".format(getsj['version']))
    else:
        print("连接出现错误。状态码：{0}".format(gets.status_code))