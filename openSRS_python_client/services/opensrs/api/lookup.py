#lookup as per https://domains.opensrs.guide/docs/lookup-domain
def lookup(domain):
    xml = '''\
    <?xml version='1.0' encoding="UTF-8" standalone="no" ?>
    <!DOCTYPE OPS_envelope SYSTEM "ops.dtd">
    <OPS_envelope>
        <header>
            <version>0.9</version>
        </header>
        <body>
            <data_block>
                <dt_assoc>
                    <item key="protocol">XCP</item>
                    <item key="object">DOMAIN</item>
                    <item key="action">LOOKUP</item>
                    <item key="attributes">
                        <dt_assoc>
                            <item key="domain">{Domain}</item>
                            <item key="no_cache">1</item>
                        </dt_assoc>
                    </item>
                    <item key="registrant_ip">111.121.121.121</item>
                </dt_assoc>
            </data_block>
        </body>
    </OPS_envelope>\
    '''.format(Domain = domain)
    return xml