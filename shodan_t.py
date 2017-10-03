#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shodan

def main():
    api = shodan.Shodan('API_Key')
    try:
    	res = api.search("redis port:\"6379\" country:\"US\"")
    	print(res['total'])
    	with open("./redis_ip.txt","w") as fo:
    		for res in res['matches']:
    			fo.write(res['ip_str'])
    except shodan.APIError as e:
    	print(e)
        
        
if __name__ == '__main__':
	main()


