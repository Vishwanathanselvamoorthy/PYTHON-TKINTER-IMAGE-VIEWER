from tkinter import *

from PIL import ImageTk,Image

app = Tk()

app.title('IMAGE VIEWER')

app.iconbitmap('D:/PYTHON/TKINTER/icon.ico')

app.config(bg="#a2d2ff")



myImg1=Image.open("D:/PYTHON/TKINTER PORJECTS/Gallery/images/p1.jpg")

resized=myImg1.resize((400,400),Image.ANTIALIAS)

newImg1=ImageTk.PhotoImage(resized)



myImg2=Image.open("D:/PYTHON/TKINTER PORJECTS/Gallery/images/p2.jpg")

resized=myImg2.resize((400,400),Image.ANTIALIAS)

newImg2=ImageTk.PhotoImage(resized)



myImg3=Image.open("D:/PYTHON/TKINTER PORJECTS/Gallery/images/p3.jpg")

resized=myImg3.resize((400,400),Image.ANTIALIAS)

newImg3=ImageTk.PhotoImage(resized)



myImg4=Image.open("D:/PYTHON/TKINTER PORJECTS/Gallery/images/p4.jpg")

resized=myImg4.resize((400,400),Image.ANTIALIAS)

newImg4=ImageTk.PhotoImage(resized)



myImg5=Image.open("D:/PYTHON/TKINTER PORJECTS/Gallery/images/p5.jpg")

resized=myImg5.resize((400,400),Image.ANTIALIAS)

newImg5=ImageTk.PhotoImage(resized)




imageList = [newImg1, newImg2, newImg3, newImg4, newImg5]

heading_label = Label(app, text="IMAGE VIEWER", font=("Times", 20), bg="#a2d2ff")

heading_label.grid(row=0, column=0, columnspan=3, pady=(10, 20))





myLabel = Label(image=newImg1,padx=100,pady=100)

myLabel.grid(row=1, column=0, columnspan=3)

def forward(imgNo):
    
	global myLabel
    
	global buttonForward
    
	global buttonBack

	myLabel.grid_forget()
    
	myLabel = Label(image=imageList[imgNo-1])
    
	buttonForward = Button(app, text=">>", command=lambda: forward(imgNo+1),bg="black",fg="black")
    
	buttonBack = Button(app, text="<<", command=lambda: back(imgNo-1),bg="black",fg="black")
	
	if imgNo == 5:
        
		buttonForward = Button(app, text=">>", state=DISABLED,bg="gray",fg="gray")

	myLabel.grid(row=1, column=0, columnspan=3)
    
	buttonBack.grid(row=3, column=0)
    
	buttonForward.grid(row=3, column=2)

def back(imgNo):
    
	global myLabel
    
	global buttonforward
    
	global buttonBack

	myLabel.grid_forget()
    
	myLabel = Label(image=imageList[imgNo-1])
    
	buttonForward = Button(app, text=">>", command=lambda: forward(imgNo+1),bg="black",fg="black")
    
	buttonBack = Button(app, text="<<", command=lambda: back(imgNo-1),bg="black",fg="black")

	if imgNo == 1:
        
		buttonBack = Button(app, text="<<", state=DISABLED,bg="gray",fg="gray")

	myLabel.grid(row=1, column=0, columnspan=3)
    
	buttonBack.grid(row=3, column=0)
    
	buttonForward.grid(row=3, column=2)



buttonBack = Button(app, text="<<",font=(35), command=back, state=DISABLED,bg="#343a40")

buttonExit = Button(app, text="EXIT", command=app.quit,bg="#c1121f",width=29,font=(35))

buttonForward = Button(app, text=">>", font=(35), command=lambda: forward(2),bg="#343a40")


buttonBack.grid(row=3, column=0,pady=25)

buttonExit.grid(row=3, column=1,pady=25)

buttonForward.grid(row=3, column=2,pady=25)

app.mainloop()