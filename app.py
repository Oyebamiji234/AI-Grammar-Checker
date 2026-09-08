from flask import Flask, render_template, request

app = Flask(__name__)


def check_grammar(text):
    corrections = {
    "She go to school yesterday.": "She went to school yesterday.",
    "He go to school every day.": "He goes to school every day.",
    "They is happy.": "They are happy.",
    "I is a student.": "I am a student.",
    "She are my friend.": "She is my friend.",
    "He don't like rice.": "He doesn't like rice.",
    "I has a book.": "I have a book.",
    "She have a car.": "She has a car.",
    "They was playing football.": "They were playing football.",
    "We is going home.": "We are going home."
}
    

    cleaned_text = text.strip().lower().rstrip(".!?")

    return corrections.get(cleaned_text, "No correction found.")


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