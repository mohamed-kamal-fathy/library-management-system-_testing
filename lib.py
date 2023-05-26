import json
import tkinter as tk

import pytest


class LibraryManagementSystem:

    
    def __init__(self, master, db_file):
        self.master = master
        master.title("Library Management System")
        #give color for background  gui
        self.master.config(background="light green")
        self.label_image = tk.Label(self.master)

        # Load books from the database
        self.db_file = db_file
        self.books = self.load_books()

        #>>> Labels
        self.label_books = tk.Label(master, text=" << Welcome to our library >>")
        self.label_books.place(relx=0.30,rely=0, relwidth=0.50,relheight=0.1)

        self.label_books = tk.Label(master, text="Books:")
        self.label_books.place(relx=0.30,rely=0.1, relwidth=0.10,relheight=0.1)
        
        self.label_add = tk.Label(master, text="Add book:")
        self.label_add.place(relx=0.30,rely=0.60, relwidth=0.10,relheight=0.1)
       
        self.label_delete = tk.Label(master, text="Delete book:")
        self.label_delete.place(relx=0.30,rely=0.75, relwidth=0.10,relheight=0.1)
        
        self.label_search = tk.Label(master, text="search book:")
        self.label_search.place(relx=0.30,rely=0.90, relwidth=0.10,relheight=0.1)
        
        #>>> Listbox
        self.list_books = tk.Listbox(master)
        for book in self.books:
            self.list_books.insert(tk.END, book)
        self.list_books.place(relx=0.40,rely=0.10, relwidth=0.30,relheight=0.50)
        
        #>>> Entries
        self.entry_add = tk.Entry(master)
        self.entry_add.place(relx=0.40,rely=0.60, relwidth=0.30,relheight=0.1)

        self.entry_delete = tk.Entry(master)
        self.entry_delete.place(relx=0.40,rely=0.75, relwidth=0.30,relheight=0.1)
        
        self.entry_search = tk.Entry(master)
        self.entry_search.place(relx=0.40,rely=0.90, relwidth=0.30,relheight=0.1)
        
        #>>> Buttons
        self.button_add = tk.Button(master,text="Add ",bg='black', fg='white', command=self.add_book)
        self.button_add.place(relx=0.70,rely=0.60, relwidth=0.08,relheight=0.1)

        self.button_delete = tk.Button(master, text="Delete",bg='black', fg='white', command=self.delete_book)
        self.button_delete.place(relx=0.70,rely=0.75, relwidth=0.08,relheight=0.1)
        
        self.button_search = tk.Button(master, text="Search",bg='black', fg='white', command=self.search_book)
        self.button_search.place(relx=0.70,rely=0.90, relwidth=0.08,relheight=0.1)
        
        

#--------------------------------------------------------------------------------------------------#

    @pytest.fixture(scope="module")
    def app():
     yield app
     root.destroy() #after each test run this 

    # -- open the "books.json" file in read mode using the json.load() function   
    
    def load_books(self):
        # try:
            with open(self.db_file, "r") as f:
                books = json.load(f)
        # except FileNotFoundError:
        #     books = []
            return books

# --  open the "books.json" file in write mode using the json.dump() function
    def save_books(self):
        with open(self.db_file, "w") as f:
            json.dump(self.books, f)

# -- fun to add books
    
    def add_book(self):
        book = self.entry_add.get()
        if book:
            #add to json
            self.books.append(book)
            self.list_books.insert(tk.END, book)
            self.entry_add.delete(0, tk.END)
            self.save_books()


# -- fun to delete books
    def delete_book(self):
        book = self.entry_delete.get()
        if book in self.books:
            #remove from json
            self.books.remove(book)
            self.list_books.delete(self.list_books.get(0, tk.END).index(book))
            self.entry_delete.delete(0, tk.END)
            self.save_books()
            

# -- fun to search books
    def search_book(self):
        book = self.entry_search.get()
        if book in self.books:
           # self.list_books.selection_clear(0, tk.END)
            index = self.list_books.get(0, tk.END).index(book)
            self.list_books.selection_set(index)
            self.entry_search.delete(0, tk.END)
        # Get the search query from the entry widget
        query = self.entry_search.get()
        # Filter the books list to only include books that match the query
        matching_books = [book for book in self.books if query in book]
        # Extract the titles of the matching books into a list and return it
        matching_titles = [book for book in matching_books]
        return matching_titles
    
root = tk.Tk()
app = LibraryManagementSystem(root,"books.json")
#root.title("Library Management System")
root.minsize(width=920,height=432)
root.geometry("920x432")
# Start the Tkinter event loop
root.mainloop()



