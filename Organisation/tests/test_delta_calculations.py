import pytest
from ..calculations.delta_calculation_VA import create_delta_functions, calculate_deltas
from ..customers.lynx_client import create_lynx_client

def test_create_delta_functions():
    cli, _ = create_lynx_client("test_api_key")
    installation = 1234
    function = {
        "meta": {
            "topic_read": "current_volume_topic",
            "device_id": "device123",
            "eui": "eui123"
        }
    }
    create_delta_functions(cli, installation, function)
    # Lägg till assertions för att verifiera att delta funktioner skapades korrekt

def test_calculate_deltas():
    cli, mqttc = create_lynx_client("test_api_key")
    installation = 1234
    calculate_deltas(cli, mqttc, installation)
    # Lägg till assertions för att verifiera att deltas beräknades korrekt
