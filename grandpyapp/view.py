from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template('base.html')

@app.route('/api', methods=['POST'])
def api():
    # appel parser
    # appel APIs (google, wikipedia)
    user_question = request.form['question']

    print('question envoyé par l\'utilisateur : {question}'.format(question=user_question))

    return render_template('base.html', question=user_question)

if __name__ == "__main__":
    app.run()