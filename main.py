import markdown
import time
import webbrowser
import os

import module_task_processing
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
    print("2.获取项目信息")
    print("3.搜索项目\n")
    print("q.退出此分类")
    print("-----------------------------")

    function_p = input("")
    if function_p == "1":
        check_project(input("请输入项目的id或名称："))
        time.sleep(2)
    elif function_p == "2":
        project_info(module_get_project.IGd(get_project(input("请输入项目的id或名称："))))
    elif function_p == "3":
        q = input("请输入要搜索的名称：")
        facets = search_project_I()
        
        search_project_O(module_get_project.IEs(q, facets, ""))

def connection_test():
    print(module_task_processing.CTt())

def about():
    print("-----------------------------")
    print("modrinth小助手 —— GavinCQTD")
    print("v1.1.0 dev2d2")
    print("github：https://github.com/gi-b716/modrinth-api-tools")
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
        time.sleep(2)
        return None
    return module_get_project.IEg(idorslug)

def project_info(info):
    if info is None:
        return 0
    
    temp = ''
    
    print("--------{0}--------\n{1}\n类型：{2} 客户端支持：{3} 服务端支持：{4}\n下载数：{5} 关注数：{6}\n".format(info[0], info[1], info[2], info[3], info[4], info[5], info[6]))
    time.sleep(3)
    
    while temp!="q":
        print('\n1.查看项目描述')
        print("2.查看项目支持版本")
        print("3.查看项目相关链接\n")
        print("4.打开项目链接")
        print("q.退出项目信息")
        temp = input("请选择功能：    (输入功能编号)")
        
        if temp=="1":
            # print("\nmarkdown:{0}\n\nhtml:{1}\n\n许可证：{2}\n".format(info[7], markdown.markdown(info[7]),info[8]))
            print("\n{0}\n\n许可证：{1}\n".format(info[7], info[8]))
            if input("输入h打开网页形式的描述，输入其他字符退出：")=="h":
                with open("view.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
                    output_file.write(markdown.markdown(info[7]))
                webbrowser.open(os.path.abspath("view.html"))
        elif temp=="2":
            print("\n支持的游戏版本：{0}\n支持的mod加载器：{1}".format(info[9], info[10]))
            time.sleep(3)
        elif temp=="3":
            print("\n问题反馈链接：{0} 项目链接：{1}\nwiki链接：{2} discord链接：{3}\n打赏链接：{4}".format(info[11], info[12], info[13], info[14], info[15]))
            time.sleep(3)
        elif temp=="4":
            webbrowser.open("https://modrinth.com/{0}/{1}".format(info[2], info[16]))

def search_project_I():
    temp = None
    facets = []
    temp_l = []
    
    while temp != "q":
        temp = input("请输入想让搜索结果支持的Minecraft版本：(支持快照、愚人节版，请输入规范)  输入q结束输入")
        temp_l.append(temp)
    if module_get_project.IEs_Gfl(temp_l, "test") != "empty":
        facets.append(module_get_project.IEs_Gfl(temp_l, "versions"))
        
    temp_l = []
    temp = None
    print("\n请选择搜索结果的类型：")
    print("------------------------")
    print("1.模组/服务器插件/数据包")
    print("2.模组包")
    print("3.资源包")
    print("4.光影包")
    print("5.全部")
    print("------------------------")
    while temp != "q":
        try:
            temp = int(input("请输入你想搜索的类型编号："))
        except ValueError:
            print("请规范输入选项！")
            continue
        else:
            if temp not in [1,2,3,4,5]:
                print("请输入正确序号！")
                continue
            elif temp == 5:
                temp_l.append("q")
                break
            fields = ["mod", "modpack", "resourcepack", "shader"]
            temp_l.append(fields[temp-1])
    if module_get_project.IEs_Gfl(temp_l, "test") != "empty":
        facets.append(module_get_project.IEs_Gfl(temp_l, "project_type"))
    
    return facets
    

def search_project_O(s_json):
    r = list()
    r_n = list()
    temp = None
    try:
        for i in range(len(s_json['hits'])):
            r.append(s_json['hits'][i]['title'])
            r_n.append(s_json['hits'][i]['slug'])
    except KeyError:
        print("\n---没有查询到任何结果！---\n")
        time.sleep(2)
    except TypeError:
        print("请检查你的网络设置！")
        time.sleep(2)
    else:
        print("\n------查询结果------")
        for _ in range(len(r)):
            print(str(_+1)+". "+r[_])
        print("------查询结果------\n")
        time.sleep(3)
        while temp != "q":
            temp = input("请输入要查看项目信息的项目的编号：  输入其他字符退出")
            try:
                temp = int(temp)
            except ValueError:
                break
            else:
                if temp == 0:
                    print("请输入正确的编号！")
                try:
                    slug = r_n[temp-1]
                except IndexError:
                    print("请输入正确的编号！")
                else:
                    project_info(module_get_project.IGd(get_project(slug)))


about()
while function!="q":
    main()
print("------感谢使用！------")