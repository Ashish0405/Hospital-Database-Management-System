from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import mysql.connector
from datetime import date
import os.path
from tkinter import filedialog
from fpdf import FPDF

root=Tk()
root.title("Hospital Management System")
root.geometry("500x400+300+100")
root.configure(background="LIGHT GREEN")

def f1():
	loginid=entid.get()
	password=entpass.get()
	if loginid=='123' and password=='meera':
		showinfo("Success:","Logined successfully")
		root.withdraw()
		first.deiconify()
	elif loginid=="" or password=="":
		showwarning("Failure","Please enter all the details")
	else:
		showerror("Faliure:","Incorrect password or id")

def f2():
	first.withdraw()
	newp.deiconify()

def f3():
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		pid=int(entpid.get())
		pname=entpname.get()
		pphone=entpphone.get()
		pdisease=entpdisease.get()
		pdoctor=int(entpdoctor.get())
		args=(pid,pname,pphone,pdisease,pdoctor)
		s="insert into patient values(%s,%s,%s,%s,%s)"
		cur.execute(s,args)
		#r="insert into perrec values(%s,%s,%s,%s,%s)"
		#cur.execute(r,args)
		mydb.commit()
		showinfo("Success","Record added")
		entpname.delete(0,END)
		entpid.delete(0,END)
		entpphone.delete(0,END)
		entpdisease.delete(0,END)
		entpdoctor.delete(0,END)
	except Exception as e:
		mydb.rollback()
		showerror("Faliure",e)

def f4():
	newp.withdraw()
	first.deiconify()

def f5():
	docdata.delete(1.0,END)
	docrec.deiconify()
	first.withdraw()
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		cur.callproc('doctor')
		for res in cur.stored_results():
			d=res.fetchall()
		info=""
		i="Doctorid \t|\tNAME\t\n"+"-"*30+"\n"
		docdata.insert(INSERT,i)
		for i in d:
			info=info+str(i[0])+"\t  |\t"+str(i[1])+"\n"
		docdata.insert(INSERT,info)
	except Exception as e:
		showerror("Select issue",e)
def f6():
	docrec.withdraw()
	first.deiconify()

def f7():
	patdata.delete(1.0,END)
	patrec.deiconify()
	first.withdraw()
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		cur.callproc('patient')
		for res in cur.stored_results():
			d=res.fetchall()
		info=""
		i="id\t|\tname\t|\tphone\t   |\tdisease\t|\tDoctor Assigned\n"+"-"*80+"\n"
		patdata.insert(INSERT,i)
		for i in d:
			info=info+str(i[0])+"\t|\t"+str(i[1])+"\t|\t"+str(i[2])+"\t|\t"+str(i[3])+"\t|\t"+str(i[4])+"\n"
		patdata.insert(INSERT,info)
	except Exception as e:
		showerror("Select issue",e)


def f8():
	patrec.withdraw()
	first.deiconify()
def f9():
	adddoc.deiconify()
	first.withdraw()
	

def f10():
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		did=int(entdid.get())
		dname=entdname.get()
		args=(did,dname)
		s="insert into doctor values(%s,%s)"
		cur.execute(s,args)	
		mydb.commit()
		showinfo("Success :","Doctor Added")
		entdid.delete(0,END)
		entdname.delete(0,END)
	except Exception as e:
		mydb.rollback()
		showerror("Faliure",e)

def f11():
	adddoc.withdraw()
	first.deiconify()

def f12():
	roomdata.delete(1.0,END)
	room.deiconify()
	first.withdraw()
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		cur.callproc('room')
		for res in cur.stored_results():
			d=res.fetchall()
		info=""
		i="id\t|\tname\t|\tphone\t    |\tdisease\t|\tRoomNo\t|\tadmitted date\n"+"-"*190+"\n"
		roomdata.insert(INSERT,i)
		for i in d:
			info=info+str(i[0])+"\t|\t"+str(i[1])+"\t|\t"+str(i[2])+"\t|\t"+str(i[3])+"\t|\t"+str(i[4])+"\t|\t"+str(i[5])+"\t\t"+"\n"
		roomdata.insert(INSERT,info)
	except Exception as e:
		showerror("Select issue",e)
def f13():
	room.withdraw()
	first.deiconify()

def f14():
	billdata.delete(1.0,END)	
	bill.deiconify()
	first.withdraw()

