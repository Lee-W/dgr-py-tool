"""
dgr-py-tool: A tool for Data Garage usage

Usage
-----

Usage is simple::

    import dgr

"""

import requests

def fetchAll(dataId): 
	res = requests.get('http://localhost:3000/api/' + dataId)
	return res.content

# print(fetchAll('52e12d31203b41ab5d14964b'))

def fetchCustom(dataId, form):
	res = requests.get('http://localhost:3000/api/' + dataId, params=form)
	return res.content

# print(fetchCustom('52e12d31203b41ab5d14964b', {'limit': '3'}))