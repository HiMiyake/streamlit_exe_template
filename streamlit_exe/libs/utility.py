# standard library
import sys
from pathlib import Path
import shutil


def is_launch_with_exe() -> bool:
    """アプリが .exe 形式で実行されているかを判定"""
    return getattr(sys, "frozen", False)


def get_root_directory() -> Path:
    """スクリプトまたは実行ファイルのルートディレクトリを取得"""
    return Path(sys.executable).parent if is_launch_with_exe() else Path.cwd()


def my_find(lst: list, x) -> int:
    """リスト内の要素のインデックスを取得（存在しない場合は 0）"""
    return lst.index(x) if x in lst else 0


def clear_folder(folder_path: Path):
    if not folder_path.is_dir():
        raise ValueError(f"{folder_path} is not a valid directory.")

    for item in folder_path.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()  # ファイルまたはシンボリックリンクを削除
        elif item.is_dir():
            shutil.rmtree(item)  # フォルダを再帰的に削除
