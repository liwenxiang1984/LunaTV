import streamlit as st

LUNATV_REPO = "https://github.com/liwenxiang1984/LunaTV"
DEPLOYED_LUNATV_URL = "https://your-lunatv-instance.example.com"  # 改成你自己的 LunaTV 部署地址

st.set_page_config(
    page_title="LunaTV Launcher",
    page_icon="📺",
    layout="wide"
)

st.title("📺 LunaTV on Streamlit")
st.caption("这是一个用于 Streamlit Cloud 的 LunaTV 导航与说明页面，不是原生 LunaTV 运行环境。")

st.warning(
    "LunaTV 是 Next.js 项目，不能直接作为 Streamlit 应用运行在 share.streamlit.io / streamlit.app。"
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("项目仓库")
    st.markdown(f"[打开 LunaTV GitHub 仓库]({LUNATV_REPO})")

with col2:
    st.subheader("在线实例")
    st.markdown(f"[打开已部署的 LunaTV 实例]({DEPLOYED_LUNATV_URL})")

st.divider()

st.subheader("部署说明")
st.markdown(
    """
1. 把这个 `streamlit_app.py` 上传到你自己的 GitHub 仓库根目录。  
2. 在 Streamlit Community Cloud 里选择该仓库。  
3. Main file path 填 `streamlit_app.py`。  
4. 点击 Deploy。  
5. 如果你要真正运行 LunaTV，请把 LunaTV 部署到支持 Next.js 的平台，再把地址填到 `DEPLOYED_LUNATV_URL`。  
"""
)

st.divider()

st.subheader("为什么不能直接运行原项目")
st.code(
    """LunaTV -> Next.js / TypeScript / Tailwind
Streamlit Cloud -> Python / streamlit_app.py""",
    language="text"
)

st.info(
    "如果你已经有可访问的 LunaTV 网址，这个页面可以作为入口页、说明页或书签页来使用。"
)

with st.expander("可选：显示在线实例（若目标站点允许 iframe）"):
    st.write("部分站点会禁止被 iframe 嵌入；如果打不开，使用上方链接直接访问。")
    iframe_html = f'''
    <iframe
        src="{DEPLOYED_LUNATV_URL}"
        width="100%"
        height="900"
        style="border:1px solid #ddd; border-radius:12px;"
    ></iframe>
    '''
    st.components.v1.html(iframe_html, height=920, scrolling=True)
