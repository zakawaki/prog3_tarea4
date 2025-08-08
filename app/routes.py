from app import app, contacts
from flask import render_template, request, redirect, url_for, session

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        return render_template('login.html', error='Credenciales incorrectas')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    contacts.append({
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone']
    })
    return redirect(url_for('dashboard'))

@app.route('/delete/<int:index>')
def delete_contact(index):
    contacts.pop(index)
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_contact(index):
    if index >= len(contacts):
        return "Contacto no encontrado", 404

    if request.method == 'POST':
        contacts[index]['name'] = request.form['name']
        contacts[index]['email'] = request.form['email']
        contacts[index]['phone'] = request.form['phone']
        return redirect(url_for('dashboard'))

    contact = contacts[index]
    return render_template('edit.html', contact=contact, index=index)



