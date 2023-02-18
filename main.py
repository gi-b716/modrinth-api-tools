import module_connection_test


function = ""


def main():
    global function

    print("-----------------------------")
    print("请选择功能：    (输入功能编号)")
    print("1.api连接测试")
    print("2.关于\n")
    print("q.退出程序")
    print("-----------------------------")
    
    function = input("")
    if function=="1":
        connection_test()
    elif function=="2":
        about()
    
def connection_test():
    print(module_connection_test.CTt())

def about():
    print("-----------------------------")
    print("modrinth小助手 —— GavinCQTD")
    print("v1.0.0 d3")
    print("-----------------------------\n")


about()
while function!="q":
    main()
print("------感谢使用！------")