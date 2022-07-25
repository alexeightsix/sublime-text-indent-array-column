import re


class parse:

    def __init__(self, text):
        self.text = text
        self.longest = 0

    def get_rules(self) -> list:
        return {
            r"(?P<left>([\$].*))(?P<mid>=)(?P<right>(.*);$\n?)",
            r"(?P<left>([\"|'|$].*)([\"|'|$])).*(?P<mid>=>?)(?P<right>.*[,|;|\n])",
            r"(?P<left>\$.*\[[\"|'].*[\"|']].*)(?P<mid>=)(?P<right>.*;[\n|$])"
        }

    def format(self, matches) -> str:
        str = ''
        for m in matches:
            left = m.group('left').strip()
            mid = m.group('mid').strip()
            right = m.group('right').strip()
            spacing = self.longest - len(left) + len(mid)
            str = str + left + " " + mid.rjust(spacing) + " " + right + '\n'
        return str

    def indent(self) -> str:
        for idx, rule in enumerate(self.get_rules()):
            matches = self.get_matches(rule, self.text)
            if (len(matches) > 0):
                return self.format(matches)

    def get_matches(self, rule, text) -> list:
        pairs = []
        for m in re.finditer(rule, text, re.MULTILINE):
            current_length = len(m.group('left').strip())
            pairs.append(m)
            if (current_length > self.longest):
                self.longest = current_length
        return pairs
