#!/usr/bin/env python3

import fileinput
from sys import stdout, stderr


lparen = '([{'
rparen = ')]}'


def paren_recurse(txt, start, lchar, rchar):
    dosplit = True
    li = start + 1
    i = start
    if i > 0 and txt[i - 1] not in (lparen + ' '):
        dosplit = False
    i += 1
    while i < len(txt) and txt[i] != rchar:
        if txt[i] == lchar:
            txt, i = paren_recurse(txt, i, lchar, rchar)
        i += 1
    if i < len(txt) - 1 and txt[i + 1] not in (rparen + ' '):
        # Strange exception for stuff like "(LPS)-stimulated"
        # if txt[i+1] == '-':
        #     j = i + 2
        #     while j < len(txt) and txt[j] != ' ':
        #         if not(txt[j].isupper() or txt[j].islower()):
        #             dosplit = False
        #             break
        #         j += 1
        # else:
        #     dosplit = False
        dosplit = False
    if dosplit:
        txt = txt[:li] + ' ' + txt[li:i] + ' ' + txt[i:]
        i += 2
        newtxt = txt.replace(' )-', ' ) - ')
        i += len(newtxt) - len(txt)
        txt = newtxt
    return txt, i


def paren_split(txt):
    for lchar, rchar in zip(lparen, rparen):
        i = 0
        while i < len(txt):
            if txt[i] == lchar:
                txt, i = paren_recurse(txt, i, lchar, rchar)
            i += 1
    return txt


def raw_tokenize(txt):
    txt = txt.replace(' ', ' ')  # Weird unicode spaces.
    txt = txt.replace('.\n', ' . ').replace(', ', ' , ')  # Periods, commas.
    if txt[-1] == '.':
        txt = txt[:-1] + ' .'  # Handle final period.
    # Qmarks, exclamation points.
    txt = txt.replace('?\n', ' ? ').replace('!\n', ' ! ')
    # Colons and semicolons.
    txt = txt.replace('; ', ' ; ').replace(': ', ' : ')
    txt = txt.replace('“', '``').replace('”', '\'\'')  # Change quotes.
    # Space quotes.
    txt = txt.replace(' ``', ' `` ').replace('\'\' ', ' \'\' ')
    txt = paren_split(txt)  # Advanced paren/bracket splitting.
    txt = txt.replace('  ', ' ').replace('  ', ' ')  # Get rid of extra spaces.
    return txt

if __name__ == '__main__':
    try:
        for line in fileinput.input():
            print(line)
            stdout.write(raw_tokenize(line) + '\n')
            print('')
    except IOError:
        pass
    finally:
        stderr.close()
        stdout.close()