def f15():
	billdata.delete(1.0,END)
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		id=int(entbpid.get())
		args=(id,)
		s="select pname,pphone,pdisease,dname from patient,doctor where pdoctor=did and pid=%s"
		cur.execute(s,args)
		d=cur.fetchall()
		for i in d:
			data="Name of Patient :"+str(i[0])+"\nPatient Phone Number :"+str(i[1])+"\nDisease :"+str(i[2])+"\nDoctor Name :"+str(i[3])+"\n"
		admitteddate=date.today()
		q="select startdate from patient,room where patient.pid=room.pid and room.pid=%s"
		cur.execute(q,args)
		d1=cur.fetchall()
		if d1==[]:
			data=data+"Admitted Date :"+str(admitteddate)+"\n"
		else:
			for i in d1:
				data=data+"Admitted Date :"+str(i[0])+"\n\n"
				admitteddate=i[0]
		dischargedate=entdischarge.get()
		data=data+"Discharge Date :"+str(dischargedate)+"\n\n"
		args=(admitteddate,dischargedate,)
		cur.callproc('days',args)
		d=cur.stored_results()
		for res in cur.stored_results():
			d=res.fetchall()
		
		for i in d:
			data=data+"Total Bill :"+str((i[0]+1)*500)+"Rs"+"\n"
		billdata.insert(INSERT,data)
	except Exception as e:
		showerror("Bill issue",e)

def f16():

	addroom.deiconify()
	newp.withdraw()

def f17():
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		rno=(entroomid.get())
		startdate=entstartdate.get()
		pid=int(entpatid.get())
		args=(rno,startdate,pid)
		s="insert into room values(%s,%s,%s)"
		cur.execute(s,args)
		mydb.commit()
		showinfo("Success","Record added")	
		entpatid.delete(0,END)	
		entroomid.delete(0,END)
		entstartdate.delete(0,END)
		
	except Exception as e:
		mydb.rollback()
		showerror("Faliure",e)
	
def f18():
	addroom.withdraw()
	newp.deiconify()

def f19():
	bill.withdraw()
	first.deiconify()

def f20():
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		id=int(entbpid.get())
		args=(id,)
		r="select * from patient where pid=%s"
		cur.execute(r,args)
		d=cur.fetchall()
		print(d)
		if d==[]:
			showerror("Failure","Patient does not exists")
		else:
			s="delete from patient where pid=%s"
			cur.execute(s,args)
			mydb.commit()
			showinfo("Success ","Patient discharge")
			entbpid.delete(0,END)
			entdischarge.delete(0,END)
			billdata.delete(1.0,END)
	except Exception as e:
		mydb.rollback()
		showerror("Faliure",e)

def f21():
	first.withdraw()
	permrec.deiconify()
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		s='''	drop event if exists e1;
			create event e1 on schedule every 1 minute do
			begin
				insert ignore into perrec select * from patient;
			end ;
			'''
		cur.execute(s)		
	except Exception as e:
		showerror("Faliure",e)
def f23():
	try:
		mydb=mysql.connector.connect(host='localhost',user='root',password='abc456',database='hospital')
		cur=mydb.cursor()
		s="select * from perrec"
		cur.execute(s)
		d=cur.fetchall()
		i="id\t|\tname\t|\tphone\t|\tdisease\t|\tDoctor Assigned\n"+"-"*80+"\n"
		perdata.insert(INSERT,i)
		info=""
		for i in d:
			info=info+str(i[0])+"\t|\t"+str(i[1])+"\t|\t"+str(i[2])+"\t|\t"+str(i[3])+"\t|\t"+str(i[4])+"\n"
		perdata.insert(INSERT,info)
	except Exception as e:
		showerror("Faliure",e)	
def f22():
	perdata.delete(1.0,END)
	permrec.withdraw()
	first.deiconify()

def f24():
	file_name=entbpid.get()+"_bill.txt" 	
	if os.path.exists(file_name):
		showinfo(file_name,"Already Exists")
	else:
		data=billdata.get(1.0, END)
		if file_name=="_bill.txt" or data=="\n":
			showerror("Failure","Please enter all details or generate the bill first")
		else:
			f=None
			try:
				f=open(file_name,"a")
				print(file_name,"Created")
				
				data=billdata.get(1.0, END)
				data="MEERA HOSPITAL\n"+data
				f.write(data+"\n")	
				showinfo("Success","Bill Downloaded")
			except Execution as e:
				showerror("creation issue",e)
			finally:
				if f is not None:
					f.close()
			fi=open(file_name,"r")
			def convert_file(file):
				pdf=FPDF()
				pdf.add_page()
				line1=1
				for text in file:
					if(line1==1):
						pdf.set_font("Arial","B",size=18) #For title text
						pdf.cell(w=200,h=10,txt=text,ln=1,align="C")
						line1=0
					else:
						pdf.set_font("Arial",size=15)
						pdf.multi_cell(w=0,h=10,txt=text,align="L")
				pdf_name=entbpid.get()+".pdf"
				pdf.output(pdf_name)
			convert_file(fi)
			showinfo("Success","PDF Created")
