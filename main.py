 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memories.db'
db = SQLAlchemy(app)

# Define the Memory model
class Memory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Create the database tables
db.create_all()

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to display memories
@app.route('/memories')
def memories():
    memories = Memory.query.all()
    return render_template('memories.html', memories=memories)

# Define the route to add a new memory
@app.route('/add_memory', methods=['POST'])
def add_memory():
    title = request.form['title']
    description = request.form['description']
    new_memory = Memory(title=title, description=description)
    db.session.add(new_memory)
    db.session.commit()
    return redirect(url_for('memories'))

# Define the route to edit a memory
@app.route('/edit_memory/<int:memory_id>', methods=['GET', 'POST'])
def edit_memory(memory_id):
    memory = Memory.query.get_or_404(memory_id)
    if request.method == 'POST':
        memory.title = request.form['title']
        memory.description = request.form['description']
        db.session.commit()
        return redirect(url_for('memories'))
    return render_template('edit_memory.html', memory=memory)

# Define the route to delete a memory
@app.route('/delete_memory/<int:memory_id>')
def delete_memory(memory_id):
    memory = Memory.query.get_or_404(memory_id)
    db.session.delete(memory)
    db.session.commit()
    return redirect(url_for('memories'))

# Run the app
if __name__ == '__main__':
    app.run()
