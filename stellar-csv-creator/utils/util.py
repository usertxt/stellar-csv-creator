import os


def user_dir():
    if os.name == 'posix':
        return os.path.join(os.environ["HOME"], ".stellar-csv-creator")
    elif "APPDATA" in os.environ:
        return os.path.join(os.environ["APPDATA"], "Stellar CSV Creator")
