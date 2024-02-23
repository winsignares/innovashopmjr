from flask import Flask, render_template

app = Flask(__name__, template_folder='config/templates')

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/login')
def admin_index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
