import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

header = {"Authorization": config.get('openet_key') }

args = {
	"date_range": [
		"2023-01-01",
		"2023-12-31"
	],
	"interval": "monthly",
	"geometry": [
		-121.78441021712464, 36.73156565501349
	],
	"model": "Ensemble",
	"variable": "ET",
	"reference_et": "gridMET",
	"units": "mm",
	"file_format": "JSON"
}

res = requests.post(headers=header, json=args, url="https://openet-api.org/raster/timeseries/point")

print(res.json())