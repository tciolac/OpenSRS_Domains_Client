def keyGuard(item,value):
	keyChain = {
			'apiOpenSRSTest' : {
				'user':'ENTERUSERNAME',
				'apiKey':'ENTERAPIKEY',
				'host':'https://horizon.opensrs.net:55443'
			},
			'apiOpenSRSProd' : {
				'user':'ENTERUSERNAME',
				'apiKey':'ENTERAPIKEY',
				'host':'rr-n1-tor.opensrs.net:55443'
			}
		}

	return (keyChain[item][value])