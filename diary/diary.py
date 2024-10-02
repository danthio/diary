import tkinter as tk
from PIL import Image,ImageTk
import datetime
import math
import sqlite3 as db
from tkinter import ttk
import time




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
		#x=int(v)

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

	global can,state,title,text,te_st,t_st,sel,search,s_st
	global show_st,pw,pw2,un,pst1,pst,pim

	global user_id_,user_name_

	if 10<=e.x<=40:
		if 5<=e.y<=35:
			home()
			un.place_forget()
			pw.place_forget()



	if 1000-40<=e.x<=1000-10:
		if 5<=e.y<=35:
			pst=0
			un.delete(0,tk.END)
			pw.delete(0,tk.END)
			un.place_forget()
			pw.place_forget()

			logout()


	if state=="profile":
		


		if 641<=e.x<=670:
			if 285<=e.y<=314:

				if pst==0:
					pst=1
				elif pst==1:
					pst=0

				if pst==0:
					can.delete(pst1)

					pim=ImageTk.PhotoImage(file="data/show.png")
					pst1=can.create_image(641,285,image=pim,anchor="nw")
					pw["show"]="*"
				elif pst==1:
					can.delete(pst1)
					pim=ImageTk.PhotoImage(file="data/dshow.png")
					pst1=can.create_image(641,285,image=pim,anchor="nw")
					pw["show"]=""



		con=0

		if 430<=e.x<=570:
			if 340<=e.y<=370:
				con=1

		cx,cy=430,355

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:
			con=1


		cx,cy=570,355

		r=math.sqrt((e.x-cx)**2+(e.y-cy)**2)

		if r<=15:
			con=1

		if con==1:

			if un.get()=="" or pw.get()=="":

				message(500,300+100+40,"Fill all details!",0)
				return


			db_user=db.connect('data/user.db')
			cur=db_user.cursor()

			cur.execute("SELECT * FROM user")
			rows=cur.fetchall()

			con=0

			for row in rows:

				if row[0]==user_id_:
					continue

				un_=decrypt(row[1])

				if u==un_:
					con=1

			if con==1:
				message(500,300+100+40,"User name exists!",0)
				return


			db_user=db.connect('data/user.db')
			cur=db_user.cursor()
			cur.execute("UPDATE user SET user_name='"+str(encrypt(un.get()))+"' WHERE user_id="+str(user_id_))
			cur.execute("UPDATE user SET password='"+str(encrypt(pw.get()))+"' WHERE user_id="+str(user_id_))
			db_user.commit()

			message(500,300+100+40,"Detail saved!",1)

			user_name_=un.get()



			un.delete(0,tk.END)
			pw.delete(0,tk.END)

			un.place_forget()
			pw.place_forget()

			home()
			pst=0


	elif state=="create_account":

		cx,cy=375+15,375+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			un.delete(0,tk.END)
			pw.delete(0,tk.END)
			pw2.delete(0,tk.END)

			un.place_forget()
			pw.place_forget()			
			pw2.place_forget()

			login()

			return


		cx,cy=475-15,375+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			un.delete(0,tk.END)
			pw.delete(0,tk.END)
			pw2.delete(0,tk.END)

			un.place_forget()
			pw.place_forget()			
			pw2.place_forget()

			login()

			return

		if 375+15<=e.x<=475-15:
			if 375<=e.y<=405:

				un.delete(0,tk.END)
				pw.delete(0,tk.END)
				pw2.delete(0,tk.END)

				un.place_forget()
				pw.place_forget()			
				pw2.place_forget()

				login()

				return














		cx,cy=525+15,375+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			create_account2()

			return


		cx,cy=625-15,375+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			create_account2()

			return

		if 525+15<=e.x<=625-15:
			if 375<=e.y<=405:

				create_account2()

				return


	elif state=="login":


		if 638<=e.x<=638+29:
			if 261<=e.y<=261+29:

				if show_st==0:
					show_st=1
				elif show_st==1:
					show_st=0

				login()
				pw.focus_set()
				return



		cx,cy=410+15,325+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			validate()
			return

		cx,cy=590-15,325+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			validate()
			return




		if 410+15<=e.x<=590-15:
			if 325<=e.y<=355:
				validate()
				return


		if 332<=e.x<=452:
			if 385<=e.y<=405:
				create_account()
				return








	elif state=="home":

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
				profile()


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

				cur.execute("INSERT INTO entries VALUES("+str(user_id_)+","+str(v)+",'"+str(title_)+"','"+str(date)+"','"+str(body)+"')")
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



		cx,cy=800+10+15,35+40+15-5

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			title["state"]="normal"
			text["state"]="normal"

			search.delete(0,tk.END)
			search.insert(0,"Search")
			s_st=0

			view_entries()


		cx,cy=800+10+15,35+40+40+15-5

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:

			title["state"]="normal"
			text["state"]="normal"

			db_diary=db.connect('data/entry.db')
			cur=db_diary.cursor()

			cur.execute("DELETE FROM entries WHERE id="+str(sel)+" AND user_id="+str(user_id_))
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





