import datetime
import os
from humanfriendly import parse_timespan


class Documentation():

    def __init__(self, list_of_documations):
        self.list_of_documations = []

    def find_documentations(self):
        for root, dirs, files in os.walk(".", topdown=False):
            for file in files:
                if ".rst" in file:
                    self.list_of_documations.append(Document(file))

    def document_scanner():
        for documentation in self.list_of_documations:
            document = Document(documentation)
            document.scan()




class Document():

    do_review = False

    def __init__(self, name):
        self.name = name

    def scan(self):
        file = open(self.name, "w")
        for line in file:
            if "last review" in line:
                _, last_review = line.split(":")
            if "review schedule" in line
                _, line = line.split(":")
                review_time = parse_timespan(line)
            if last_review + review_time < datetime.datetime.today()
                self.do_review = True

