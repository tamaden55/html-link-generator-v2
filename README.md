# 🔗 HTML Link Generator v2

このアプリは、画像URLや任意のテキストをもとに、WordPressやHTMLで使えるリンクタグを簡単に生成できるツールです。

## 🌐 オンライン版

**GitHub Pages**: [https://yourusername.github.io/html-link-generator-v2/](https://yourusername.github.io/html-link-generator-v2/)

**Streamlit Cloud**: [https://html-link-generator-v2-kcvfgrkbanmavsgykshgga.streamlit.app/](https://html-link-generator-v2-kcvfgrkbanmavsgykshgga.streamlit.app/)

---

## 🚀 機能一覧

- 画像URLを入力すると、WordPress用の `<figure>` タグ付き画像リンクを生成
- 任意テキストとURLから `<a>` タグを生成（新しいタブで開く設定も可）
- コピー用ボタンでHTMLタグを一発コピー
- Enterキーでもコピー可能＆ポップアップで通知
- 完全にレスポンシブ対応（モバイル・タブレット・デスクトップ）

---

## 💻 GitHub Pagesでの使用方法

### 1. このリポジトリをフォーク
1. 右上の「Fork」ボタンをクリック
2. あなたのGitHubアカウントにリポジトリをコピー

### 2. GitHub Pagesを有効化
1. フォークしたリポジトリの「Settings」タブをクリック
2. 左サイドバーの「Pages」をクリック
3. Source を「GitHub Actions」に設定
4. 自動デプロイが開始されます

### 3. アクセス
`https://yourusername.github.io/html-link-generator-v2/` でアクセス可能

---

## 🔧 ローカル開発（Streamlit版）

```bash
# 仮想環境の作成と有効化（初回のみ）
python3 -m venv venv
source venv/bin/activate

# 依存ライブラリのインストール
pip install -r requirements.txt

# アプリの起動
streamlit run app.py
```

---

## 📁 ファイル構成

```
html-link-generator-v2/
├── index.html              # 静的版（GitHub Pages用）
├── app.py                  # Streamlit版
├── requirements.txt        # Python依存関係
├── .github/workflows/      # GitHub Actions設定
│   └── deploy.yml
├── .streamlit/            # Streamlit設定
│   └── config.toml
├── Procfile               # Heroku/Railway用
├── railway.json           # Railway設定
└── README.md
```

---

## 🌟 特徴

- **静的ホスティング対応**: GitHub Pages、Netlify、Vercel、AWS S3など
- **動的ホスティング対応**: Streamlit Cloud、Railway、Render、Heroku
- **レスポンシブデザイン**: すべてのデバイスで快適に使用可能
- **高速**: 静的版は瞬時に読み込み、サーバー不要
- **常時オンライン**: 静的版はスリープしない

---

## 🎨 カスタマイズ

`index.html` のCSSセクションを編集することで、デザインを自由にカスタマイズできます。

---

## 📱 モバイル対応

スマートフォンやタブレットでも快適に使用できるよう、完全レスポンシブ対応しています。

---

## 🔗 関連リンク

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Streamlit Documentation](https://docs.streamlit.io/)