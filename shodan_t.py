#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shodan

def main:
    api = shodan.Shodan('82IESk6o76nJnPOl0mnm89fvSGHgpSGH')
    try:
    	res = api.search("redis port:\"6379\" country:\"US\"")
    	print(res['total'])
    	with open("./redis_ip.txt","w") as fo:
    		for res in res['matches']:
    			fo.write(res['ip_str'])
    except shodan.APIError as e:
    	print(e)


