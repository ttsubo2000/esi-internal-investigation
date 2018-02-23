# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Loadbalancer(load_balancer_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63"
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
        "if_name": "0/1"
    }, 
    "resource_type": "load_balancer_interfaces"
}
```

- Response

```
{
    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:22:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "0/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63"
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
    "id": "130f173c-2799-4337-8ee5-d1a93a9882a9", 
    "resource_type": "load_balancer_interfaces"
}
```

### This is JSON data for checking "Loadbalancer(load_balancer_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9
```

- Response

```
{
    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:22:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "0/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63"
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
    "id": "130f173c-2799-4337-8ee5-d1a93a9882a9", 
    "resource_type": "load_balancer_interfaces"
}
```
and then ...
```
{
    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63", 
    "field_name": "interface", 
    "created_at": "2018-02-19T05:22:01Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3", 
        "if_name": "0/1"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63"
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
    "id": "130f173c-2799-4337-8ee5-d1a93a9882a9", 
    "resource_type": "load_balancer_interfaces"
}
```
