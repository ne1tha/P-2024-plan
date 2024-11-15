import json
from collections import deque

STU_LIST = []
STU_FILE = "students.json"
TOFILE = "todo.json"
HISTORY = deque()
TOLIST = deque()

def stu_init():
    global STU_LIST
    global STU_FILE
    global TOLIST

    try:
        with open(STU_FILE, 'r') as f:
            STU_LIST = json.load(f)
        try:
            with open(TOFILE, 'r') as t:
                TOLISTL = json.load(t)
                TOLIST = deque(TOLISTL)
        except FileNotFoundError:
            print("-" * 30)
            print("无待办事项存档。")
            print("-" * 30)
    except FileNotFoundError:
        print("-" * 30)
        print("无学生信息存档。")
        print("-" * 30)


def get_choice() -> int:
    menu()
    try:
        choice = int(input("请输入："))
        HISTORY.appendleft(choice)
        return choice
    except ValueError:
        print("非法输入，请重试。")
        return get_choice()


def menu():
    print("-" * 30)
    print("操作菜单")
    print("-" * 30)
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改学生")
    print("4. 查询学生")
    print("5. 保存学生信息")
    print("6. 查看操作历史")
    print("7. 添加待办事项")
    print("8. 删除待办事项")
    print("9. 查看待办事项")
    print("10.查看所有学生")
    print("0. 退出")
    print("-" * 30)


def execute_operation(choice):
    global STU_LIST

    if choice == 1:
        stu_add()
    elif choice == 2:
        stu_del()
    elif choice == 3:
        stu_mod()
    elif choice == 4:
        stu_sel()
    elif choice == 5:
        stu_save()
    elif choice == 6:
        stu_his()
    elif choice == 7:
        stu_toadd()
    elif choice == 8:
        stu_todel()
    elif choice == 9:
        stu_todo()
    elif choice == 10:
        stu_look()
    elif choice == 0:
        print("拜拜了您。")
    else:
        print("非法输入，请重试。")


def stu_add():
    global STU_LIST

    name = input("请输入姓名：")
    id = input("请输入学号：")
    student = {"name": name, "id": id}
    STU_LIST.append(student)
    print(f"已成功添加学生：{name}，学号：{id}")


def stu_del():
    global STU_LIST

    id = input("请输入学号：")
    for student in STU_LIST:
        if student["id"] == id:
            STU_LIST.remove(student)
            print(f"已成功删除学号为 {id} 的学生。")
            return
    print(f"未找到学号为 {id}。")


def stu_mod():
    global STU_LIST

    id = input("请输入学号：")
    for student in STU_LIST:
        if student["id"] == id:
            new_name = input(f"请输入新的学生姓名（原姓名：{student["name"]}）：")
            new_id = input(f"请输入新的学生学号（原学号：{student["id"]}）：")
            student["name"] = new_name
            student["id"] = new_id
            print(f"已成功修改学号为 {id} 的学生信息。")
            return
    print(f"未找到学号为 {id} 的学生，无法修改。")


def stu_sel():
    global STU_LIST

    id = input("请输入要查询学生的学号：")
    for student in STU_LIST:
        if student["id"] == id:
            print(f"查询到学生信息：姓名：{student["name"]}，学号：{student["id"]}")
            return
    print(f"未找到学号为 {id} 的学生，无法查询。")


def stu_save():
    global STU_LIST
    global STU_FILE

    with open(STU_FILE, 'w') as f:
        json.dump(STU_LIST, f, indent=4)
    with open(TOFILE, 'w') as t:
        TOLISTL = list(TOLIST)
        json.dump(TOLISTL, t, indent=4)
    print("信息已成功保存到文件中。")
    
    
def stu_his():
    global HISTORY
    
    print("历史记录")
    print("-" * 30)
    for i,choice in enumerate(HISTORY):
        if choice == 1:
            print(f"第{i+1}条记录：1. 添加学生")
        elif choice == 2:
            print(f"第{i+1}条记录：2. 删除学生")
        elif choice == 3:
            print(f"第{i+1}条记录：3. 修改学生")
        elif choice == 4:
            print(f"第{i+1}条记录：4. 查询学生")
        elif choice == 5:
            print(f"第{i+1}条记录：5. 保存学生信息")
        elif choice == 6:
            print(f"第{i+1}条记录：6. 查看操作历史")
        elif choice == 7:
            print(f"第{i+1}条记录：7. 添加待办事项")
        elif choice == 8:
            print(f"第{i+1}条记录：8. 删除待办事项")
        elif choice == 9:
            print(f"第{i+1}条记录：9. 查看待办事项")
        elif choice == 10:
            print(f"第{i+1}条记录：10. 查看所有学生")
    print("-" * 30)
                
def stu_toadd():
    global TOLIST
    
    todo = input("请输入代办事项：")
    TOLIST.append(todo)
    
    
def stu_todel():
    global TOLIST

    try:
        todel = int(input("请输入你想删除的记录序号："))
        if 1 <= todel <= len(TOLIST):
            del TOLIST[todel - 1]
            print(f"已成功删除第{todel}项待办事项。")
        else:
            print("输入的序号无效，请重新输入。")
    except ValueError:
        print("请输入有效的数字序号。")
            
            
def stu_todo():
    global TOLIST
    
    print("-" * 30)
    for i,todo in enumerate(TOLIST):
        print(f"第{i+1}项：{todo}")
    print("-" * 30)
        
        
def stu_look():
    global STU_LIST
    
    print("-" * 30)
    for stu in STU_LIST:
        for key,value in stu.items():
            print(f"{key}:{value}")
    print("-" * 30)
        
            
if __name__ == '__main__':
    stu_init()
    user_choice = get_choice()
    while user_choice!= 0:
        execute_operation(user_choice)
        c = input()
        user_choice = get_choice()