from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", contents=contents())


def contents():
    lines = []
    for i in range(3):
        line = []
        for j in range(4):
            item = {}
            item['title'] = f"Title-{i}{j}"
            line.append(item)
        lines.append(line)
    return lines


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2572, debug=True)
