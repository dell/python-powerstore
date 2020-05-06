# -*- coding: utf-8 -*-
# Copyright: (c) 2019, Dell EMC

""" Protection Policy Module Operations"""

from PyPowerStore import powerstore_conn

CONN = powerstore_conn.PowerStoreConn(username="<username>",
                                      password="<password>",
                                      server_ip="<IP>",
                                      verify=False,
                                      application_type="<Application>")

# Snapshot rule examples
# Create a snapshot rule by interval
RESP = CONN.protection.create_snapshot_rule_by_interval(
    name="pr-sdk-srule", desired_retention=1, interval="Fifteen_Minutes",
    days_of_week=["Monday", "Tuesday"]
)
CREATED_SRULE_ID = RESP.get("id")
print(RESP)

# Get a list of snapshot rules
RESP = CONN.protection.get_snapshot_rules()
print(RESP)

# Get details of a particular snapshot rule
RESP = CONN.protection.get_snapshot_rule_details(
    snapshot_rule_id=CREATED_SRULE_ID
)
print(RESP)

# Get a snapshot rule by name
RESP = CONN.protection.get_snapshot_rule_by_name(name="pr-sdk-srule")
print(RESP)

# Modify a snapshot rule
RESP = CONN.protection.modify_snapshot_rule(
    snapshot_rule_id=CREATED_SRULE_ID, name="pr-sdk-srule-modified",
    desired_retention=8, interval="Four_Hours"
)
print(RESP)

# Delete a snapshot rule
CONN.protection.delete_snapshot_rule(snapshot_rule_id=CREATED_SRULE_ID)

# Protection policy examples
SRULE_IDS = []
for index in range(1, 4):
    srule_id = CONN.protection.create_snapshot_rule_by_interval(
        name="pr-sdk-srule-{}".format(index), desired_retention=1,
        interval="Five_Minutes").get('id')
    if srule_id:
        SRULE_IDS.append(srule_id)
# Create a protection policy
RESP = CONN.protection.create_protection_policy(
    name="pr-sdk-prot-pol",
    description="protection policy for testing pypowerstore",
    snapshot_rule_ids=SRULE_IDS[:1]
)
CREATED_PP_ID = RESP.get("id")
print(RESP)

# Get a list of protection policies
RESP = CONN.protection.get_protection_policies()
print(RESP)

# Get details of a particular protection policy
RESP = CONN.protection.get_protection_policy_details(policy_id=CREATED_PP_ID)
print(RESP)

# Get a protection policy by name
RESP = CONN.protection.get_protection_policy_by_name(name="pr-sdk-prot-pol")
print(RESP)

# Add snapshot rules to the protection policy
RESP = CONN.protection.add_snapshot_rules_to_protection_policy(
    policy_id=CREATED_PP_ID, add_snapshot_rule_ids=SRULE_IDS[1:]
)
print(RESP)

# Remove snapshot rules from the protection policy
RESP = CONN.protection.remove_snapshot_rules_from_protection_policy(
    policy_id=CREATED_PP_ID, remove_snapshot_rule_ids=SRULE_IDS
)
print(RESP)

# Delete a protection policy
CONN.protection.delete_protection_policy(policy_id=CREATED_PP_ID)
for srule_id in SRULE_IDS:
    CONN.protection.delete_snapshot_rule(snapshot_rule_id=srule_id)
