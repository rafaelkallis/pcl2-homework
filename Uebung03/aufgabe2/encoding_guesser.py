#!/usr/bin/env python3
# coding: utf-8

# Some encodings don't get guessed correctly,
# utf-16_file.txt gets recognized as CP1252


def getEncoding(filename):
    try:
        open(filename, encoding="ascii").read()
        print("ascii")
    except:
        try:
            open(filename, encoding="CP1252").read()
            print("CP1252")
        except:
            try:
                open(filename, encoding="utf-8").read()
                print("utf-8")
            except:
                try:
                    open(filename, encoding="utf-16").read()
                    print("utf-16")
                except:
                    try:
                        open(filename, encoding="utf-32").read()
                        print("utf-32")
                    except:
                        print("other")


def main():
    getEncoding("utf-8_file.txt")


if __name__ == '__main__':
    main()
