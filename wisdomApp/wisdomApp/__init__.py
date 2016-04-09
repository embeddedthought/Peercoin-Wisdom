from flask import Flask, render_template, url_for, redirect, abort,request,session

app = Flask(__name__)
app.config['SECRET_KEY'] = '';

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/chart/<exchange>/<pair>')
def chartpage(exchange,pair):
    return render_template("chart.html",exchange=exchange,pair=pair)

@app.route('/Journal')
def journal():
    user= ""
    return render_template('journal.html',user=user)

@app.route('/PeerReview')
def peerreview():
    pair = ""
    return render_template('peerreview.html',pair=pair)

@app.route('/Resources')
def resources():
    pair = ""
    return render_template('resources.html',pair=pair)

@app.route('/Explorer')
def explorer():
    return render_template('explorer.html')

@app.route('/PSA')
def assets():
    pair = ""
    return render_template('PSA.html',pair=pair)

@app.route('/signup', methods=['POST'])
def signup():
    session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@app.route('/message')
def message():
    if not 'username' in session:
        return abort(403)
    return render_template('message.html', username=session['username'], 
                                           message=session['message'])

if __name__ == '__main__':
    app.run()
