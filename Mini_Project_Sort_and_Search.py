from tkinter import*
from tkinter import messagebox
from tkinter import ttk

arrayInt = []
for i in range(101):
    arrayInt.append(i)

window = Tk()
window.geometry("1080x608+250+100")
window.title("โปรแกรมขั้นตอนวิธี")
window.configure(background="#5F9EA0")
index_image = PhotoImage(file="D:\Datastructure\Image\start.png") 
index_label = Label(window, image=index_image) 
index_label.place(relwidth=1.0, relheight=1.0)

def menuExit(): 
    window.destroy() 

def Bubble_sort(): 
    windowBubble = Toplevel(window) 
    windowBubble.title("แบบฟองสบู่") 
    windowBubble.configure(background="#FFFFFF")  
    windowBubble.geometry("495x700+520+40") 
    index_Bubble_image = PhotoImage(file="D:\Datastructure\Image\Bubble.png") 
    Bubble_label = Label(windowBubble, image=index_Bubble_image)
    Bubble_label.place(relwidth=1.0, relheight=1.0)

    def menuExitBubble(): 
        windowBubble.destroy()

    def Work_proces_Bubble() :
        windowBubble2 = Toplevel(window) 
        windowBubble2.title("ขั้นตอนการทำงานแบบฟองสบู่") 
        windowBubble2.configure(background="#FFFFFF")  
        windowBubble2.geometry("1080x608+250+100")
        index_Insert_image = PhotoImage(file="D:\Datastructure\Image\StepBubble1.png") 
        proces_Bubble_label = Label(windowBubble2, image=index_Insert_image)
        proces_Bubble_label.place(relwidth=1.0, relheight=1.0)
        def menuExit_proces_Bubble(): 
            windowBubble2.destroy()
        Bubble_botton = Button(windowBubble2,text=" < ",font = 102,bg="#FCD24F",bd=5,command = menuExit_proces_Bubble)
        Bubble_botton.place(x=500,y=460,width=90,height=40)
        windowBubble2.mainloop()

    def Procedure_Bubble(): 
        windowBubble1 = Toplevel(window) 
        windowBubble1.title("ขั้นตอนการทำงานแบบฟองสบู่") 
        windowBubble1.configure(background="#FFFFFF")  
        windowBubble1.geometry("1080x608+250+100") 
        index_Bubble_image = PhotoImage(file="D:\Datastructure\Image\StepBubble.png") 
        Procedure_Bubble_label = Label(windowBubble1, image=index_Bubble_image)
        Procedure_Bubble_label.place(relwidth=1.0, relheight=1.0)
        def menuExit_Procedure_Bubble(): 
            windowBubble1.destroy()
        Bubble_Button1 = Button(windowBubble1,text=" > ",font = 102,bg="#FCD24F",bd=5,command = Work_proces_Bubble)
        Bubble_Button1.place(x=500,y=460,width=90,height=40)
        myMenu = Menu()
        myMenu.add_command(label="Exit",command=menuExit_Procedure_Bubble)
        windowBubble1.config(menu=myMenu)
        windowBubble1.mainloop()

    def menuclear():
        num1.set("")
        num2.set("")
        num3.set("")
        num4.set("")
        result.set("")

    def Bubble_sort(arrint):
        def swap(i, j):
            arrint[i], arrint[j]= arrint[j], arrint[i]

        n = len(arrint)
        swapped = True

        x = -1
        
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if arrint[i - 1] > arrint[i]:
                    swap(i - 1, i)
                    swapped = True

        return arrint

    def calculate_Bubble_sort():
        try:
            if num1 and num2 and num3 and num4 != "":
                input_Var1 = int(num1.get())
                input_Var2 = int(num2.get())
                input_Var3 = int(num3.get())
                input_Var4 = int(num4.get())
                input_array = [input_Var1, input_Var2, input_Var3, input_Var4]
                sorted_array = Bubble_sort(input_array)
            result.set(sorted_array)
        except ValueError:
            messagebox.showerror(title="Error",message="กรุณาป้อนตัวเลข")
    
    Bubble_label1=Button(windowBubble,text="Number 1",font = 15,width=9,fg="black",bg="#EFEFEF") 
    Bubble_label1.place(x=30,y=150,width=130,height=40)

    num1 = StringVar()
    num1.set("")
    txtBubble1 = Entry(windowBubble,font=2,width = 25,bg="#BFC2BF",textvariable=num1)
    txtBubble1.place(x=190,y=150,width=270,height=40)

    Bubble_label2=Button(windowBubble,text="Number 2",font = 15,width=9,fg="black",bg="#EFEFEF")
    Bubble_label2.place(x=30,y=220,width=130,height=40)

    num2 = StringVar()
    num2.set("")
    txtBubble2 = Entry(windowBubble,font=2,width = 25,bg="#BFC2BF",textvariable=num2)
    txtBubble2.place(x=190,y=220,width=270,height=40)

    Bubble_label3=Button(windowBubble,text="Number 3",font = 15,width=9,fg="black",bg="#EFEFEF")
    Bubble_label3.place(x=30,y=290,width=130,height=40)
    
    num3 = StringVar()
    num3.set("")
    txtBubble3 = Entry(windowBubble,font=2,width = 25,bg="#BFC2BF",textvariable=num3)
    txtBubble3.place(x=190,y=290,width=270,height=40)

    Bubble_label4=Button(windowBubble,text="Number 4",font = 15,fg="black",width=9,bg="#EFEFEF")
    Bubble_label4.place(x=30,y=360,width=130,height=40)
    
    num4 = StringVar()
    num4.set("")
    txtBubble4 = Entry(windowBubble,font=2,width = 25,bg="#BFC2BF",textvariable=num4)
    txtBubble4.place(x=190,y=360,width=270,height=40)

    Bubble_label5=Button(windowBubble,text="Result",font = 15,fg="black",width=9,bg="#339DA6")
    Bubble_label5.place(x=30,y=430,width=130,height=40)

    result = StringVar()
    result.set("")
    txtBubble5 = Entry(windowBubble,font=2,width = 25,textvariable=result)
    txtBubble5["state"] = "readonly"
    txtBubble5.place(x=190,y=430,width=270,height=40)

    
    Bubble_btCir = Button(windowBubble,text="Compute",font=2,bg="#36B7DA",bd=5,command=calculate_Bubble_sort)
    Bubble_btCir.place(x=110,y=580,width=100,height=40)
    
    Bubble_btCancel = Button(windowBubble,text="Cancel",font = 102,bg="#FC5658",bd=5,command = menuclear)
    Bubble_btCancel.place(x=300,y=580,width=100,height=40)

    Bubble_btStep = Button(windowBubble,text="Work process",font = 102,bg="#FCD24F",bd=5,command = Procedure_Bubble)
    Bubble_btStep.place(x=180,y=510,width=160,height=50)

    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitBubble)
    windowBubble.config(menu=myMenu)
    windowBubble.mainloop()