pst1=0
pst=0

pim=0

def profile():

	global state,can,bg,homei,logouti,pw,un
	global user_id_,pst1,pst,pim

	state="profile"

	can.delete("all")
	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")


	homei=ImageTk.PhotoImage(file="data/home.png")
	can.create_image(10,5,image=homei,anchor="nw")

	logouti=ImageTk.PhotoImage(file="data/logout.png")
	can.create_image(1000-40,5,image=logouti,anchor="nw")





	can.create_oval(500-180,300-100, 500-180+20,300-100+20,fill="#ffffff",outline="#ffffff")
	can.create_oval(500+180-20,300-100,500+180,300-100+20,fill="#ffffff",outline="#ffffff")

	can.create_oval(500-180,300+100-20, 500-180+20,300+100,fill="#ffffff",outline="#ffffff")
	can.create_oval(500+180-20,300+100-20,500+180,300+100,fill="#ffffff",outline="#ffffff")

	can.create_polygon(500-180+10,300-100, 500+180-10,300-100, 500+180,300-100+10, 500+180,300+100-10,
		500+180-10,300+100, 500-180+10,300+100, 500-180,300+100-10, 500-180,300-100+10,fill="#ffffff",outline="#ffffff")




	can.create_text(500-180+30,300-100+30+20,text="User Name",font=("FreeMono",13),anchor="w")


	can.create_text(500-180+30,300-100+30+20+50,text="Password",font=("FreeMono",13),anchor="w")




	can.create_arc(500-180+150-3,300-100+30+10-3, 500-180+150-3+10,300-100+30+10-3+10,start=90,extent=90,style="arc")
	can.create_arc(500-180+150-3,300-100+30+10-3+16, 500-180+150-3+10,300-100+30+10-3+10+16,start=180,extent=90,style="arc")

	can.create_arc(500-180+150-3+200-40-1,300-100+30+10-3, 500-180+150-3+10+200-40-1,300-100+30+10-3+10,start=0,extent=90,style="arc")
	can.create_arc(500-180+150-3+200-40-1,300-100+30+10-3+16, 500-180+150-3+10+200-40-1,300-100+30+10-3+10+16,start=270,extent=90,style="arc")

	can.create_line(500-180+150-3+5,300-100+30+10-3, 500-180+150-3+10+200-40-1-5+1,300-100+30+10-3)
	can.create_line(500-180+150-3+5,300-100+30+10-3+10+16, 500-180+150-3+10+200-40-1-5,300-100+30+10-3+10+16)

	can.create_line(500-180+150-3,300-100+30+10-3+5, 500-180+150-3,300-100+30+10-3+10+16-5)
	can.create_line(500-180+150-3+10+200-40-1,300-100+30+10-3+5, 500-180+150-3+10+200-40-1,300-100+30+10-3+10+16-5)



	can.create_arc(500-180+150-3,300-100+30+10-3+50, 500-180+150-3+10,300-100+30+10-3+10+50,start=90,extent=90,style="arc")
	can.create_arc(500-180+150-3,300-100+30+10-3+16+50, 500-180+150-3+10,300-100+30+10-3+10+16+50,start=180,extent=90,style="arc")

	can.create_arc(500-180+150-3+200-40-1,300-100+30+10-3+50, 500-180+150-3+10+200-40-1,300-100+30+10-3+10+50,start=0,extent=90,style="arc")
	can.create_arc(500-180+150-3+200-40-1,300-100+30+10-3+16+50, 500-180+150-3+10+200-40-1,300-100+30+10-3+10+16+50,start=270,extent=90,style="arc")

	can.create_line(500-180+150-3+5,300-100+30+10-3+50, 500-180+150-3+10+200-40-1-5+1,300-100+30+10-3+50)
	can.create_line(500-180+150-3+5,300-100+30+10-3+10+16+50, 500-180+150-3+10+200-40-1-5,300-100+30+10-3+10+16+50)

	can.create_line(500-180+150-3,300-100+30+10-3+5+50, 500-180+150-3,300-100+30+10-3+10+16-5+50)
	can.create_line(500-180+150-3+10+200-40-1,300-100+30+10-3+5+50, 500-180+150-3+10+200-40-1,300-100+30+10-3+10+16-5+50)


	#641 285 670 314

	un.delete(0,tk.END)
	pw.delete(0,tk.END)



	db_user=db.connect("data/user.db")
	cur=db_user.cursor()
	cur.execute("SELECT * FROM user WHERE user_id="+str(user_id_))
	rows=cur.fetchall()

	for row in rows:

		uname=decrypt(row[1])
		pword=decrypt(row[2])



	un.insert(tk.END,uname)
	pw.insert(tk.END,pword)

	un.place(in_=root,x=500-180+150,y=300-100+30+10)
	pw.place(in_=root,x=500-180+150,y=300-100+30+10+50)

	un.focus_set()



	if pst==0:
		can.delete(pst1)

		pim=ImageTk.PhotoImage(file="data/show.png")
		pst1=can.create_image(641,285,image=pim,anchor="nw")
		pw["show"]="*"
	elif pst==1:
		can.delete(pst1)
		pim=ImageTk.PhotoImage(file="data/dshow.png")
		pst1=can.create_image(641,285,image=pim,anchor="nw")
		pw["show"]=""




	can.create_oval(500-70-15,300+100-30-30,500-70+15,300+100-30,fill="#000000",outline="#000000")
	can.create_oval(500+70-15,300+100-30-30,500+70+15,300+100-30,fill="#000000",outline="#000000")
	can.create_rectangle(500-70,300+100-30-30, 500+70,300+100-30,fill="#000000",outline="#000000")

	can.create_text(500,300+100-30-15,text="Save",font=("FreeMono",13),fill="#ffffff")




