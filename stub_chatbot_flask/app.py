from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat():
    user = None
    bot  = None
    if request.method == 'POST':
        user = request.form['message']
        bot  = f"Echo bot: «{user}»"
    return render_template('index.html', user=user, bot=bot)

if __name__ == "__main__":
    # Levanta el servidor en 127.0.0.1:5000 con modo debug
    app.run(host="127.0.0.1", port=5000, debug=True)
