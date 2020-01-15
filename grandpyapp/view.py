from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template('base.html')

@app.route('/api')
def api():
    # appel parser
    # appel APIs (google, wikipedia)
    return

if __name__ == "__main__":
    app.run()