def view(v):

	global state,bg,can,title,text,cali,homei,logouti,entriesf,backi,bini,sel,search,user_id_



	sel=v
	state="view"

	entriesf.place_forget()
	search.place_forget()




	db_diary=db.connect('data/entry.db')
	cur=db_diary.cursor()

	cur.execute("SELECT * FROM entries WHERE id="+str(sel)+" AND user_id="+str(user_id_))
	rows=cur.fetchall()

	
	for row in rows:
		t1=decrypt(row[2])
		date=row[3]
		t2=decrypt(row[4])



	




	can.delete("all")

	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")


	homei=ImageTk.PhotoImage(file="data/home.png")
	can.create_image(10,5,image=homei,anchor="nw")

	logouti=ImageTk.PhotoImage(file="data/logout.png")
	can.create_image(1000-40,5,image=logouti,anchor="nw")




	can.create_oval(200-5,35+40-5, 200+5,35+40+5,fill="#ffffff",outline="#ffffff")
	can.create_oval(200-5,600-40-5, 200+5,600-40+5,fill="#ffffff",outline="#ffffff")

	can.create_oval(200+600-5,35+40-5, 200+600+5,35+40+5,fill="#ffffff",outline="#ffffff")
	can.create_oval(200+600-5,600-40-5, 200+600+5,600-40+5,fill="#ffffff",outline="#ffffff")

	can.create_polygon(200,35+40-5, 200+600,35+40-5, 200+600+5,35+40, 200+600+5,600-40,
	200+600,600-40+5, 200,600-40+5, 200-5,600-40, 200-5,35+40,fill="#ffffff",outline="#ffffff"  )


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
	can.create_image(800+10,35+40-5,image=backi,anchor="nw")

	bini=ImageTk.PhotoImage(file="data/bin.png")
	can.create_image(800+10,35+40+40-5,image=bini,anchor="nw")

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
	global title,text,searchi,s_st,state,sval,user_id_,user_name_

	title.place_forget()
	text.place_forget()
	entriesf.place_forget()

	entries=[]
	db_diary=db.connect('data/entry.db')
	cur=db_diary.cursor()

	cur.execute("SELECT * FROM entries WHERE user_id="+str(user_id_)+" ORDER BY id DESC")
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


	can.create_oval(200,35+40, 200+10,35+40+10,fill="#ffffff",outline="#ffffff")
	can.create_oval(200+600-10,35+40, 200+600,35+40+10,fill="#ffffff",outline="#ffffff")
	can.create_rectangle(200+5,35+40, 200+600-5,35+40+5,fill="#ffffff",outline="#ffffff")
	can.create_rectangle(200,35+40+5,200+600,35+40+100,fill="#ffffff",outline="#ffffff")


	un=user_name_.lower()
	un=un[0].upper()+un[1:]

	can.create_text(220,35+40+30,text=str(un)+"'s Journal.",font=("FreeMono",25),anchor="w")

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
			t1=i[3]
		else:
			t1=decrypt(i[2])[:38]

		if s_st==1:
			if t1.lower().find(sval)==-1:

				if i[3].find(sval)==-1:
					continue

		c+=1
		entries2.append([yvar,i[1]])

		t2=decrypt(i[4]).split("\n")[0][:47]

		if len(decrypt(i[4]).split("\n")[0])>47:
			t2+="..."

		c_entries.create_image(10,yvar+20,image=squarei,anchor="nw")
		


		c_entries.create_text(40,yvar+15,text=t1,font=("FreeMono",13,"bold"),fill="#555555",anchor="w")
		c_entries.create_text(40,yvar+55,text=t2,font=("FreeMono",13),fill="#555555",anchor="sw")

		c_entries.create_text(410,yvar+30,text=i[3],font=("FreeMono",13),fill="#555555",anchor="w")

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

	can.create_oval(200-5,35+40-5, 200+5,35+40+5,fill="#ffffff",outline="#ffffff")
	can.create_oval(200-5,600-40-5, 200+5,600-40+5,fill="#ffffff",outline="#ffffff")

	can.create_oval(200+600-5,35+40-5, 200+600+5,35+40+5,fill="#ffffff",outline="#ffffff")
	can.create_oval(200+600-5,600-40-5, 200+600+5,600-40+5,fill="#ffffff",outline="#ffffff")

	can.create_polygon(200,35+40-5, 200+600,35+40-5, 200+600+5,35+40, 200+600+5,600-40,
	200+600,600-40+5, 200,600-40+5, 200-5,600-40, 200-5,35+40,fill="#ffffff",outline="#ffffff"  )



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


	can.create_oval(800+20,35+40, 800+20+30,35+40+30,fill="#000000",outline="#000000")
	can.create_oval(800+20+160-30,35+40, 800+20+160,35+40+30,fill="#000000",outline="#000000")
	can.create_rectangle(800+20+15,35+40, 800+20+160-15,35+40+30, fill="#000000",outline="#000000")

	can.create_text(800+20+80,35+40+15,text="Save",font=("FreeMono",13),fill="#ffffff")



	can.create_oval(800+20,35+40+40, 800+20+30,35+40+30+40,fill="#ee6b6e",outline="#ee6b6e")
	can.create_oval(800+20+160-30,35+40+40, 800+20+160,35+40+30+40,fill="#ee6b6e",outline="#ee6b6e")
	can.create_rectangle(800+20+15,35+40+40, 800+20+160-15,35+40+30+40, fill="#ee6b6e",outline="#ee6b6e")

	can.create_arc(800+20,35+40+40, 800+20+30,35+40+30+40,start=90,extent=180,outline="#555555",style="arc")
	can.create_arc(800+20+160-30,35+40+40, 800+20+160,35+40+30+40,start=270,extent=180,outline="#555555",style="arc")

	can.create_line(800+20+15,35+40+40, 800+20+160-15,35+40+40,fill="#555555")
	can.create_line(800+20+15-1,35+40+30+40, 800+20+160-15,35+40+30+40,fill="#555555")

	can.create_text(800+20+80,35+40+15+40,text="Clear",font=("FreeMono",13),fill="#000000")

