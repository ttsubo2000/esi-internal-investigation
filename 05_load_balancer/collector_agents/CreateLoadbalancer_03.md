# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Loadbalancer(load_balancer_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
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
        "if_name": "1/2"
    }, 
    "resource_type": "load_balancer_interfaces"
}
```

- Response

```
{
    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:22:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "1/2"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "type": "snmp_ports", 
    "id": "c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
    "resource_type": "load_balancer_interfaces"
}
```

### This is JSON data for checking "Loadbalancer(load_balancer_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/c2ad3511-dcc2-4e31-9702-a2e01ea39b27
```

- Response

```
{
    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:22:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "1/2"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "values": [], 
    "type": "snmp_ports", 
    "id": "c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
    "resource_type": "load_balancer_interfaces"
}
```
and then ...
```
{
    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:22:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "1/2"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "interface"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-19T05:23:01Z", 
            "last_changed": "2018-02-19T05:23:01Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-19T05:23:01Z", 
            "last_changed": "2018-02-19T05:23:01Z", 
            "value": 1519017781, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-19T05:23:01Z", 
            "last_changed": "2018-02-19T05:23:01Z", 
            "value": 1519017781, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "c2ad3511-dcc2-4e31-9702-a2e01ea39b27", 
    "resource_type": "load_balancer_interfaces"
}
```
