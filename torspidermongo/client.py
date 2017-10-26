from datetime import datetime
import motor
import pymongo
import logging

REPORTS_COLLECTION = 'reports'

class MongoClient:
    @classmethod
    def setup(cls, db=None, reports_collection=REPORTS_COLLECTION, io_loop=None):
        dbname = db.split('/')[-1]
        dbconn =  '/'.join(db.split('/')[:-1])
        logging.info('Connecting to database: %s...', dbname)
        conn = pymongo.MongoClient(db)
        client = conn[dbname]
        client[REPORTS_COLLECTION].create_index('url', name='url_unique', unique=True, background=True )
        client[REPORTS_COLLECTION].create_index('ts', name='ts', background=True )

        if io_loop:
            conn = motor.motor_tornado.MotorClient(dbconn, io_loop=io_loop)
        else:
            conn = motor.motor_tornado.MotorClient(dbconn)
        cls.db = conn[dbname]
        logging.info('Ready for asyncronous connections to %s', db)
        cls.reports = reports_collection
        logging.debug('MongoClient ready.')

    async def save_report(self, task):
        report = {
            'ts': datetime.utcnow(),
            'url': task['url']
        }
        if 'error' in task:
            report['error'] = task['error']
            msg = 'failure '
        else:
            report['page'] = task['page'].as_dict()
            msg = ''
        res = await self.db[self.reports].update_one(
            {'url': task['url']},
            {'$set': report},
            upsert=True
        )
        if res.upserted_id:
            logging.debug('Inserted %sreport for %s', msg, task['url'])
        return res.upserted_id

    async def reports_count(self):
        return await self.db[self.reports].count()
