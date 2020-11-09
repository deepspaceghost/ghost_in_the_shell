#!/usr/bin/python

# Importing os module
import argparse
import os
import sys


def command_control(args):
    """
    """

    try:
        if args[1] == "create_file":
            create_file(args[2], args[3])

        elif args[1] == "delete_file":
            delete_file(args[2])

        elif args[1] == "create_directory":
            create_directory(args[2])

        elif args[1] == "delete_directory":
            delete_directory(args[2])

        else:
            print_usage()

    except IndexError:
        print("Nice try, jackass.")
        print_usage()


def create_file(filename, content):
    """
    """

    if not os.path.exists(filename):
        f = open(filename, "w")
        f.write(content)
        f.close()
        print("{0} has been created.".format(filename))
    else:
        print("File already exists.")


def create_directory(foldername):
    """
    """

    if os.path.isdir(foldername):
        print("This directory already exists.")
    else:
        print("I'll see what I can do.")
        try:
            path = os.path.join(os.getcwd(), foldername)
            os.mkdir(path)
            print("New directory created.")
        except FileExistsError:
            print("Bro, what is you doing?")


def delete_directory(foldername):
    """
    """

    if os.path.exists(foldername):
        os.remove(foldername)
    else:
        print("This folder does not exist.")


def delete_file(filename):
    """
    """

    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist.")


def print_usage():
    """
    """

    print("Usage: python3 puppet_master.py help")
    print("Usage: python3 puppet_master.py create_directory [foldername]")
    print("Usage: python3 puppet_master.py create_file [filename] [content]")
    print("Usage: python3 puppet_master.py delete_directory [foldername]")
    print("Usage: python3 puppet_master.py delete_file [filename]")


def main():
    """
    """

    command_control(sys.argv)


if __name__ == "__main__":
    """
    """

    main()
