def customNS(*nsx):
    count = (len(nsx))
    if count < 2:
        return False
    if count > 1:
        key = -1
        sort = 0
        XMLchild = ""
        for ns in nsx:
            if sort < count:
                sort += 1
                key += 1
            XMLns='''
            <item key="{Key}">
            <dt_assoc>
            <item key="name">{NS}</item>
            <item key="sortorder">{Sort}</item>
            </dt_assoc>
            </item>
            '''.format(NS=ns, Key = key, Sort = sort)
            XMLchild += XMLns
        xml='''
        <item key="nameserver_list">
        <dt_array>
        {XMLChild}
        </dt_array>
        </item>
        '''.format(XMLChild = XMLchild)
        return xml