import json
import string
import requests
import sched
import time
from traffic_speed_prediction.util.config.ReadConfig import read_config, convert_to_date
from traffic_speed_prediction.model.Dataobject import Dataobject


# Fetch data from any given endpoint
def get_text_from_endpoint(path: string):
    return requests.get(path).text


def fetch_and_create_db_object_from_tms_station_data():
    objects = []

    # Runs through the specified id's in the data.json file and fetches all the data
    # Then creates a Dataobject 0
    for station_id in read_config()["urls"]["tms_station"]["ids"]:
        data = json.loads(requests.get(read_config()["urls"]["tms_station"]["base_url"] + station_id).text)
        for item in data['tmsStations'][0]['sensorValues']:
            if item["sensorUnit"] == "km/h":
                object_id = item["id"]
                roadstation_id = item["roadStationId"]
                station_name = read_config()["urls"]["tms_station"]["ids"][station_id]
                speed = item["sensorValue"]
                date = convert_to_date(item["measuredTime"])[0]
                time = convert_to_date(item["measuredTime"])[1]
                data_object = Dataobject(object_id, roadstation_id, station_name, speed, date, time)
                objects.append(data_object)

    # Returns a list of Dataobjects
    return objects


def repeat_fetching(minutes: int):
    timer = time.time()
    minutes = minutes * 60
    counter = 0
    while True:
        counter += 1
        print("CURRENT BATCH: " + str(counter) + " DATA = ")
        for item in fetch_and_create_db_object_from_tms_station_data():
            print(item.tostring())
        time.sleep(minutes - ((time.time() - timer) % minutes))


# Test code
if __name__ == '__main__':
    repeat_fetching(1)
