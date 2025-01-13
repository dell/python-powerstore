class LdapData():
    ldap_list = [
        "37b76535-612b-456a-a694-1389f17632c7",
        "37b76535-612b-456a-a694-1389f17632c"]

    ldap_domain_list = [{
        'protocol_l10n': 'LDAP',
        'ldap_timeout': 30000,
        'is_global_catalog': False,
        'ldap_servers': ['xx.xxx.x.xx'],
        'domain_name': "ldap.com",
        'ldap_server_type': 'AD',
        'user_object_class': 'user',
        'ldap_server_type_l10n': 'AD',
        'protocol': 'LDAP',
        'user_search_path': 'cn=Users',
        'group_object_class': 'group',
        'user_id_attribute': 'sAMAccountName',
        'port': 389,
        'group_search_level': 0,
        'group_search_path': 'cn=Users',
        'id': '3',
        'group_member_attribute': 'member',
        'bind_user': 'cn=admin,dc=ldap,dc=com',
        'group_name_attribute': 'cn'
    }]

    ldap_domain_details1 = {
        'protocol_l10n': 'LDAP',
        'ldap_timeout': 30000,
        'is_global_catalog': False,
        'ldap_servers': ['xx.xxx.x.xx'],
        'domain_name': "ldap.com",
        'ldap_server_type': 'AD',
        'user_object_class': 'user',
        'ldap_server_type_l10n': 'AD',
        'protocol': 'LDAP',
        'user_search_path': 'cn=Users',
        'group_object_class': 'group',
        'user_id_attribute': 'sAMAccountName',
        'port': 389,
        'group_search_level': 0,
        'group_search_path': 'cn=Users',
        'id': '3',
        'group_member_attribute': 'member',
        'bind_user': 'cn=admin,dc=ldap,dc=com',
        'group_name_attribute': 'cn'
    }

    create_ldap_domain_dict = {
        "domain_name": "<<domain_name>>",
        "ldap_servers": [
            "<<ldap_server_ip>>"
        ],
        "protocol": "LDAP",
        "ldap_server_type": "AD",
        "bind_user": "<<LDAP_user_DN>>",
        "bind_password": "<<password>>",
        "is_global_catalog": False,
        "user_search_path": "cn=Users",
        "group_search_path": "cn=Users"
    }

    modify_ldap_domain_dict = {
        "ldap_server_type": "OpenLDAP"
    }

    create_ldap_domain_response = {'id': '3'}
