#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is the template for exercise 07. Please adjust, add or remove code and
comments where necessary.
"""

import argparse
import logging
from _io import TextIOWrapper
import re


# LOGGER CONFIGURATION (only change log-file according to your name)
# ----------------------------------------------------------------------------
logging.basicConfig(
    format="%(asctime)s ::  %(name)s :: %(levelname)s ::  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="mustermann_max.log",
    filemode="a",
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------


def excercise_01(text: str) -> int:
    return len(re.findall('|'.join(['Glück', 'Frieden', 'Thor']), text))


def excercise_02(text: str) -> int:
    return len(re.findall('[a-zA-Z]+keit', text))

def excercise_03(text: str) -> [str]:
    non_whitespace = '[a-zA-Z,\'\"äüö]'
    including_whitespace = '[a-zA-Z\s,\'\"äüö]+'
    ends = '[\.\:]'
    return re.findall(non_whitespace + including_whitespace + ends, text)


def excercise_04(text: str) -> int:
    return re.search('Zarathustra', text).start()

def excercise_05(text: str) -> int:
    return re.search('Zarathustra', text, re.IGNORECASE).start()


def excercise_06(text: str) -> int:
    emails = r'[\w\.-]+@[\w\.-]+[\w-]'
    return len(re.findall(emails, text))

def excercise_07(text: str) -> str:
    nums_in_context = re.findall('[0-9]+.', text)
    nums_in_context.sort(key=lambda n: -int(n[0: len(n) - 1]))
    largest = nums_in_context[0]
    return largest[len(largest) - 1:len(largest)]

def excercise_08(text: str) -> str:
    return re.sub('(Zarathustra)', '\g<1>/Eigennname', text)


def excercise_09(text: str) -> None:
    """
    Determine how often in the text there is more than one consecutive linebreak

    :param text: textfile for this exercise
    :type text: str
    :return: count of multiple consecutive linebreaks
    :rtype: int
    """
    return len(re.findall('\n\n+', text))


def read_textfile(textfile: TextIOWrapper) -> str:
    """
    Read the whole file into memory

    :param textfile: open, readable textfile
    :type textfile: TextIOWrapper
    :return: whole text from file
    :rtype: str
    """
    try:
        logger.debug("Reading textfile {}".format(textfile.name))
        return textfile.read()
    except Exception as exc:
        logger.critical("Unexpected error occured.")
        logger.exception(exc)
        raise exc


# UNCOMMENT THE EXERCISES YOU HAVE IMPLEMENTED TO SEE IF THEY ARE WORKING
def main(textfilepath: TextIOWrapper) -> None:
    """
    Control flow of the whole program

    :param textfilepath: path to textfile
    :type textfilepath: str
    """
    text = read_textfile(textfilepath)

    print('result_01 ' + str(excercise_01(text)))
    print('result_02 ' + str(excercise_02(text)))
    print('result_03 EXCERPT ' + str(excercise_03(text)[0:2]))
    print('result_04 ' + str(excercise_04(text)))
    print('result_05 ' + str(excercise_05(text)))
    print('result_06 ' + str(excercise_06(text)))
    print('result_07 ' + str(excercise_07(text)))
    print('result_08 EXCERPT' + str(excercise_08(text))[0:100])
    print('result_09 ' + str(excercise_09(text)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Prog I - Exercise 07"
    )
    parser.add_argument(
        'textfile',
        type=argparse.FileType('r'),
        help='Path to input file'
    )
    args = parser.parse_args()
    main(args.textfile)
