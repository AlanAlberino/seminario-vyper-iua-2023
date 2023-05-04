import pytest
import brownie
import uuid

@pytest.fixture
def manufacturer_contract(manufacturer, accounts):
    yield manufacturer.deploy({'from': accounts[0]})

def test_upload_new_batch(manufacturer_contract):
    newBatchNumber = "testCode"
    newProductId = str(uuid.uuid4())
    manufacturer_contract.loadNewBatch(newProductId, newBatchNumber)
    productBatch = manufacturer_contract.viewBatchData(newBatchNumber)
    assert (productBatch[0] == newProductId)

def test_not_found_exception(manufacturer_contract):
    inexistentBatchNumber = "ABCD1234"
    with brownie.reverts("No se encuentra el lote indicado"):
        manufacturer_contract.viewBatchData(inexistentBatchNumber)