def Insert_sort(): 
    windowInsert = Toplevel(window) 
    windowInsert.title("แบบแทรก") 
    windowInsert.configure(background="#DCDCDC")  
    windowInsert.geometry("495x700+520+40") 
    index_Insert_image = PhotoImage(file="D:\Datastructure\Image\Insert.png") 
    Insert_label = Label(windowInsert, image=index_Insert_image)
    Insert_label.place(relwidth=1.0, relheight=1.0)
    def menuExitInsert(): 
        windowInsert.destroy()
    def Work_Insert_proces() :
        windowInsert2 = Toplevel(window) 
        windowInsert2.title("ขั้นตอนการทำงานแบบเเทรก") 
        windowInsert2.configure(background="#FFFFFF")  
        windowInsert2.geometry("1080x608+250+100")
        index_Insert_image = PhotoImage(file="D:\Datastructure\Image\Stepinsert1.png") 
        Proces_Insert_label = Label(windowInsert2, image=index_Insert_image)
        Proces_Insert_label.place(relwidth=1.0, relheight=1.0) 
        def menuExit_proces_Insert(): 
            windowInsert2.destroy()
        Insert_Button = Button(windowInsert2,text="<",font = 102,bg="#FCD24F",bd=5,command = menuExit_proces_Insert)
        Insert_Button.place(x=500,y=460,width=90,height=40)
        windowInsert2.mainloop()

    def Procedure_Insert(): 
        windowInsert1 = Toplevel(window) 
        windowInsert1.title("ขั้นตอนการทำงานแบบเเทรก") 
        windowInsert1.configure(background="#DCDCDC")  
        windowInsert1.geometry("1080x608+250+100") 
        index_Insert_image = PhotoImage(file="D:\Datastructure\Image\Stepinsert.png") 
        Procedure_Insert_label = Label(windowInsert1, image=index_Insert_image)
        Procedure_Insert_label.place(relwidth=1.0, relheight=1.0)
        def menuExit_Procedure_Insert(): 
            windowInsert1.destroy()
        Insert_Button1 = Button(windowInsert1,text=">",font = 102,bg="#FCD24F",bd=5,command = Work_Insert_proces)
        Insert_Button1.place(x=500,y=460,width=90,height=40)
        myMenu = Menu()
        myMenu.add_command(label="Exit",command=menuExit_Procedure_Insert)
        windowInsert1.config(menu=myMenu)
        windowInsert1.mainloop()

    def menuclear():
        num1.set("")
        num2.set("")
        num3.set("")
        num4.set("")
        result.set("")

    def Insertion_sort(arr):
        for i in range(len(arr)):
            cursor = arr[i]
            pos = i 
            
            while pos > 0 and arr[pos - 1] > cursor:
                arr[pos] = arr[pos - 1]
                pos = pos - 1
            arr[pos] = cursor
        return arr

    def calculate_Insert_sort():
        try:
            if num1 and num2 and num3 and num4 != "":
                input_Var1 = int(num1.get())
                input_Var2 = int(num2.get())
                input_Var3 = int(num3.get())
                input_Var4 = int(num4.get())
                input_array = [input_Var1, input_Var2, input_Var3, input_Var4]
                sorted_array = Insertion_sort(input_array)
            result.set(sorted_array)
        except ValueError:
            messagebox.showerror(title="Error",message="กรุณาป้อนตัวเลข")
    
    Insert_label1=Button(windowInsert,text="Number 1",font = 15,fg="black",width=9,bg="#EFEFEF") 
    Insert_label1.place(x=30,y=150,width=130,height=40)
    
    num1 = StringVar()
    num1.set("")
    txtInsert1 = Entry(windowInsert,font=2,width = 25,bg="#BFC2BF",textvariable=num1)
    txtInsert1.place(x=190,y=150,width=270,height=40)

    Insert_label2=Button(windowInsert,text="Number 2",font = 15,fg="black",bg="#EFEFEF") 
    Insert_label2.place(x=30,y=220,width=130,height=40)
    
    num2 = StringVar()
    num2.set("")
    txtInsert2 = Entry(windowInsert,font=2,width = 25,bg="#BFC2BF",textvariable=num2)
    txtInsert2.place(x=190,y=220,width=270,height=40)

    Insert_label3=Button(windowInsert,text="Number 3",font = 15,fg="black",bg="#EFEFEF") 
    Insert_label3.place(x=30,y=290,width=130,height=40)
    
    num3 = StringVar()
    num3.set("")
    txtInsert3 = Entry(windowInsert,font=2,width = 25,bg="#BFC2BF",textvariable=num3)
    txtInsert3.place(x=190,y=290,width=270,height=40)

    Insert_label4=Button(windowInsert,text="Number 4",font = 15,fg="black",bg="#EFEFEF") 
    Insert_label4.place(x=30,y=360,width=130,height=40)
    
    num4 = StringVar()
    num4.set("")
    txtInsert4 = Entry(windowInsert,font=2,width = 25,bg="#BFC2BF",textvariable=num4)
    txtInsert4.place(x=190,y=360,width=270,height=40)

    Insert_label5=Button(windowInsert,text="Result",font=1,fg="black",bg="#339DA6")
    Insert_label5.place(x=30,y=430,width=130,height=40)

    result = StringVar()
    result.set("")
    txtInsert5 = Entry(windowInsert,font=2,width = 25,textvariable=result)
    txtInsert5["state"] = "readonly"
    txtInsert5.place(x=190,y=430,width=270,height=40)

    Insert_btCal = Button(windowInsert,text="Compute",font=2,bg="#36B7DA",bd=5,command = calculate_Insert_sort)
    Insert_btCal.place(x=110,y=580,width=100,height=40)
    
    Insert_btCancel = Button(windowInsert,text="Cancel",font = 102,bg="#FC5658",bd=5,command = menuclear)
    Insert_btCancel.place(x=300,y=580,width=100,height=40)

    Insert_btStep = Button(windowInsert,text="Work process",font = 102,bg="#FCD24F",bd=5,command = Procedure_Insert)
    Insert_btStep.place(x=180,y=510,width=160,height=50)
    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitInsert)
    windowInsert.config(menu=myMenu)
    windowInsert.mainloop()

