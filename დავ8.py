import sqlite3

conn = sqlite3.connect('books_db.sqlite3')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE bookk
             (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
              title VARCHAR(40),
              author VARCHAR(40),
              release_year INTEGER,
              price INTEGER)''');

cursor.execute('''INSERT INTO bookk (title, author, release_year, price)
                  VALUES ('ნარინჯისფერი ბიჭი', 'პატრის ლორენსი', 2022,15)''')
book_list = [
    ('ყვავების ფოსტა', ' თემურ ელიავა ', 2022, 11.95),
    ('სამოსელი პირველი', 'გურამ დოჩანაშვილი', 1975, 39),
    ('დიდოსტატის კონსტანტინეს მარჯვენა', 'კონსტანტინე გამსახურდია', 1938, 30),
    ('ტუმარ-მასპინძელი', 'ვაჟა ფშაველა', 1893, 14.99)
]
cursor.executemany('''
INSERT INTO bookk(title, author, release_year,price) VALUES(?, ?,?,?)
''', book_list)

conn.commit()
conn.close()

# N2
conn = sqlite3.connect('titanic.sqlite3')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE passenger
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              passenger_name VARCHAR(50),
              age INTEGER,
              sex VARCHAR(30),
              ticket  VARCHAR(30),
              cabin  INT);''')

name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
sex = input("Enter passenger sex (M/F): ")
ticket = input("passenger ticket number: ")
cabin = input("passenger cabin number: ")
cursor.execute('''INSERT INTO passenger(passenger_name, age, sex,ticket,cabin) VALUES(?,?,?,?,?)''', (name, age, sex, ticket, cabin))


travel = []
for i in range(3):
    pass_name = input("Enter passenger name:")
    pass_age = int(input("Enter passenger age: "))
    pass_sex = input("Enter passenger sex (M/F): ")
    pass_ticket = input("passenger ticket number: ")
    pass_cabin = int(input("passenger cabin number: "))
    all = (pass_name, pass_age, pass_sex, pass_ticket, pass_cabin)
    travel.append(all)
cursor.executemany("INSERT INTO passenger(passenger_name, age, sex, ticket, cabin) VALUES (?,?,?,?,?)", travel)


conn.commit()
conn.close()


#N3
class Movie:
    def __init__(self, title, genre, year, imdb):
        self.title = title
        self.genre = genre
        self.year = year
        self.imdb = imdb

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Year: {self.year}, IMDB: {self.imdb}"


conn = sqlite3.connect('movies.sqlite3')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE movies
             (movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
              title VARCHAR(100),
              genre VARCHAR(50),
              yearr INTEGER,
              imdb  FLOAT);''')


movie1 = Movie("The Lord of the Ring", "Drama", 2003, 9.3)
cursor.execute("INSERT INTO movies (title, genre, yearr, imdb) VALUES (?, ?, ?, ?)",
               (movie1.title, movie1.genre, movie1.year, movie1.imdb))

movie2 = Movie("The Godfather", "Crime", 1972, 9.2)
movie3 = Movie("The Dark Knight", "Action", 2008, 9.0)
movie4 = Movie("titanic", "drama", 1997, 8.9)

movie_list = [(movie2.title, movie2.genre, movie2.year, movie2.imdb),
              (movie3.title, movie3.genre, movie3.year, movie3.imdb),
              (movie4.title, movie4.genre, movie4.year, movie4.imdb)]

cursor.executemany("INSERT INTO movies (title, genre, yearr, imdb) VALUES (?, ?, ?, ?)", movie_list)

conn.commit()
conn.close()