lbltitle=Label(root,text="Welcome to Meera Hospital",font=("arial ",20,"bold"),borderwidth=4,bg="lightgreen")
lblid=Label(root,text="Enter Login id",font=("arial",18,"bold"),bg="lightgreen")
entid=Entry(root,bd=5,font=("arial",18,"bold"))
lblpass=Label(root,text="Enter Password",font=("arial",18,"bold"),bg="lightgreen")
entpass=Entry(root,bd=5,font=("arial",18,"bold"), show="*")
btnlogin=Button(root,text="LOGIN",font=("arial",18,"bold"),command=f1)

lbltitle.pack(pady=10)
lblid.pack(pady=10)
entid.pack(pady=10)
lblpass.pack(pady=10)
entpass.pack(pady=10)
btnlogin.pack(pady=10)

first=Toplevel(root)
first.title("First Window")
first.geometry("500x500+300+100")
first.withdraw()

btnnewpatient=Button(first,text="New Patient",font=("arial",18,"bold"),width=30,command=f2)
btnviewdoc=Button(first,text="Doctor Records",font=("arial",18,"bold"),width=30,command=f5)
btnviewpatient=Button(first,text="Patient Records",font=("arial",18,"bold"),width=30,command=f7)
btnnewdoc=Button(first,text="ADD Doctor",font=("arial",18,"bold"),width=30,command=f9)
btnroom=Button(first,text="ROOM",font=("arial",18,"bold"),width=30,command=f12)
btnbill=Button(first,text="Genrate Bill",font=("arial",18,"bold"),width=30,command=f14)
btnperrec=Button(first,text="Permanent Records",font=("arial",18,"bold"),width=30,command=f21)

btnnewdoc.pack(pady=5)
btnnewpatient.pack(pady=5)
btnviewdoc.pack(pady=5)
btnviewpatient.pack(pady=5)
btnroom.pack(pady=5)
btnbill.pack(pady=5)
btnperrec.pack(pady=5)

newp=Toplevel(root)
newp.title("Add New patient")
newp.geometry("500x650+300+100")
newp.withdraw()

lblpid=Label(newp,text="Enter patient id",font=("arial",15,"bold"))
entpid=Entry(newp,bd=5,font=("arial",15,"bold"))
lblpname=Label(newp,text="Enter patient name",font=("arial",15,"bold"))
entpname=Entry(newp,bd=5,font=("arial",15,"bold"))
lblpphone=Label(newp,text="Enter patient phone number",font=("arial",15,"bold"))
entpphone=Entry(newp,bd=5,font=("arial",15,"bold"))
lblpdisease=Label(newp,text="Enter patient disease",font=("arial",15,"bold"))
entpdisease=Entry(newp,bd=5,font=("arial",15,"bold"))
lblpdoctor=Label(newp,text="Assign doctor",font=("arial",15,"bold"))
entpdoctor=Entry(newp,bd=5,font=("arial",15,"bold"))
btnadd=Button(newp,text="Add",font=("arial",15,"bold"),command=f3)
btnback=Button(newp,text="Back",font=("arial",15,"bold"),command=f4)
btnaddroom=Button(newp,text="Assign Room",font=("arial",15,"bold"),command=f16)

lblpid.pack(pady=5)
entpid.pack(pady=5)
lblpname.pack(pady=5)
entpname.pack(pady=5)
lblpphone.pack(pady=5)
entpphone.pack(pady=5)
lblpdisease.pack(pady=5)
entpdisease.pack(pady=5)
lblpdoctor.pack(pady=5)
entpdoctor.pack(pady=5)

btnadd.pack(pady=5)
btnaddroom.pack(pady=5)
btnback.pack(pady=5)


docrec=Toplevel(root)
docrec.title("Docter Records")
docrec.geometry("500x600+300+100")
docrec.withdraw()

docdata=ScrolledText(docrec,width=60,height=10)
btndback=Button(docrec,text="BACK",font=("arial",18,"bold"),command=f6)

docdata.pack(pady=10)
btndback.pack(pady=10)

