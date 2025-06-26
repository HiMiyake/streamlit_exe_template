## 使用技術一覧
### 言語
- [Python 3.11.4(公式サイト)](https://www.python.org/downloads/release/python-3114/)

### フレームワーク
- [Streamlit](https://streamlit.io/)

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [gitのクローン](#gitのクローン)
3. [仮想環境の作成](#仮想環境の作成)
4. [パッケージのインストール](#パッケージのインストール)
5. [実行ファイル化の方法](#実行ファイル化の方法)

## プロジェクトについて
StreamlitはPython製のオープンソースWebアプリフレームワークです。 数行のコードを書くだけでインタラクティブなデータ可視化アプリを即時に構築できます。豊富なウィジェットと自動リロード機能によりデータ分析やダッシュボード開発を迅速に進められます。このプロジェクトは、StreamlitをPythonがインストールされてないPCでも動作するように実行ファイル形式にするテンプレートです。

## gitのクローン
ターミナルで以下のコマンドを実行。

プロジェクトフォルダを作成するディレクトリでリポジトリをクローン。
```
git clone http://10.21.30.60:3000/YosoGijyutsu/streamlit_exe_template.git
```

streamlit_exe_templateのフォルダが作成されるため、任意の名前にリネームする。しなくてもよい。

Visual Studio Code 等で"ファイル"->"フォルダを開く"で作成されたフォルダを開く。  
フォルダを右クリックし"Codeで開く"でもよい。


## 仮想環境の作成
ターミナルで以下のコマンドを実行。

仮想環境のフォルダを作成。
```
python -m venv env
```

仮想環境をアクティベート。
```
.\env\Scripts\activate
```

ちなみに、仮想環境を終了するコマンドは以下(ディアクティベート)
```
deactivate
```

## パッケージのインストール
ターミナルで以下のコマンドを実行。

pip自信をアップグレード(インターネット接続必要)。
```
python.exe -m pip install --upgrade pip
```

requirements.txtにあるパッケージをインストールする。
```
pip install -r requirements.txt
```


## 実行ファイル化の方法
ターミナルで以下のコマンドを実行。
```
pyinstaller your_app.spec --clean
```

