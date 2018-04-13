# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Common Function Gateway(logical_port)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1"
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
        "if_name": "xe-0/0/4.1025"
    }, 
    "resource_type": "ese_logical_ports"
}
```

- Response

```
{
    "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
    "field_name": "logical_port", 
    "created_at": "2018-04-09T04:50:07Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1"
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
    "id": "7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
    "resource_type": "ese_logical_ports"
}
```

### This is JSON data for checking "Common Function Gateway" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7f066c44-1dc2-44b2-95f7-d59d70bd77fb
```

- Response

```
{
    "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
    "field_name": "logical_port", 
    "created_at": "2018-04-09T04:50:07Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1"
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
    "id": "7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
    "resource_type": "ese_logical_ports"
}
```
and then ...
```
{
    "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1", 
    "field_name": "logical_port", 
    "created_at": "2018-04-09T04:50:07Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
                        "resource_id": "e8555ee6-529c-42d9-8bb1-bfbe217133b1"
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
            "last_reported": "2018-04-09T04:51:07Z", 
            "last_changed": "2018-04-09T04:51:07Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-09T04:51:07Z", 
            "last_changed": "2018-04-09T04:51:07Z", 
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
    "id": "7f066c44-1dc2-44b2-95f7-d59d70bd77fb", 
    "resource_type": "ese_logical_ports"
}
```
