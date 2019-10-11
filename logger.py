import datetime
from typing import TextIO
import os


def write_begin_to_file(fp):
    begin = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S").ljust(40, "-").rjust(60, "-") + "\n"
    fp.write(begin)
    fp.flush()


def write_end_file(fp):
    end = "####END####".ljust(40, "-").rjust(60, "-") + "\n\n"
    fp.write(end)
    fp.flush()


class Logger:
    def __init__(self, stdout_path, stderr_path):
        self.stdout_path = stdout_path
        self.stderr_path = stderr_path

        self._openFiles()

    def _openFiles(self):
        self.stdout_file = open(self.stdout_path, "a+")
        self.stderr_file = open(self.stderr_path, "a+")

        write_begin_to_file(self.stdout_file)
        write_begin_to_file(self.stderr_file)

    def closeFiles(self):
        write_end_file(self.stdout_file)
        write_end_file(self.stderr_file)

        self.stdout_file.close()
        self.stderr_file.close()

    def getStdOutFile(self) -> TextIO:
        return self.stdout_file

    def getStdErrFile(self) -> TextIO:
        return self.stderr_file
