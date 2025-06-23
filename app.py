import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="リンク生成ツール", layout="centered")

st.title("🔗 リンク生成ツール")

tab1, tab2 = st.tabs(["🖼️ 画像リンク生成", "📝 テキストリンク生成"])

# --- タブ1：画像リンク ---
with tab1:
    st.subheader("画像URLを入力してください")
    url = st.text_input(
        "画像のURL", placeholder="https://example.com/image.jpg", key="image_url"
    )

    if url:
        p1 = '<figure class="wp-block-image size-large"><a href="'
        p2 = '"><img src="'
        p3 = '?w=769" alt="" class="wp-image-10478"/></a></figure>'
        result = p1 + url + p2 + url + p3

        st.markdown("### ✅ 生成されたHTMLコード")
        st.text_area("コード", result, height=100, key="image_result")

        components.html(
            f"""
        <script>
        function copyImageText() {{
            const text = `{result}`;
            navigator.clipboard.writeText(text).then(function() {{
                alert("✅ 画像リンクをコピーしました！");
            }});
        }}
        document.addEventListener("keydown", function(e) {{
            if (e.key === "Enter") {{
                e.preventDefault();
                copyImageText();
            }}
        }});
        </script>
        <button onclick="copyImageText()">📋 コピーする</button>
        """,
            height=100,
        )


# --- タブ2：テキストリンク ---
with tab2:
    st.subheader("テキストリンクを生成")
    target = st.text_input(
        "リンクにするテキスト", placeholder="ここをクリック", key="link_text"
    )
    link_url = st.text_input(
        "リンク先のURL", placeholder="https://example.com", key="link_url"
    )
    new_tab = st.checkbox("新しいタブで開く", value=False)

    if target and link_url:
        target_attr = ' target="_blank"' if new_tab else ""
        link = f'<a href="{link_url}"{target_attr}>{target}</a>'

        st.markdown("### ✅ 生成されたHTMLコード")
        st.text_area("コード", link, height=80, key="text_link_result")

        components.html(
            f"""
        <script>
        function copyTextLink() {{
            const text = `{link}`;
            navigator.clipboard.writeText(text).then(function() {{
                alert("✅ テキストリンクをコピーしました！");
            }});
        }}
        document.addEventListener("keydown", function(e) {{
            if (e.key === "Enter") {{
                e.preventDefault();
                copyTextLink();
            }}
        }});
        </script>
        <button onclick="copyTextLink()">📋 コピーする</button>
        """,
            height=100,
        )
