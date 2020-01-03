from typing import List, Union, Tuple

from IPython.core.display import display, HTML

from lab.logger.colors import StyleCode
from lab.logger.destinations import Destination


class IpynbDestination(Destination):
    def __init__(self):
        self.__last_handle = None
        self.__last_id = 1
        self.__cell_lines = []
        self.__cell_count = 0

    def is_same_cell(self):
        cells = get_ipython().ev('len(In)')
        if cells == self.__cell_count:
            return True

        self.__cell_count = cells
        self.__cell_lines = []
        self.__last_handle = None

        return False

    @staticmethod
    def __html_code(text: str, color: List[StyleCode] or StyleCode or None):
        """
        ### Add ansi color codes
        """
        if text == '\n':
            assert color is None
            return text

        if color is None:
            return text
        elif type(color) is list:
            style = "".join(color.html_style())
        else:
            style = color.html_style()

        return f"<span style=\"{style}\">{text}</span>"

    def log(self, parts: List[Union[str, Tuple[str, StyleCode]]], *,
            is_new_line=True):
        tuple_parts = []
        for p in parts:
            if type(p) == str:
                text = p
                style = None
            else:
                text, style = p
            lines = text.split('\n')
            for line in lines[:-1]:
                tuple_parts.append((line, style))
                tuple_parts.append(('\n', None))
            tuple_parts.append((lines[-1], style))

        coded = [self.__html_code(text, color) for text, color in tuple_parts]

        text = "".join(coded)
        lines = text.split('\n')
        if self.is_same_cell():
            self.__cell_lines.pop()
            self.__cell_lines += lines
            text = '\n'.join(self.__cell_lines)
            html = HTML(f"<pre>{text}</pre>")
            self.__last_handle.update(html)
        else:
            self.__cell_lines = lines
            text = '\n'.join(self.__cell_lines)
            html = HTML(f"<pre>{text}</pre>")
            self.__last_handle = display(html, display_id=self.__last_id)
            self.__last_id += 1

        # print(len(self.__cell_lines), self.__cell_lines[-1], is_new_line)
        if is_new_line:
            self.__cell_lines.append('')

    def new_line(self):
        self.__cell_lines.append('')