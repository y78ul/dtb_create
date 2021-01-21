import os
import errno
from enum import Enum
from parsers.dtb import DTB


class FileParserError(Enum):
    NO_ERROR = 'No error'
    ERROR_FILE_NOT_FOUND = 'Error: File not found'


class FileParser(object):
    """ Abstract class which provides basic functionality to parse a single file. The particular way of parsing is
    managed by the automatically called _parse() method which needs to be overridden in inherited classes.
    """
    def __init__(self, file_name):
        self.dtb = DTB()
        self.__status = FileParserError.NO_ERROR
        self.__set_file_name(file_name)
        if self.__status == FileParserError.ERROR_FILE_NOT_FOUND:
            raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), file_name)
        elif self.__status == FileParserError.NO_ERROR:
            self.__status = self._parse()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def _parse(self):
        raise NotImplementedError('{} is an abstract class and may not be instantiated itself.'.
                                  format(self.__class__.__name__))

    def __set_file_name(self, file_name):
        self._file_name = ''
        if os.path.exists(file_name):
            self._file_name = file_name
        else:
            self.__status = FileParserError.ERROR_FILE_NOT_FOUND

    def __get_status(self):
        return self.__status

    status = property(__get_status)
