import streamlit.web.cli as stcli
import os
import sys
import time


def streamlit_run():
    # pyinstallerでバンドルされたファイルにアクセスするため、sys._MEIPASSを使用
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller でバンドルされた場合、_MEIPASS を使ってリソースパスを取得
        src = os.path.join(sys._MEIPASS, "streamlit_exe/pg.py")
        print(src)
        # time.sleep(30)
    else:
        # 通常の開発環境の場合、相対パスでhome.pyを指定
        src = os.path.join(os.path.dirname(__file__), "streamlit_exe/pg.py")
        print(src)
    # Streamlitを実行するために引数を設定
    sys.argv = [
        "streamlit",
        "run",
        src,
        # "--server.port=8502",
        # "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())


if __name__ == "__main__":
    streamlit_run()
