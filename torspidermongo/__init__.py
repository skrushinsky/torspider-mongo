from .client import MongoClient
import logging

client = None

def init_client(io_loop=None, db='mongodb://localhost:27017/torspider'):
    global client
    logging.debug('Initializing client. db: %s', db)
    MongoClient.setup(db=db, io_loop=io_loop)
    client = MongoClient()

async def save_report(report):
    return await client.save_report(report)


__all__ = [MongoClient,]
