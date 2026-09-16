from flask import Flask, render_template, request

app = Flask(__name__)


def check_grammar(text):
    corrections = {
        "She go to school yesterday.": "She went to school yesterday.",
        "He go to school every day.": "He goes to school every day.",
        "I has a book.": "I have a book.",
        "They is happy.": "They are happy.",
        "He have a car.": "He has a car.",
        "She have a pen.": "She has a pen.",
        "They was happy.": "They were happy.",
        "I is a student.": "I am a student.",
        "We is ready.": "We are ready.",
        "He don't like it.": "He doesn't like it."
    }

    text = text.strip()

    if text in corrections:
        return corrections[text]

    return "No correction found."


@app.route("/", methods=["GET", "POST"])
def home():
    text = ""
    result = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        result = check_grammar(text)

    return render_template("index.html", text=text, result=result)


if __name__ == "__main__":
    app.run(debug=True)