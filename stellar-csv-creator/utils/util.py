import os
import json
import stat
import logging
import platform
import subprocess


def open_folder(path):
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def user_dir():
    if os.name == "posix":
        return os.path.join(os.environ["HOME"], ".stellar-csv-creator")
    elif "APPDATA" in os.environ:
        return os.path.join(os.environ["APPDATA"], "Stellar CSV Creator")


def make_dir(path, allow_symlink=True):
    if not os.path.exists(path):
        if not allow_symlink and os.path.islink(path):
            raise Exception("Dangling link: " + path)
        os.mkdir(path)
        os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)


def setup_config():
    config_file = os.path.join(user_dir(), "config.json")
    if not os.path.exists(config_file):
        config = {
                  "APP": {
                    "THEME": "default"
                  },
                  "CSV": {
                    "MIN_THRESH": "1",
                    "MAX_THRESH": "2",
                    "SOURCE": "Source",
                    "MEMO": "Memo",
                    "DESTINATION": os.path.join(user_dir(), "CSV Files")
                  }
                }
        with open(config_file, "w") as f:
            f.write(json.dumps(config, indent=2))
        logging.info(f"Config not found. Creating config file in {user_dir()}")
    else:
        logging.info("Config found. Skipping creation.")