def home():
	global state,bg,can,writei,listi,settingi,title,text,homei,logouti,entriesf,user_name_

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

	can.create_oval(315,55, 315+20,55+20, fill="#0583d2",outline="#0583d2")
	can.create_oval(315,600-40, 315+20,600-20, fill="#0583d2",outline="#0583d2")





	n=16

	a=525/(n+1)

	aa=a
	s=20



	can.create_polygon(315+10,55, 315+10+40,55, 315+10+40,55+a-s/2, 315,55+a-s/2, 315,55+10,fill="#0583d2",outline="#0583d2")
	
	can.create_polygon(315, 600-20-a+s/2, 315+10+40,600-20-a+s/2, 315+10+40,600-20, 315+10, 600-20, 315,600-20-10  ,fill="#0583d2",outline="#0583d2")

	

	ar=[315,55+a-s/2]

	for _ in range(n):


		cx,cy=315+20-5+s/2,35+20+aa

		_a=180
		for a_ in range(180):

			xx=s/2*math.sin(math.radians(_a))+cx
			yy=s/2*math.cos(math.radians(_a))+cy

			ar.append(xx)
			ar.append(yy)

			_a+=1


		if not _==n-1:

			yv=ar[-1]

			ar.append(315+20-5+s/2)
			ar.append(yv+a-s)




		aa+=a

	ar.append(315)
	ar.append(600-20-a+s/2)

	can.create_polygon(ar,fill="#0583d2",outline="#0583d2")





	aa=a
	ar=[315+10+40,55+a-s/2]

	for _ in range(n):

		cx,cy=315+20-5+s/2,35+20+aa

		_a=180
		for a_ in range(180):

			xx=s/2*math.sin(math.radians(_a))+cx
			yy=s/2*math.cos(math.radians(_a))+cy

			ar.append(xx)
			ar.append(yy)

			_a-=1


		if not _==n-1:

			yv=ar[-1]

			ar.append(315+20-5+s/2)
			ar.append(yv+a-s)




		aa+=a

	ar.append(315+10+40)
	ar.append(600-20-a+s/2)

	can.create_polygon(ar,fill="#0583d2",outline="#0583d2")



	aa=a

	for _ in range(n):
		can.create_arc(315+20-5,35+20+aa-s/2, 315+20+s-5,35+20+aa+s/2, start=180+35, extent=180+45-35,style="arc",outline="#ffffff")


		can.create_line(315-10,35+20+aa, 315+20-5+s/2,35+20+aa, fill="#ffffff",width=3 )

		aa+=a



	x=(1000-170)/2



	can.create_rectangle(x-7,75+20-7, x+170+7,145+20+7,fill="cyan",outline="cyan")
	can.create_rectangle(x,75+20, x+170,145+20,fill="#ffffff",outline="#ffffff",)

	can.create_line(x,75+20+35,x+171,75+20+35,fill="#999999")

	un=user_name_.lower()
	un=un[0].upper()+un[1:]

	can.create_text(x+170/2,75+20+35/2,text=str(un)+"'s Journal",font=("FreeMono",13),anchor="c")

	can.create_text(x+30,145+20-35/2,text="New Entry",font=("FreeMono",13),anchor="w")
	can.create_line(x+110,145+20-35,x+110,145+21,fill="#999999")
	can.create_line(x+140,145+20-35,x+140,145+21,fill="#999999")


	writei=ImageTk.PhotoImage(file="data/write.png")
	listi=ImageTk.PhotoImage(file="data/list.png")
	settingi=ImageTk.PhotoImage(file="data/user.png")


	can.create_image(x+2.5,145+20-35+5,image=writei,anchor="nw")
	can.create_image(x+2.5+110,145+20-35+5,image=listi,anchor="nw")
	can.create_image(x+2.5+110+30,145+20-35+5,image=settingi,anchor="nw")


