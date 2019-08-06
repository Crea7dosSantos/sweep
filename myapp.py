from flask import Flask

# flaskアプリケーションの作成
app = Flask(__name__)


# ルーティングを行い、アクションを指定する。
@app.route('/')
def index():
    return 'Hello World'


# flaskのアプリケーションを実行。引数のdebugにTrueを指定してデバッグモードにすることで、エラー時にブラウザで確認することができる。
app.run(debug=True)
