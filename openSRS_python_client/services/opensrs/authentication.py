def authentication(testMode):
    from core.getCredentials import keyGuard
    if testMode == 1:
        user = keyGuard('apiOpenSRSTest','user')
        key = keyGuard('apiOpenSRSTest','apiKey')
        host = keyGuard('apiOpenSRSTest','host')
    else:
        user = keyGuard('apiOpenSRSProd','user')
        key = keyGuard('apiOpenSRSProd','apiKey')
        host = keyGuard('apiOpenSRSProd','host')
    return {'user' : user, 'key': key, 'host' : host}

#Double md5 header hash

def headers(currentRequest,user,key):
    import hashlib
    md5_obj = hashlib.md5()
    md5_obj.update((currentRequest + key).encode('utf-8'))
    signature = md5_obj.hexdigest()

    md5_obj = hashlib.md5()
    md5_obj.update((signature + key).encode('utf-8'))
    signature = md5_obj.hexdigest()

    headers = {
        'Content-Type':'text/xml',
        'X-Username': user,
        'X-Signature': signature,
    }
    return headers