def _on_mousewheel(e):
	global c_entries,yvar

	if yvar>350:
		c_entries.yview_scroll(int(-1*(e.delta/120)), "units")



def validate():
	global un,pw
	global user_name_,user_id_

	user_name=un.get()
	password=pw.get()

	db_user=db.connect("data/user.db")
	cur=db_user.cursor()
	cur.execute("SELECT * FROM user")
	rows=cur.fetchall()

	

	for row in rows:
		_un=decrypt(row[1])
		_pw=decrypt(row[2])

		if user_name==_un and password==_pw:
			un.place_forget()
			pw.place_forget()

			un.delete(0,tk.END)
			pw.delete(0,tk.END)

			user_name_=user_name
			user_id_=row[0]


			home()
			return

	message(500,(600-200)/2+200+40,"Invalid Entry!",0)
	un.focus_set()

			

def check_un(u):

	db_user=db.connect('data/user.db')
	cur=db_user.cursor()

	cur.execute("SELECT * FROM user")
	rows=cur.fetchall()

	con=0

	for row in rows:

		un_=decrypt(row[1])

		if u==un_:
			con=1
	return con

def timer():
	global target_time
	global can,message_1,message_2,message_3,message_4

	if time.time()>target_time:
		can.delete(message_1)
		can.delete(message_2)
		can.delete(message_3)
		can.delete(message_4)

	root.after(1,timer)

def message(x,y,txt,con):

	global can,message_1,message_2,message_3,message_4
	global target_time


	can.delete(message_1)
	can.delete(message_2)
	can.delete(message_3)
	can.delete(message_4)


	if con==0:
		col="#ee6b6e"
	elif con==1:
		col="#5bd75b"

	


	message_1=can.create_rectangle(x-100-20,y-15,x+100+20,y+15,fill=col,outline=col)
	message_2=can.create_oval(x-120-15,y-15, x-120+15,y+15,fill=col,outline=col)
	message_3=can.create_oval(x+120-15,y-15, x+120+15,y+15,fill=col,outline=col)

	message_4=can.create_text(x,y,text=txt,font=("FreeMono",13),fill="#000000")

	target_time=time.time()+2




