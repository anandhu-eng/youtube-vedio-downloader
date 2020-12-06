#youtube vedio downloader
from tkinter import *
from pytube import YouTube
from tkinter import messagebox


#function for downloading the youtube vedio
def download():
	vedio_url=url.get()
	try:
		youtube=YouTube(vedio_url)
		vedio=youtube.streams.first()
		vedio.download()
		messagebox.showinfo("SUCCESS!","Vedio successfully downloaded!:)")
	except:
		messagebox.showerror("ERROR","Could not download the vedio\nCheck whether you have given the correct URL:(")

#main window
win=Tk()
win.title("YouTube video Downloader")
#creating labels
label1=Label(win, text="YouTube Video Downloader",fg="red",font=("calibri",10)).grid(sticky=N,padx=100,row=0)
label2=Label(win,text="Please enter the URL of the video to download:",fg="black",font=("calibri",10,"bold")).grid(sticky=N,row=1,pady=2)
url=StringVar()
#Entry
#should split the entry column bcoz  In python when you do a().b(), the result of the expression is whatever b() returns, therefore Entry(...).grid(...) will return None.
url=Entry(win,textvariable=url,width=50)
url.grid(sticky=N,row=2,pady=4)

#button
button1=Button(win,text="Download video",command=download).grid(sticky=N,row=3,pady=20)


win.mainloop()