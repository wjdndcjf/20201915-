import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


# 이름 중간 기말 성적을 받아 평균 학점을 도출 후 List로 반환
def getGrade(name, mid, final):
    li = []
    li.append(name)
    li.append(mid)
    li.append(final)
    avg = (int(mid) + int(final)) / 2
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    li.append(avg)
    li.append(grade)
    return li


# 테이블에 모든 학생들을 저장한다.
def clickShowAll():
    treeview.delete(*treeview.get_children())
    for i in sDict:
        treeview.insert("", "end", text=i, values=sDict[i], iid=str(i))


# 테이블에 검색한 학생만 저장한다.
def showSearch(id):
    if id in sDict:
        treeview.delete(*treeview.get_children())
        treeview.insert("", "end", text=id, values=sDict[id], iid=str(id))
    else:
        # 학생이 존재하지 않으므로 예외처리 한다.
        messagebox.showerror("ERROR", "NO SUCH STUDENT")


# 검색할 학생 ID를 받는 창을 띄운다.
def clickSearch():
    inputPop = tk.Tk()
    inputPop.title("Input")
    inputPop.geometry("300x100+200+200")
    inputPop.resizable(False, False)
    label = tk.Label(inputPop, text="Input Student ID")
    label.pack(pady=3)
    inputPlace = ttk.Entry(inputPop)
    inputPlace.pack(pady=3)
    button = tk.Button(
        inputPop,
        text="확인",
        padx=20,
        command=lambda: (showSearch(inputPlace.get()), inputPop.destroy()),
    )
    button.pack(pady=3)


# 테이블에 검색한 학점의 학생들만 저장한다.
def showSearchByGrade(grade):
    treeview.delete(*treeview.get_children())
    for id in sDict:
        if grade == sDict[id][4]:
            treeview.insert("", "end", text=id, values=sDict[id], iid=str(id))


# 검색할 학점을 받는 창을 띄운다.
def clickSearchByGrade():
    inputPop = tk.Tk()
    inputPop.title("Input")
    inputPop.geometry("300x100+200+200")
    inputPop.resizable(False, False)
    label = tk.Label(inputPop, text="Select Grade")
    label.pack(pady=3)
    a = ["A", "B", "C", "D", "F"] 
    combobox = ttk.Combobox(inputPop) 
    combobox.config(height=5) 
    combobox.config(values=a) 
    combobox.config(state="readonly") 
    combobox.set("A")  
    combobox.pack()
    button = tk.Button(
        inputPop,
        text="Confirm",
        padx=20,
        command=lambda: (showSearchByGrade(combobox.get()), inputPop.destroy()),
    )
    button.pack(pady=3)


# 작성한 학생을 추가한다.
def CanAddStudent(id, name, mid, final):
    if id in sDict:
        # 중복된 학생이 있을경우 예외처리한다.
        messagebox.showerror("ERROR", "ALREADY EXIST STUDENT")
    else:
        sDict[id] = getGrade(name, mid, final)
        treeview.insert("", "end", text=id, values=sDict[id], iid=str(id))

# 학생에 대한 정보를 입력받는 창을 띄운다.
def clickAddStudent():
    addPop = tk.Tk()
    addPop.title("Input")
    addPop.geometry("300x300+200+200")
    addPop.resizable(False, False)
    idLabel = tk.Label(addPop, text="Input Student ID")
    idLabel.pack(pady=3)
    idInput = ttk.Entry(addPop)
    idInput.pack(pady=3)
    nameLabel = tk.Label(addPop, text="Input Name")
    nameLabel.pack(pady=3)
    nameInput = ttk.Entry(addPop)
    nameInput.pack(pady=3)
    midLabel = tk.Label(addPop, text="Input Midterm Score")
    midLabel.pack(pady=3)
    midInput = ttk.Entry(addPop)
    midInput.pack(pady=3)
    finalLabel = tk.Label(addPop, text="Input Final Score")
    finalLabel.pack(pady=3)
    finalInput = ttk.Entry(addPop)
    finalInput.pack(pady=10)

    button = tk.Button(
        addPop,
        text="Confirm",
        padx=20,
        command=lambda: (
            CanAddStudent(
                idInput.get(), nameInput.get(), midInput.get(), finalInput.get()
            ),
            addPop.destroy(),
        ),
    )
    button.pack(pady=3)

# 수정된 값을 반영한다.
def doModify(id, exam, score):
    if exam == "Midterm":
        sDict[id][1] = score
    else:
        sDict[id][2] = score
    sDict[id] = getGrade(sDict[id][0], sDict[id][1], sDict[id][2])
    clickShowAll()