def Select_sort(): 
    windowSelect = Toplevel(window) 
    windowSelect.title("แบบเลือก") 
    windowSelect.configure(background="#DCDCDC")  
    windowSelect.geometry("495x700+520+40") 
    index_Select_image = PhotoImage(file="D:\Datastructure\Image\Selection.png") 
    Select_label = Label(windowSelect, image=index_Select_image)
    Select_label.place(relwidth=1.0, relheight=1.0)
    def menuExitSelect(): 
        windowSelect.destroy()
    def Work_Select_proces() :
        windowSelect2 = Toplevel(window) 
        windowSelect2.title("ขั้นตอนการทำงานแบบเลือก") 
        windowSelect2.configure(background="#FFFFFF")  
        windowSelect2.geometry("1080x608+250+100")
        index_Select_image = PhotoImage(file="D:\Datastructure\Image\Stepselect1.png") 
        proces_Select_label = Label(windowSelect2, image=index_Select_image)
        proces_Select_label.place(relwidth=1.0, relheight=1.0) 
        def menuExit_proces_Select(): 
            windowSelect2.destroy()
        Select_Button = Button(windowSelect2,text="<",font = 102,bg="#FCD24F",bd=5,command = menuExit_proces_Select)
        Select_Button.place(x=500,y=460,width=90,height=40)
        windowSelect2.mainloop()
    def Procedure_Select(): 
        windowSelect1 = Toplevel(window) 
        windowSelect1.title("ขั้นตอนการทำงานแบบเลือก") 
        windowSelect1.configure(background="#DCDCDC")  
        windowSelect1.geometry("1080x608+250+100") 
        index_Select_image = PhotoImage(file="D:\Datastructure\Image\Stepselect.png") 
        Procedure_Select_label = Label(windowSelect1, image=index_Select_image)
        Procedure_Select_label.place(relwidth=1.0, relheight=1.0)
        def menuExit_Procedure_Selct(): 
            windowSelect1.destroy()
        Select_Button1 = Button(windowSelect1,text=">",font = 102,bg="#FCD24F",bd=5,command = Work_Select_proces)
        Select_Button1.place(x=500,y=460,width=90,height=40)
        myMenu = Menu()
        myMenu.add_command(label="Exit",command=menuExit_Procedure_Selct)
        windowSelect1.config(menu=myMenu)
        windowSelect1.mainloop()

    def menuclear():
        num1.set("")
        num2.set("")
        num3.set("")
        num4.set("")
        result.set("")

    def Select_sort(arr):
        for i in range(len(arr)):
            minimum = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minimum]:
                    minimum = j
            arr[minimum],arr[i] = arr[i], arr[minimum]
        return arr

    def calculate_Select_sort():
        try:
            if num1 and num2 and num3 and num4 != "":
                input_Var1 = int(num1.get())
                input_Var2 = int(num2.get())
                input_Var3 = int(num3.get())
                input_Var4 = int(num4.get())
                input_array = [input_Var1, input_Var2, input_Var3, input_Var4]
                sorted_array = Select_sort(input_array)
            result.set(sorted_array)
        except ValueError:
            messagebox.showerror(title="Error",message="กรุณาป้อนตัวเลข")
    
    Select_label1=Button(windowSelect,text="Number 1",font = 15,fg="black",bg="#EFEFEF") 
    Select_label1.place(x=30,y=150,width=130,height=40)
    
    num1 = StringVar()
    num1.set("")
    txtSelect1 = Entry(windowSelect,font=2,width = 25,bg="#BFC2BF",textvariable=num1)
    txtSelect1.place(x=190,y=150,width=270,height=40)

    Select_label2=Button(windowSelect,text="Number 2",font = 15,fg="black",bg="#EFEFEF") 
    Select_label2.place(x=30,y=220,width=130,height=40)
    
    num2 = StringVar()
    num2.set("")
    txtSelect2 = Entry(windowSelect,font=2,width = 25,bg="#BFC2BF",textvariable=num2)
    txtSelect2.place(x=190,y=220,width=270,height=40)

    Select_label3=Button(windowSelect,text="Number 3",font = 15,fg="black",bg="#EFEFEF") 
    Select_label3.place(x=30,y=290,width=130,height=40)
    
    num3 = StringVar()
    num3.set("")
    txtSelect3 = Entry(windowSelect,font=2,width = 25,bg="#BFC2BF",textvariable=num3)
    txtSelect3.place(x=190,y=290,width=270,height=40)

    Select_label4=Button(windowSelect,text="Number 4",font = 15,fg="black",bg="#EFEFEF") 
    Select_label4.place(x=30,y=360,width=130,height=40)
    
    num4 = StringVar()
    num4.set("")
    txtSelect4 = Entry(windowSelect,font=2,width = 25,bg="#BFC2BF",textvariable=num4)
    txtSelect4.place(x=190,y=360,width=270,height=40)

    Select_label5=Button(windowSelect,text="Result",font=1,fg="black",bg="#339DA6")
    Select_label5.place(x=30,y=430,width=130,height=40)
    result = StringVar()
    result.set("")
    txtSelect5 = Entry(windowSelect,font=2,width = 25,textvariable=result)
    txtSelect5["state"] = "readonly"
    txtSelect5.place(x=190,y=430,width=270,height=40)

    Select_btCal = Button(windowSelect,text="Compute",font=2,bg="#36B7DA",bd=5,command=calculate_Select_sort)
    Select_btCal.place(x=110,y=580,width=100,height=40)
    
    Select_btCancel = Button(windowSelect,text="Cancle",font = 102,bg="#FC5658",bd=5,command = menuclear)
    Select_btCancel.place(x=300,y=580,width=100,height=40)

    Select_btStep = Button(windowSelect,text="Work process",font = 102,bg="#FCD24F",bd=5,command = Procedure_Select)
    Select_btStep.place(x=180,y=510,width=160,height=50)
    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitSelect)
    windowSelect.config(menu=myMenu)
    windowSelect.mainloop()

