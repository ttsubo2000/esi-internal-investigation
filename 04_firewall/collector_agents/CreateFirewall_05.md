# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Firewall(firewall_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "field_name": "interface", 
    "type": "snmp_ports", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s4"
    }, 
    "resource_type": "firewall_interfaces"
}
```

- Response

```
{
    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
    "field_name": "interface", 
    "created_at": "2018-02-12T07:44:52Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s4"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/d82baca9-9854-4da2-80c8-f823489be960", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "type": "snmp_ports", 
    "id": "d82baca9-9854-4da2-80c8-f823489be960", 
    "resource_type": "firewall_interfaces"
}
```

### This is JSON data for checking "Firewall(firewall_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d82baca9-9854-4da2-80c8-f823489be960
```

- Response

```
{
    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
    "field_name": "interface", 
    "created_at": "2018-02-12T07:44:52Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s4"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/d82baca9-9854-4da2-80c8-f823489be960", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [], 
    "type": "snmp_ports", 
    "id": "d82baca9-9854-4da2-80c8-f823489be960", 
    "resource_type": "firewall_interfaces"
}
```
and then ...
```
{
    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
    "field_name": "interface", 
    "created_at": "2018-02-12T07:44:52Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s4"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/d82baca9-9854-4da2-80c8-f823489be960", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-12T07:45:52Z", 
            "last_changed": "2018-02-12T07:45:52Z", 
            "value": 1518421552, 
            "key": "traffic.out", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-12T07:45:52Z", 
            "last_changed": "2018-02-12T07:45:52Z", 
            "value": 1518421552, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-12T07:45:52Z", 
            "last_changed": "2018-02-12T07:45:52Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "d82baca9-9854-4da2-80c8-f823489be960", 
    "resource_type": "firewall_interfaces"
}
```
