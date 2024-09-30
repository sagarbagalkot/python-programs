print("U15IG22S0071")
import tkinter as tk
import tkinter.messagebox as msgbox
form=tk.Tk()
form.geometry('500x500')
lblti=tk.Label(form,text="U15IG22S0071",font=("Arial",18,"bold"),fg="red")
lblti.grid(row=0,column=1,sticky=tk.W,padx=10,pady=10)
lbluno=tk.Label(form,text="UUCMSNO")
lbluno.grid(row=1,column=1,sticky=tk.W)
etuno=tk.Entry(form,width=20)
etuno.grid(row=1,column=2,padx=10,pady=5) 

lblname=tk.Label(form,text="NAME")
lblname.grid(row=2,column=1,sticky=tk.W)
etname=tk.Entry(form,width=20)
etname.grid(row=2,column=2,padx=10,pady=5)

lblgender=tk.Label(form,text="gender")
lblgender.grid(row=3,column=2,sticky=tk.W)
gendervar=tk.StringVar()
gendervar.set("male")
rdbmale=tk.Radiobutton(form,variable=gendervar,value="male",text="male")
rdbfemale=tk.Radiobutton(form,variable=gendervar,value="female",text="female")
rdbmale.grid(row=3,column=2,padx=10,pady=5)
rdbfemale.grid(row=3,column=3,padx=20,pady=5)

lblnotify=tk.Label(form,text="Notification want to recive through")
lblnotify.grid(row=4,column=1,sticky=tk.W)
wappvar=tk.BooleanVar()
chkbwapp=tk.Checkbutton(form,text="WhatsApp",variable=wappvar)
emailvar=tk.BooleanVar()
chkbemail=tk.Checkbutton(form,text="Email",variable=emailvar)
chkbwapp.grid(row=4,column=2,padx=10,pady=5)
chkbemail.grid(row=4,column=3,padx=10,pady=5)

def save():
    uno=etuno.get()
    name=etname.get()
    gender=gendervar.get()
    wapp=wappvar.get()
    email=emailvar.get()
    row=f"UUCMSNO={uno} name={name} gender={gender}"
    if wapp:
        row=row+"notification through whatsapp"
        if email:
            row=row+"and email"
    file=open("student.cvs","a")
    file.write(row)
    file.close()
    msgbox.showinfo("message","data saved successfully")
btnsave=tk.Button(form,text="save",command=save)
btnsave.grid(row=5,columnspan=3,padx=50,pady=20)
form.mainloop()