from __future__ import annotations

import errno
import os
from types import TracebackType
from typing import Optional, Type

import black
import isort

from . import AST

TAB_LENGTH = 4


class WriterImpl(AST.Writer):
    def __init__(self, filepath: str):
        self._filepath = filepath
        self._indent = 0
        self._has_written_anything = False
        self._last_character_is_newline = False
        self._content = ""

    def write(self, content: str) -> None:
        content_ends_in_newline = len(content) > 0 and content[-1] == "\n"

        # temporarily remove the trailing newline, since we don't want to add the prefix after it
        content_without_trailing_newline = content[:-1] if content_ends_in_newline else content

        # indent all lines
        indent = self._get_indent_str()
        indented_content = content_without_trailing_newline.replace("\n", f"\n{indent}")
        if self._is_at_start_of_line():
            indented_content = indent + indented_content
        if content_ends_in_newline:
            indented_content += "\n"

        self._write(indented_content)

    def _is_at_start_of_line(self) -> bool:
        return self._last_character_is_newline or not self._has_written_anything

    def _get_indent_str(self) -> str:
        return " " * TAB_LENGTH * self._indent

    def _write(self, content: str) -> None:
        if len(content) > 0:
            self._has_written_anything = True
            self._last_character_is_newline = content[-1] == "\n"
        self._content += content

    def write_line(self, content: str = "") -> None:
        self.write(content)
        self.write_newline_if_last_line_not()

    def write_newline_if_last_line_not(self) -> None:
        if not self._last_character_is_newline:
            self.write("\n")

    def indent(self) -> IndentableWriterImpl:
        """
        with writer.indent():
            writer.write_line("# here's an indented line")
        """
        self._indent += 1

        # ensure the cursor is indented properly
        if self._last_character_is_newline:
            self._write(self._get_indent_str())
        else:
            self.write("\n")

        return IndentableWriterImpl(writer=self)

    def start(self) -> None:
        mkdir_p(os.path.dirname(self._filepath))

    def finish(self) -> None:
        try:
            self._content = isort.code(self._content, quiet=True)
            self._content = black.format_file_contents(
                self._content,
                fast=True,
                # todo read their config?
                mode=black.FileMode(magic_trailing_comma=False, line_length=120),
            )
        except black.report.NothingChanged:
            pass
        finally:  # write to disk even if the the formatting failed
            with open(self._filepath, "w") as file:
                file.write(self._content)

    def outdent(self) -> None:
        self._indent = max(0, self._indent - 1)

    def __enter__(self) -> WriterImpl:
        self.start()
        return self

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        if exctype is None:
            self.finish()


class IndentableWriterImpl(AST.IndentableWriter):
    def __init__(self, writer: AST.Writer):
        self._writer = writer

    def __enter__(self) -> None:
        pass

    def __exit__(
        self,
        exctype: Optional[Type[BaseException]],
        excinst: Optional[BaseException],
        exctb: Optional[TracebackType],
    ) -> None:
        self._writer.outdent()


# Taken from https://stackoverflow.com/a/600612/119527
def mkdir_p(path: str) -> None:
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
