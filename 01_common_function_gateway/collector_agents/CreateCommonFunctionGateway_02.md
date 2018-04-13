# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Common Function Gateway(logical_port)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824"
                    }
                ]
            }
        }, 
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        }
    }, 
    "field_name": "logical_port", 
    "type": "snmp_ports", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3.1025"
    }, 
    "resource_type": "ese_logical_ports"
}
```

- Response

```
{
    "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824", 
    "field_name": "logical_port", 
    "created_at": "2018-04-09T04:50:07Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bdc2f00e-073d-49d6-ac27-43782568b081", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824"
                    }
                ]
            }
        }, 
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "snmp_ports", 
    "id": "bdc2f00e-073d-49d6-ac27-43782568b081", 
    "resource_type": "ese_logical_ports"
}
```

### This is JSON data for checking "Common Function Gateway" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bdc2f00e-073d-49d6-ac27-43782568b081
```

- Response

```
{
    "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824", 
    "field_name": "logical_port", 
    "created_at": "2018-04-09T04:50:07Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bdc2f00e-073d-49d6-ac27-43782568b081", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824"
                    }
                ]
            }
        }, 
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [], 
    "type": "snmp_ports", 
    "id": "bdc2f00e-073d-49d6-ac27-43782568b081", 
    "resource_type": "ese_logical_ports"
}
```
and then ...
```
{
    "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824", 
    "field_name": "logical_port", 
    "created_at": "2018-04-09T04:50:07Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bdc2f00e-073d-49d6-ac27-43782568b081", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
                        "resource_id": "be66c7e0-b222-4e76-bf81-af75e8cf1824"
                    }
                ]
            }
        }, 
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-09T04:51:08Z", 
            "last_changed": "2018-04-09T04:51:08Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-09T04:51:08Z", 
            "last_changed": "2018-04-09T04:51:08Z", 
            "value": 1523249467, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-09T04:51:08Z", 
            "last_changed": "2018-04-09T04:51:08Z", 
            "value": 1523249467, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "bdc2f00e-073d-49d6-ac27-43782568b081", 
    "resource_type": "ese_logical_ports"
}
```
