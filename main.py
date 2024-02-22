from flask import Flask, render_template


app = Flask(__name__)


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof.lower())


@app.route("/list_prof/<lst>")
def list_prof(lst):
    professions = ["инженер", "строитель", "врач", "пожарный"]
    return render_template("list_prof.html", lst=lst, professions=professions)


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")