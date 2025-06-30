import os
import shutil
import tempfile
import ctypes
from pathlib import Path

def clear_temp_files():
    temp_dir = tempfile.gettempdir()
    print(f"Cleaning temp directory: {temp_dir}")
    try:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Failed to delete file {file_path}: {e}")
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Deleted directory: {dir_path}")
                except Exception as e:
                    print(f"Failed to delete directory {dir_path}: {e}")
    except Exception as e:
        print(f"Error cleaning temp files: {e}")

def clear_recycle_bin():
    # خاص بنظام ويندوز
    try:
        print("Emptying recycle bin...")
        SHERB_NOCONFIRMATION = 0x00000001
        SHERB_NOPROGRESSUI = 0x00000002
        SHERB_NOSOUND = 0x00000004

        result = ctypes.windll.shell32.SHEmptyRecycleBinW(None, None,
            SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND)

        if result == 0:
            print("Recycle bin emptied successfully.")
        else:
            print(f"Failed to empty recycle bin. Error code: {result}")
    except Exception as e:
        print(f"Error clearing recycle bin: {e}")

def clear_cache_folder(cache_folder):
    print(f"Cleaning cache folder: {cache_folder}")
    cache_path = Path(cache_folder)
    if not cache_path.exists():
        print("Cache folder does not exist.")
        return
    try:
        for item in cache_path.iterdir():
            try:
                if item.is_file():
                    item.unlink()
                    print(f"Deleted file: {item}")
                elif item.is_dir():
                    shutil.rmtree(item)
                    print(f"Deleted directory: {item}")
            except Exception as e:
                print(f"Failed to delete {item}: {e}")
    except Exception as e:
        print(f"Error cleaning cache folder: {e}")

if __name__ == "__main__":
    print("Starting System Cleaner Py...")

    clear_temp_files()

    # فقط على ويندوز
    if os.name == 'nt':
        clear_recycle_bin()
    else:
        print("Recycle bin cleaning is supported only on Windows.")

    # مثال على مجلد كاش - يمكنك تعديله حسب حاجتك
    example_cache_folder = os.path.expanduser("~/.cache")
    clear_cache_folder(example_cache_folder)

    print("Cleaning completed.")
