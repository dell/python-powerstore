class CertificateData():


    certificate_id1 = "37b76535-612b-456a-a694-1389f17632c7"
    certificate_id2 = "37b76535-612b-456a-a694-1389f17632c3"
    invalid_certificate_id = "37b76535-612b-456a-a694-1389f17632c"
    certificate_list = [
        {"id": certificate_id1}
    ]
    certificate_details = {
        "id": "37b76535-612b-456a-a694-1389f17632c7",
        "type": "Client",
        "type_l10n": "Client",
        "service": "Replication_HTTP",
        "service_l10n": "Replication_HTTP",
        "scope": "PS00d01e1bb312",
        "is_current": False,
        "is_valid": True,
        "members": [
            {
                "subject": "C=US+O=Dell+L=Hopkinton+OU=PowerStore+ST=Massachusetts+CN=ReplicationHTTP.PS00d01e1bb312",
                "serial_number": "939c5a1cf39cb49f",
                "signature_algorithm": "SHA256withRSA",
                "issuer": "CN=Dell EMC PowerStore CA VYEEMAKP,O=Dell EMC,ST=MA,C=US",
                "valid_from": "2021-05-26T03:29:15.0Z",
                "valid_to": "2026-05-25T03:29:15.0Z",
                "public_key_algorithm": "RSA",
                "key_length": 4096,
                "thumbprint_algorithm": "SHA-256",
                "thumbprint_algorithm_l10n": "SHA-256",
                "thumbprint": "31e566035b26bca8b1f7506d645aea2310696bbed131e94209349754df58ea8f",
                "certificate": "MIIFaTCCA1GgAwIBAgIJAJOcWhzznLSfMA0GCSqGSIb3DQEBCwUAMFcxCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJNQTERMA8GA1UEChMIRGVsbCBFTUMxKDAmBgNVBAMTH0RlbGwgRU1DIFBvd2VyU3RvcmUgQ0EgVllFRU1BS1AwHhcNMjEwNTI2MDMyOTE1WhcNMjYwNTI1MDMyOTE1WjB8MXowCQYDVQQGEwJVUzALBgNVBAoTBERlbGwwEAYDVQQHEwlIb3BraW50b24wEQYDVQQLEwpQb3dlclN0b3JlMBQGA1UECBMNTWFzc2FjaHVzZXR0czAlBgNVBAMTHlJlcGxpY2F0aW9uSFRUUC5QUzAwZDAxZTFiYjMxMjCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALyiOCzCKfKY/iXpQ/AjhLeCOwEVbvyrK+2m3KWanx3YDMYoj5kePrunzteDobXivsTILAwxTay12pTRCBq3Zrt79VCj3Jo322e7G4c6KDYS9C83W0quAwZwg5HLX9XyndVVD/knJc2uwwUZE8VyScfTrwRTdC9Fh+WPBk84cZGwd2FZdM1b0glogangy3CVnsFoWY/E5sE8n8waupscQSfnSsb+SCByo801uBjAGd/619sapEJ9hvuiWvir7IdO+lcF2xIkD1mYHw2hpYBzfxQYyLDfcFeRIB4O9OzEZ7yr5ZCeK1Z6Gq4e3giISYo45NDEKtXOiYfuK/KhLOjYEC4NsEPQyeSFWYHwcyEVsr3Rpb8SRbhZRDzbxaPj3iZSknyECHowSDRSahUZHIhlX0vAKtGtBLPk3Ek48rZhmnSij2DMwl+KfS95/HojI7q6nmtZzmKvgrtW/dpvij9vBmA8mwm9IZTJYf6A4u7c+XCAFGJweJ2gW2uo36BxsLCze3mmNpH/rwCli0w0aQFEmaJQy8JjoJYdynoGTDgPVLE9tgnJE9MmGWFRkdnnxehfIBsvTlXz1om2Uzgc8at1z26WzCF1XqjWQYsh/5h948uDVNR+5pawYCc1CxRPz3lZkG0jvlUlXHgSrMzIqLfHxGxsqAje/Hvq+wG0DXIWRNo5AgMBAAGjEzARMA8GA1UdEQQIMAaHBArmGCEwDQYJKoZIhvcNAQELBQADggIBAAMZaYIk76FmHr1fsYeRQ+Tek7NiBkFpk0udL2IkJGSeUQLYjWcetMOZIxiIwdJLcmVFykrHBp7ewUPEdFPS2rkNZnrReJlzUXtTdJAWEcCC3sedrk1tb4If+jrhibtgFeg9BxvsUIsLryXB35CuP1mhpT8JnnFnIdTjhxSnQS4IyOipYEtrQMe4gN9OCxhCAY+A/b/X2DMorqGMVJA9OgyKLkOPpACppyde9JpXa+CLPNvz9cVIzEBFYZqa486Ezq5DM86Id/u9+PsFcGbjI1NP6uQwQpMEwm8t4jxb+dLV3wvxOXotQjxsfP8dsU53wBrLXa1Q3ws9JaNSn6k6Q1c1tCnWpTinPeq9o4NaMk4ZOAnQcXgRT/W4V2h7SxDsCNN7yvEsVws58/Dmf1SJwr0FzyFoW/PkPaCEXoDFScnK0HEsN5nwmvN23pzX2IbdPJM6rCUX96mgu70DA7PHmK3SxxZ4iU2uyaGmpxzv9LpwrOPMxhIhdx8nHIc/o4tkxralTFMlC2UE+g06XDC2gOTWWIAHW6GA7zr2+KMQIBwZkotLBrEma7ymhBF1c+NF1vgqvceHpewPBynXZQUwLZ0ZJhTAzui14sBkUc4JZC0LzfDpq4Y+2fSrLHFlhLHMytsitN1YlA+80TCUt3OBtwD891l8eYTaQi5GuBA5TB7Z",
                "depth": 1,
                "subject_alternative_names": [
                    "1xx.2xx.3xx.4xx"
                ]
            }
        ]
    }
    certificate_details_2 = {
        "id": "37b76535-612b-456a-a694-1389f17632c3"
    }
    certificate_error = {
        404: {
               "messages": [
                {
                     "code": "0xE0901001001D",
                     "severity": "Error",
                     "message_l10n": "Failed to find specific certificate id 37b76535-612b-456a-a694-1389f17632c from credential store.",
                     "arguments": [
                                   "37b76535-612b-456a-a694-1389f17632c"
                                  ]
                }
                            ]
              },
        400:  {
                "messages": [
                {
                     "code": "0xE04040010005",
                     "severity": "Error",
                     "message_l10n": "Invalid REST request."
                }
                            ]
              },
        422:  {
                "messages": [
                {
                    "code": "0xE09010010013",
                    "severity": "Error",
                    "message_l10n": "Failed to update certificate in credential store."
                }
                            ]
              }
    }
    certificate_create_response = {
        "id": certificate_id1
    }
    certificate_create_params = {
        "type": "CA_Client_Validation",
        "service": "VASA_HTTP",
        "scope": "",
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIFEjCCAvoCCQCPPyeIag8eITANBgkqhkiG9w0BAQsFADAqMREwDwYDVQQKDAhEZWxsLUVNQzEVMBMGA1UEAwwMd3d3LmRlbGwuY29tMB4XDTIxMDkzMDEwMTIyOVoXDTIyMDkzMDEwMTIyOVowbDFqMAkGA1UEBhMCVVMwDwYDVQQKEwhEZWxsLUVNQzAPBgNVBAsTCFNlY3VyaXR5MBAGA1UEBxMJSG9wa2ludG9uMBMGA1UEAxMMd3d3LmRlbGwuY29tMBQGA1UECBMNTWFzc2FjaHVzZXR0czCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALbe7wpfr43LF99LwSNSpPBC8uV5xC86lNNXNeE7sVDbvb1rKHuiG7jHvs2HoX5bEmRqpwSPe38co1yUQHD4IFbIa0K4LMMh58H3ELf0Valkg2CD+05ZCe0RZgcQqoq6NC135qc0WacIuoP5v87fQNFR2nju06/NyKmUXHblWVRIh5UY0GOXa22OYK8zMxqwasJiYa1xJEjP6QzIRUVxxO6Ia4h9Dvo1LaVoI1cUHI9I3oRMAssqbnbpgPafEnToVWrWtd6dvQeVv3cuUU5n+NpQ9Xv1ITFKH7bRfxUG4hs2cwNsRPa5yzod9vAWzmUcPWYEyfdWU6y39hyFPv7GpQZRRpEdw4DN3wHOnjzAqibaIxIPga/hTQzm0eaJJBh65TnolXKQLiveDScnmB/resiIwBqZpGrPKsAtMpQ/GGYekC8+7yvRZvpfX4dVKB9Z+TdG3JKnXmbH9AkPqqWkFvIhO+jwrIU1gS8bHkzC2ERQ5yY7RohZBNEIQsxTqoQLTNiUiIXRXGpdUDeawW0pub671eqhVyw6h2MrPTE9dKucOPJeiCrd6ctB9VXfXZTM2nb7AvbAF0QicPzV/N5KEJcr+7PFzY2/+KNegPqyLJ776Mqfyc6ri+R8vWPj4iGqsjwmf4rnS4Qq1D5jyGvspNuwVQ8pLRzhOsCW0lUGSTUJAgMBAAEwDQYJKoZIhvcNAQELBQADggIBAGIQdhVVkMNZPf1NSQJZhGpaW4m7dcjNaRamuUOh7LO8yQkkDr+hF38xrlKN5gMtzNEnFTxeqD58rBRAe1MNvvF8pI3ioqNYEQXYu5P9TtZdQW6UPbtFejdBLB2WahWrTJKSGXH/DHl7TU/tesOpN1JirjHv3OtZ1cT0FCxHKBdmCssLhB1DGNQK2aEwXWgrJAMkAQtrjhKHZFLBC6wz8ox5rhvM6Sbqxw5xOLyQu7LnZo3Yhq1rwiobtkhRJoVy/fcwesLfxqsN9oCT4Op4ZndU1CZqHf0tjhJGwFGxmzQNGXZ1Lt29wnSA/ux0/2lTvbFBFRxrCSoZaQf4VRY8pSYB56vz6ODYaalmmj+DQzr9poZzCSJ7Wb6SW/zMJ2kL3TO08hrbZ9MZ4K2zz7QzvVuoVSPT6fGQS2IfmISBTehQgDPjW7w66YzLxxKiRHJxPxPd46CoaFk29AgkQyepr7LsDuvrNyOO/KlVUuQKbiHfLsZVgSDp7Fs5uYC6/3YyXPm1yhYYOwAWFM4Dqytfa1/A2ggrFO9uuhfCLe9MGP3UwE+fX2ZrQS1CCvc1GKuIDQO+Ng0mUC4qXCF9scR+oXp+HeVBX94fiSn6of8BWi4SCXM1qPVzgcJiM7Axcvvuw1pocjF/1NqBn8CEQomAGxW5EQhGE1MOtNK/jfrFSl+2\n-----END CERTIFICATE-----\n",
        "private_key" : "",
        "passphrase": "sample_password",
        "is_current": True
    }
    certificate_reset_params = {
        "service": "VASA_HTTP",
    }
    certificate_exchange_params = {
        "service": "Replication_HTTP",
        "address": "1xx.2xx.3xx.4xx",
        "port": 443,
        "username": "sample_user",
        "password": "sample_password"
    }
    certificate_modify_params = {
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIFEjCCAvoCCQCPPyeIag8eITANBgkqhkiG9w0BAQsFADAqMREwDwYDVQQKDAhEZWxsLUVNQzEVMBMGA1UEAwwMd3d3LmRlbGwuY29tMB4XDTIxMDkzMDEwMTIyOVoXDTIyMDkzMDEwMTIyOVowbDFqMAkGA1UEBhMCVVMwDwYDVQQKEwhEZWxsLUVNQzAPBgNVBAsTCFNlY3VyaXR5MBAGA1UEBxMJSG9wa2ludG9uMBMGA1UEAxMMd3d3LmRlbGwuY29tMBQGA1UECBMNTWFzc2FjaHVzZXR0czCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALbe7wpfr43LF99LwSNSpPBC8uV5xC86lNNXNeE7sVDbvb1rKHuiG7jHvs2HoX5bEmRqpwSPe38co1yUQHD4IFbIa0K4LMMh58H3ELf0Valkg2CD+05ZCe0RZgcQqoq6NC135qc0WacIuoP5v87fQNFR2nju06/NyKmUXHblWVRIh5UY0GOXa22OYK8zMxqwasJiYa1xJEjP6QzIRUVxxO6Ia4h9Dvo1LaVoI1cUHI9I3oRMAssqbnbpgPafEnToVWrWtd6dvQeVv3cuUU5n+NpQ9Xv1ITFKH7bRfxUG4hs2cwNsRPa5yzod9vAWzmUcPWYEyfdWU6y39hyFPv7GpQZRRpEdw4DN3wHOnjzAqibaIxIPga/hTQzm0eaJJBh65TnolXKQLiveDScnmB/resiIwBqZpGrPKsAtMpQ/GGYekC8+7yvRZvpfX4dVKB9Z+TdG3JKnXmbH9AkPqqWkFvIhO+jwrIU1gS8bHkzC2ERQ5yY7RohZBNEIQsxTqoQLTNiUiIXRXGpdUDeawW0pub671eqhVyw6h2MrPTE9dKucOPJeiCrd6ctB9VXfXZTM2nb7AvbAF0QicPzV/N5KEJcr+7PFzY2/+KNegPqyLJ776Mqfyc6ri+R8vWPj4iGqsjwmf4rnS4Qq1D5jyGvspNuwVQ8pLRzhOsCW0lUGSTUJAgMBAAEwDQYJKoZIhvcNAQELBQADggIBAGIQdhVVkMNZPf1NSQJZhGpaW4m7dcjNaRamuUOh7LO8yQkkDr+hF38xrlKN5gMtzNEnFTxeqD58rBRAe1MNvvF8pI3ioqNYEQXYu5P9TtZdQW6UPbtFejdBLB2WahWrTJKSGXH/DHl7TU/tesOpN1JirjHv3OtZ1cT0FCxHKBdmCssLhB1DGNQK2aEwXWgrJAMkAQtrjhKHZFLBC6wz8ox5rhvM6Sbqxw5xOLyQu7LnZo3Yhq1rwiobtkhRJoVy/fcwesLfxqsN9oCT4Op4ZndU1CZqHf0tjhJGwFGxmzQNGXZ1Lt29wnSA/ux0/2lTvbFBFRxrCSoZaQf4VRY8pSYB56vz6ODYaalmmj+DQzr9poZzCSJ7Wb6SW/zMJ2kL3TO08hrbZ9MZ4K2zz7QzvVuoVSPT6fGQS2IfmISBTehQgDPjW7w66YzLxxKiRHJxPxPd46CoaFk29AgkQyepr7LsDuvrNyOO/KlVUuQKbiHfLsZVgSDp7Fs5uYC6/3YyXPm1yhYYOwAWFM4Dqytfa1/A2ggrFO9uuhfCLe9MGP3UwE+fX2ZrQS1CCvc1GKuIDQO+Ng0mUC4qXCF9scR+oXp+HeVBX94fiSn6of8BWi4SCXM1qPVzgcJiM7Axcvvuw1pocjF/1NqBn8CEQomAGxW5EQhGE1MOtNK/jfrFSl+2\n-----END CERTIFICATE-----\n",
        "is_current": True
    }
    invalid_create_certificate = {
        "type": "CA_Client_Validation",
        "scope": "",
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIFEjCCAvoCCQCPPyeIag8eITANBgkqhkiG9w0BAQsFADAqMREwDwYDVQQKDAhEZWxsLUVNQzEVMBMGA1UEAwwMd3d3LmRlbGwuY29tMB4XDTIxMDkzMDEwMTIyOVoXDTIyMDkzMDEwMTIyOVowbDFqMAkGA1UEBhMCVVMwDwYDVQQKEwhEZWxsLUVNQzAPBgNVBAsTCFNlY3VyaXR5MBAGA1UEBxMJSG9wa2ludG9uMBMGA1UEAxMMd3d3LmRlbGwuY29tMBQGA1UECBMNTWFzc2FjaHVzZXR0czCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALbe7wpfr43LF99LwSNSpPBC8uV5xC86lNNXNeE7sVDbvb1rKHuiG7jHvs2HoX5bEmRqpwSPe38co1yUQHD4IFbIa0K4LMMh58H3ELf0Valkg2CD+05ZCe0RZgcQqoq6NC135qc0WacIuoP5v87fQNFR2nju06/NyKmUXHblWVRIh5UY0GOXa22OYK8zMxqwasJiYa1xJEjP6QzIRUVxxO6Ia4h9Dvo1LaVoI1cUHI9I3oRMAssqbnbpgPafEnToVWrWtd6dvQeVv3cuUU5n+NpQ9Xv1ITFKH7bRfxUG4hs2cwNsRPa5yzod9vAWzmUcPWYEyfdWU6y39hyFPv7GpQZRRpEdw4DN3wHOnjzAqibaIxIPga/hTQzm0eaJJBh65TnolXKQLiveDScnmB/resiIwBqZpGrPKsAtMpQ/GGYekC8+7yvRZvpfX4dVKB9Z+TdG3JKnXmbH9AkPqqWkFvIhO+jwrIU1gS8bHkzC2ERQ5yY7RohZBNEIQsxTqoQLTNiUiIXRXGpdUDeawW0pub671eqhVyw6h2MrPTE9dKucOPJeiCrd6ctB9VXfXZTM2nb7AvbAF0QicPzV/N5KEJcr+7PFzY2/+KNegPqyLJ776Mqfyc6ri+R8vWPj4iGqsjwmf4rnS4Qq1D5jyGvspNuwVQ8pLRzhOsCW0lUGSTUJAgMBAAEwDQYJKoZIhvcNAQELBQADggIBAGIQdhVVkMNZPf1NSQJZhGpaW4m7dcjNaRamuUOh7LO8yQkkDr+hF38xrlKN5gMtzNEnFTxeqD58rBRAe1MNvvF8pI3ioqNYEQXYu5P9TtZdQW6UPbtFejdBLB2WahWrTJKSGXH/DHl7TU/tesOpN1JirjHv3OtZ1cT0FCxHKBdmCssLhB1DGNQK2aEwXWgrJAMkAQtrjhKHZFLBC6wz8ox5rhvM6Sbqxw5xOLyQu7LnZo3Yhq1rwiobtkhRJoVy/fcwesLfxqsN9oCT4Op4ZndU1CZqHf0tjhJGwFGxmzQNGXZ1Lt29wnSA/ux0/2lTvbFBFRxrCSoZaQf4VRY8pSYB56vz6ODYaalmmj+DQzr9poZzCSJ7Wb6SW/zMJ2kL3TO08hrbZ9MZ4K2zz7QzvVuoVSPT6fGQS2IfmISBTehQgDPjW7w66YzLxxKiRHJxPxPd46CoaFk29AgkQyepr7LsDuvrNyOO/KlVUuQKbiHfLsZVgSDp7Fs5uYC6/3YyXPm1yhYYOwAWFM4Dqytfa1/A2ggrFO9uuhfCLe9MGP3UwE+fX2ZrQS1CCvc1GKuIDQO+Ng0mUC4qXCF9scR+oXp+HeVBX94fiSn6of8BWi4SCXM1qPVzgcJiM7Axcvvuw1pocjF/1NqBn8CEQomAGxW5EQhGE1MOtNK/jfrFSl+2\n-----END CERTIFICATE-----\n",
        "private_key" : "",
        "passphrase": "sample_password",
        "is_current": True
    }
    invalid_modify_certificate = {
        "certificate": "-----BEGIN CERTIFICATE-----\nMIIFEjCCAvoCCQCPPyeIag8eITANBgkqhkiG9w0BAQsFADAqMREwDwYDVQQKDAhEZWxsLUVNQzEVMBMGA1UEAwwMd3d3LmRlbGwuY29tMB4XDTIxMDkzMDEwMTIyOVoXDTIyMDkzMDEwMTIyOVowbDFqMAkGA1UEBhMCVVMwDwYDVQQKEwhEZWxsLUVNQzAPBgNVBAsTCFNlY3VyaXR5MBAGA1UEBxMJSG9wa2ludG9uMBMGA1UEAxMMd3d3LmRlbGwuY29tMBQGA1UECBMNTWFzc2FjaHVzZXR0czCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALbe7wpfr43LF99LwSNSpPBC8uV5xC86lNNXNeE7sVDbvb1rKHuiG7jHvs2HoX5bEmRqpwSPe38co1yUQHD4IFbIa0K4LMMh58H3ELf0Valkg2CD+05ZCe0RZgcQqoq6NC135qc0WacIuoP5v87fQNFR2nju06/NyKmUXHblWVRIh5UY0GOXa22OYK8zMxqwasJiYa1xJEjP6QzIRUVxxO6Ia4h9Dvo1LaVoI1cUHI9I3oRMAssqbnbpgPafEnToVWrWtd6dvQeVv3cuUU5n+NpQ9Xv1ITFKH7bRfxUG4hs2cwNsRPa5yzod9vAWzmUcPWYEyfdWU6y39hyFPv7GpQZRRpEdw4DN3wHOnjzAqibaIxIPga/hTQzm0eaJJBh65TnolXKQLiveDScnmB/resiIwBqZpGrPKsAtMpQ/GGYekC8+7yvRZvpfX4dVKB9Z+TdG3JKnXmbH9AkPqqWkFvIhO+jwrIU1gS8bHkzC2ERQ5yY7RohZBNEIQsxTqoQLTNiUiIXRXGpdUDeawW0pub671eqhVyw6h2MrPTE9dKucOPJeiCrd6ctB9VXfXZTM2nb7AvbAF0QicPzV/N5KEJcr+7PFzY2/+KNegPqyLJ776Mqfyc6ri+R8vWPj4iGqsjwmf4rnS4Qq1D5jyGvspNuwVQ8pLRzhOsCW0lUGSTUJAgMBAAEwDQYJKoZIhvcNAQELBQADggIBAGIQdhVVkMNZPf1NSQJZhGpaW4m7dcjNaRamuUOh7LO8yQkkDr+hF38xrlKN5gMtzNEnFTxeqD58rBRAe1MNvvF8pI3ioqNYEQXYu5P9TtZdQW6UPbtFejdBLB2WahWrTJKSGXH/DHl7TU/tesOpN1JirjHv3OtZ1cT0FCxHKBdmCssLhB1DGNQK2aEwXWgrJAMkAQtrjhKHZFLBC6wz8ox5rhvM6Sbqxw5xOLyQu7LnZo3Yhq1rwiobtkhRJoVy/fcwesLfxqsN9oCT4Op4ZndU1CZqHf0tjhJGwFGxmzQNGXZ1Lt29wnSA/ux0/2lTvbFBFRxrCSoZaQf4VRY8pSYB56vz6ODYaalmmj+DQzr9poZzCSJ7Wb6SW/zMJ2kL3TO08hrbZ9MZ4K2zz7QzvVuoVSPT6fGQS2IfmISBTehQgDPjW7w66YzLxxKiRHJxPxPd46CoaFk29AgkQyepr7LsDuvrNyOO/KlVUuQKbiHfLsZVgSDp7Fs5uYC6/3YyXPm1yhYYOwAWFM4Dqytfa1/A2ggrFO9uuhfCLe9MGP3UwE+fX2ZrQS1CCvc1GKuIDQO+Ng0mUC4qXCF9scR+oXp+HeVBX94fiSn6of8BWi4SCXM1qPVzgcJiM7Axcvvuw1pocjF/1NqBn8CEQomAGxW5EQhGE1MOtNK/jfrFSl+2\n-----END CERTIFICATE-----\n"
    }
