import tkinter as tk
from PIL import Image,ImageTk
import datetime
import math
import sqlite3 as db
from tkinter import ttk

import time

"""im=Image.open("data/search.png")
im=im.resize((25,25))
im.save("data/search.png")"""


char="~!@#$%^&*()_+\t`{}[];:\'\"<>?,.-= /|\\1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM\n"
crypt=['75566', '47993', '63571', '82296', '12073', '86026', '92162', '47291', '93283', '77244', '79114', '23463', '83592', '75047', '39909', '71118', '86940', '25677', '18081', '13375', '69320', '16834', '75031', '46116', '18381', '34688', '89309', '78305', '70146', '69069', '26581', '48156', '78392', '22141', '15751', '62499', '43332', '17591', '82819', '39523', '49558', '32659', '50062', '95536', '67652', '50540', '17096', '58772', '54129', '70215', '32404', '63187', '55158', '58191', '11164', '68322', '32539', '22066', '96847', '28251', '99336', '61676', '69941', '81645', '91359', '81609', '42315', '94932', '16451', '27280', '56866', '69164', '61417', '78754', '40682', '16397', '67712', '44575', '68774', '97423', '83049', '17517', '48188', '54692', '22711', '61495', '70324', '66364', '49784', '23487', '90164', '66047', '31200', '50687', '95673','72134','12004']




def encrypt(v):
	global char,crypt

	encrypt_=""

	for l in str(v):

		index=char.find(l)
		encrypt_+=crypt[index]
	
	
	return encrypt_

def decrypt(v):
	global char,crypt
	
	decrypt_=""

	try:
		x=int(v)

		if len(str(v))%5==0:

			dv=int(len(str(v))/5)
			dv3=0

			for i in range(dv):
				dv2=crypt.index(str(v)[dv3:][:5])
				decrypt_+=char[dv2]
				dv3+=5
	except:
		decrypt_=""

	
	return decrypt_








def can_commands(e):

	global state,title,text,te_st,t_st,sel,search,s_st


	if 10<=e.x<=40:
		if 5<=e.y<=35:
			home()



	if 1000-40<=e.x<=1000-10:
		if 5<=e.y<=35:
			logout()


	if state=="home":

		if 415<=e.x<=525:
			if 130<=e.y<=165:
				new_entry()


		cx,cy=415+110+15,130+15

		if cx-15<e.x<cx+15:
			if cy-15-2.5<e.y<cy+15+2.5:

				search.delete(0,tk.END)
				search.insert(0,"Search")
				s_st=0

				view_entries()

		cx,cy=415+110+30+15,130+15

		if cx-15<e.x<cx+15:
			if cy-15-2.5<e.y<cy+15+2.5:
				settings()


	elif state=="new":

		if 820<=e.x<=980:
			if 75<=e.y<=105:

				now=datetime.datetime.now()
				date=str(now.day)+"/"+str(now.month)+"/"+str(now.year)

				title_=encrypt(title.get())
				body=encrypt(text.get("1.0",tk.END))

				if t_st==0:
					title_=""
				if te_st==0:
					body=""

				db_diary=db.connect('data/entry.db')
				cur=db_diary.cursor()

				cur.execute("SELECT MAX(id) FROM entries")
				rows=cur.fetchall()

				v=0
				for row in rows:
					v=row[0]
				if v==None:
					v=1
				else:
					v+=1

				cur.execute("INSERT INTO entries VALUES("+str(v)+",'"+str(title_)+"','"+str(date)+"','"+str(body)+"')")
				db_diary.commit()



				home()

		if 820<=e.x<=980:
			if 115<=e.y<=145:
				title.delete(0,tk.END)
				text.delete("1.0",tk.END)

				title.insert(0,"Entry Title.")
				text.insert(tk.END,"Your entry here.")

				te_st=0
				t_st=0

				

				title.focus_set()

	elif state=="view":

		if 800+10<=e.x<=800+10+30:
			if 35+40<=e.y<=35+40+30:

				title["state"]="normal"
				text["state"]="normal"

				search.delete(0,tk.END)
				search.insert(0,"Search")
				s_st=0

				view_entries()

			if 35+40+40<=e.y<=35+40+30+40:

				title["state"]="normal"
				text["state"]="normal"

				db_diary=db.connect('data/entry.db')
				cur=db_diary.cursor()

				cur.execute("DELETE FROM entries WHERE id="+str(sel))
				db_diary.commit()


				search.delete(0,tk.END)
				search.insert(0,"Search")
				s_st=0

				view_entries()

