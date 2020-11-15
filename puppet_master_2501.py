#!/usr/bin/python
​
import argparse
import os
​
​
def create_file(filename, content):
    """
    """
​
    if not os.path.exists(filename):
        f = open(filename, "w")
        f.write(content)
        f.close()
        print("{0} has been created.".format(filename))
​
    else:
        print("Oh, how original?")
        print("{0} already exists.".format(filename))
​
​
def create_dir(dirname):
    """
    """
​
    if not os.path.isdir(dirname):
        path = os.path.join(os.getcwd(), dirname)
        os.mkdir(path)
        print("{0} has been created.".format(dirname))
​
    else:
        print("Bro, what is you doin'?")
        print("{0} already exists.".format(dirname))
​
​
def delete_dir(dirname):
    """
    """
​
    if os.path.exists(dirname):
        os.rmdir(dirname)
        print("{0} has been deleted.".format(dirname))
​
    else:
        print("{0} does not exist.".format(dirname))
​
​
def delete_file(filename):
    """
    """
​
    if os.path.exists(filename):
        os.remove(filename)
        print("{0} has been deleted.".format(filename))
​
    else:
        print("{0} does not exists.".format(filename))
​
​
def main():
    """
    """
​
    parser = argparse.ArgumentParser()
    parser.add_argument("--create_dir",
                        action="store",
                        nargs=1,
                        help="Usage: python3 puppet_master.py --create_dir [dirname]",
                        dest="create_dir_args")
    parser.add_argument("--create_file",
                        action="store",
                        nargs=2,
                        help="Usage: python3 puppet_master.py --create_file [filename] [content]",
                        dest="create_file_args")
    parser.add_argument("--delete_dir",
                        action="store",
                        nargs=1,
                        help="Usage: python3 puppet_master.py --delete_dir [dirname]",
                        dest="delete_dir_args")
    parser.add_argument("--delete_file",
                        action="store",
                        nargs=1,
                        help="Usage: python3 puppet_master.py --delete_file [filename]",
                        dest="delete_file_args")
​
    args = parser.parse_args()
​
    if args.create_dir_args:
        dirname = args.create_dir_args[0]
        create_dir(dirname)
​
    elif args.create_file_args:
        filename = args.create_file_args[0]
        content = args.create_file_args[1]
        create_file(filename, content)
​
    elif args.delete_dir_args:
        dirname = args.delete_dir_args[0]
        delete_dir(dirname)
​
    elif args.delete_file_args:
        filename = args.delete_file_args[0]
        delete_file(filename)
​
​
if __name__ == "__main__":
    """
    """
​
    main()
