# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface(logical_port)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892"
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
    "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892", 
    "field_name": "logical_port", 
    "created_at": "2018-04-04T05:02:32Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/501b16b0-8059-4263-9e40-06aabfa1d72f", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892"
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
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "snmp_ports", 
    "id": "501b16b0-8059-4263-9e40-06aabfa1d72f", 
    "resource_type": "ese_logical_ports"
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/501b16b0-8059-4263-9e40-06aabfa1d72f
```

- Response

```
{
    "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892", 
    "field_name": "logical_port", 
    "created_at": "2018-04-04T05:02:32Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/501b16b0-8059-4263-9e40-06aabfa1d72f", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892"
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
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [], 
    "type": "snmp_ports", 
    "id": "501b16b0-8059-4263-9e40-06aabfa1d72f", 
    "resource_type": "ese_logical_ports"
}
```
and then ...
```
{
    "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892", 
    "field_name": "logical_port", 
    "created_at": "2018-04-04T05:02:32Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/3.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/501b16b0-8059-4263-9e40-06aabfa1d72f", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
                        "resource_id": "02112bb1-389c-4ff8-9354-94ab43459892"
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
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-04T05:03:30Z", 
            "last_changed": "2018-04-04T05:03:30Z", 
            "value": 1522818210, 
            "key": "traffic.out", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-04T05:03:31Z", 
            "last_changed": "2018-04-04T05:03:31Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-04T05:03:31Z", 
            "last_changed": "2018-04-04T05:03:31Z", 
            "value": 1522818210, 
            "key": "traffic.in", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "501b16b0-8059-4263-9e40-06aabfa1d72f", 
    "resource_type": "ese_logical_ports"
}
```
