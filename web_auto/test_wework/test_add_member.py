#from web_auto.test_wework.index import Index
from cekai.web_auto.web_po.index import Index


class TestAddMember:
    def setup(self):
        self.index = Index()

    def test_add_member(self):
        self.index.goto_add_member().add_member()