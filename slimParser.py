'''
this script parses conf file [section] -> content as key value pairs of Slimparser()
'''

import re


class SlimParser():
    def __init__(self,file):
        self.file = file
        self.headers = {}
        self.current_key = None

        #run on init
        with open(file, 'r') as f:
            text = f.read()

        lines = text.splitlines()
        sections = re.findall(r'\[[^\[\]\n]+\]', text)

        for line in lines:
            line = line.strip()
            if line in sections:
                self.current_key = line.strip('[]')
                self.headers[self.current_key] = []
            elif self.current_key:
                self.headers[self.current_key].append(line)

    def getHeaders(self):
        return (self.headers.keys())

    def get(self,section):
        """Returns the header"""
        return self.headers.get(section)

    def cleanSection(self, section):
        """Strips and removes empty lines, duplicates from a section."""
        if section in self.headers:
            self.headers[section] = set(
                    line.strip() for line in self.headers[section] if line.strip()
                    )

        elif section not in self.headers:
            raise ValueError(f"Section '{section}' not found in headers.")





test = SlimParser('../data.txt')

print(test.getHeaders())

test.cleanSection('Programs')
print(test.get('Programs'))

