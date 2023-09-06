import unittest
import wrapper
from database import *

api = wrapper.APIWrapper()


class TestingAPIRequest(unittest.TestCase):

    def test_response_dictionary_length(self):
        result = api.request({"type": "education"})
        self.assertEqual(len(result), 7)
        result1 = api.request({"minprice": 5, "maxprice": 1})
        self.assertEqual(len(result1), 1)
        result2 = api.request({})
        self.assertEqual(len(result2), 7)

    def test_response_relevancy(self):
        result = api.request({"type": "busywork", "participants": 1})
        self.assertEqual(result, result | {"type": "busywork", "participants": 1})
        result1 = api.request({"minaccessibility": "pomylka"})
        self.assertEqual(list(result1), ["error"])


class TestingDatabase(unittest.TestCase):
    engine = create_engine(configuration.databaseData,
                           connect_args={'options': '-csearch_path={}'.format(configuration.schemaName)},
                           echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    def setUp(self):
        Base.metadata.create_all(self.engine)
        self.session.add(Activity({'activity': 'Test', 'accessibility': 0.1,
                                   'type': 'relaxation', 'participants': 1, 'price': 0.05,
                                   'link': '', 'key': '0099'}))
        self.session.commit()

    def tearDown(self):
        self.session.query(Activity).filter(Activity.key == "0099").delete()
        self.session.commit()

    def test_insertion_and_retrieving(self):
        query = self.session.query(Activity).order_by(Activity.id.desc()).limit(1).one()
        self.assertEqual(query.name, "Test")


if __name__ == "__main__":
    unittest.main()