patrec=Toplevel(root)
patrec.title("Patient Records")
patrec.geometry("700x600+300+100")
patrec.withdraw()

patdata=ScrolledText(patrec,width=100,height=10)
btnpback=Button(patrec,text="BACK",font=("arial",18,"bold"),command=f8)

patdata.pack(pady=10)
btnpback.pack(pady=10)

adddoc=Toplevel(root)
adddoc.title("Add new doctor")
adddoc.geometry("500x600+300+100")
adddoc.withdraw()

lbldid=Label(adddoc,text="Doctor id",font=("arial",18,"bold"))
entdid=Entry(adddoc,bd=5,font=("arial",18,"bold"))
lbldname=Label(adddoc,text="Doctor name",font=("arial",18,"bold"))
entdname=Entry(adddoc,bd=5,font=("arial",18,"bold"))
btndadd=Button(adddoc,text="ADD",font=("arial",18,"bold"),command=f10)
btndback=Button(adddoc,text="BACK",font=("arial",18,"bold"),command=f11)

lbldid.pack(pady=10)
entdid.pack(pady=10)
lbldname.pack(pady=10)
entdname.pack(pady=10)
btndadd.pack(pady=10)
btndback.pack(pady=10)

room=Toplevel(root)
room.title("Room Records")
room.geometry("800x400+300+100")
room.withdraw()

roomdata=ScrolledText(room,width=120,height=20,font=("arial",10,"bold"))
btnrback=Button(room,text="BACK",font=("arial",18,"bold"),command=f13)

roomdata.pack(pady=10)
btnrback.pack(pady=10)

bill=Toplevel(root)
bill.title("Bill generator")
bill.geometry("500x700+300+100")
bill.withdraw()

lblbpid=Label(bill,text="Enter patient id",font=("arial",18,"bold"))
entbpid=Entry(bill,bd=5,font=("arial",18,"bold"))
lbldischarge=Label(bill,text="Enter Discharge date",font=("arial",18,"bold"))
entdischarge=Entry(bill,bd=5,font=("arial",18,"bold"))
billdata=ScrolledText(bill,width=60,height=10)
btngenrate=Button(bill,text="Genrate Bill",font=("arial",18,"bold"),command=f15)
btndischarge=Button(bill,text="Dicharge Patient",font=("arial",15,"bold"),command=f20)
btndownloadbill=Button(bill,text="Download Bill",font=("arial",15,"bold"),command=f24)
btnback=Button(bill,text="BACK",font=("arial",18,"bold"),command=f19)

lblbpid.pack(pady=10)
entbpid.pack(pady=10)
lbldischarge.pack(pady=10)
entdischarge.pack(pady=10)
billdata.pack(pady=10)
btngenrate.pack(pady=10)
btndischarge.pack(pady=10)
btndownloadbill.pack(pady=10)
btnback.pack(pady=10)

addroom=Toplevel(root)
addroom.title("Assign room")
addroom.geometry("500x600+300+100")
addroom.withdraw()

lblpatid=Label(addroom,text="Enter patient id",font=("arial",15,"bold"))
entpatid=Entry(addroom,bd=5,font=("arial",15,"bold"))
lblroomid=Label(addroom,text="Enter room id",font=("arial",15,"bold"))
entroomid=Entry(addroom,bd=5,font=("arial",15,"bold"))
lblstartdate=Label(addroom,text="Enter Admitted date",font=("arial",15,"bold"))
entstartdate=Entry(addroom,bd=5,font=("arial",15,"bold"))
btnadd=Button(addroom,text="ADD",font=("arial",15,"bold"),command=f17)
btnback=Button(addroom,text="BACK",font=("arial",15,"bold"),command=f18)

lblpatid.pack(pady=10)
entpatid.pack(pady=10)
lblroomid.pack(pady=10)
entroomid.pack(pady=10)
lblstartdate.pack(pady=10)
entstartdate.pack(pady=10)
btnadd.pack(pady=10)
btnback.pack(pady=10)

permrec=Toplevel(root)
permrec.title("Permanent records")
permrec.geometry("700x400+300+100")
permrec.withdraw()

perdata=ScrolledText(permrec,width=80,height=10)
btnback=Button(permrec,text="Back",font=("arial",18,"bold"),command=f22)
btnget=Button(permrec,text="Get Records",font=("arial",18,"bold"),command=f23)

perdata.pack(pady=10)
btnget.pack(pady=10)
btnback.pack(pady=10)

root.mainloop()