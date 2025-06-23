# 🔗 HTML Link Generator v2

このアプリは、画像URLや任意のテキストをもとに、WordPressやHTMLで使えるリンクタグを簡単に生成できるツールです。  
Streamlit で構築されており、ブラウザ上でシンプルに動作します。

---

## 🚀 機能一覧

- 画像URLを入力すると、WordPress用の `<figure>` タグ付き画像リンクを生成
- 任意テキストとURLから `<a>` タグを生成（新しいタブで開く設定も可）
- コピー用ボタンでHTMLタグを一発コピー
- Enterキーでもコピー可能＆ポップアップで通知

---

## 💻 使用方法

```bash
# 仮想環境の作成と有効化（初回のみ）
python3 -m venv venv
source venv/bin/activate

# 依存ライブラリのインストール
pip install -r requirements.txt

# アプリの起動
streamlit run app.py