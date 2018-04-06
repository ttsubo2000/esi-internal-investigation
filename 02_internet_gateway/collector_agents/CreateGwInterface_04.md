# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "version": 2, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "field_name": "vmi", 
    "type": "virtual_machine_interface", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "resource_type": "ports"
}
```

- Response

```
{
    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
    "field_name": "vmi", 
    "created_at": "2018-04-04T05:02:38Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1650b87a-0a56-4ef0-a411-42a4c6efc185", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "virtual_machine_interface", 
    "id": "1650b87a-0a56-4ef0-a411-42a4c6efc185", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1650b87a-0a56-4ef0-a411-42a4c6efc185
```

- Response

```
{
    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
    "field_name": "vmi", 
    "created_at": "2018-04-04T05:02:38Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1650b87a-0a56-4ef0-a411-42a4c6efc185", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [], 
    "type": "virtual_machine_interface", 
    "id": "1650b87a-0a56-4ef0-a411-42a4c6efc185", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47", 
    "field_name": "vmi", 
    "created_at": "2018-04-04T05:02:38Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1650b87a-0a56-4ef0-a411-42a4c6efc185", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "ce965922-538a-4335-9644-7a98dce9fb47"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-04-04T05:03:38Z", 
            "last_changed": "2018-04-04T05:03:38Z", 
            "value": "FAIL", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "1650b87a-0a56-4ef0-a411-42a4c6efc185", 
    "resource_type": "ports"
}
```