def manage_entry():
	global t_st,te_st,title,text,state,search,s_st




	if state=="new":

		widget=str(root.focus_get())



		try:
			widget=widget.split(".!")[1]

			if widget=="entry":

				if title.get()=="":
					t_st=0
					title.delete(0, tk.END)
					title.insert(0,"Entry Title.")


				if t_st==0:
					title.icursor(0)
					title["selectbackground"]="#ffffff"
					title["selectforeground"]="#000000"


			elif widget=="text":
				if text.get("1.0",tk.END)=="\n":
					
					te_st=0
					text.delete('1.0', tk.END)
					text.insert(tk.END,"Your entry here.")


				if te_st==0:
					text.mark_set("insert", "1.0")

					text["selectbackground"]="#ffffff"
					text["selectforeground"]="#000000"

		except:
			pass

	elif state=="entries":

		widget=str(root.focus_get())



		try:
			widget=widget.split(".!")[1]


			if widget=="entry2":

				if search.get()=="":
					s_st=0
					search.delete(0, tk.END)
					search.insert(0,"Search.")



				if s_st==0:
					search.icursor(0)
					search["selectbackground"]="#ffffff"
					search["selectforeground"]="#000000"

		except:
			pass

	root.after(1,manage_entry)


def text_keyp(e):
	global text,te_st


	if te_st==0:
		text.delete('1.0', tk.END)

	text["selectbackground"]="#000000"
	text["selectforeground"]="#ffffff"

	te_st=1

def title_keyp(e):
	global title,t_st


	if t_st==0:
		title.delete(0,tk.END)
	title["selectbackground"]="#000000"
	title["selectforeground"]="#ffffff"

	t_st=1



def settings():

	global can,bg,homei,logouti

	state="settings"

	can.delete("all")
	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")

	homei=ImageTk.PhotoImage(file="data/home.png")
	can.create_image(10,5,image=homei,anchor="nw")

	logouti=ImageTk.PhotoImage(file="data/logout.png")
	can.create_image(1000-40,5,image=logouti,anchor="nw")


def view(v):

	global state,bg,can,title,text,cali,homei,logouti,entriesf,backi,bini,sel,search



	sel=v
	state="view"

	entriesf.place_forget()
	search.place_forget()




	db_diary=db.connect('data/entry.db')
	cur=db_diary.cursor()

	cur.execute("SELECT * FROM entries WHERE id="+str(sel)+" ")
	rows=cur.fetchall()

	
	for row in rows:
		t1=decrypt(row[1])
		date=row[2]
		t2=decrypt(row[3])


	




	can.delete("all")

	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")

	homei=ImageTk.PhotoImage(file="data/home.png")
	can.create_image(10,5,image=homei,anchor="nw")

	logouti=ImageTk.PhotoImage(file="data/logout.png")
	can.create_image(1000-40,5,image=logouti,anchor="nw")
	can.create_rectangle(200,35+40,200+600,600-40,fill="#ffffff",outline="#ffffff")

	can.create_line(200,121-3,800,121-3,fill="#999999")
	can.create_line(200,121-3+30,800,121-3+30,fill="#999999")

	title.place(in_=root,x=200+2,y=35+40+2)
	text.place(in_=root,x=200+2,y=148+2+3)

	title.delete(0, tk.END)
	text.delete('1.0', tk.END)
	
	title.insert(0,t1)
	text.insert(tk.END,t2)


	
	
	

	cali=ImageTk.PhotoImage(file="data/calendar.png")

	can.create_image(200+2.5,118+2.5,image=cali,anchor="nw")

	can.create_text(200+30+10,118+15,text=date,font=("FreeMono",13),anchor="w",fill="#000000")

	backi=ImageTk.PhotoImage(file="data/back.png")
	can.create_image(800+10,35+40,image=backi,anchor="nw")

	bini=ImageTk.PhotoImage(file="data/bin.png")
	can.create_image(800+10,35+40+40,image=bini,anchor="nw")

	title["state"]="disabled"
	text["state"]="disabled"


def search_():
	global s_st,search,state,sval,s_st2


	if state=="entries":

		if s_st==1:

			if not search.get()==sval:

				sval=search.get()

				view_entries()
		elif s_st==0:

			if s_st2==0:
				view_entries()

				s_st2=1






	root.after(1,search_)