def Merge_sort(): 
    windowMerg = Toplevel(window) 
    windowMerg.title("แบบรวม") 
    windowMerg.configure(background="#DCDCDC")  
    windowMerg.geometry("495x700+520+40")
    index_Merge_image = PhotoImage(file="D:\Datastructure\Image\Merge.png") 
    Merge_label = Label(windowMerg, image=index_Merge_image)
    Merge_label.place(relwidth=1.0, relheight=1.0)
    def menuExitMerge(): 
        windowMerg.destroy()
    def Work_Merge_proces() :
        windowMerge2 = Toplevel(window) 
        windowMerge2.title("ขั้นตอนการทำงานแบบรวม") 
        windowMerge2.configure(background="#FFFFFF")  
        windowMerge2.geometry("1080x608+250+100")

        index_Merge_image = PhotoImage(file="D:\Datastructure\Image\Stepmerge1.png") 
        proces_Merge_label = Label(windowMerge2, image=index_Merge_image)
        proces_Merge_label.place(relwidth=1.0, relheight=1.0)

        def menuExit_proces_Merge(): 
            windowMerge2.destroy()
        Merge_Button = Button(windowMerge2,text="<",font = 102,bg="#FCD24F",bd=5,command = menuExit_proces_Merge)
        Merge_Button.place(x=500,y=460,width=90,height=40)
        windowMerge2.mainloop()

    def Procedure_Merge(): 
        windowMerge1 = Toplevel(window) 
        windowMerge1.title("ขั้นตอนการทำงานแบบรวม") 
        windowMerge1.configure(background="#DCDCDC")  
        windowMerge1.geometry("1080x608+250+100") 
        index_Merge_image = PhotoImage(file="D:\Datastructure\Image\Stepmerge.png") 
        Procedure_Merge_label = Label(windowMerge1, image=index_Merge_image)
        Procedure_Merge_label.place(relwidth=1.0, relheight=1.0)
        def menuExit_Procedure_Merge(): 
            windowMerge1.destroy()
        Merge_Button1 = Button(windowMerge1,text=">",font = 102,bg="#FCD24F",bd=5,command = Work_Merge_proces)
        Merge_Button1.place(x=500,y=460,width=90,height=40)
        myMenu = Menu()
        myMenu.add_command(label="Exit",command=menuExit_Procedure_Merge)
        windowMerge1.config(menu=myMenu)
        windowMerge1.mainloop()

    def menuclear():
        num1.set("")
        num2.set("")
        num3.set("")
        num4.set("")
        result.set("")

    def merge_sort(arrint):
        
        if len(arrint) <= 1:
            return arrint
        mid = len(arrint) // 2

        left, right = merge_sort(arrint[:mid]), merge_sort(arrint[mid:])

        return merge(left, right, arrint.copy())

    def merge(left, right, merged):
        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left) and right_cursor < len(right):
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor + right_cursor] = left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1

        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]

        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]
        
        return merged

    def calculate_merge_sort():
        try:
            if num1 and num2 and num3 and num4 != "":
                input_Var1 = int(num1.get())
                input_Var2 = int(num2.get())
                input_Var3 = int(num3.get())
                input_Var4 = int(num4.get())
                input_array = [input_Var1, input_Var2, input_Var3, input_Var4]
                sorted_array = merge_sort(input_array)
            result.set(sorted_array)
        except ValueError:
            messagebox.showerror(title="Error",message="กรุณาป้อนตัวเลข")
    
    Merge_label1=Button(windowMerg,text="Number 1",font = 15,fg="black",bg="#EFEFEF") 
    Merge_label1.place(x=30,y=150,width=130,height=40)
    
    num1 = StringVar()
    num1.set("")
    txtMerg1 = Entry(windowMerg,font=2,width = 25,bg="#BFC2BF",textvariable=num1)
    txtMerg1.place(x=190,y=150,width=270,height=40)

    Merge_label2=Button(windowMerg,text="Number 2",font = 15,fg="black",bg="#EFEFEF") 
    Merge_label2.place(x=30,y=220,width=130,height=40)
    
    num2 = StringVar()
    num2.set("")
    txtMerg2 = Entry(windowMerg,font=2,width = 25,bg="#BFC2BF",textvariable=num2)
    txtMerg2.place(x=190,y=220,width=270,height=40)

    Merge_label3=Button(windowMerg,text="Number 3",font = 15,fg="black",bg="#EFEFEF") 
    Merge_label3.place(x=30,y=290,width=130,height=40)
    
    num3 = StringVar()
    num3.set("")
    txtMerg3 = Entry(windowMerg,font=2,width = 25,bg="#BFC2BF",textvariable=num3)
    txtMerg3.place(x=190,y=290,width=270,height=40)

    Merge_label4=Button(windowMerg,text="Number 4",font = 15,fg="black",bg="#EFEFEF") 
    Merge_label4.place(x=30,y=360,width=130,height=40)
    
    num4 = StringVar()
    num4.set("")
    txtMerg4 = Entry(windowMerg,font=2,width = 25,bg="#BFC2BF",textvariable=num4)
    txtMerg4.place(x=190,y=360,width=270,height=40)

    Merge_label5=Button(windowMerg,text="Result",font=1,fg="black",bg="#339DA6")
    Merge_label5.place(x=30,y=430,width=130,height=40)

    result = StringVar()
    result.set("")
    txtMerg5 = Entry(windowMerg,font=2,width = 25,textvariable=result)
    txtMerg5["state"] = "readonly"
    txtMerg5.place(x=190,y=430,width=270,height=40)

    Merge_btCal = Button(windowMerg,text="Compute",font=2,bg="#36B7DA",bd=5,command=calculate_merge_sort)
    Merge_btCal.place(x=110,y=580,width=100,height=40)
    
    Merge_btCancel = Button(windowMerg,text="Cancel",font = 102,bg="#FC5658",bd=5,command = menuclear)
    Merge_btCancel.place(x=300,y=580,width=100,height=40)

    Merge_btStep = Button(windowMerg,text="Work process",font = 102,bg="#FCD24F",bd=5,command = Procedure_Merge)
    Merge_btStep.place(x=180,y=510,width=160,height=50)
    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitMerge)
    windowMerg.config(menu=myMenu)

    windowMerg.mainloop()

