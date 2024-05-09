from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cs')
def cs():
    return render_template('cs.html')

@app.route('/fb')
def fb():
    return redirect('https://www.facebook.com/p/St-Michaels-PU-College-Rajivnagar-Mysore-100064244760588/')

@app.route('/address')
def address():
    return redirect("https://www.google.com/maps/place/ST.+MICHAEL'S+PU+COLLEGE/@12.332346,76.6826403,17z/data=!3m1!4b1!4m6!3m5!1s0x3baf7053556e9d63:0x944c16c9f5cd8cb!8m2!3d12.332346!4d76.6875112!16s%2Fg%2F11g8j_wntf?entry=ttu")

if __name__ == "__main__":
  app.run(debug=True)