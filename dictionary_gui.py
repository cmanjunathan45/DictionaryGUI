from PyDictionary import PyDictionary
from tkinter import *
global val,text
tk=Tk()
tk.title("Dictionary App | Manjunathan C")
tk.geometry('400x500')
head=Label(tk,text="Dictionary",font=("Courier",40,"italic"))
head.grid(row=0,columnspan=2)
entry=Entry(tk)
entry.grid(row=1,column=0)
search_button=Button(tk,text="Search",command=lambda:search(entry,result))
search_button.grid(row=1,column=1)
result=Label(tk)
result.grid(row=2,columnspan=2)
def search(entry,result):
	dictionary=PyDictionary()
	try:
		val=dictionary.meaning(entry.get())
		val=val['Noun']
		text=""
		for vals in val:
			text=text+"\n\n"+str(vals) 
		result.configure(text=text,wraplength=300,justify=LEFT,font=("Courier",10,"italic"))
	except:
		result.configure(text="Check The Spelling Of your text \n\tor\nCheck your Connection",wraplength=300,justify=LEFT)
tk.mainloop()
