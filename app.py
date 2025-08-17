from flask import Flask

from src import config

app = Flask(__name__)

# config.pyに定義されている、SQLAlchemyの初期化処理を呼び出す。
config.init_sql_alchemy(app)

from flask import Flask, request

app = Flask(__name__)

# 得点を保存するリスト（今回はDBを使わずに簡単に）
scores = []

@app.route("/")
def index():
    html = """
    <html>
    <head><title>カラオケ得点記録</title></head>
    <body style="font-family:Arial; text-align:center;">
        <h1>🎤 カラオケ得点記録 🎶</h1>

        <form action="/add" method="post">
            <input type="text" name="name" placeholder="名前" required>
            <input type="text" name="song" placeholder="曲名" required>
            <input type="number" name="score" placeholder="点数" required>
            <button type="submit">記録！</button>
        </form>

        <h2>記録一覧</h2>
        <table border="1" style="margin:auto; border-collapse:collapse;">
            <tr><th>名前</th><th>曲名</th><th>得点</th></tr>
    """
    for s in scores:
        html += f"<tr><td>{s['name']}</td><td>{s['song']}</td><td>{s['score']}</td></tr>"

    avg = round(sum([s["score"] for s in scores]) / len(scores), 2) if scores else 0
    html += f"</table><h3>平均点: {avg}</h3></body></html>"
    return html

@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    song = request.form.get("song")
    score = request.form.get("score")

    if name and song and score:
        scores.append({"name": name, "song": song, "score": int(score)})

    return index()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"
