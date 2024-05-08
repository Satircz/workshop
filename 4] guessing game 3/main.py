from flask import Flask, request, render_template


app = Flask(__name__)
min_guess = 0
max_guess = 1000




@app.route("/")
def guess_number():
    global min_guess, max_guess
    return render_template("get.html",min_guess=min_guess, max_guess=max_guess, new_guess=500)

@app.route("/", methods=["POST"])
def guessing_numbers():
    global min_guess, max_guess
    current = int(((max_guess - min_guess) / 2) + min_guess)
    user_input = request.form["user_input"]
    if user_input == "too big":
        max_guess = current
    elif user_input == "too small":
        min_guess = current
    else:
        return "You WIN"

    new_guess = int(((max_guess - min_guess) / 2) + min_guess)
    return render_template("get.html", min_guess=min_guess, max_guess=max_guess, new_guess=new_guess)



if __name__ == '__main__':
    app.run(debug=True)