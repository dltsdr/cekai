from web_auto.web_po.index import Index
from web_auto.web_po.register import Register


class TestRegister:
    def setup(self):
        self.index = Index()

    def test_register(self):
        result = self.index.goto_register().register()
        assert  result