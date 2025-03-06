from flask import Flask, render_template, request

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def home():
    return render_template('index.html')

# Сторінка "Про нас"
@app.route('/about/<username>')
def about(username):
    return render_template('about.html', username=username)

# Сторінка з формою
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return render_template('form_result.html', name=name, email=email, message=message)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