def Sequen_search(): 
    windowSequen = Toplevel(window) 
    windowSequen.title("แบบลำดับ") 
    windowSequen.configure(background="#DCDCDC")  
    windowSequen.geometry("800x450+380+160")
    index_Sequen_image = PhotoImage(file="D:\Datastructure\Image\Sequen.png") 
    Sequen_label = Label(windowSequen, image=index_Sequen_image)
    Sequen_label.place(relwidth=1.0, relheight=1.0)

    def menuExitSequan(): 
        windowSequen.destroy()
    def Work_Sequen_proces() :
        windowSequen2 = Toplevel(window) 
        windowSequen2.title("ขั้นตอนการทำงานแบบลำดับ") 
        windowSequen2.configure(background="#FFFFFF")  
        windowSequen2.geometry("1080x608+250+100")
        index_Sequan_image = PhotoImage(file="D:\Datastructure\Image\StepSequen1.png") 
        proces_Sequan_label = Label(windowSequen2, image=index_Sequan_image)
        proces_Sequan_label.place(relwidth=1.0, relheight=1.0)

        def menuExit_proces_Sequen(): 
            windowSequen2.destroy()
        Sequen_Button = Button(windowSequen2,text="<",font = 102,bg="#FCD24F",bd=5,command = menuExit_proces_Sequen)
        Sequen_Button.place(x=500,y=470,width=90,height=40)
        windowSequen2.mainloop()
    def Procedure_Sequen(): 
        windowSequen1 = Toplevel(window) 
        windowSequen1.title("ขั้นตอนการทำงานแบบลำดับ") 
        windowSequen1.configure(background="#DCDCDC")  
        windowSequen1.geometry("1080x608+250+100")
        index_Sequen_image = PhotoImage(file="D:\Datastructure\Image\StepSequen.png") 
        Procedure_Sequen_label = Label(windowSequen1, image=index_Sequen_image)
        Procedure_Sequen_label.place(relwidth=1.0, relheight=1.0)
        def menuExit_Procedure_Sequen(): 
            windowSequen1.destroy()
        Sequen_Button1 = Button(windowSequen1,text=">",font = 102,bg="#FCD24F",bd=5,command = Work_Sequen_proces)
        Sequen_Button1.place(x=500,y=460,width=90,height=40)
        myMenu = Menu()
        myMenu.add_command(label="Exit",command=menuExit_Procedure_Sequen)
        windowSequen1.config(menu=myMenu)
        windowSequen1.mainloop()

    def menuclear():
        num1.set("")
        result.set("")

    def Sequen(arrayInt, target):
 
        for i, item in enumerate(arrayInt):
            if item == target:
                return i  
        return -1  


    def calculate_Sequen_search():
        try:
            if num1 != "":
                input_Var1 = int(num1.get())
                sorted_array = Sequen(arrayInt,input_Var1)

            if sorted_array != -1:
                result.set(f"Element {input_Var1} found at index {sorted_array}")
            else:
                result.set(f"Element {input_Var1} not found in the list")
        except ValueError:
            messagebox.showerror(title="Error",message="กรุณาป้อนตัวเลข")
    
    Sequen_label1=Button(windowSequen,text="Number to search",font = 15,fg="black",bg="#EFEFEF") 
    Sequen_label1.place(x=90,y=160,width=200,height=40)
        
    num1 = StringVar()
    num1.set("")
    txtSequen1 = Entry(windowSequen,font=2,width = 25,bg="#BFC2BF",textvariable=num1)
    txtSequen1.place(x=330,y=160,width=370,height=40)

    Sequen_label2=Button(windowSequen,text="Result",font=1,fg="black",bg="#339DA6")
    Sequen_label2.place(x=90,y=230,width=200,height=40)
    result = StringVar()
    result.set("")
    txtSequen2 = Entry(windowSequen,font=2,width = 25,textvariable=result)
    txtSequen2["state"] = "readonly"
    txtSequen2.place(x=330,y=230,width=370,height=40)

    Sequen_btCal = Button(windowSequen,text="Compute",font=2,bg="#36B7DA",bd=5,command = calculate_Sequen_search)
    Sequen_btCal.place(x=250,y=370,width=100,height=40)
        
    Sequen_btCancel = Button(windowSequen,text="Cancel",font = 102,bg="#FC5658",bd=5,command = menuclear)
    Sequen_btCancel.place(x=440,y=370,width=100,height=40)

    Sequen_btStep = Button(windowSequen,text="Work process",font = 102,bg="#FCD24F",bd=5,command = Procedure_Sequen)
    Sequen_btStep.place(x=320,y=300,width=150,height=50)

    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitSequan)
    windowSequen.config(menu=myMenu)
    windowSequen.mainloop()

