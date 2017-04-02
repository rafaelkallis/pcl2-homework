#!/usr/bin/env python3
# coding: utf-8


# not working as expected... Don't have the time to fix; solution appreciated!

def main():
    with open("./ueberraschung.txt", 'rb') as source_file:
        with open("./ueberraschung_encoded.txt", 'w+b') as dest_file:
            contents = source_file.read()
            dest_file.write(contents.decode('utf-16').encode('utf-8'))


if __name__ == '__main__':
    main()
