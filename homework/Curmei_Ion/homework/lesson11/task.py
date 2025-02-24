class Book:
    book_name = "IT"
    author = "Dostoievski"
    number_page = 400
    isbn = 65654313513
    reserved = False

    def __init__(self, material_pages, text):
        self.material_pages = material_pages
        self.text = text
        self.reserved = False


book1 = Book('paper', 'Python')
book2 = Book('paper', 'Java')
book3 = Book('paper', 'C++')
book4 = Book('paper', 'CSS')
book5 = Book('paper', 'Javascript')

book1.reserved = True
book3.reserved = True

for book in [book1, book2, book3, book4, book5]:
    if book.reserved:
        print(
            f'Book name: {book.book_name}, author: {book.author}, pages: {book.number_page},'
            f'material: {book.material_pages}, Reserved: {book.reserved}'
        )
    else:
        print(
            f'Book name: {book.book_name}, author: {book.author}, pages: {book.number_page},'
            f'material: {book.material_pages}')


class StudentsBook(Book):
    objects = 'math'
    student_class = 9
    homework = True

    def __init__(self):
        super().__init__(200, 'Math')
        pass


student1 = StudentsBook()
student2 = StudentsBook()
student3 = StudentsBook()

student1.book_name = 'Algebra'
student1.author = 'Gauss'

student2.book_name = 'Algebra'
student2.author = 'Gauss'

student3.book_name = 'Algebra'
student3.author = 'Gauss'

student2.reserved = True

for student in [student1, student2, student3]:
    if student.reserved:
        print(
            f'Book name: {student.book_name}, author: {student.author}, pages: {student.number_page}, '
            f'object: {student.objects}, class: {student.student_class} Reserved: {student.reserved}'
        )
    else:
        print(
            f'Book name: {student.book_name}, author: {student.author}, pages: {student.number_page},'
            f'object: {student.objects} class: {student.student_class}'
        )
