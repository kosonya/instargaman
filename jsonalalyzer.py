#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle


def main():
	dump = open("json.pkl", "rb")
	data = pickle.load(dump)
	dump.close()
	print data

if __name__ == "__main__":
	main()
