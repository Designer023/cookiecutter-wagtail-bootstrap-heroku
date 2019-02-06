import os
import binascii


def set_secret_key():
    flag="!!!SET DJANGO_SECRET_KEY!!!"
    value = binascii.hexlify(os.urandom(24)).decode('utf-8')

    file_path = os.path.join(".env")


    with open(file_path, "r+") as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()


def append_to_project_gitignore():
    os.rename('_gitignore', '.gitignore')


def main():

    set_secret_key()
    append_to_project_gitignore()


if __name__ == "__main__":
    main()