from flask import *

app = Flask(__name__)

a = 1

@app.route('/')
def hello_world():
    global a
    a += 1
    return f'''
    <html>
            <body>
                <h1>Здесь HTML разметка</h1>
                <p>Немного тектса тут и там</p>
                <p>{a}</p>
            </body>
        </html>
    '''

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/main')
def glavnaya():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
