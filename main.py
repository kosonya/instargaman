#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import datetime
import time
import pickle

def make_request_string(lat = None, lng = None, min_timestamp = None, max_timestamp = None, distance = None, access_token = "1788801871.ea82aa4.5a449ec870444423ac313b1de80b3b46"):
	res = "https://api.instagram.com/v1/media/search?access_token=%s" % access_token
	if lat:
		res += "&lat=%f" % lat
	if lng:
		res += "&lng=%f" % lng
	if min_timestamp:
		res += "&min_timestamp=%f" % min_timestamp
	if max_timestamp:
		res += "&max_timestamp=%f" % max_timestamp
	if distance:
		res += "&distance=%d" % distance
	return res

def main():
	start_t = datetime.datetime(year = 2013, month = 9, day = 10, hour = 10, minute = 0)
	stop_t = datetime.datetime(year = 2013, month = 9, day = 11, hour = 20, minute = 0)

	start_timestamp = time.mktime(start_t.timetuple())
	stop_timestamp = time.mktime(stop_t.timetuple())

	request_string = make_request_string(lat=36.30, lng=-86.90, distance=5000)

	print request_string

	r = requests.get(request_string)

	print r.status_code
	print r.text
	print r.json()

	dump = open("json.pkl", "wb")
	pickle.dump(r.json(), dump)
	dump.clos()

if __name__ == "__main__":
	main()
