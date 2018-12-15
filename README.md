# OpenSRS_Domains_Client
# v 1.0
# Written by Tudor Ciolac
# Dec 14th 2018
# Prerequisites python3
# Dependancies. Stock Python 3 Libs & requests (obtained via pip installer: https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3, https://stackoverflow.com/questions/17309288/importerror-no-module-named-requests)

#Purpose: Sends requests to the OpenSRS Domains API Service

#Parameters Needed:
#See testCaller.py

#Authentication:
#Input your username and api key in openSRS_python_client/core/getCredentials.py

#Features:
#Logs requests and responses in the logs directory. Log file hierachy auto-generated based on date
#Submits 'Lookup' and 'Register' requests, but is flexible to work with virtually all domain request types
#Reads contact handles stored in JSON format
#Submits default values if no nameservers or contact handles are presented in args
