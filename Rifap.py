# -*- CREATED BY: DtxdF -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-

from thread import *
from json import *
from requests import *
from colorama import init, Fore
from time import sleep

init()

class color:
	red = Fore.RED
	blue = Fore.BLUE
	green = Fore.GREEN
	yellow = Fore.YELLOW
	cyan = Fore.CYAN
	error = Fore.RED+"["+Fore.RESET+"-"+Fore.RED+"]"+Fore.RESET+" "
	adv = Fore.YELLOW+"["+Fore.RESET+"!"+Fore.YELLOW+"]"+Fore.RESET+" "
	ble = Fore.BLUE+"["+Fore.RESET+"*"+Fore.BLUE+"]"+Fore.RESET+" "
	reset = Fore.RESET
	
def error_msg(msg):
	print "\n"
	print color.error+color.red+"Error {0} not found".format(msg)+color.reset
	
def resquest_proc():
	
	code_error = "Apparently you are not connected to the internet, The answer was not positive:"
	
	try:
		if get("http://example.com").status_code == 200:
			pass
		else:
			print code_error+" %s" % str(get("http://example.com").status_code)
	except exceptions.ConnectionError:
		print code_error+" 404"
	except Exception as a:
		print "Unknown error ..."
			
api_key = '<Your API KEY>'

if api_key == '':
	api_key == None

def geo(number):
	try:
		if api_key == None:
			print color.yellow+"[!] "+color.reset+"Your API its not defined ..."
			sleep(5)
			exit()
		api = 'http://apilayer.net/api/validate?access_key='+api_key+'&number='+number+'&country_code&format=1'
		get_out = get(api)
		content = get_out.text
		obj = loads(content)
		
		# TEXT TO SHOW IN THE WINDOW
		
		valid = obj['valid']
		number = obj['local_format']
		country = obj['country_name']
		country_code = obj['country_code']
		carrier_number = obj['carrier']
		line = obj['line_type']
		location = obj['location']
		
		if valid == 'False':
			print color.red+"[-] "+color.reset+"The number is invalid ..."
			sleep(5)
			exit()
		if country == '':
			country = None
			error_msg("Country")
		if country_code == '':
			country_code = None
			error_msg("Country Code")
		if carrier_number == '':
			carrier_number = None
			error_msg("Carrier of number")
		if line == '':
			line = None
			error_msg("Line type")
		if location == '':
			location = None
			error_msg("Location")
			
		print "\n"
		print "\tNumber \t\t::"+color.yellow+" {0}".format(number)+color.reset
		print "\tCountry \t::"+color.yellow+" {0}({1})".format(country,country_code)+color.reset
		print "\tCompany \t::"+color.yellow+" {0}".format(carrier_number)+color.reset
		print "\tLine type \t::"+color.yellow+" {0}".format(line)+color.reset
		print "\tLocation \t::"+color.yellow+" {0}".format(location)+color.reset
		print "\n"
	except exceptions.ConnectionError as a:
		print color.error+"Failed Connection ..."
	except Exception as a:
		print color.error+"Error: %s" % str(a)
print """
	*----------------------------------------*
	*                                        *
	*                                        *
	* [ Retrieving information from a phone  *
	*   (Rifap) ]                            *
	*                                        *
	* [ A script to gather the information   *
	*   of a telephone, using the api of:    *
	*        https://numverify.com/ ]        *
	*                                        *
	*          [Created by: DtxdF]           *
	*                                        *
	*----------------------------------------*
"""

print "\nInsert a phone number with the country code, example: %s\n" % str("+1 412-858-6273")

start_new(resquest_proc, ())

while True:
	try:
		debug = raw_input(color.ble+"Number: "+color.yellow).strip()
		color.reset
		if not debug:
			continue
		else:
			geo(debug)
	except KeyboardInterrupt as a:
		print color.adv+"CTRL-C ..."
		sleep(3.5)
		exit()
	except EOFError as a:
		print color.error+"Invalid key"
	except Exception as a:
		print color.error+"Error: "+str(a)