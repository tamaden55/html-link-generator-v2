# 🔗 HTML Link Generator v2

画像URLや任意のテキストから、WordPressやHTMLで使えるリンクタグを簡単に生成できるツールです。

## 🌐 ライブデモ

### メインサイト（推奨）
**GitHub Pages**: [https://tamaden55.github.io/html-link-generator-v2/](https://tamaden55.github.io/html-link-generator-v2/)
- ⚡ 高速読み込み（静的サイト）
- 🌐 常時オンライン
- 📱 完全レスポンシブ対応

### バックアップサイト
**Streamlit Cloud**: [https://html-link-generator-v2-kcvfgrkbanmavsgykshgga.streamlit.app/](https://html-link-generator-v2-kcvfgrkbanmavsgykshgga.streamlit.app/)
- 🐍 Python/Streamlit版
- ⏰ 初回アクセス時に少し時間がかかる場合があります

---

## ✨ 主な機能

### 🖼️ 画像リンク生成
- 画像URLを入力するだけで、WordPress用の `<figure>` タグ付き画像リンクを自動生成
- 適切な画像サイズ指定（`?w=769`）とクラス名を含んだ完全なHTMLコード

### 📝 テキストリンク生成
- 任意のテキストとURLから `<a>` タグを生成
- 新しいタブで開く設定（`target="_blank"`）のオン/オフ切り替え可能

### 🚀 使いやすさ
- 📋 ワンクリックでクリップボードにコピー
- ⌨️ Enterキーでも瞬時にコピー可能
- 🔔 コピー完了の視覚的な通知
- 📱 全デバイス対応（スマホ・タブレット・PC）

---

## 🛠️ 自分用にカスタマイズする方法

### 1. このリポジトリをフォーク
1. 右上の「Fork」ボタンをクリック
2. あなたのGitHubアカウントにリポジトリをコピー

### 2. GitHub Pagesを有効化
1. フォークしたリポジトリの「Settings」タブをクリック
2. 左サイドバーの「Pages」をクリック
3. Source を「Deploy from a branch」に設定
4. Branch を「main」、フォルダを「/ (root)」に設定
5. 「Save」をクリック

### 3. あなた専用のサイトにアクセス
`https://あなたのユーザー名.github.io/html-link-generator-v2/` でアクセス可能

### 4. カスタマイズ
`index.html` を編集して、デザインや機能を自由にカスタマイズできます。

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

## 🌟 技術的特徴

### 🚀 パフォーマンス
- **超高速**: 静的HTMLファイルで瞬時に読み込み
- **サーバーレス**: CDN配信でグローバルに高速アクセス
- **常時稼働**: スリープしない、ダウンタイムなし

### 🏗️ 柔軟なデプロイ
- **静的ホスティング**: GitHub Pages、Netlify、Vercel、AWS S3など
- **動的ホスティング**: Streamlit Cloud、Railway、Render、Heroku
- **ハイブリッド構成**: 静的版と動的版の両方を提供

### 📱 デバイス対応
- **完全レスポンシブ**: スマートフォンからデスクトップまで
- **タッチ操作対応**: モバイルデバイスでの快適な操作
- **高解像度対応**: Retinaディスプレイにも対応

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