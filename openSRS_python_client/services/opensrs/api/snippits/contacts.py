import sys
sys.path.append('../')
import json
import os.path
#if custom_nameservers = 1
def contactData(contactHandle):
    contactFile = 'data/domains/contactHandles/'+contactHandle+'.json'
    try:
        os.path.isfile(contactFile)
    except:
        contactFile = 'data/domains/contactHandles/default.json'
    with open(contactFile,'r') as read_file:
        data = json.load(read_file)
    xml = '''
    <dt_assoc>
    <item key="country">{country}</item>
    <item key="address3">{address3}</item>
    <item key="org_name">{org_name}</item>
    <item key="phone">{phone}</item>
    <item key="last_name">{last_name}</item>
    <item key="address2">{address2}</item>
    <item key="state">{state}</item>
    <item key="email">{email}</item>
    <item key="city">{city}</item>
    <item key="postal_code">{postal_code}</item>
    <item key="fax">{fax}</item>
    <item key="address1">{address1}</item>
    <item key="first_name">{first_name}</item>
    </dt_assoc>
    '''.format(
        first_name = data['details']['first_name'],
        last_name = data['details']['last_name'],
        org_name = data['details']['org_name'],
        email = data['details']['email'],
        country = data['details']['country'],
        state = data['details']['state'],
        city = data['details']['city'],
        postal_code = data['details']['postal_code'],
        address1 = data['details']['address1'],
        address2 = data['details']['address2'],
        address3 = data['details']['address3'],
        phone = data['details']['phone'],
        fax = data['details']['fax']
    )
    return xml
