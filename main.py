from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # SQLite database file
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Display a list of books
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = int(request.form['publication_year'])

        book = Book(title=title, author=author, publication_year=publication_year)
        db.session.add(book)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
