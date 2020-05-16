from pytube import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory

foldername = ""

root = Tk()
root.config(bg = '#FAE00E')
root.title("YouTube Downloader")
q = StringVar()
r = StringVar()
s = StringVar()
yimage = PhotoImage(file = "C:\\Users\Himank Jerolia\\Desktop\\ylogo.png")
ilabel = Label(root, image=yimage, bg='#FAE00E')
ilabel.grid(row = 0, columnspan = 2)
entry1 = Entry(root)
label1 = Label(text = "Enter or paste video link ",bg='#FAE00E')
entry1.grid(row='1',column='1')
label1.grid(row='1',column='0')
label5 = Label(root, textvariable= r, fg= 'red',bg='#FAE00E')
label5.grid(row = 2, column = 1)
label6 = Label(root, textvariable = s, fg = 'red',bg='#FAE00E')
label6.grid(row = 4, columnspan = 2)
downloadChoices = ["MP4 720p",
                   "MP4 144p",
                   "Video 3gp",
                   "Song MP3"]

youtubeChoices = ttk.Combobox(root, values = downloadChoices)
youtubeChoices.grid(row = 3, columnspan=2)

label3 = Label(text = "Saved In: ",bg='#FAE00E')
label4 = Label(root, textvariable = q,bg='#FAE00E')
label4.grid(row = 6, column=1)

label3.grid(row = 6, column = 0)

def viddownload():
    foldername = askdirectory()
    r.set("")
    s.set("")
    if len(foldername) > 1:
        q.set(foldername)
        link = entry1.get()
        choice = youtubeChoices.get()
        if len(link) > 1:
            yt = YouTube(link)
            if (choice == downloadChoices[0]):
                selectedVideo = yt.streams.filter(progressive=True).first()
                selectedVideo.download(foldername)

            elif (choice == downloadChoices[1]):
                selectedVideo = yt.streams.filter(progressive=True,
                                                  file_extension='mp4').last()
                selectedVideo.download(foldername)

            elif (choice == downloadChoices[2]):
                selectedVideo = yt.streams.filter(file_extension='3gp').first()
                selectedVideo.download(foldername)

            elif (choice == downloadChoices[3]):
                selectedVideo = yt.streams.filter(only_audio=True).first()
                selectedVideo.download(foldername)
            else:
                s.set("Select a valid choice")
        else:
            r.set("Please Enter a valid link")
    else:
        q.set("Please select a destination.")

button2 = Button(text = "Download",command = viddownload)
button2.grid(row='5', columnspan=2)

root.mainloop()