def create_account2():

	global un,pw,pw2



	user_name=un.get()
	password1=pw.get()
	password2=pw2.get()

	if user_name=="" or password1=="" or password2=="":
		message(500,(600-200)/2+230+40,"Enter all fields!",0)
		return

	a=check_un(user_name)

	if a==1:
		message(500,(600-200)/2+230+40,"User name exists!",0)
		return

	if password1!=password2:
		message(500,(600-200)/2+230+40,"Password does't match!",0)
		return


	db_user=db.connect('data/user.db')
	cur=db_user.cursor()

	cur.execute("SELECT MAX(user_id) FROM user")
	rows=cur.fetchall()

	v=0
	for row in rows:
		v=row[0]
	if v==None:
		v=1
	else:
		v+=1

	user_name=encrypt(user_name)
	password=encrypt(password1)

	cur.execute("INSERT INTO user VALUES("+str(v)+",'"+str(user_name)+"','"+str(password)+"')")
	db_user.commit()

	login()

	message(500,(600-200)/2+200+40,"Accont has been created!",1)


def create_account():

	global state,title,text,entriesf,search,bg,can
	global un,pw,pw2
	state="create_account"

	title.place_forget()
	text.place_forget()
	entriesf.place_forget()
	search.place_forget()

	un.delete(0,tk.END)
	pw.delete(0,tk.END)
	pw2.delete(0,tk.END)

	can.delete("all")

	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")


	xx=350
	yy=250

	x=(1000-xx)/2

	y=(600-yy)/2



	#can.create_rectangle(x,y, x+xx,y+yy)

	can.create_oval(x,y, x+20,y+20,fill="#ffffff",outline="#ffffff")
	can.create_oval(x+xx-20,y, x+xx,y+20,fill="#ffffff",outline="#ffffff")
	can.create_oval(x,y+yy-20, x+20,y+yy,fill="#ffffff",outline="#ffffff")
	can.create_oval(x+xx-20,y+yy-20, x+xx,y+yy,fill="#ffffff",outline="#ffffff")

	can.create_polygon(x+10,y, x+xx-10,y, x+xx,y+10, x+xx,y+yy-10, x+xx-10,y+yy, x+10,y+yy,
		x,y+yy-10, x,y+10,fill="#ffffff",outline="#ffffff")


	can.create_text(x+30,y+40, anchor="w",text="User name",fill="#000000",font=("FreeMono","13"))
	can.create_text(x+30,y+40+50, anchor="w",text="Password",fill="#000000",font=("FreeMono","13"))
	can.create_text(x+30,y+40+50+50, anchor="w",text="Password*",fill="#000000",font=("FreeMono","13"))




	can.create_arc(x+150-2-10,y+30-2, x+150-2+10-10,y+30-2+10,style="arc",start=90,extent=90,outline="#000000")
	can.create_arc(x+150-2-10,y+30+20+5-10, x+150-2+10-10,y+30+20+5,style="arc",start=180,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30-2, x+150+168-10,y+30-2+10,style="arc",start=0,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30+20+5-10, x+150+168-10,y+30+20+5,style="arc",start=270,extent=90,outline="#000000")

	can.create_line(x+150-2-10,y+30-2+5, x+150-2-10,y+30+20+5-5,fill="#000000")
	can.create_line(x+150+168-10,y+30-2+5, x+150+168-10,y+30+20+5-5,fill="#000000")

	can.create_line(x+150-2+5-10,y+30-2, x+150+168-5+1-10,y+30-2,fill="#000000")
	can.create_line(x+150-2+5-10,y+30+20+5, x+150+168-5-10,y+30+20+5,fill="#000000")


	can.create_arc(x+150-2-10,y+30-2+50, x+150-2+10-10,y+30-2+10+50,style="arc",start=90,extent=90,outline="#000000")
	can.create_arc(x+150-2-10,y+30+20+5-10+50, x+150-2+10-10,y+30+20+5+50,style="arc",start=180,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30-2+50, x+150+168-10,y+30-2+10+50,style="arc",start=0,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30+20+5-10+50, x+150+168-10,y+30+20+5+50,style="arc",start=270,extent=90,outline="#000000")

	can.create_line(x+150-2-10,y+30-2+5+50, x+150-2-10,y+30+20+5-5+50,fill="#000000")
	can.create_line(x+150+168-10,y+30-2+5+50, x+150+168-10,y+30+20+5-5+50,fill="#000000")

	can.create_line(x+150-2+5-10,y+30-2+50, x+150+168-5+1-10,y+30-2+50,fill="#000000")
	can.create_line(x+150-2+5-10,y+30+20+5+50, x+150+168-5-10,y+30+20+5+50,fill="#000000")



	can.create_arc(x+150-2-10,y+30-2+50+50, x+150-2+10-10,y+30-2+10+50+50,style="arc",start=90,extent=90,outline="#000000")
	can.create_arc(x+150-2-10,y+30+20+5-10+50+50, x+150-2+10-10,y+30+20+5+50+50,style="arc",start=180,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30-2+50+50, x+150+168-10,y+30-2+10+50+50,style="arc",start=0,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30+20+5-10+50+50, x+150+168-10,y+30+20+5+50+50,style="arc",start=270,extent=90,outline="#000000")

	can.create_line(x+150-2-10,y+30-2+5+50+50, x+150-2-10,y+30+20+5-5+50+50,fill="#000000")
	can.create_line(x+150+168-10,y+30-2+5+50+50, x+150+168-10,y+30+20+5-5+50+50,fill="#000000")

	can.create_line(x+150-2+5-10,y+30-2+50+50, x+150+168-5+1-10,y+30-2+50+50,fill="#000000")
	can.create_line(x+150-2+5-10,y+30+20+5+50+50, x+150+168-5-10,y+30+20+5+50+50,fill="#000000")




	un.place(in_=root,x=x+151-10,y=y+31)
	pw.place(in_=root,x=x+151-10,y=y+31+50)
	pw2.place(in_=root,x=x+151-10,y=y+31+50+50)

	un.focus_set()



	can.create_oval(x+20+30,y+yy-20-30, x+20+30+30,y+yy-20,outline="#000000",fill="#000000")
	can.create_oval(x+20+100+30-30,y+yy-20-30, x+20+100+30,y+yy-20,outline="#000000",fill="#000000")

	can.create_rectangle(x+20+30+15,y+yy-20-30, x+20+100+30-15,y+yy-20,fill="#000000",outline="#000000")



	can.create_text(x+20+30+50,y+yy-20-30+15,text="Cancel",font=("FreeMono",13),fill="red",anchor="c")



	can.create_oval(x+xx-100-20-30,y+yy-20-30, x+xx-100-20-30+30,y+yy-20,outline="#000000",fill="#000000")
	can.create_oval(x+xx-20-30-30,y+yy-20-30, x+xx-20-30,y+yy-20,outline="#000000",fill="#000000")

	can.create_rectangle(x+xx-100-20-30+15,y+yy-20-30, x+xx-20-30-15,y+yy-20,outline="#000000",fill="#000000")

	can.create_text(x+xx-100-20-30+50,y+yy-20-30+15,text="Sign Up",font=("FreeMono",13),fill="#ffffff",anchor="c")


	






