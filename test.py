from flask import request, redirect

@app.route('https://tonnygol.github.io/TestForGitPages/', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('https://tonnygol.github.io/TestForGitPages/')
