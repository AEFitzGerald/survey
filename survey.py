from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Wonder World'# set a secret key for security purposes


# write info to session in this method- aka get data to store
@app.route('/')
def survey():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def get_survey():
    print("Got Post Info")
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['location'] = request.form['location']
    session['comments'] = request.form['comments']
    session['language'] = request.form['language']

    return redirect('/results')

#session data is available directly in our templates
@app.route('/results')
def show_data():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(debug=True)