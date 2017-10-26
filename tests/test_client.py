import sys
import logging
import unittest
from tornado import testing
import pymongo

# import application packages
import torspidermongo as tsmongo

MONGO_DB_NAME = 'test_torspider'
MONGO_DB = "mongodb://localhost:27017/%s" % MONGO_DB_NAME

mongo = pymongo.MongoClient('mongodb://localhost:27017')

class SaveReportCase(testing.AsyncTestCase):

    def setUp(self):
        logging.info('setUp')
        super(SaveReportCase, self).setUp()
        tsmongo.init_client(io_loop=self.io_loop, db=MONGO_DB)

    def tearDown(self):
        super(SaveReportCase, self).tearDown()
        logging.info('tearDown')
        mongo.drop_database(MONGO_DB_NAME)
        logging.debug('%s deleted.', MONGO_DB_NAME)

    @testing.gen_test
    def test_save_report(self):
        res = yield tsmongo.save_report({'url': 'http://httpbin.org/', 'page': {}})
        self.assertIsNotNone(res)


class ReportsCountCase(testing.AsyncTestCase):

    def setUp(self):
        logging.info('setUp')
        mongo[MONGO_DB_NAME].reports.insert_one({'url': 'http://httpbin.org/', 'page': {}})
        super(ReportsCountCase, self).setUp()
        tsmongo.init_client(io_loop=self.io_loop, db=MONGO_DB)
        self.mongo = tsmongo.MongoClient()

    def tearDown(self):
        super(ReportsCountCase, self).tearDown()
        logging.info('tearDown')
        mongo.drop_database(MONGO_DB_NAME)
        logging.debug('%s deleted.', MONGO_DB_NAME)

    @testing.gen_test
    def test_reports_count(self):
        res = yield self.mongo.reports_count()
        self.assertEqual(1, res)


def all():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(SaveReportCase))
    test_suite.addTest(unittest.makeSuite(ReportsCountCase))

    return test_suite


if __name__ == '__main__':
    logging.basicConfig(
        #level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S',
        format='%(asctime)s - %(levelname)-8s - %(message)s',
        stream=sys.stderr
    )
    testing.main(verbosity=4)
