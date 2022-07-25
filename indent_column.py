import sublime
import sublime_plugin
import re
from .parser import parse


class indent_column(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:

            text_input = self.view.substr(region)

            text_input = text_input.lstrip()
            text_input = text_input.rstrip()

            string_formatted = parse(text_input).indent()

            if string_formatted:
                self.view.replace(edit, region, string_formatted)
