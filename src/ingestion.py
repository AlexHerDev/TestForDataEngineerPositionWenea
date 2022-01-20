import asyncio
import json
import logging
import uuid
from typing import Dict

import aiohttp
import gridfs
from constants.constants import *
from src.infraestructure.mongo_repository import MongoRepository
from pymongo import MongoClient
from retrying import retry


def persist_using_gridfs(data: str, collection_name: str, db: MongoClient) -> None:
    fs = gridfs.GridFS(db, collection_name)
    try:
        logging.info(f"Starting persistion in {collection_name}")
        fs.put(data, encoding="utf-8")
        logging.info(f"End persistion in {collection_name}")
    except Exception as e:
        raise Exception(f"Exception in persistor using gridfs: {e}")


def persist_using_document(data: str, collection_name: str, db: MongoClient) -> None:

    collection = db[collection_name]

    try:
        if isinstance(data, list):
            logging.info(f"Starting persistion in {collection_name}")
            collection.insert_many(json.loads(data))
            logging.info(f"End persistion in {collection_name}")
        else:
            logging.info(f"Starting persistion in {collection_name}")
            collection.insert_one(json.loads(data))
            logging.info(f"End persistion in {collection_name}")
    except Exception as e:
        raise Exception(f"Exception in persistor document: {e}")


def persist_data(data: str, mongo_repository: MongoRepository) -> None:
    collection_name: str = str(uuid.uuid4())
    try:
        if len(data) >= MAX_BYTES_TO_PERSIST:
            persist_using_gridfs(data, collection_name, mongo_repository.db)
        else:
            persist_using_document(data, collection_name, mongo_repository.db)
    finally:
        mongo_repository.close_connection()


@retry(
    wait_exponential_multiplier=1000,
    wait_exponential_max=10000,
    stop_max_attempt_number=3,
)
async def get_data_from_url(url: str) -> str:
    logging.info(f"Starting fetch data {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise Exception("Error: Status is {response.status}")
            raw_data = await response.text()
            logging.info(f"End fetch data {url}")
            return raw_data


async def extract_and_store(url: str) -> None:
    data: str = await get_data_from_url(url)
    persist_data(data, MongoRepository())


def run_parallel_process() -> None:
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(extract_and_store(DATA_URL), extract_and_store(DATA_URL_2))
    )
    loop.close()