def Binary_search(): 
    windowBinary = Toplevel(window) 
    windowBinary.title("แบบทวิภาค") 
    windowBinary.configure(background="#DCDCDC")  
    windowBinary.geometry("800x450+380+160")
    index_Binary_image = PhotoImage(file="D:\Datastructure\Image\Binary.png") 
    Binary_label = Label(windowBinary, image=index_Binary_image)
    Binary_label.place(relwidth=1.0, relheight=1.0)

    def menuExitBinary(): 
        windowBinary.destroy()
    def Work_Binary_proces() :
        windowBinary2 = Toplevel(window) 
        windowBinary2.title("ขั้นตอนการทำงานแบบทวิภาค") 
        windowBinary2.configure(background="#FFFFFF")  
        windowBinary2.geometry("1080x608+250+100")
        index_Binary_image = PhotoImage(file="D:\Datastructure\Image\Stepbinary1.png") 
        proces_Binary_label = Label(windowBinary2, image=index_Binary_image)
        proces_Binary_label.place(relwidth=1.0, relheight=1.0)
        def menuExit_proces_Binary(): 
            windowBinary2.destroy()
        Binary_Button = Button(windowBinary2,text=" < ",font = 102,bg="#FCD24F",bd=5,command = menuExit_proces_Binary)
        Binary_Button.place(x=500,y=460,width=90,height=40)
        windowBinary2.mainloop()

    def Procedure_Binary(): 
        windowBinary1 = Toplevel(window) 
        windowBinary1.title("ขั้นตอนการทำงานแบบทวิภาค") 
        windowBinary1.configure(background="#DCDCDC")  
        windowBinary1.geometry("1080x608+250+100") 
        index_Binary_image = PhotoImage(file="D:\Datastructure\Image\Stepbinary.png") 
        Procedure_Binary_label = Label(windowBinary1, image=index_Binary_image)
        Procedure_Binary_label.place(relwidth=1.0, relheight=1.0)
        def menuExit_Procedure_Binary(): 
            windowBinary1.destroy()
        Binary_Button1 = Button(windowBinary1,text=" > ",font = 102,bg="#FCD24F",bd=5,command = Work_Binary_proces)
        Binary_Button1.place(x=500,y=460,width=90,height=40)
        myMenu = Menu()
        myMenu.add_command(label="Exit",command=menuExit_Procedure_Binary)
        windowBinary1.config(menu=myMenu)
        windowBinary1.mainloop()

    def menuclear():
        num1.set("")
        result.set("")

    def Binary(arrayInt, low, high, x):
        
        if high >= low:
    
            mid = (high + low) // 2
    
            if arrayInt[mid] == x[0]:    
                return mid
    
            elif arrayInt[mid] > x[0]:
                return Binary(arrayInt, low, mid - 1, x)
    
            else:
                return Binary(arrayInt, mid + 1, high, x)
    
        else:

            return -1

    def calculate_Bainary_search():
        try:
            if num1 != "":
                input_Var1 = int(num1.get())
                input_array = [input_Var1]
                sorted_array = Binary(arrayInt, 0, len(arrayInt)-1,input_array)

            if sorted_array != -1:
                result.set("Element is present at index " + str(sorted_array))
            else:
                result.set("Element is not present in array")
        except ValueError:
            messagebox.showerror(title="Error",message="กรุณาป้อนตัวเลข")        

    
    Binary_label=Button(windowBinary,text="Number to search",font = 15,fg="black",bg="#EFEFEF") 
    Binary_label.place(x=90,y=160,width=200,height=40)
        
    num1 = StringVar()
    num1.set("")
    txtBinary = Entry(windowBinary,font=2,width = 25,bg="#BFC2BF",textvariable=num1)
    txtBinary.place(x=330,y=160,width=370,height=40)

    Binary_label1=Button(windowBinary,text="Result",font=1,fg="black",bg="#339DA6")
    Binary_label1.place(x=90,y=230,width=200,height=40)
    result = StringVar()
    result.set("")
    txtBinary1 = Entry(windowBinary,font=2,width = 25,textvariable=result)
    txtBinary1["state"] = "readonly"
    txtBinary1.place(x=330,y=230,width=370,height=40)

    Binary_btCal = Button(windowBinary,text="Compute",font=2,bg="#36B7DA",bd=5,command = calculate_Bainary_search)
    Binary_btCal.place(x=250,y=370,width=100,height=40)
        
    Binary_btCancel = Button(windowBinary,text="Cancel",font = 102,bg="#FC5658",bd=5,command = menuclear)
    Binary_btCancel.place(x=440,y=370,width=100,height=40)

    Binary_btStep = Button(windowBinary,text="Work process",font = 102,bg="#FCD24F",bd=5,command = Procedure_Binary)
    Binary_btStep.place(x=320,y=300,width=150,height=50)

    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitBinary)
    windowBinary.config(menu=myMenu)
    windowBinary.mainloop()

