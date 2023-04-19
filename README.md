# streamlit_web_app
streamlit上で文字起こしを行うプログラムです。

# 開発

# 事前準備
・Python3.9以上がインストールされていること
・任意のフォルダを作成し、実行環境を作成すること
->以下のコマンドをcmdにて実行する。
1. 仮想環境を作成する。
python -m venv env
2. 仮想環境をアクティベートする。
.¥env¥Scripts¥activate

# 環境構築手順
1. ソースコードをダウンロードする。
2. 先程作成したフォルダで".¥env¥Scripts¥activate"を実行する。
2. ダウンロードフォルダを先程作成したフォルダに移動し、requirements.txt をインストールする。
-> pip install -r requirements.txt
3. streamlit run str_voice_to_text.py
-> ブラウザが立ち上がる

# 実施方法
1. openai社のサイトにアクセスし、APIキーを取得する
https://platform.openai.com/account/api-keys
2. 「openaiのAPIキーを入力してください」の下にあるテキストボックスに貼り付け
3. ファイルアップローダー箇所にて任意の音声または動画ファイルをアップロードする。
※ファイルサイズは200MBまでです。
4. しばらく待機すると、文字起こし結果とようやく結果が記載される。
