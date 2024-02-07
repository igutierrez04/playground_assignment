from flask import Flask, render_template, redirect
app = Flask(__name__)

# not included but i wanted the user to be redirected straight into the "/play" URL
@app.route('/')
def home():
    return redirect('/play')

# Have the URL render 3 blue boxes
@app.route('/play')
def play():
    return render_template('index.html', times=3, color = "aqua")

# Have the URL render any amount of boxes inputed by the user
@app.route('/play/<int:num>')
def play_more(num):
    return render_template('index.html', times= num, color = "aqua")


# Have the URL render any amount of boxes and color of the users choosing
@app.route('/play/<int:num>/<string:color>')
def play_with_color(num, color):
    return render_template('index.html', times= num, color = color)

if __name__=="__main__":
    app.run(debug=True)