def menuInfo():
    windowInfo = Toplevel(window)
    windowInfo.title("ผู้จัดทำ")
    windowInfo.geometry("1080x608+250+100")
    windowInfo.configure(background="#FF7256")
    index_image = PhotoImage(file="D:/Datastructure/Image/start2.png") 
    index_label = Label(windowInfo, image=index_image) 
    index_label.place(relwidth=1.0, relheight=1.0)
    def menuExitInfo(): 
        windowInfo.destroy()

    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitInfo)
    windowInfo.config(menu=myMenu)

    windowInfo.mainloop()

def Sorting():
    windowSorting = Toplevel(window)
    windowSorting.title("การเรียงลำดับข้อมูล")
    windowSorting.geometry("1080x608+250+100")
    windowSorting.configure(background="#FF7256")
    index_image = PhotoImage(file="D:\Datastructure\Image\sorting.png") 
    index_label = Label(windowSorting, image=index_image)
    index_label.place(relwidth=1.0, relheight=1.0)
    def menuExitSorting(): 
        windowSorting.destroy() 
    
    btCal = Button(windowSorting,text="Bubble sort",font=2,bd=10,bg="#FCD24F",height = 1,width = 15,command=Bubble_sort)
    btCal.place(x=420,y=160,width=250,height=70)

    btCal = Button(windowSorting,text="Insertion sort",font=2,bd=10,bg="#FCD24F",height = 1,width = 15,command=Insert_sort)
    btCal.place(x=420,y=240,width=250,height=70)

    btCal = Button(windowSorting,text="Selection sort",font=2,bd=10,bg="#FCD24F",height = 1,width = 15,command=Select_sort)
    btCal.place(x=420,y=320,width=250,height=70)

    btCal = Button(windowSorting,text="Merge Sort",font=2,bd=10,bg="#FCD24F",height = 1,width = 15,command=Merge_sort)
    btCal.place(x=420,y=400,width=250,height=70)

    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitSorting)
    windowSorting.config(menu=myMenu)

    windowSorting.mainloop()
    
