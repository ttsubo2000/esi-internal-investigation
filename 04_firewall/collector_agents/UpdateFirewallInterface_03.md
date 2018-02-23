# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Update Firewall Interface(firewall_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 2, 
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
    "created_at": "2018-02-12T07:49:04Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s4"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/52573ce4-285d-4e48-859b-fdabcfc88a89", 
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
    "id": "52573ce4-285d-4e48-859b-fdabcfc88a89", 
    "resource_type": "firewall_interfaces"
}
```

### This is JSON data for checking "Firewall Interface(firewall_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/52573ce4-285d-4e48-859b-fdabcfc88a89
```

- Response

```
{
    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
    "field_name": "interface", 
    "created_at": "2018-02-12T07:49:04Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s4"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/52573ce4-285d-4e48-859b-fdabcfc88a89", 
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
    "id": "52573ce4-285d-4e48-859b-fdabcfc88a89", 
    "resource_type": "firewall_interfaces"
}
```
and then ...
```
{
    "resource_id": "3543155d-0d9a-43a3-ae77-3479cf8a0e4a", 
    "field_name": "interface", 
    "created_at": "2018-02-12T07:49:04Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s4"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/52573ce4-285d-4e48-859b-fdabcfc88a89", 
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
            "last_reported": "2018-02-12T07:50:52Z", 
            "last_changed": "2018-02-12T07:50:52Z", 
            "value": 1518421852, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-12T07:50:52Z", 
            "last_changed": "2018-02-12T07:50:52Z", 
            "value": 1518421852, 
            "key": "traffic.out", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-12T07:50:52Z", 
            "last_changed": "2018-02-12T07:49:52Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "52573ce4-285d-4e48-859b-fdabcfc88a89", 
    "resource_type": "firewall_interfaces"
}
```
