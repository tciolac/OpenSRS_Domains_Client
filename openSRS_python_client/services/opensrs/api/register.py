import string
import random
from services.opensrs.api.snippits.nameservers import customNS
from services.opensrs.api.snippits.contacts import contactData

regParams = {
    "autoRenew":"0",
    "regType":"new",
    "regUsername" : ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)),
    "regPassword" : ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12)),
    "contactPrivacyBool":"0",
    "period":"1"
}

def takeNameservers(*nameservers):
    nsData = []
    if len(nameservers) != 0:
        if len(nameservers) < 2:
            return "At least two nameservers are required"
        else:
            nsData.append('1')
            nsData.append(customNS(*nameservers))
    #if no nameservers provided set to stock registrar nameservers
    else:
        nsData.append('0')
        nsData.append("")
    return(nsData)

def takeContacts(*contacts):
    userInput = False
    counter = 0
    contactXML = []
    if len(contacts) <= 4 and len(contacts) != 0:
        userInput = True
        for c in contacts:
            contactXML.append(contactData(c))
            counter += 1
        while counter < 4 and userInput == False:
            contactXML.append(contactData('default'))
            counter += 1
    if len(contacts) > 4:
        return "Too many contacts provided"
    else:
        while counter < 4:
            contactXML.append(contactData('default'))
            counter += 1
    return(contactXML)

#register as per https://domains.opensrs.guide/docs/sw_register-domain
def register(domain,nameservers,contacts):

    xml = '''
    <?xml version='1.0' encoding="UTF-8" standalone="no"?>
    <OPS_envelope>
    <header>
    <version>0.9</version>
    </header>
    <body>
    <data_block>
    <dt_assoc>
    <item key="protocol">XCP</item>
    <item key="object">DOMAIN</item>
    <item key="action">SW_REGISTER</item>
    <item key="attributes">
    <dt_assoc>
    <item key="auto_renew">{AutoRenew}</item>
    <item key="domain">{Domain}</item>
    <item key="reg_type">{RegType}</item>
    <item key="reg_username">{RegUsername}</item>
    <item key="reg_password">{RegPassword}</item>
    <item key="f_whois_privacy">{ContactPrivacyBool}</item>
    <item key="period">{Period}</item>
    <item key="custom_nameservers">{NameserverBool}</item>
    <item key="handle">process</item>
    <item key="contact_set">
    <dt_assoc>
    <item key="owner">
    {OwnerContact}
    </item>
    <item key="admin">
    {AdminContact}
    </item>
    <item key="billing">
    {BillingContact}
    </item>
    <item key="tech">
    {TechContact}
    </item>
    </dt_assoc>
    </item>
    {NSXML}
    </dt_assoc>
    </item>
    </dt_assoc>
    </data_block>
    </body>
    </OPS_envelope>
    '''.format(
        Domain = domain,
        NameserverBool = nameservers[0],
        NSXML = nameservers[1],
        OwnerContact = contacts[0],
        AdminContact = contacts[1],
        TechContact = contacts[2],
        BillingContact = contacts[3],
        AutoRenew = regParams['autoRenew'],
        RegType = regParams['regType'],
        RegUsername = regParams['regUsername'],
        RegPassword = regParams['regPassword'],
        ContactPrivacyBool = regParams['contactPrivacyBool'],
        Period = regParams['period']
        )
    return xml