def Searching():
    windowSearching = Toplevel(window)
    windowSearching.title("การค้นหาข้อมูล")
    windowSearching.geometry("1080x608+250+100")
    windowSearching.configure(background="#FF7256")
    index_image = PhotoImage(file="D:\Datastructure\Image\Searching.png") 
    index_label = Label(windowSearching, image=index_image) 
    index_label.place(relwidth=1.0, relheight=1.0)
    def menuExitsearching(): 
        windowSearching.destroy() 


    btCal = Button(windowSearching,text="Sequential Search",font=2,bg="#FCD24F",height = 1,width = 15,bd=10,command=Sequen_search)
    btCal.place(x=440,y=230,width=220,height=80)
    btCal = Button(windowSearching,text="Binary Search",font=2,bg="#FCD24F",height = 1,width = 15,bd=10,command=Binary_search)
    btCal.place(x=440,y=340,width=220,height=80)
    
    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitsearching)
    windowSearching.config(menu=myMenu)
    windowSearching.mainloop()
    
def Start():
    def menuExitStart(): 
        windowStart.destroy()
    windowStart = Toplevel(window)
    windowStart.title("โปรเเกรมการทำงาน")
    windowStart.geometry("1080x608+250+100")
    windowStart.configure(background="#FF7256")  
    index_image = PhotoImage(file="D:\Datastructure\Image\exit.png") 
    index_label = Label(windowStart, image=index_image)
    index_label.place(relwidth=1.0, relheight=1.0)

    btCal = Button(windowStart,text="Sorting",font=2,bd=10,bg="#FC5658",height = 2,width = 15,command=Sorting)
    btCal.place(x=440,y=220,width=220,height=80)
    btCal = Button(windowStart,text="Searching",font=2,bd=10,bg="#36B7DA",height = 2,width = 15,command=Searching)
    btCal.place(x=440,y=340,width=220,height=80)

    myMenu = Menu()
    myMenu.add_command(label="Exit",command=menuExitStart)
    windowStart.config(menu=myMenu)

    windowStart.mainloop()

btCal = Button(window,text="Start",font=2,bg="#FCD24F",height = 2,width = 15,bd=10,command=Start)
btCal.place(x=440,y=410,width=200,height=80)
btCal = Button(window,text="Creator",font=2,bg="#33BBFF",height = 1,width = 10,bd=10,command=menuInfo)
btCal.place(x=290,y=430,width=120,height=50)
btCal = Button(window,text="Exit",font=2,bg="#FC5658",height = 1,width = 10,bd=10,command=menuExit)
btCal.place(x=670,y=430,width=120,height=50)

window.mainloop()