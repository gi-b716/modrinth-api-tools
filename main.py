import markdown
import time

import module_connection_test
import module_get_project


function = ""


def main():
    global function

    print("-----------------------------")
    print("请选择功能：    (输入功能编号)")
    print('1.关于项目的功能\n')
    print("2.api连接测试")
    print("3.关于\n")
    print("q.退出程序")
    print("-----------------------------")
    
    function = input("")
    if function=="1":
        project()
    elif function=="2":
        connection_test()
        time.sleep(2)
    elif function=="3":
        about()
        time.sleep(2)

def project():
    print("-----------------------------")
    print("请选择功能：    (输入功能编号)")
    print('1.检查某个项目是否存在')
    print("2.获取项目信息\n")
    print("q.退出此分类")
    print("-----------------------------")

    function_p = input("")
    if function_p == "1":
        check_project(input("请输入项目的id或名称："))
        time.sleep(2)
    elif function_p == "2":
        pass

def connection_test():
    print(module_connection_test.CTt())

def about():
    print("-----------------------------")
    print("modrinth小助手 —— GavinCQTD")
    print("v1.0.0 d4")
    print("-----------------------------\n")

def check_project(idorslug):
    check = module_get_project.IEc(idorslug)
    if check=="Error":
        print("请检查你的网络设置！")
    elif check:
        print("存在该项目。")
    else:
        print("该项目不存在。")


about()
while function!="q":
    main()
print("------感谢使用！------")