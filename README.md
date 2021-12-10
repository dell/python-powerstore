# PyPowerStore
PyPowerStore is a python library which lets you 
manage Dell EMC PowerStore.


## Installation

###- PyPowerStore can be installed from pypi.org using below mentioned command:
        
        pip install PyPowerStore==<pypowerstore_version>

        'pypowerstore_version' needs to be replaced with actual version. 

###- PyPowerStore can be installed from the source code in github using below mentioned steps:
  
  i) go to the root of the project where setup.py file is present, and execute:

        pip install .

## Examples

The examples for the library are available under 'ProgrammersGuideExamples' folder.

```
from PyPowerStore import powerstore_conn

conn = powerstore_conn.PowerStoreConn('user',
                                      'password',
                                      'IP',
                                      False)


volume_create = conn.provisioning.create_volume(name='foo',
                                                size=1073741824)
all_replication_rules = conn.protection.get_replication_rules()
all_networks = conn.config_mgmt.get_networks()

```


## Documentation

The library docs are available under 'docs' folder.


## Requirements

This library uses python's "requests" library.

PyPowerStore officially supports Python 3.7, 3.8 and 3.9.


## Support

PyPowerStore is supported by Dell EMC and is provided under the terms of the license attached to the source code.
For any setup, configuration issues, questions or feedback, join the [Dell EMC Automation community](https://www.dell.com/community/Automation/bd-p/Automation).
For any Dell EMC storage issues, please contact Dell support at: https://www.dell.com/support.
For clarity, Dell EMC does not provide support for any source code modifications.
