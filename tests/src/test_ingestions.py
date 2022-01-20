from unittest import mock

import pytest
from constants.constants import *

from tests.src.mock_response import MockResponse
from tests.src.conftest import *
from src.ingestion import *
from pytest_mock_resources import create_mongo_fixture

from unittest.mock import MagicMock

mongo = create_mongo_fixture()

'''
def test_persist_using_gridfs(mongo):
    collection_test_name: str = "collection_test_name"

    persist_using_gridfs(data_test_1, collection_test_name, mongo)

    collection = mongo[collection_test_name]
    returned = collection.find_many()

    assert {} == {}


def test_persist_using_document():
    collection_test_name: str = "collection_test_name"

    persist_using_document(data_test_persisted_doc, collection_test_name, mongo)

    collection = mongo[collection_test_name]
    returned = collection.find_one()

    assert data_test_persisted_doc == returned 

'''

def test_persist_data_when_data_is_greater_to_max_bytes_to_persist(
    external_dependencies_mock,
):
    persist_data(data_test_1, external_dependencies_mock["mongo_repository_mock"])
    external_dependencies_mock["persist_using_gridfs_mock"].assert_called_once()


def test_persist_data_when_data_is_equal_to_max_bytes_to_persist(
    external_dependencies_mock,
):
    persist_data(data_test_2, external_dependencies_mock["mongo_repository_mock"])
    external_dependencies_mock["persist_using_gridfs_mock"].assert_called_once()


def test_persist_data_when_data_is_minor_to_max_bytes_to_persist(
    external_dependencies_mock,
):
    persist_data(data_test_3, external_dependencies_mock["mongo_repository_mock"])
    external_dependencies_mock["persist_using_document_mock"].assert_called_once()


@pytest.mark.asyncio
async def test_get_data_from_url_when_200(mocker):
    data = {}
    resp = MockResponse(json.dumps(data), 200)
    mocker.patch("aiohttp.ClientSession", return_value=resp)
    res = await get_data_from_url("url_test")
    print(res)
    assert res == data


@pytest.mark.asyncio
async def test_get_data_from_url_when_no_200(mocker):
    data = {}
    resp = MockResponse(json.dumps(data), 404)
    mocker.patch("aiohttp.ClientSession", return_value=resp)
    with pytest.raises(Exception):
        res = await get_data_from_url("url_test")
