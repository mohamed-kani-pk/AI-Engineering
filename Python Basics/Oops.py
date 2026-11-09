 #class - it is a blueprint of an object. It is a user-defined data type that holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class defines the properties and behaviors of an object.
 #object - it is an instance of a class. It is a real-world entity that has a state and behavior. An object is created from a class and can access the data members and member functions of that class.
 
class Book:
   def __init__(self, title, author, genre):
       self.title = title
       self.author = author
       self.genre = genre

   def display_info(self):
     
       print(f"Title: {self.title}")
       print(f"Author: {self.author}")
       print(f"Genre: {self.genre}")
       
   def reading(self):
       print(f"You are reading '{self.title}' by {self.author}. Enjoy!")
       
   def update_genre(self, new_genre):
       self.genre = new_genre
       
   def __str__(self):
      return f"Book(title={self.title}, author={self.author}, genre={self.genre})"  

book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")  # creating an object of the class Book
print(book.title)  # accessing instance variable
book.display_info()  # calling method of the class
book.reading()  # calling reading method
book.update_genre(new_genre="Classic Literature")  # updating genre
print(book)  # calling __str__ method of the class


class EBook(Book):
  
  def __init__(self, title, author, genre,filesize,fileformat):
    super().__init__(title, author, genre)
    self.filesize = filesize
    self.fileformat = fileformat

  def __str__(self):
    return f"EBook(title={self.title}, author={self.author}, genre={self.genre}, filesize={self.filesize}, fileformat={self.fileformat})"
  
  def test(self):
    print("This is a test method in the EBook class.")
    print(f"{self}")
    print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}")
    
ebook = EBook("1984", "George Orwell", "Dystopian", "1.5MB", "PDF")  # creating an object of the class EBook
ebook.test()  # calling test method of the EBook class
print(ebook)  # calling __str__ method of the EBook class
display_info = ebook.__str__()  # calling __str__ method of the EBook class
print(display_info)  # printing the returned string from the __str__ method

print(issubclass(EBook, Book))  # checking if EBook is a subclass of Book
print(issubclass(Book, EBook))  # checking if Book is a subclass of EBook
print(issubclass(EBook, object))  # checking if EBook is a subclass of object
print(isinstance(ebook, EBook))  # checking if ebook is an instance of EBook
print(isinstance(ebook, Book))  # checking if ebook is an instance of Book
print(isinstance(book, EBook))  # checking if book is an instance of EBook