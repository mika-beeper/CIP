import csv
import pandas as pd
import os
import random
def main():
    file_path = 'my_lib.csv'
    books_df = pd.read_csv(file_path) #reads the file into a pandas dataframe
    choice = 0
    while choice != 'x':
        print("Welcome to your library! Please select an option from the menu below.")
        print("1. Search to see if a book is already in your library.")
        print("2. Search by author.")
        print("3. Add a book to your library.")
        print("4. View your TBR(to be read list)")
        print("Or press 'x' to exit")
        choice = input("Please select your option:")

    if choice == '1':
        search = input("Search to see if title is already in your library: ")
        search_book(books_df, search)
    elif choice == '2':
        search_book_by_author(books_df)
    elif choice == '3':
        add_a_new_entry()
    elif choice == '4':
        view_tbr_list(books_df)
    

def search_book(books_df, search):
    #print(pd.read_csv("my_lib.csv").info()) #this tests to make sure the file is reading right with the correct number of rows and columns
    #search = input("Search to see if title is already in your library: ")
    if not books_df[books_df['Title'] == search].empty:
        print (f"You have the book in your library!")
    else:
        answer = input (f"Oh no! This book isn't in your library yet, would you like to add it?")
        if answer == "yes":
            add_a_new_entry()

def search_book_by_author(books_df):
    search = input("Search to see if you have books by this author on your list: ")
    result = books_df[books_df['Authors'] == search] #goes through the my_lib.csv and checks if there are books relating the search entered
    printable = result['Title'].to_string(index = False) #this helps format the text so it doesn't appear as a dataframe 
    if not result.empty:
        print (f"You have found {len(result)} matches for Author {search}! Here are the results - \n {printable}")
    else:
        print (f"We have not found any books by the author {search}!")

def add_a_new_entry():
    title = input("Enter the tite: ")
    author = input("Enter the name of the author: ")
    read = input("Have you read this book or would you like to add it as 'to-read'?")
    star_rating = float(input("What would you like to rate the book?"))
    review = input ("Would you like to add a review? ")

    data = { 
        'Title': [title],
        'Authors' : [author],
        'Read Status' : [read],
        'Star Rating' : [star_rating],
        'Review' : [review]
    }
    new_entry = pd.DataFrame(data)

    new_entry.to_csv('my_lib.csv', mode = 'a', index = True, header = False)

    print("Data added successfully!")

def view_tbr_list(books_df):
    answer = input("Would you like to see the first 10 books in your To Be Read list?")
    if answer == "Yes":
        to_read = books_df['Read Status'].isin(['to-read'])
        list_to_print = books_df.loc[to_read, ['Title', 'Authors']].sample(10)
        print(list_to_print)


if __name__ == "__main__":
    main()