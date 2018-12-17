from services.opensrs.stage import osrs

def testCall(service):
	if service == 0:
		#OpenSRS API
		# 3 Args minumum
			# Arg #0: 0 = lookup, 1 = registration
			# Arg #1: 0 = live, 1 = test
			# Arg #2: domain
			# Arg 3+: contacts or nameservers, in heiracherial order
				#if Arg contains '.' then nameserver
				#else contact
		response = osrs(1,1,'examplesarethebest.com','test','ns1.digitalocean.com','default','ns2.digitalocean.com','test')
#check log folder for input and output
testCall(0)
