# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface(logical_port)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
                        "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
                        "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066"
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
    "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066", 
    "field_name": "logical_port", 
    "created_at": "2018-04-04T05:02:30Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/81ea42e1-779e-4c1e-8f19-82d6019ee14c", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
                        "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
                        "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066"
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
    "id": "81ea42e1-779e-4c1e-8f19-82d6019ee14c", 
    "resource_type": "ese_logical_ports"
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/81ea42e1-779e-4c1e-8f19-82d6019ee14c
```

- Response

```
{
    "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066", 
    "field_name": "logical_port", 
    "created_at": "2018-04-04T05:02:30Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/81ea42e1-779e-4c1e-8f19-82d6019ee14c", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
                        "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
                        "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066"
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
    "id": "81ea42e1-779e-4c1e-8f19-82d6019ee14c", 
    "resource_type": "ese_logical_ports"
}
```
and then ...
```
{
    "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066", 
    "field_name": "logical_port", 
    "created_at": "2018-04-04T05:02:30Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.34", 
        "if_name": "xe-0/0/4.1025"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/81ea42e1-779e-4c1e-8f19-82d6019ee14c", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
                        "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
                        "resource_id": "aabc9b64-ec2c-4894-a6a8-ee0ea429c066"
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
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-04-04T05:03:31Z", 
            "last_changed": "2018-04-04T05:03:31Z", 
            "value": 1522818210, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "81ea42e1-779e-4c1e-8f19-82d6019ee14c", 
    "resource_type": "ese_logical_ports"
}
```
