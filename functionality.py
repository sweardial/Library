from tkinter import *
from tkinter import filedialog, scrolledtext
from table import *
import csv


def open_file():
	file = filedialog.askopenfile(initialdir='/user', filetypes=(('csv files', '*.csv'), ('txt files', "*.txt")))
	if file is not None:
		with open(f'{file.name}', 'r') as csv_file:
			csv_reader = csv.reader(csv_file)
			for line in csv_reader:
				append_book(line[1], line[2], line[3])


def update_csv():
	file = filedialog.askopenfile(initialdir='/user', filetypes=(('csv files', '*.csv'), ('txt files', "*.txt")))
	if file is not None:
		with open(f'{file.name}', 'w') as csv_file:
			csv_writer = csv.writer(csv_file)
			mycursor.execute('SELECT * FROM librarian')
			for line in mycursor:
				csv_writer.writerow(line)


def save_in_file():
	file = filedialog.asksaveasfile(initialdir='/user', filetypes=(('txt files', '*.txt'), ('csv files', '*.csv')))
	if file is not None:
		with open(f'{file.name}', 'w') as books:
			csv_writer = csv.writer(books)
			mycursor.execute("SELECT * FROM librarian")
			for line in mycursor:
				csv_writer.writerow(line)


def showing_books(query='SELECT * FROM librarian'):
	labels = Text(width=44,
	              height=21,
	              bd=2,
	              bg='#4D2E02',
	              font='Times 20',
	              relief='solid',
	              fg='white')

	results = scrolledtext.ScrolledText(width=52,
	                                    height=28,
	                                    bd=2,
	                                    bg='#F0CF9F',
	                                    font='Times 14',
	                                    fg='black',
	                                    )

	labels.insert(INSERT, 'id    Name\t\t       Book\t\t       Released')
	labels.config(state='disabled')
	labels.grid(row=1, column=0, rowspan=100, columnspan=10, padx=5, pady=5)
	results.grid(row=2, column=0, rowspan=100, columnspan=10, padx=5, pady=5)

	mycursor.execute(query)
	for el in mycursor:
		id = el[0]
		name = el[1]
		book = el[2]
		release = str(el[3])
		results.insert(0.0, release + '\n')
		results.insert(0.10, book + '\t\t' + '      '),
		results.insert(0.20, name + '\t\t\t')
		results.insert(0.30, str(id) + '  ')
	results.config(state='disabled')


def adding_enter():
	# Creating a functionality for a button which will be adding books in library
	root_add = Tk()
	root_add.geometry('450x170+480+320')
	root_add.title('Add Book')
	root_add.config(bg='#FEF1DE')
	name_label = Label(root_add,
	                   text='* Name: ',
	                   bg='#FEF1DE'
	                   )
	book_label = Label(root_add,
	                   text='* Book: ',
	                   bg='#FEF1DE'
	                   )
	release_label = Label(root_add,
	                      text='* Release: ',
	                      bg='#FEF1DE'
	                      )
	or_label = Label(root_add,
	                 text='OR',
	                 fg='red',
	                 bg='#FEF1DE'
	                 )

	name_entry = Entry(root_add,
	                   width=40,
	                   borderwidth=3
	                   )
	book_entry = Entry(root_add,
	                   width=40,
	                   borderwidth=3
	                   )
	release_entry = Entry(root_add,
	                      width=40,
	                      borderwidth=3
	                      )
	action_button = Button(root_add,
	                       text='Add',
	                       padx=5,
	                       highlightbackground='#FEF1DE',
	                       command=lambda: [append_book(name=name_entry.get(),
	                                                    book=book_entry.get(),
	                                                    released=release_entry.get()),
	                                        root_add.destroy(),
	                                        showing_books()])
	add_from_file_button = Button(root_add,
	                              text='Add from file',
	                              padx=5,
	                              highlightbackground='#FEF1DE',
	                              command=lambda: [open_file(),
	                                               root_add.destroy(),
	                                               showing_books()])

	name_label.grid(row=0, column=0)
	book_label.grid(row=1, column=0)
	release_label.grid(row=2, column=0)
	name_entry.grid(row=0, column=1)
	book_entry.grid(row=1, column=1)
	release_entry.grid(row=2, column=1)
	action_button.grid(row=3, columnspan=5)
	or_label.grid(row=5, columnspan=5)
	add_from_file_button.grid(row=6, columnspan=5)


