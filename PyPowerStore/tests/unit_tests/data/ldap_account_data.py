class LdapAccountData:
    ldap_account_list = [
        "37b76535-612b-456a-a694-1389f17632c7",
        "37b76535-612b-456a-a694-1389f17632c",
    ]

    ldap_account_list = [
        {
            "id": "2",
            "role_id": "1",
            "domain_id": "2",
            "name": "ldap_test_user_1",
            "type": "User",
            "type_l10n": "User",
            "dn": "cn=ldap_test_user_1,dc=ansildap,dc=com",
        },
    ]

    ldap_account_details1 = {
        "id": "2",
        "role_id": "1",
        "domain_id": "2",
        "name": "ldap_test_user_1",
        "type": "User",
        "type_l10n": "User",
        "dn": "cn=ldap_test_user_1,dc=ansildap,dc=com",
    }

    create_ldap_account_dict = {
        "domain_id": "2",
        "name": "ldap_test_user_1",
        "type": "User",
        "role_id": "1",
    }

    modify_ldap_account_dict = {"role_id": "2"}

    create_ldap_account_response = {"id": "2"}