# 수정하고자 하는 값을 받는 창을 띄운다.
def clickModify(id):
    if id == "":
        # 수정하고자 하는 ID가 없으므로 예외처리한다.
        messagebox.showerror("ERROR", "DID NOT CHOOSE STUDENT")
        return
    modifyPop = tk.Tk()
    modifyPop.title("Input")
    modifyPop.geometry("300x200+200+200")
    modifyPop.resizable(False, False)
    idLabel = tk.Label(modifyPop, text="Modify " + id)
    idLabel.pack(pady=3)

    nameLabel = tk.Label(modifyPop, text="Choose Modify Exam")
    nameLabel.pack(pady=3)

    a = ["Midterm", "Final"]  
    combobox = ttk.Combobox(modifyPop) 
    combobox.config(height=5) 
    combobox.config(values=a)  
    combobox.config(state="readonly")  
    combobox.set("Midterm") 
    combobox.pack()

    scoreLabel = tk.Label(modifyPop, text="Input Modify Score")
    scoreLabel.pack(pady=3)
    scoreInput = ttk.Entry(modifyPop)
    scoreInput.pack(pady=10)
    button = tk.Button(
        modifyPop,
        text="Confirm",
        padx=20,
        command=lambda: (
            doModify(id, combobox.get(), scoreInput.get()),
            modifyPop.destroy(),
        ),
    )
    button.pack(pady=3)

# 선택된 학생을 삭제한다.
def doDelete(id):
    treeview.delete(id)
    del sDict[id]

# 정말로 삭제할지 확인한다.
def clickDelete(id):
    if id == "":
        # 삭제하고자 하는 ID가 없으므로 예외처리한다.
        messagebox.showerror("ERROR", "DID NOT CHOOSE STUDENT")
        return
    deletePop = tk.Tk()
    deletePop.title("Input")
    deletePop.geometry("300x100+200+200")
    deletePop.resizable(False, False)
    idLabel = tk.Label(deletePop, text="Delete " + id)
    idLabel.pack(pady=3)
    button = tk.Button(
        deletePop,
        text="Confirm",
        padx=20,
        command=lambda: (doDelete(id), deletePop.destroy()),
    )
    button.pack(pady=3)

# 파일로 저장한다.
def save():
    file = open("students.txt", "w")
    for id in sDict:
        line = (
            id + "\t" + sDict[id][0] + "\t" + sDict[id][1] + "\t" + sDict[id][2] + "\n"
        )
        file.write(line)
    file.close()
    messagebox.showinfo("success", "Save Success")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grade Management")
    root.geometry("750x400+100+100")
    root.resizable(False, False)

    #테이블 셋팅
    treeview = ttk.Treeview(
        root,
        columns=["one", "two", "three", "four", "five"],
        displaycolumns=["one", "two", "three", "four", "five"],
    )
    treeview.pack(side="left", fill="y", padx=(10, 0), pady=(5, 10))

    treeview.column(
        "#0",
        width=150,
    )
    treeview.heading("#0", text="student")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="name", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="Midterm", anchor="center")

    treeview.column("#3", width=100, anchor="center")
    treeview.heading("three", text="Final", anchor="center")

    treeview.column("#4", width=100, anchor="center")
    treeview.heading("four", text="Average", anchor="center")

    treeview.column("#5", width=70, anchor="center")
    treeview.heading("five", text="Grade", anchor="center")

    # 라이브러리 import
    import sys
    import os

    # 저장된 데이터가 있을경우 불러온다.
    if not os.path.isfile("students.txt"):
        open("students.txt", "w")
    file = open("students.txt", "r")
    rawDict = {}
    for line in file:
        li = []
        li = line.strip().split("\t")
        id = li.pop(0)
        rawDict[id] = li

    # 불러온 데이터를 가공한다.
    sDict = {}
    for id in rawDict:
        sDict[id] = getGrade(rawDict[id][0], rawDict[id][1], rawDict[id][2])

    # 표에 데이터 삽입
    for i in sDict:
        treeview.insert("", "end", text=i, values=sDict[i], iid=str(i))

    # 메뉴 버튼
    showAll = tk.Button(
        root, text="ShowAll", width=13, pady=10, command=lambda: clickShowAll()
    )
    serach = tk.Button(
        root, text="Search", width=13, pady=10, command=lambda: clickSearch()
    )
    gradeSearch = tk.Button(
        root,
        text="SearchByGrade",
        width=13,
        pady=10,
        command=lambda: clickSearchByGrade(),
    )
    AddStudent = tk.Button(
        root, text="Add", width=13, pady=10, command=lambda: clickAddStudent()
    )
    modify = tk.Button(
        root,
        text="Modify",
        width=13,
        pady=10,
        command=lambda: clickModify(treeview.focus()),
    )
    delete = tk.Button(
        root,
        text="Delete",
        width=13,
        pady=10,
        command=lambda: clickDelete(treeview.focus()),
    )
    saveBtn = tk.Button(root, text="Save", width=13, pady=10, command=lambda: save())
    showAll.pack(pady=5)
    serach.pack(pady=5)
    gradeSearch.pack(pady=5)
    AddStudent.pack(pady=5)
    modify.pack(pady=5)
    delete.pack(pady=5)
    saveBtn.pack(pady=5)

    root.mainloop()