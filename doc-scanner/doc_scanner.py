import datetime
from datetime import timedelta
from humanfriendly import parse_timespan
import os



class DocumentationsDirectory():

    def __init__(self, list_of_documations, work_dir):
        self.list_of_documations = list_of_documations
        self.work_dir = work_dir + "/"

    def find_documentations(self):
        for root, dirs, files in os.walk(self.work_dir, topdown=False):
            for file in files:
                if ".rst" in file:
                    self.list_of_documations.append(Document(file, self.work_dir))
        self.list_of_documations.sort(key=lambda d: d.name)
        return self.list_of_documations

    def document_scanner(self):
        list_of_must_reviewed = []
        list_of_must_not_reviewed = []
        for documentation in self.list_of_documations:
            documentation.scan()
            reviewed = documentation.must_reviewed()
            if reviewed:
                list_of_must_reviewed.append(documentation.name)
            else:
                list_of_must_not_reviewed.append(documentation.name)
        return list_of_must_reviewed, list_of_must_not_reviewed

class Document():

    do_review = False

    def __init__(self, name, work_dir):
        self.name = name
        self.work_dir = work_dir

    def scan(self):
        with open(self.work_dir + self.name, "r") as f:
            self.file = f.read()
            return self.file

    def must_reviewed(self):
        for line in self.file.splitlines():
            if "last review" in line:
                _, last_review = line.split(":")
                last_review =  datetime.datetime.strptime(last_review, "%d-%m-%Y")
            if "review schedule" in line:
                _, line = line.split(":")
                review_time = parse_timespan(line)
                review_time = timedelta(seconds=review_time)
        if last_review + review_time < datetime.datetime.today():
            self.do_review = True
            return True
        return False

