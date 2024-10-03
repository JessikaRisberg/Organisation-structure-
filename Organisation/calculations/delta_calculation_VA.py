import json 
from datetime import datetime
from lynx import Function
from Soltak.config.lynx_client import create_lynx_client, cli, mqttc, installation

# Delta calculation for VA sensors (Ambiductor w1h, w1e, w1t)

def create_delta_functions(cli, installation, function):
    delta_topic = function.meta["topic_read"].replace("current_volume", "delta_volume")
    delta_liters_topic = function.meta["topic_read"].replace("current_volume", "delta_volume_liters")

    if not cli.get_functions(installation, {"type": "delta_volume", "topic_read": delta_topic}):
        new_function = Function(installation, type="delta_volume", meta={
            "device_id": function.meta["device_id"],
            "topic_read": delta_topic,
            "lora_type": "delta_volume",
            "eui": function.meta["eui"],
            "name": function.meta["eui"] + " - delta_volume"
        })
        cli.create_function(new_function)

    if not cli.get_functions(installation, {"type": "delta_volume_liters", "topic_read": delta_liters_topic}):
        new_function = Function(installation, type="delta_volume_liters", meta={
            "device_id": function.meta["device_id"],
            "topic_read": delta_liters_topic,
            "lora_type": "delta_liters",
            "eui": function.meta["eui"],
            "name": function.meta["eui"] + " - delta_volume_liters"
        })
        cli.create_function(new_function)

def calculate_deltas(cli, mqttc, installation):
    # Get all current volume functions
    functions = cli.get_functions(installation, {"lora_type": "current_volume"})

    # Traverse all functions and get logs and calculate deltas
    for f in functions:
        create_delta_functions(cli, installation, f)
        delta_topic = f.meta["topic_read"].replace("current_volume", "delta_volume")
        delta_liters_topic = f.meta["topic_read"].replace("current_volume", "delta_volume_liters")
        
        # Start look 48 hours back. Should have at least 24 measurements.
        now = datetime.now()
        start = now.timestamp() - 3600 * 48

        # Get logs from last 25 hours back
        logs = cli.get_logs(installation, fromm=start, limit=25, topics=[f.meta["topic_read"]])

        # Most likely we have 25 lines, but lets use the number given by the API
        # Note that we traverse from 1 to 25 (While we have values from 0 to 24).
        for i in range(1, logs.count):
            # Msg is a json object with start and end and the last accumulated value (don't know if that is needed)       
            msg = '{"start": ' + str(logs.data[i].timestamp) + ', "end": ' + str(logs.data[i-1].timestamp) + ', "end_acc": ' + str(logs.data[i-1].value) + '}'
            delta_cubic_meters = round(logs.data[i-1].value - logs.data[i].value, 3)

            # Convert delta to liters (1 cubic meter = 1000 liters)
            delta_liters = round(delta_cubic_meters * 1000, 3)

            print(f"Delta Volume (m^3): {delta_cubic_meters}, Delta Volume (liters): {delta_liters}")

            # Publish data to mqtt (on delta_topic)
            mqttc.publish(str(installation) + "/" + delta_topic, '{ "value":' + str(delta_cubic_meters) + ', "msg":' + json.dumps(msg) + ', "timestamp": ' + str(logs.data[i-1].timestamp) +  ' }')

            # Publish data to MQTT for delta_volume (liters)
            mqttc.publish(str(installation) + "/" + delta_liters_topic, '{ "value":' + str(delta_liters) + ', "msg":' + json.dumps(msg) + ', "timestamp": ' + str(logs.data[i-1].timestamp) + '}')
