from doc_scanner import Documentation
from doc_scanner import Document
import pytest


def test_scan_documentation(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "docs.txt"
    p.write_text("""
        last review:2021-07-09 \n
        review schedule:1 year \n
        """)
    assert p.read_text() == """
        last review:2021-07-09 \n
        review schedule:1 year \n
        """
    document1 = Document(p)
    document1.scan()
    document1.must_reviewed()
