#!/usr/bin/python3

import argparse
import logging
import os
import shutil


print("Setting up logging...")
log_path = os.path.join(os.getcwd(), "logs/puppet_master.log")
if not os.path.isdir("logs"):
    print("Logging directory not found.")
    print("Creating logging directory...")
    log_dir_path = os.path.join(os.getcwd(), "logs")
    os.mkdir(log_dir_path)
    f = open(log_path, "x")
    f.close()

elif not os.path.exists(log_path):
    f = open(log_path, "x")
    f.close()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=log_path)

logger = logging.getLogger()


def copy_file(filename, dirname):
    """
    """

    print("Copying file...")
    logger.info("Copying file...")
    src = filename
    dest = dirname
    if os.path.isfile(filename):
        shutil.copy(src, dest)
        print("{0} has been copied.".format(filename))
        logger.info("{0} has been copied.".format(filename))

    else:
        print("What do you mean you're looking at him right now?")
        logger.info("What do you mean you're looking at him right now?")
        print("{0} is already there.".format(filename))
        logger.info("{0} is already there.".format(filename))


def create_dir(dirname):
    """
    """

    print("Creating directory...")
    logger.info("Creating directory...")
    if not os.path.isdir(dirname):
        path = os.path.join(os.getcwd(), dirname)
        os.mkdir(path)
        print("{0} has been created.".format(dirname))
        logger.info("{0} has been created.".format(dirname))

    else:
        print("Bro, what is you doin'?")
        logger.info("I think we already got him, Jet.")
        print("{0} already exists.".format(dirname))
        logger.info("{0} already exists.".format(dirname))


def create_file(filename, content):
    """
    """

    print("Creating file...")
    logger.info("Creating file...")
    if not os.path.exists(filename):
        f = open(filename, "w")
        f.write(content)
        f.close()
        print("{0} has been created.".format(filename))
        logger.info("{0} has been created.".format(filename))

    else:
        print("Tell me something I don't know.")
        logger.info("Tell me something I don't know.")
        print("{0} already exists.".format(filename))
        logger.info("{0} already exists.".format(filename))


def delete_dir(dirname):
    """
    """

    print("Deleting directory...")
    logger.info("Deleting directory...")
    if os.path.isdir(dirname):
        os.rmdir(dirname)
        print("{0} has been deleted.".format(dirname))
        logger.info("{0} has been deleted.".format(dirname))

    else:
        print("{0} does not exist.".format(dirname))
        logger.info("{0} does not exist.".format(dirname))


def delete_file(filename):
    """
    """

    print("Deleting file...")
    logger.info("Deleting file...")
    if os.path.isfile(filename):
        os.remove(filename)
        print("{0} has been deleted.".format(filename))
        logger.info("{0} has been deleted.".format(filename))

    else:
        print("Who?")
        logger.info("Who?")
        print("{0} does not exists.".format(filename))
        logger.info("{0} does not exists.".format(filename))


def find_file(filename, search_path):

    print("Looking for file...")
    logger.info("Looking for file...")
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            print("Found it!")
            logger.info("Found it!")
            print(result.append(os.path.join(root, filename)))
            logger.info(result.append(os.path.join(root, filename)))

        elif filename not in files:
            print("Call off the search.")
            logger.info("Call off the search.")
            print("{0} could not be found.".format(filename))
            logger.info("{0} could not be found.".format(filename))


def open_file(filename):
    """
    """

    print("One moment...")
    logger.info("One moment...")
    if os.path.exists(filename):
        print("Opening file...")
        logger.info("Opening file...")
        f = open(filename, "r")
        print(f.read())
        logger.info(f.read())
    else:
        print("{0} does not exist.".format(filename))
        logger.info("{0} does not exist.".format(filename))


def rename_dir(olddirname, newdirname):
    """
    """

    print("Renaming directory...")
    logger.info("Renaming directory...")
    source = olddirname
    dest = newdirname
    if os.path.exists(olddirname):
        os.rename(source, dest)
        print("This directory has been renamed.")
        logger.info("This directory has been renamed.")

    elif not os.path.exists(olddirname):
        print("Let me see those directions.")
        logger.info("Let me see those directions.")
        print("{0} cannot be found.".format(olddirname))
        logger.info("{0} cannot be found.".format(olddirname))

    elif os.path.exists(newdirname):
        print("Let me see those directions.")
        logger.info("Let me see those directions.")
        print("{0} is somewhere else.".format(newdirname))
        logger.info("{0} is somewhere else.".format(newdirname))


def rename_file(oldfilename, newfilename):
    """
    """

    print("Renaming file...")
    logger.info("Renaming file...")
    source = oldfilename
    dest = newfilename
    if os.path.exists(oldfilename):
        os.rename(source, dest)
        print("This file has been renamed.")
        logger.info("This file has been renamed.")

    elif not os.path.exists(oldfilename):
        print("Let me see those directions.")
        logger.info("Let me see those directions.")
        print("{0} cannot be found.".format(oldfilename))
        logger.info("{0} cannot be found.".format(oldfilename))

    elif os.path.exists(newfilename):
        print("Let me see those directions.")
        logger.info("Let me see those directions.")
        print("{0} is somewhere else.")
        logger.info("{0} is somewhere else.")


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
    parser.add_argument("--open_file",
                        action="store",
                        nargs=1,
                        help="Usage: ./puppet_master.py --open_file [filename]",
                        dest="open_file_args")
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

    elif args.open_file_args:
        filename = args.open_file_args[0]
        open_file(filename)

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