def view_entries():
	global can,bg,homei,logouti,entries,entries2,entriesf,c_entries,yvar,squarei
	global title,text,searchi,s_st,state,sval

	title.place_forget()
	text.place_forget()
	entriesf.place_forget()

	entries=[]
	db_diary=db.connect('data/entry.db')
	cur=db_diary.cursor()

	cur.execute("SELECT * FROM entries ORDER BY id DESC")
	rows=cur.fetchall()

	
	for row in rows:
		entries.append(row)

	state="entries"

	can.delete("all")
	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")

	homei=ImageTk.PhotoImage(file="data/home.png")
	can.create_image(10,5,image=homei,anchor="nw")

	logouti=ImageTk.PhotoImage(file="data/logout.png")
	can.create_image(1000-40,5,image=logouti,anchor="nw")



	can.create_rectangle(200,35+40,200+600,35+40+100,fill="#ffffff",outline="#ffffff")

	can.create_text(220,35+40+30,text="Dan's Journal.",font=("FreeMono",25),anchor="w")

	can.create_text(800-20,35+40+20,text=str(len(entries))+" entries.",font=("FreeMono",13),anchor="e")


	can.create_arc(220,35+40+100-5-30, 220+10,35+40+100-5-30+10,style="arc",start=90,extent=90,outline="#323232")
	can.create_arc(220,35+40+100-5-10, 220+10,35+40+100-5,style="arc",start=180,extent=90,outline="#323232")

	can.create_arc(220+300-10,35+40+100-5-30, 220+300,35+40+100-5-30+10,style="arc",start=0,extent=90,outline="#323232")
	can.create_arc(220+300-10,35+40+100-5-10, 220+300,35+40+100-5,style="arc",start=270,extent=90,outline="#323232")

	can.create_line(220+5,35+40+100-5-30,220+300-5+1,35+40+100-5-30,fill="#323232")
	can.create_line(220+5,35+40+100-5,220+300-5,35+40+100-5,fill="#323232")

	can.create_line(220,35+40+100-5-30+5, 220,35+40+100-5-5,fill="#323232")
	can.create_line(220+300,35+40+100-5-30+5, 220+300,35+40+100-5-5,fill="#323232")


	searchi=ImageTk.PhotoImage(file="data/search.png")
	can.create_image(220+5,35+40+100-5-30+2.5,image=searchi,anchor="nw")

	search.place(in_=root,x=220+5+25+2.5,y=35+40+100-5-30+2.5)




	can.create_line(200,35+40+100+5,800,35+40+100+5,fill="#ffffff",width=2)


	c_entries["scrollregion"]=(0,0,600-7,0)

	squarei=ImageTk.PhotoImage(file="data/square.png")


	yvar=0

	entries2=[]

	c_entries.delete("all")

	c=0
	for i in entries:



		

		if i[1]=="":
			t1=i[2]
		else:
			t1=decrypt(i[1])[:38]

		if s_st==1:
			if t1.lower().find(sval)==-1:

				if i[2].find(sval)==-1:
					continue

		c+=1
		entries2.append([yvar,i[0]])

		t2=decrypt(i[3]).split("\n")[0][:47]

		if len(decrypt(i[3]).split("\n")[0])>47:
			t2+="..."

		c_entries.create_image(10,yvar+20,image=squarei,anchor="nw")
		


		c_entries.create_text(40,yvar+15,text=t1,font=("FreeMono",13,"bold"),fill="#555555",anchor="w")
		c_entries.create_text(40,yvar+55,text=t2,font=("FreeMono",13),fill="#555555",anchor="sw")

		c_entries.create_text(410,yvar+30,text=i[2],font=("FreeMono",13),fill="#555555",anchor="w")

		c_entries.create_line(0,yvar+60,800-7,yvar+60,fill="#999999")

		yvar+=60



	if yvar>350:
		y=350
	else:
		y=yvar

	entriesf["height"]=y
	c_entries["height"]=y

	c_entries["scrollregion"]=(0,0,600-7,yvar)


	if c>0:

		entriesf.place(in_=root,x=200,y=35+40+100+5+5)
	else:

		can.create_text(500,35+40+100+5+50,text="No entry",fill="#ffffff",font=("FreeMono",20))

	search.focus_set()

