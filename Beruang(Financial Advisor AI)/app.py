from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/register')
def register():
    return redirect(url_for('name'))


@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('age'))
    return render_template('name.html')


@app.route('/age', methods=['GET', 'POST'])
def age():
    if 'name' not in session:
        return redirect(url_for('name'))

    if request.method == 'POST':
        session['age'] = request.form.get('age')
        return redirect(url_for('occupation'))
    return render_template('age.html', name=session['name'])


@app.route('/occupation', methods=['GET', 'POST'])
def occupation():
    if 'age' not in session:
        return redirect(url_for('age'))

    if request.method == 'POST':
        session['occupation'] = request.form.get('occupation')
        return redirect(url_for('financial'))
    return render_template('occupation.html', name=session['name'])


@app.route('/financial', methods=['GET', 'POST'])
def financial():
    if 'occupation' not in session:
        return redirect(url_for('occupation'))

    if request.method == 'POST':
        # Process all financial data here
        session['income'] = request.form.get('income')
        session['savings'] = request.form.get('savings')
        session['expenses'] = request.form.get('expenses')
        return redirect(url_for('dashboard'))  # You'll create this later

    return render_template('financial.html', name=session['name'])


@app.route('/login')
def login():
    return "Login page will be here"  # You can implement this later


if __name__ == '__main__':
    app.run(debug=True)