def login():
	global state,title,text,entriesf,search,bg,can
	global show_p,dshow_p,show_st,un,pw,pw2

	state="login"

	title.place_forget()
	text.place_forget()
	entriesf.place_forget()
	search.place_forget()
	pw2.place_forget()

	#un.delete(0,tk.END)
	#pw.delete(0,tk.END)
	#pw2.delete(0,tk.END)




	can.delete("all")

	bg=ImageTk.PhotoImage(file="data/wood.jpg")
	can.create_image(0,0,image=bg,anchor="nw")




	xx=350
	yy=230

	x=(1000-xx)/2

	y=(600-yy)/2



	#can.create_rectangle(x,y, x+xx,y+yy)

	can.create_oval(x,y, x+20,y+20,fill="#ffffff",outline="#ffffff")
	can.create_oval(x+xx-20,y, x+xx,y+20,fill="#ffffff",outline="#ffffff")
	can.create_oval(x,y+yy-20, x+20,y+yy,fill="#ffffff",outline="#ffffff")
	can.create_oval(x+xx-20,y+yy-20, x+xx,y+yy,fill="#ffffff",outline="#ffffff")

	can.create_polygon(x+10,y, x+xx-10,y, x+xx,y+10, x+xx,y+yy-10, x+xx-10,y+yy, x+10,y+yy,
		x,y+yy-10, x,y+10,fill="#ffffff",outline="#ffffff")


	can.create_text(x+30,y+40, anchor="w",text="User name",fill="#000000",font=("FreeMono","13"))
	can.create_text(x+30,y+40+50, anchor="w",text="Password",fill="#000000",font=("FreeMono","13"))





	can.create_arc(x+150-2-10,y+30-2, x+150-2+10-10,y+30-2+10,style="arc",start=90,extent=90,outline="#000000")
	can.create_arc(x+150-2-10,y+30+20+5-10, x+150-2+10-10,y+30+20+5,style="arc",start=180,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30-2, x+150+168-10,y+30-2+10,style="arc",start=0,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30+20+5-10, x+150+168-10,y+30+20+5,style="arc",start=270,extent=90,outline="#000000")

	can.create_line(x+150-2-10,y+30-2+5, x+150-2-10,y+30+20+5-5,fill="#000000")
	can.create_line(x+150+168-10,y+30-2+5, x+150+168-10,y+30+20+5-5,fill="#000000")

	can.create_line(x+150-2+5-10,y+30-2, x+150+168-5+1-10,y+30-2,fill="#000000")
	can.create_line(x+150-2+5-10,y+30+20+5, x+150+168-5-10,y+30+20+5,fill="#000000")


	can.create_arc(x+150-2-10,y+30-2+50, x+150-2+10-10,y+30-2+10+50,style="arc",start=90,extent=90,outline="#000000")
	can.create_arc(x+150-2-10,y+30+20+5-10+50, x+150-2+10-10,y+30+20+5+50,style="arc",start=180,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30-2+50, x+150+168-10,y+30-2+10+50,style="arc",start=0,extent=90,outline="#000000")
	can.create_arc(x+150+168-10-10,y+30+20+5-10+50, x+150+168-10,y+30+20+5+50,style="arc",start=270,extent=90,outline="#000000")

	can.create_line(x+150-2-10,y+30-2+5+50, x+150-2-10,y+30+20+5-5+50,fill="#000000")
	can.create_line(x+150+168-10,y+30-2+5+50, x+150+168-10,y+30+20+5-5+50,fill="#000000")

	can.create_line(x+150-2+5-10,y+30-2+50, x+150+168-5+1-10,y+30-2+50,fill="#000000")
	can.create_line(x+150-2+5-10,y+30+20+5+50, x+150+168-5-10,y+30+20+5+50,fill="#000000")


	un.place(in_=root,x=x+151-10,y=y+31)
	pw.place(in_=root,x=x+151-10,y=y+31+50)


	un.focus_set()


	show_p=ImageTk.PhotoImage(file="data/show.png")
	dshow_p=ImageTk.PhotoImage(file="data/dshow.png")

	if show_st==0:
		can.create_image(x+xx-37,y+78-2,image=show_p,anchor="nw")
		pw["show"]="*"
	elif show_st==1:
		can.create_image(x+xx-37,y+78-2,image=dshow_p,anchor="nw")
		pw["show"]=""



	can.create_oval(x+100-(30/2), y+130+20+30-30-10, x+100+(30/2), y+130+20+30-30+30-10,fill="#000000",outline="#000000")
	can.create_oval(x+250-(30/2), y+130+20+30-30-10, x+250+(30/2), y+130+20+30-30+30-10,fill="#000000",outline="#000000")

	can.create_rectangle(x+100-(30/2)+15, y+130+20+30-30-10, x+250+(30/2)-15,y+130+20+30-10,fill="#000000",outline="#000000")


	can.create_text(x+350/2,y+130+20+30-30+15-10,text="Login",font=("FreeMono","13"),fill="#ffffff")



	can.create_text(x+10,y+yy-20,text="Create account.",font=("FreeMono",13),anchor="w",fill="red")



