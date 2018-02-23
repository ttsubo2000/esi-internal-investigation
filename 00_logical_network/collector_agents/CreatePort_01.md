# HTTP Methods for RESTful between heat-engine and CollectorAgents

### These are stored data for "Create Port(logical_port)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
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
        "device_ip": "10.161.0.33", 
        "if_name": "xe-0/0/1.1003"
    }, 
    "resource_type": "ese_logical_ports"
}
```

- Response

```
{
    "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
    "field_name": "logical_port", 
    "created_at": "2018-02-15T06:55:22Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33", 
        "if_name": "xe-0/0/1.1003"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
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
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "type": "snmp_ports", 
    "id": "9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
    "resource_type": "ese_logical_ports"
}
```

### This is JSON data for checking "Port(logical_port)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568
```

- Response

```
{
    "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
    "field_name": "logical_port", 
    "created_at": "2018-02-15T06:55:22Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33", 
        "if_name": "xe-0/0/1.1003"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
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
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "values": [], 
    "type": "snmp_ports", 
    "id": "9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
    "resource_type": "ese_logical_ports"
}
```
and then ...
```
{
    "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7", 
    "field_name": "logical_port", 
    "created_at": "2018-02-15T06:55:22Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "10.161.0.33", 
        "if_name": "xe-0/0/1.1003"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "in", 
                        "port_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
                    }
                ]
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": [
                    {
                        "direction": "out", 
                        "port_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
                        "resource_id": "ced1435d-6dfa-4dab-bb7c-19da4d8e48b7"
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
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "values": [
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-15T06:56:22Z", 
            "last_changed": "2018-02-15T06:56:22Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-15T06:56:22Z", 
            "last_changed": "2018-02-15T06:56:22Z", 
            "value": 1518677782, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "SNMPPortPool", 
            "last_reported": "2018-02-15T06:56:22Z", 
            "last_changed": "2018-02-15T06:56:22Z", 
            "value": 1518677782, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_ports", 
    "id": "9dcbbbbc-e9ea-4276-ba65-68ce8737e568", 
    "resource_type": "ese_logical_ports"
}
```
