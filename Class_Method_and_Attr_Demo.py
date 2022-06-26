class ParentTestCase:
    destination = "localhost"
    @classmethod
    def setUpClass(cls):
        print(cls.destination)


class ChildTestCase1(ParentTestCase):
    @classmethod
    def setUpClass(cls):
        cls.destination = "google.com"
        super().setUpClass()

class ChildTestCase2(ParentTestCase):
    @classmethod
    def setUpClass(cls):
        cls.destination = "stackoverflow.com"
        super().setUpClass()

ChildTestCase1.setUpClass()
ChildTestCase2.setUpClass()