def new_entry():
	global state,bg,can,title,text,cali,t_st,te_st,homei,logouti

	state="new"

	can.delete("all")


	title["state"]="normal"
	text["state"]="normal"

	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")

	homei=ImageTk.PhotoImage(file="data/home.png")
	can.create_image(10,5,image=homei,anchor="nw")

	logouti=ImageTk.PhotoImage(file="data/logout.png")
	can.create_image(1000-40,5,image=logouti,anchor="nw")
	can.create_rectangle(200,35+40,200+600,600-40,fill="#ffffff",outline="#ffffff")

	can.create_line(200,121-3,800,121-3,fill="#999999")
	can.create_line(200,121-3+30,800,121-3+30,fill="#999999")

	title.place(in_=root,x=200+2,y=35+40+2)
	text.place(in_=root,x=200+2,y=148+2+3)

	title.delete(0, tk.END)
	text.delete('1.0', tk.END)
	
	title.insert(0,"Entry Title.")
	text.insert(tk.END,"Your entry here.")


	now=datetime.datetime.now()
	date=str(now.day)+"/"+str(now.month)+"/"+str(now.year)
	

	cali=ImageTk.PhotoImage(file="data/calendar.png")

	can.create_image(200+2.5,118+2.5,image=cali,anchor="nw")

	can.create_text(200+30+10,118+15,text=date,font=("FreeMono",13),anchor="w",fill="#000000")

	t_st=0
	te_st=0

	title.focus_set()
	title.icursor(0)


	can.create_oval(800+20,35+40, 800+20+30,35+40+30,fill="#ffffff",outline="#ffffff")
	can.create_oval(800+20+160-30,35+40, 800+20+160,35+40+30,fill="#ffffff",outline="#ffffff")
	can.create_rectangle(800+20+15,35+40, 800+20+160-15,35+40+30, fill="#ffffff",outline="#ffffff")

	can.create_text(800+20+80,35+40+15,text="Save",font=("FreeMono",13))



	can.create_oval(800+20,35+40+40, 800+20+30,35+40+30+40,fill="#ffffff",outline="#ffffff")
	can.create_oval(800+20+160-30,35+40+40, 800+20+160,35+40+30+40,fill="#ffffff",outline="#ffffff")
	can.create_rectangle(800+20+15,35+40+40, 800+20+160-15,35+40+30+40, fill="#ffffff",outline="#ffffff")

	can.create_text(800+20+80,35+40+15+40,text="Clear",font=("FreeMono",13),fill="red")

def home():
	global state,bg,can,writei,listi,settingi,title,text,homei,logouti,entriesf

	title.place_forget()
	text.place_forget()
	entriesf.place_forget()
	search.place_forget()

	state="home"

	can.delete("all")

	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")

	homei=ImageTk.PhotoImage(file="data/home.png")
	can.create_image(10,5,image=homei,anchor="nw")

	logouti=ImageTk.PhotoImage(file="data/logout.png")
	can.create_image(1000-40,5,image=logouti,anchor="nw")



	can.create_rectangle(315+10+40,35+20,315+370, 600-20,fill="#0583d2",outline="#0583d2")

	can.create_oval(315,55, 315+20,55+20, fill="#323232",outline="#323232")
	can.create_oval(315,600-40, 315+20,600-20, fill="#323232",outline="#323232")

	can.create_polygon(315+10,55, 315+10+40,55, 315+10+40,600-20+1, 315+10,600-20+1,
		315,600-30+1, 315,55+10,fill="#323232")

	

	x=(1000-170)/2

	can.create_oval(x,75+20, x+20,75+20+20,fill="#ffffff",outline="#ffffff")
	can.create_oval(x,145+20-20, x+20,145+20,fill="#ffffff",outline="#ffffff")

	can.create_oval(x+170-20,75+20, x+170,75+20+20,fill="#ffffff",outline="#ffffff")
	#can.create_oval(x+170-20,145+20-20, x+170,145+20,fill="#ffffff",outline="#ffffff")

	can.create_polygon(x+10,75+20, x+170-20+10,75+20, x+170,75+20+10,
		x+170,145+20,  x,145+20, x,75+20+10,
		fill="#ffffff",outline="#ffffff")

	can.create_line(x,75+20+35,x+171,75+20+35,fill="#999999")

	can.create_text(x+170/2,75+20+35/2,text="Dan's Journal",font=("FreeMono",13),anchor="c")

	can.create_text(x+30,145+20-35/2,text="New Entry",font=("FreeMono",13),anchor="w")
	can.create_line(x+110,145+20-35,x+110,145+21,fill="#999999")
	can.create_line(x+140,145+20-35,x+140,145+21,fill="#999999")


	writei=ImageTk.PhotoImage(file="data/write.png")
	listi=ImageTk.PhotoImage(file="data/list.png")
	settingi=ImageTk.PhotoImage(file="data/setting.png")


	can.create_image(x+2.5,145+20-35+5,image=writei,anchor="nw")
	can.create_image(x+2.5+110,145+20-35+5,image=listi,anchor="nw")
	can.create_image(x+2.5+110+30,145+20-35+5,image=settingi,anchor="nw")


