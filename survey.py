from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Wonder World'# set a secret key for security purposes


@app.route('/')
def survey():
    return render_template('index.html')

#write data to session
@app.route('/process', methods=['POST'])
def process():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['location'] = request.form['location']
    session['comments'] = request.form['comments']
    session['language'] = request.form['language']

    return redirect('/results')

#session data is available results template
@app.route('/results')
def show_data():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)