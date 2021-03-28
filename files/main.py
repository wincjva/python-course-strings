__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os


def clean_cache():
    dirname = os.path.dirname(__file__)
    folder = dirname + "\\cache\\"
    try:
        os.makedirs(folder)
    except FileExistsError:
        # directory already exists
        pass
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    print(
                        """dir encountered when removing files,
                        did not remove the dir:""",
                        file_path,
                    )
            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (file_path, e))


def cache_zip(path_to_zip_file, cachedir):
    clean_cache()
    # clean_cache takes no arguments as instructed
    # if it would, I would send 'path_to_zip_file' and 'cachedir'
    import zipfile

    with zipfile.ZipFile(path_to_zip_file, "r") as zip_ref:
        zip_ref.extractall(cachedir)
        print("extracted:", path_to_zip_file, "\n  to :", cachedir)


def cached_files():
    dirname = os.path.dirname(__file__)
    folder = dirname + "\\cache\\"
    onlyfiles = [
        folder + f
        for f in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, f))
    ]
    return onlyfiles


def find_password(onlyfiles):
    count = 0
    for fpath in onlyfiles:
        f = open(fpath, "r")
        if "password:" in f.read():
            print("World domination password found in file: ", fpath, "\n")
            password_text = open(fpath, "r").read()
        else:
            count += 1
    password_line = password_text.split("password: ")
    password_text = password_line[1].splitlines()
    world_domination_pass = password_text[0]  # ssht.. don't tell anyone
    print("World domination achieved:", world_domination_pass)
    return world_domination_pass
