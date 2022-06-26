class ParentTestCase:
    destination = "localhost"
    @classmethod
    def setUpClass(cls):
        print(ParentTestCase.destination)


class ChildTestCase1(ParentTestCase):
    @classmethod
    def setUpClass(cls):
        ParentTestCase.destination = "google.com"
        super().setUpClass()

class ChildTestCase2(ParentTestCase):
    @classmethod
    def setUpClass(cls):
        ParentTestCase.destination = "stackoverflow.com"
        super().setUpClass()

ChildTestCase1.setUpClass()
ChildTestCase2.setUpClass()