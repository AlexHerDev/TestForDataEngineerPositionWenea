import pytest


data_test_1: str = "{data_test: 'data_test', data_test_2: 'data_test'}"
data_test_2: str = "{data_test: 'data_test', data_test_: ''}"
data_test_3: str = ""

data_test_persisted_doc: str = "{data_test: 'data_test'}"

@pytest.fixture
def external_dependencies_mock(mocker):
    persist_using_gridfs = mocker.patch("src.ingestion.persist_using_gridfs")
    persist_using_document = mocker.patch("src.ingestion.persist_using_document")

    mongo_repository = mocker.patch(
        "src.infraestructure.mongo_repository.MongoRepository"
    )
    mongo_repository.close_connection.return_value = ""

    return {
        "persist_using_gridfs_mock": persist_using_gridfs,
        "persist_using_document_mock": persist_using_document,
        "mongo_repository_mock": mongo_repository,
    }

