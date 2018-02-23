# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Firewall(firewall_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"
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
        "if_name": "dp0s5"
    }, 
    "resource_type": "firewall_interfaces"
}
```

- Response

```
{
    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704", 
    "field_name": "interface", 
    "created_at": "2018-02-12T07:44:52Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s5"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/9d7a43c7-40e2-4703-9205-d76939462572", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"
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
    "id": "9d7a43c7-40e2-4703-9205-d76939462572", 
    "resource_type": "firewall_interfaces"
}
```

### This is JSON data for checking "Firewall(firewall_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9d7a43c7-40e2-4703-9205-d76939462572
```

- Response

```
{
    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704", 
    "field_name": "interface", 
    "created_at": "2018-02-12T07:44:52Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s5"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/9d7a43c7-40e2-4703-9205-d76939462572", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"
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
    "id": "9d7a43c7-40e2-4703-9205-d76939462572", 
    "resource_type": "firewall_interfaces"
}
```
and then ...
```
{
    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704", 
    "field_name": "interface", 
    "created_at": "2018-02-12T07:44:52Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "dp0s5"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/9d7a43c7-40e2-4703-9205-d76939462572", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "cdf30a48-8cf7-4935-9f8a-5b51f1177704"
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
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-12T07:45:52Z", 
            "last_changed": "2018-02-12T07:45:52Z", 
            "value": 1518421552, 
            "key": "traffic.in", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "9d7a43c7-40e2-4703-9205-d76939462572", 
    "resource_type": "firewall_interfaces"
}
```