def logout():
	login()





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

show_p=0
dshow_p=0

show_st=0


target_time=0

message_1=0
message_2=0
message_3=0
message_4=0

user_name_=""
user_id_=0


root=tk.Tk()
root.iconbitmap(r"icon.ico")
root.title("Diary")

wd=root.winfo_screenwidth()
px=int((wd-1000)/2)

root.geometry("1000x600+"+str(px)+"+0")
root.resizable(0,0)

can=tk.Canvas(width=1000,height=600,relief="flat",highlightthickness=0,border=0)
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",can_commands)

def nxt_title(e):
	global text

	text.focus_set()

title=tk.Entry(width=33,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,
	font=("FreeMono",25),disabledbackground="#ffffff",disabledforeground="#000000"
	,selectbackground="#000000",selectforeground="#ffffff")
title.bind("<KeyPress>",title_keyp)
title.bind("<Return>",nxt_title)

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
		user_id INT,
		id INT,
		title VARCHAR(255),
		date_ VARCHAR(255),
		body VARCHAR(255)
		);""")
	db_diary.close()


except:
	pass



try:
	db_user=db.connect('data/user.db')
	cur=db_user.cursor()
	cur.execute("""CREATE TABLE user(
		user_id INT,
		user_name VARCHAR(255),
		password VARCHAR(255)
		);""")
	db_user.close()


except:
	pass


def eun(e):
	global pw

	pw.focus_set()

def epw(e):
	global pw2,state

	if state=="create_account":

		pw2.focus_set()

un=tk.Entry(width=18,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"))

un.bind("<Return>",eun)

pw=tk.Entry(width=18,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"),show="*")
pw.bind("<Return>",epw)


pw2=tk.Entry(width=18,bg="#ffffff",fg="#000000",relief="flat",highlightthickness=0,border=0,font=("FreeMono","13"),show="*")

timer()
login()
#home()
manage_entry()
search_()
root.mainloop()