def _on_mousewheel(e):
	global c_entries,yvar

	if yvar>350:
		c_entries.yview_scroll(int(-1*(e.delta/120)), "units")

def logout():
	pass

bg=()
state=""

t_st=0
te_st=0
writei=()
listi=()
settingi=()
cali=()
homei=()
logouti=()
squarei=()
bini=()
backi=()
searchi=()

entries=[]
entries2=[]

sel=0
sval=""
s_st2=0

root=tk.Tk()

wd=root.winfo_screenwidth()
px=int((wd-1000)/2)

root.geometry("1000x600+"+str(px)+"+0")
root.resizable(0,0)

can=tk.Canvas(width=1000,height=600,relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",can_commands)


title=tk.Entry(width=33,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,
	font=("FreeMono",25),disabledbackground="#ffffff",disabledforeground="#000000"
	,selectbackground="#000000",selectforeground="#ffffff")
title.bind("<KeyPress>",title_keyp)


text=tk.Text(width=66,height=21,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,
	font=("FreeMono",13),selectbackground="#000000",selectforeground="#ffffff")
text.bind("<KeyPress>",text_keyp)
text.config(wrap=tk.WORD)


style=ttk.Style()
style.element_create("My.Vertical.TScrollbar.trough", "from", "clam")
style.element_create("My.Vertical.TScrollbar.thumb", "from", "clam")
style.element_create("My.Vertical.TScrollbar.grip", "from", "clam")

style.layout("My.Vertical.TScrollbar",
   [('My.Vertical.TScrollbar.trough',
     {'children': [('My.Vertical.TScrollbar.thumb',
                    {'unit': '1',
                     'children':
                        [('My.Vertical.TScrollbar.grip', {'sticky': ''})],
                     'sticky': 'nswe'})
                  ],
      'sticky': 'ns'})])


style.configure("My.Vertical.TScrollbar", gripcount=0, background="#666666",
                troughcolor='#eeeeee', borderwidth=0, bordercolor='#eeeeee',
                lightcolor='#eeeeee',relief="flat", darkcolor='#eeeeee',
                arrowsize=7)


def c_entries_comm(e):
	global entries2,c_entries

	


	for i in entries2:
		if i[0]<=c_entries.canvasy(e.y)<=i[0]+60:

			view(i[1])


entriesf=tk.Frame(width=600,height=100,bg="#ffffff")

c_entries=tk.Canvas(entriesf,width=600-7,height=100,bg="#ffffff",relief="flat",highlightthickness=0,border=0)
c_entries.pack(side=tk.LEFT)

c_entries.bind("<Button-1>",c_entries_comm)
c_entries.bind_all("<MouseWheel>",_on_mousewheel)

c_entries["scrollregion"]=(0,0,600-7,100)

entries_bar=ttk.Scrollbar(entriesf,orient=tk.VERTICAL,style="My.Vertical.TScrollbar")

entries_bar.config(command=c_entries.yview)

c_entries.config(yscrollcommand=entries_bar.set)
entries_bar.pack(side=tk.LEFT,fill=tk.Y)

yvar=0


def search_keyp(e):

	global search,s_st,s_st2


	if s_st==0:
		search.delete(0,tk.END)

	search["selectbackground"]="#000000"
	search["selectforeground"]="#ffffff"

	s_st=1
	s_st2=0


s_st=0
search=tk.Entry(width=24,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,
	font=("FreeMono",14),selectbackground="#000000",selectforeground="#ffffff")
search.bind("<KeyPress>",search_keyp)

try:
	db_diary=db.connect('data/entry.db')
	cur=db_diary.cursor()
	cur.execute("""CREATE TABLE entries(
		id INT,
		title VARCHAR(255),
		date_ VARCHAR(255),
		body VARCHAR(255)
		);""")
	db_diary.close()


except:
	pass

home()
manage_entry()
search_()
root.mainloop()

