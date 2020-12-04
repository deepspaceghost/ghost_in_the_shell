#!/usr/bin/python3

import argparse
import os
import shutil


def copy_file(filename, dirname):
    """
    """

    src = filename
    dest = dirname
    shutil.copy(src, dest)
    print("{0} has been copied.".format(filename))


def create_dir(dirname):
    """
    """

    if not os.path.isdir(dirname):
        path = os.path.join(os.getcwd(), dirname)
        os.mkdir(path)
        print("{0} has been created.".format(dirname))

    else:
        print("Bro, what is you doin'?")
        print("{0} already exists.".format(dirname))


def create_file(filename, content):
    """
    """

    if not os.path.exists(filename):
        f = open(filename, "w")
        f.write(content)
        f.close()
        print("{0} has been created.".format(filename))

    else:
        print("Tell me something I don't know.")
        print("{0} already exists.".format(filename))


def delete_dir(dirname):
    """
    """

    if os.path.isdir(dirname):
        os.rmdir(dirname)
        print("{0} has been deleted.".format(dirname))

    else:
        print("{0} does not exist.".format(dirname))


def delete_file(filename):
    """
    """

    if os.path.isfile(filename):
        os.remove(filename)
        print("{0} has been deleted.".format(filename))

    else:
        print("Who?")
        print("{0} does not exists.".format(filename))


def find_file(filename, search_path):

    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            print("Found it!")
            print(result.append(os.path.join(root, filename)))

        elif filename not in files:
            print("Call off the search.")
            print("{0} could not be found.".format(filename))


def rename_dir(olddirname, newdirname):
    """
    """

    source = olddirname
    dest = newdirname
    if os.path.exists(olddirname):
        os.rename(source, dest)
        print("This directory has been renamed.")

    elif not os.path.exists(olddirname):
        print("Let me see those directions.")
        print("{0} cannot be found.".format(olddirname))

    elif os.path.exists(newdirname):
        print("Let me see those directions.")
        print("{0} is somewhere else.".format(newdirname))


def rename_file(oldfilename, newfilename):
    """
    """

    source = oldfilename
    dest = newfilename
    if os.path.exists(oldfilename):
        os.rename(source, dest)
        print("This file has been renamed.")

    elif not os.path.exists(oldfilename):
        print("Let me see those directions.")
        print("{0} cannot be found.".format(oldfilename))

    elif os.path.exists(newfilename):
        print("Let me see those directions.")
        print("{0} is somewhere else.")


def main():
    """
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--copy_file",
                        action="store",
                        nargs=2,
                        help="Usage: ./puppet_master.py --copy_file [filename] [dirname]",
                        dest="copy_file_args")
    parser.add_argument("--create_dir",
                        action="store",
                        nargs=1,
                        help="Usage: ./puppet_master.py --create_dir [dirname]",
                        dest="create_dir_args")
    parser.add_argument("--create_file",
                        action="store",
                        nargs=2,
                        help="Usage: ./puppet_master.py --create_file [filename] [content]",
                        dest="create_file_args")
    parser.add_argument("--delete_dir",
                        action="store",
                        nargs=1,
                        help="Usage: ./puppet_master.py --delete_dir [dirname]",
                        dest="delete_dir_args")
    parser.add_argument("--delete_file",
                        action="store",
                        nargs=1,
                        help="Usage: ./puppet_master.py --delete_file [filename]",
                        dest="delete_file_args")
    parser.add_argument("--find_file",
                        action="store",
                        nargs=2,
                        help="Usage: ./puppet_master.py --find_file [filename] [search_path]",
                        dest="find_file_args")
    parser.add_argument("--rename_dir",
                        action="store",
                        nargs=2,
                        help="Usage: ./puppet_master.py --rename_dir [olddirname] [newdirname]",
                        dest="rename_dir_args")
    parser.add_argument("--rename_file",
                        action="store",
                        nargs=2,
                        help="Usage: ./puppet_master.py --rename_file [oldfilename] [newfilename]",
                        dest="rename_file_args")

    args = parser.parse_args()

    if args.copy_file_args:
        filename = args.copy_file_args[0]
        dirname = args.copy_file_args[1]
        copy_file(filename, dirname)

    elif args.create_dir_args:
        dirname = args.create_dir_args[0]
        create_dir(dirname)

    elif args.create_file_args:
        filename = args.create_file_args[0]
        content = args.create_file_args[1]
        create_file(filename, content)

    elif args.delete_dir_args:
        dirname = args.delete_dir_args[0]
        delete_dir(dirname)

    elif args.delete_file_args:
        filename = args.delete_file_args[0]
        delete_file(filename)

    elif args.find_file_args:
        filename = args.find_files_args[0]
        search_path = args.find_files_args[1]
        find_file(filename, search_path)

    elif args.rename_dir_args:
        olddirname = args.rename_dir_args[0]
        newdirname = args.rename_dir_args[1]
        rename_dir(olddirname, newdirname)

    elif args.rename_file_args:
        oldfilename = args.rename_file_args[0]
        newfilename = args.rename_file_args[1]
        rename_file(oldfilename, newfilename)


if __name__ == "__main__":
    """
    """

    main()
