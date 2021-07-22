from doc_scanner import DocumentationsDirectory
from doc_scanner import Document
import pytest


def test_make_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "docs.txt"
    p.write_text("""
        last review:2021-07-09
        review schedule:1 year
        """)
    assert p.read_text() == """
        last review:2021-07-09
        review schedule:1 year
        """

def test_find_documentations(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = (d / "docs1.rst").write_text("asdf")
    t = (d / "docs2.rst").write_text("asdf")
    f = (d / "docs3.rst").write_text("asdf")
    documentations = DocumentationsDirectory([], str(d))
    documents = documentations.find_documentations()
    list_of_documations = []
    for documentation in documents:
        list_of_documations.append(documentation.name)
    assert list_of_documations == ["docs1.rst", "docs2.rst", "docs3.rst"]


def test_docoument_scan(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = (d / "docs1.rst").write_text("""
        docs1.rst
        last review:21-12-2020
        review schedule:1 year
        """)
    document = Document("docs1.rst", str(tmp_path) + "/sub/")
    assert document.scan() == """
        docs1.rst
        last review:21-12-2020
        review schedule:1 year
        """


def test_must_reviewed_true(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = (d / "docs1.rst").write_text("""
        docs1.rst
        last review:21-12-2010
        review schedule:1 year
        """)
    document = Document("docs1.rst", str(tmp_path) + "/sub/")
    document.scan()
    document = document.must_reviewed()
    assert document == False


def test_must_reviewed_true(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = (d / "docs1.rst").write_text("""
        docs1.rst
        last review:21-12-2019
        review schedule:1 year
        """)
    document = Document("docs1.rst", str(tmp_path) + "/sub/")
    document.scan()
    document = document.must_reviewed()
    assert document == True

def test_docoument_scaner(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = (d / "docs1.rst").write_text("""
        docs1.rst
        last review:21-12-2019
        review schedule:1 year
        """)
    t = (d / "docs2.rst").write_text("""
        docs1.rst
        last review:21-12-2020
        review schedule:1 year
        """)
    documentations = DocumentationsDirectory([], str(d))
    documentations.find_documentations()
    test_must_reviewd, test_must_not_reviewd  = documentations.document_scanner()
    assert test_must_reviewd == ["docs1.rst"]
    assert test_must_not_reviewd == ["docs2.rst"]
