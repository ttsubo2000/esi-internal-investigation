# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Firewall(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 3, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
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
    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:44:43Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/0c1b0232-9fff-46b1-9c5d-230345782739", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "type": "virtual_machine_interface", 
    "id": "0c1b0232-9fff-46b1-9c5d-230345782739", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Firewall(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/0c1b0232-9fff-46b1-9c5d-230345782739
```

- Response

```
{
    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:44:43Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/0c1b0232-9fff-46b1-9c5d-230345782739", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [], 
    "type": "virtual_machine_interface", 
    "id": "0c1b0232-9fff-46b1-9c5d-230345782739", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:44:43Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/0c1b0232-9fff-46b1-9c5d-230345782739", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "fd09eda4-10b1-4534-984a-7124c338c69d"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-12T07:46:26Z", 
            "last_changed": "2018-02-12T07:45:26Z", 
            "value": 11, 
            "key": "traffic.out", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-12T07:46:26Z", 
            "last_changed": "2018-02-12T07:45:26Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-12T07:46:26Z", 
            "last_changed": "2018-02-12T07:45:26Z", 
            "value": 14, 
            "key": "traffic.in", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "0c1b0232-9fff-46b1-9c5d-230345782739", 
    "resource_type": "ports"
}
```