# Creating a delete functionality for a button which will be deleting books from library
def delete():
	root_add = Tk()
	root_add.geometry('180x50+600+320')
	root_add.title('DELETE Book')
	id_label = Label(root_add,
	                 text='id: ')
	id_entry = Entry(root_add,
	                 width=10,
	                 borderwidth=3)
	action_button = Button(root_add,
	                       text='Delete',
	                       padx=5,
	                       command=lambda: [delete_book(id=id_entry.get()),
	                                        root_add.destroy(),
	                                        showing_books()])

	id_label.grid(row=0, column=0)
	id_entry.grid(row=0, column=1)
	action_button.grid(row=1, columnspan=10)


# Creating an updating function for already created books
def update():
	root_update = Tk()
	root_update.geometry('450x150+480+320')
	root_update.title('Update book')
	id_label = Label(root_update,
	                 text='id: '
	                 )
	new_name_label = Label(root_update,
	                       text='New name: '
	                       )
	new_book_label = Label(root_update,
	                       text='New book: '
	                       )
	new_release_label = Label(root_update,
	                          text='New release: '
	                          )

	id_entry = Entry(root_update,
	                 width=10,
	                 borderwidth=3
	                 )

	new_name_entry = Entry(root_update,
	                       width=40,
	                       borderwidth=3
	                       )
	new_book_entry = Entry(root_update,
	                       width=40,
	                       borderwidth=3
	                       )
	new_release_entry = Entry(root_update,
	                          width=40,
	                          borderwidth=3
	                          )
	update_button = Button(root_update,
	                       text='Update',
	                       padx=5,
	                       command=lambda: [updating(id=id_entry.get(),
	                                                 new_name=new_name_entry.get(),
	                                                 new_book=new_book_entry.get(),
	                                                 new_release=new_release_entry.get()),
	                                        root_update.destroy(),
	                                        showing_books()]
	                       )

	id_label.grid(row=0, column=0)
	id_entry.grid(row=0, columnspan=5)
	new_name_label.grid(row=4, column=0)
	new_book_label.grid(row=5, column=0)
	new_release_label.grid(row=6, column=0)
	new_name_entry.grid(row=4, column=1)
	new_book_entry.grid(row=5, column=1)
	new_release_entry.grid(row=6, column=1)
	update_button.grid(row=7, columnspan=5)


#searching function
def searching_enter(text):
	root_seatch = Tk()
	root_seatch.title(f'Enter {text}')
	root_seatch.geometry('250x65+550+350')
	enter_field = Entry(root_seatch, width=40)
	label_field = Label(root_seatch,
	                    text=text + ':')
	search_button = Button(root_seatch,
	                       text='Search',
	                       padx=10,
	                       pady=5,
	                       command=lambda: showing_books(f"SELECT * FROM librarian\
	                                                        WHERE {text} LIKE ('%{enter_field.get()}%')"))
	label_field.grid(row=1, column=1)
	enter_field.grid(row=1, column=2)
	search_button.grid(row=2, columnspan=10)


def searching():
	root_search = Tk()
	root_search.title('Search menu')
	root_search.geometry('150x120+600+300')
	root_search.resizable(width=False, height=False)

	search_by_name = Button(root_search,
	                        text='Search by name',
	                        padx=23,
	                        pady=10,
	                        command=lambda: [root_search.destroy(), searching_enter('Name')]

	                        )

	search_by_book = Button(root_search,
	                        text='Search by book',
	                        padx=25,
	                        pady=10,
	                        command=lambda: [root_search.destroy(), searching_enter('Book')]
	                        )

	search_by_release = Button(root_search,
	                           text='Search by relised',
	                           padx=20,
	                           pady=10,
	                           command=lambda: [root_search.destroy(), searching_enter('Released')])

	search_by_name.grid()
	search_by_book.grid()
	search_by_release.grid()


def helping_menu():
	root = Tk()
	root.geometry('530x520+450+160')
	root.title('Help menu')
	root.resizable(width=False, height=False)
	text = Text(root, wrap = WORD,background='#FDEBCD',  height = 50 )
	with open('helping_menu', 'r') as help:
		for line in help:
			text.insert(INSERT, line)
	text.pack()
	text.config(state = 'disabled')