import logging
from importlib import import_module
import sys
from pathlib import Path

# Lägg till projektets rotmapp till sys.path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from Soltak.config import tjorn_config  # Importera specifika konfigurationer här
from Soltak.config.lynx_client import create_lynx_client

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Lägg till kunder här
    customers = ["tjorn"]  # Använd strängar för att matcha konfigurationsfilernas namn

    for customer in customers:
        try:
            config_module = import_module(f"Soltak.config.{customer}_config")
            api_key = config_module.api_key
            installation = config_module.installation

            # Skapa Lynx klient och MQTT klient
            cli, mqttc = create_lynx_client(api_key)

            from Soltak.calculations.delta_calculation_VA import calculate_deltas
            logger.info(f"Starting delta calculations for {customer}")
            calculate_deltas(cli, mqttc, installation)

        except ModuleNotFoundError:
            logger.error(f"Config module '{customer}_config' not found.")
            sys.exit(1)
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            # Lägg till mer specifik felhantering här vid behov

if __name__ == "__main__":
    main()
