# streamlit_app.py — Streamlit Community Cloud 部署入口
import streamlit as st
import sys
import os

# 将项目根目录加入 Python 路径，确保可导入其他模块
sys.path.insert(0, os.path.dirname(__file__))

# ======================================================
# 页面基础配置（必须是第一个 Streamlit 调用）
# ======================================================
st.set_page_config(
    page_title="LunaTV",
    page_icon="📺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ======================================================
# 如果 LunaTV 主逻辑在独立文件中，用以下方式引入：
# 方式 A：直接导入主模块（推荐）
# ======================================================
# from luna_tv import main  # 替换为实际模块名
# main()

# ======================================================
# 方式 B：如果原项目入口是 main.py 或 app.py，
# 用 exec 动态执行（兼容性最强）
# ======================================================
# with open("main.py", "r", encoding="utf-8") as f:
#     exec(f.read())

# ======================================================
# 方式 C：如果 LunaTV 已经是 streamlit 脚本，
# 直接在此文件内写完整逻辑或复制粘贴过来
# ======================================================

# --- 示例：LunaTV 应用框架 ---
def main():
    st.title("🌙 LunaTV")
    st.markdown("---")

    # 侧边栏
    with st.sidebar:
        st.header("频道列表")
        channel = st.selectbox(
            "选择频道",
            options=["直播频道 1", "直播频道 2", "点播内容"],
        )
        st.info("由 LunaTV 提供支持")

    # 主内容区
    st.subheader(f"当前：{channel}")

    # 如需播放 M3U8/RTMP 流，可嵌入 HTML 播放器
    video_url = st.text_input("输入视频/直播流地址（M3U8 / MP4）", placeholder="https://...")
    if video_url:
        st.video(video_url)
    else:
        st.info("请在左侧选择频道或手动输入流媒体地址")

if __name__ == "__main__" or True:
    main()
