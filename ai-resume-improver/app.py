from flask import Flask, request, render_template

app = Flask(__name__)

def improve_text(resume_text):
    improved_lines = []
    lines = resume_text.split("\n")

    for line in lines:
        line = line.replace("did", "developed")
        line = line.replace("know", "proficient in")
        line = line.replace("worked on", "implemented")
        line = line.replace("made", "built")

        improved_lines.append("• " + line)

    return "\n".join(improved_lines)


@app.route("/", methods=["GET", "POST"])
def home():
    improved = ""

    if request.method == "POST":
        resume_text = request.form["resume"]
        improved = improve_text(resume_text)

    return render_template("index.html", improved=improved)


if __name__ == "__main__":
    app.run(debug=True)