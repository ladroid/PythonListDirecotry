import os
import sys
import time
import optparse

def start():
    parse = optparse.OptionParser(usage='usage: ls.py [options] [path1[path2[... pathN]]]')
    parse.add_option('-l', '--l', dest='ls', help='list of direcotry')
    parse.add_option('-H', '--hidden', dest='hide', help='show hidden files [default: on]')
    parse.add_option('-m', '--modified', dest='modify', help='show last modified date/time [defaults: on]')
    parse.add_option('-o', '--order=ORDER', help="order by ('name', 'n', 'modified', 'm', 'size') [default: name]")
    parse.add_option('-r', '--recursive', dest='recursy', help='recurse into subdirectories [default: off]')
    parse.add_option('-s', '--size', help='show sizes [default: on]')
    (opt, args) = parse.parse_args(args=sys.argv[1:])
    return opt, args

def ls(opt, dirname):
    count_file = 0
    count_dir = 0
    print('ls using')
    print(os.listdir(dirname))
    file_with_size = []
    for basename in os.listdir(dirname):
        filename = os.path.join(dirname, basename)
        if os.path.isfile(filename):
            file_with_size.append(filename)
            count_file += 1
        if os.path.isdir(basename):
            count_dir += 1
    if opt.ls:
        for basename in os.listdir(dirname):
            filename = os.path.join(dirname, basename)
            if os.path.isfile(filename):
                print(time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(os.path.getmtime(filename))), os.path.getsize(filename), filename)
        print(count_file, 'files', count_dir, 'directory')
    elif opt.modify:
        for basename in os.listdir(dirname):
            filename = os.path.join(dirname, basename)
            if os.path.isfile(filename):
                print(os.path.getsize(filename), filename)
        print(count_file, 'files', count_dir, 'directory')
    elif opt.size:
        for basename in os.listdir(dirname):
            filename = os.path.join(dirname, basename)
            if os.path.isfile(filename):
                print(filename)
        print(count_file, 'files', count_dir, 'directory')
    elif opt.recursy:
        for all_files in os.walk(dirname):
            print(all_files)
    elif opt.hide:
        for basename in os.listdir(dirname):
            filename = os.path.join(dirname, basename)
            if filename.startswith('.'):
                print(filename)

def main():
    opt, paths = start()
    ls(opt, ''.join(str(e) for e in sys.argv[2:]))

main()