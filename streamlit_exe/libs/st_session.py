# --- import ---
# standard library

# pip
import streamlit as st

# my libraries


class SessionStateManager:
    def __init__(self):
        """初期化時にセッションステートが存在しないキーをデフォルト値でセット"""
        if "user" not in st.session_state:
            st.session_state["user"] = {}

    def set(self, key, value):
        """セッションステートに値をセット"""
        st.session_state[key] = value

    def get(self, key, default=None):
        """セッションステートから値を取得（存在しない場合はデフォルト値を返す）"""
        return st.session_state.get(key, default)

    def set_user(self, key, value):
        """セッションステートに値をセット"""
        st.session_state["user"][key] = value

    def get_user(self, key, default=None):
        """セッションステートから値を取得（存在しない場合はデフォルト値を返す）"""
        return st.session_state["user"].get(key, default)

    def get_user_all(self, default=None):
        """セッションステートから値を取得（存在しない場合はデフォルト値を返す）"""
        return st.session_state.get("user", default)

    def remove_user(self, key):
        """指定したキーをセッションステートから削除"""
        if key in st.session_state["user"]:
            del st.session_state["user"][key]

    def clear_user(self):
        """セッションステートをクリア"""
        st.session_state["user"] = {}

    def on_change(self, dst_user_key, src_session_state_key):
        """セッションステートの値が変更されたときの処理"""
        if src_session_state_key is not None:
            self.set_user(dst_user_key, st.session_state[src_session_state_key])

    def on_change_user(self, dstuser_key, src_value):
        """セッションステートの値が変更されたときの処理"""
        self.set_user(dstuser_key, src_value)
