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
        project_info(module_get_project.IGd(get_project(input("请输入项目的id或名称："))))

def connection_test():
    print(module_connection_test.CTt())

def about():
    print("-----------------------------")
    print("modrinth小助手 —— GavinCQTD")
    print("v1.0.0 d5.1")
    print("-----------------------------\n")

def check_project(idorslug):
    check = module_get_project.IEc(idorslug)
    if check=="Error":
        print("请检查你的网络设置！")
    elif check:
        print("存在该项目。")
    else:
        print("该项目不存在。")

def get_project(idorslug):
    check = module_get_project.IEc(idorslug)
    if check == "Error":
        print("请检查你的网络设置！")
        return 0
    elif not check:
        print("该项目不存在。")
        return 0
    return module_get_project.IEg(idorslug)

def project_info(info):
    temp = ''
    
    print("--------{0}--------\n{1}\n类型：{2} 客户端支持：{3} 服务端支持：{4}\n下载数：{5} 关注数：{6}\n".format(info[0], info[1], info[2], info[3], info[4], info[5], info[6]))
    time.sleep(3)
    
    while temp!="q":
        print('1.查看项目描述')
        print("2.查看项目支持版本")
        print("q.退出项目信息")
        temp = input("请选择功能：    (输入功能编号)")
        
        if temp=="1":
            print("\nmarkdown:{0}\n\nhtml:{1}\n\n许可证：{2}\n".format(info[7], markdown.markdown(info[7]),info[8]))
            time.sleep(2)
        elif temp=="2":
            print("\n支持的游戏版本：{0}\n支持的mod加载器：{1}\n".format(info[9], info[10]))


about()
while function!="q":
    main()
print("------感谢使用！------")