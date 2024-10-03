from ..customers.lynx_client import create_lynx_client

def test_lynx_client_initialization():
    cli, mqttc = create_lynx_client("test_api_key")
    assert cli is not None
    assert mqttc is not None
