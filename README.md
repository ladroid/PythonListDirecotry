# This is ls program

This program shows all files with size, last modified, and subdirectories with files

**works only with python 3**

To run program type this command: ```python3 ls.py [option]```

Output will be:

```
Usage: ls.py [options] [path1[path2[... pathN]]]

Options:
  -h, --help            show this help message and exit
  -l LS, --l=LS         list of direcotry
  -H HIDE, --hidden=HIDE
                        show hidden files [default: on]
  -m MODIFY, --modified=MODIFY
                        show last modified date/time [defaults: on]
  -o ORDER=ORDER, --order=ORDER=ORDER=ORDER
                        order by ('name', 'n', 'modified', 'm', 'size')
                        [default: name]
  -r RECURSY, --recursive=RECURSY
                        recurse into subdirectories [default: off]
  -s SIZE, --size=SIZE  show sizes [default: on]
  ```
