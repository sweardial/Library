from functionality import *
from PIL import Image, ImageTk

# creating the main window
root = Tk()
root.title('BooksApp')
root.geometry('545x542+440+150')
root.config(background='#FDEBCD')
root.resizable(width=False, height=False)
image = ImageTk.PhotoImage(Image.open('book1.jpg'))
label = Label(root, width=555, height=542, image=image)
label.grid(row=0, rowspan=1000, column=0, columnspan=1000)
myLabel = Label(root,
                text='Welcome to the Library!',
                bg='#F8BC66',
                relief='groove',
                font='Didot 20'
                )

# Creating the buttons and functionality of its
button1 = Button(root,
                 text=' Add ',
                 padx=16,
                 pady=5,
                 highlightbackground='#A7670A',
                 command=adding_enter
                 )
button2 = Button(root,
                 text=' Search ',
                 padx=7,
                 pady=5,
                 highlightbackground='#A7670A',
                 command=searching
                 )
button3 = Button(root,
                 text=' Delete ',
                 padx=9,
                 pady=5,
                 highlightbackground='#A7670A',
                 command=delete
                 )
button4 = Button(root,
                 text=' Exit ',
                 padx=17,
                 pady=5,
                 highlightbackground='#6B430A',
                 command=lambda: [root.quit(), db.close()]
                 )
button6 = Button(root,
                 text='Show all',
                 padx=7,
                 pady=5,
                 highlightbackground='#A7670A',
                 command=showing_books
                 )
button7 = Button(root,
                 text='Edit',
                 padx=20,
                 pady=5,
                 highlightbackground='#A7670A',
                 command=update
                 )
button8 = Button(root,
                 text='Delete all',
                 padx=4,
                 pady=5,
                 highlightbackground='#6B430A',
                 command=lambda: [delete_all(), showing_books()]
                 )
button9 = Button(root,
                 text='Save as',
                 padx=8,
                 pady=5,
                 highlightbackground='#6B430A',
                 command=save_in_file
                 )
button10 = Button(root,
                  text='Update',
                  padx=10,
                  pady=5,
                  highlightbackground='#6B430A',
                  command=update_csv
                  )
button11 = Button(root,
                  text='Help',
                  padx=18,
                  pady=5,
                  highlightbackground='#6B430A',
                  command=helping_menu
                  )
# locating buttons with a grid method
myLabel.grid(row=0, columnspan=15)
button1.grid(row=1, column=11)
button2.grid(row=2, column=11)
button3.grid(row=3, column=11)
button4.grid(row=99, column=11)
button6.grid(row=5, column=11)
button7.grid(row=4, column=11)
button8.grid(row=98, column=11)
button9.grid(row=97, column=11)
button10.grid(row=96, column=11)
button11.grid(row=95, column=11)

if __name__ == '__main__':
	showing_books()
	root.mainloop()
