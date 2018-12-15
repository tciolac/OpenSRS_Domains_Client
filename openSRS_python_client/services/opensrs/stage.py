import requests
from logs import stenotype
import services.opensrs.api.register as osrsRegister
from services.opensrs.api.lookup import lookup as osrsLookup
from services.opensrs.authentication import authentication as osrsAuthentication
from services.opensrs.authentication import headers as osrsHeaders

def osrs(testmode,service,domain,*args):
 	#Lookup
	if service == 0:
		currRequest = osrsLookup(domain)
	#Register
	if service == 1:
		nameservers = []
		contacts = []
		for arg in args:
			if '.' in arg:
				nameservers.append(arg)
			else:
				contacts.append(arg)
		nsList = osrsRegister.takeNameservers(*nameservers)
		contactList = osrsRegister.takeContacts(*contacts)
		currRequest = osrsRegister.register(domain,nsList,contactList)
	authentication = osrsAuthentication(testmode)
	currHeaders = osrsHeaders(currRequest,authentication['user'],authentication['key'])
	request =  "\nRequest:\n" + str(currHeaders) + "\n" + str(currRequest) + "\n\nResponse:"
	response = (requests.post(authentication['host'], data=currRequest, headers=currHeaders)).text
	stenotype.logEvent(request + response,testmode)