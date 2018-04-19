# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8",
    "field_name": "logical_port",
    "type": "snmp_ports",
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/3.1025"
    },
    "resource_type": "ese_logical_ports",
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "in",
                        "port_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
                        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
                    }
                ]
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "out",
                        "port_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
                        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
                    }
                ]
            }
        },
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        }
    }
}
```

- Response

```
{
    "id": "fc210c75-e57f-4657-8114-a528d3b3aac5",
    "created_at": "2018-04-16T00:12:57Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/fc210c75-e57f-4657-8114-a528d3b3aac5",
    "type": "snmp_ports",
    "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8",
    "resource_type": "ese_logical_ports",
    "field_name": "logical_port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/3.1025"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "in",
                        "port_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
                        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
                    }
                ]
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "out",
                        "port_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
                        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
                    }
                ]
            }
        }
    }
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/fc210c75-e57f-4657-8114-a528d3b3aac5
```

- Response

```
{
    "id": "fc210c75-e57f-4657-8114-a528d3b3aac5",
    "created_at": "2018-04-16T00:12:57Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/fc210c75-e57f-4657-8114-a528d3b3aac5",
    "type": "snmp_ports",
    "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8",
    "resource_type": "ese_logical_ports",
    "field_name": "logical_port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/3.1025"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "in",
                        "port_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
                        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
                    }
                ]
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "out",
                        "port_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
                        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
                    }
                ]
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "fc210c75-e57f-4657-8114-a528d3b3aac5",
    "created_at": "2018-04-16T00:12:57Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/fc210c75-e57f-4657-8114-a528d3b3aac5",
    "type": "snmp_ports",
    "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8",
    "resource_type": "ese_logical_ports",
    "field_name": "logical_port",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "community_name": "***",
        "device_ip": "10.161.0.34",
        "if_name": "xe-0/0/3.1025"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "logical_port"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "in",
                        "port_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
                        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
                    }
                ]
            },
            "traffic.out": {
                "metric": "traffic.bytes",
                "tags": [
                    {
                        "direction": "out",
                        "port_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
                        "resource_id": "e30fdd19-2f48-422e-9c68-7c59a0e2fae8"
                    }
                ]
            }
        }
    },
    "values": [
        {
            "reporter": "SNMPPortPool",
            "key": "traffic.in",
            "value": 1523837636,
            "last_reported": "2018-04-16T00:13:56Z",
            "last_changed": "2018-04-16T00:13:56Z",
            "fail_counter": 0
        },
        {
            "reporter": "SNMPPortPool",
            "key": "traffic.out",
            "value": 1523837636,
            "last_reported": "2018-04-16T00:13:56Z",
            "last_changed": "2018-04-16T00:13:56Z",
            "fail_counter": 0
        },
        {
            "reporter": "SNMPPortPool",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:13:56Z",
            "last_changed": "2018-04-16T00:13:56Z",
            "fail_counter": 0
        }
    ]
}
```
