# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Update Loadbalancer Interface(load_balancer_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 2, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
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
        "if_name": "1/1"
    }, 
    "resource_type": "load_balancer_interfaces"
}
```

- Response

```
{
    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:26:26Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "1/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
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
    "id": "9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
    "resource_type": "load_balancer_interfaces"
}
```

### This is JSON data for checking "Loadbalancer Interface(load_balancer_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8
```

- Response

```
{
    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:26:26Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "1/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
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
    "id": "9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
    "resource_type": "load_balancer_interfaces"
}
```
and then ...
```
{
    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:26:26Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "1/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
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
            "last_reported": "2018-02-19T05:28:01Z", 
            "last_changed": "2018-02-19T05:28:01Z", 
            "value": 1519018081, 
            "key": "traffic.out", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-19T05:28:01Z", 
            "last_changed": "2018-02-19T05:27:01Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-19T05:28:01Z", 
            "last_changed": "2018-02-19T05:28:01Z", 
            "value": 1519018081, 
            "key": "traffic.in", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
    "resource_type": "load_balancer_interfaces"
}
```
