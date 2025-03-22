from BusinessLogicLayer.Grnre import Genre
from BusinessLogicLayer.Mandatory import Mandatory
from BusinessLogicLayer.Name import *
from BusinessLogicLayer.Number import Number
from Model.Book import Book
from DataLayer.Csv import *


#----------- Input Book Name -------------------
def input_bookname ():
    loop_check=True
    while loop_check  :
        bookname_obj = Mandatory(input("Enter Name of Book :"))
        if bookname_obj.is_valid_mandatory() :
            return bookname_obj.get_data()
        else :
            print("Error entering Data")


#----------- Input Author name -------------------
def input_authorname() :
    loop_check=True
    while loop_check  :
        authorname_obj = Name(input("Enter Author name:"))
        if authorname_obj.is_valid_name_mandatory([' ','.','-']):
            return authorname_obj.get_data()
        else :
            print("Error entering Data")


#----------- Input translator -------------------
def input_translator():
    loop_check=True
    while loop_check  :
        translatorname_obj = Name(input("Enter Translator name:"))
        if translatorname_obj.is_valid_name_non_mandatory([' ']):
            return translatorname_obj.get_data()
        else :
            print("Error entering Data")


#----------- Input ISBN -------------------
def input_isbn():
    loop_check=True
    while loop_check  :
        isbn_obj = Number(input("Enter ISBN:"))
        if isbn_obj.is_valid_number(minlen=0,maxlen=13):
            loop_check=False
            return isbn_obj.get_data()
        else :
            print("Error entering Data")


#----------- Input genre -------------------
def input_genre():
    loop_check=True
    while loop_check  :
        print(f"Select Item From List :")
        for i in range(1, len(Genre.generlist)+1 ) :
            print(f"{i}. {Genre.generlist[i]}" , end="   ")

        print()
        genre_obj = Genre(input("Item is : "))
        if genre_obj.is_valid_genre():
            return genre_obj.get_genre_name()
        else :
            print("Error entering Data")


# ----------- Input publisher -------------------
def input_publisher():
    loop_check = True
    while loop_check:
        publisher_obj = Name(input("Enter publisher name:"))
        if publisher_obj.is_valid_name_mandatory([' ', '.', '-']):
            return publisher_obj.get_data()
        else:
            print("Error entering Data")


#----------- Input Date-Year -------------------
def input_year():
    loop_check=True
    while loop_check  :
        year_obj = Number(input("Enter Year:"))
        if year_obj.is_valid_number(minlen=0,maxlen=4):
            return  year_obj.get_data()
        else :
            print("Error entering Data")


#----------- Input Data -------------------
def input_data():
    book_obj=Book(bookname=input_bookname(),
                  authorname=input_authorname(),
                  translatorname=    input_translator(),
                  isbn=input_isbn(),
                  genre=input_genre(),
                  publisher=input_publisher(),
                  yearpublication= input_year()
                  )
    accept=""
    while accept=="" :
        accept=input("Save Information(yes/no)? : ")
        if accept.lower()=="yes" :
            try:
                write_data_csv(book_obj.get_list(),"DB/Book.csv")
            except :
                print("Error in Data saving")
            print("save Data")
            menu_app()
        elif accept.lower()=="no" :
            menu_app()
        else:
            accept=""


#----------- Read Data -------------------

def show_data():
    try :
        datalist=read_data_csv("DB/Book.csv")
        for item in datalist :
            print(item)
    except FileNotFoundError:
        print("No data recorded yet")


#----------- Menu -------------------

def menu_app() :
    select = 0
    while select <= 0 or select >= 4:
        print("===========================")
        print("  1.View List")
        print("  2.Add Item")
        print("  3.Exit")
        print("===========================")
        select_menu =input("Select an Option :")
        if select_menu.isdecimal() :
            select=int(select_menu)
            if select ==1 :
                show_data()
                menu_app()
            elif select==2:
                input_data()
            elif select==3 :
                exit()
            else :
                print("**Please select the correct")
        else:
            print("**Please select the correct")


menu_app()