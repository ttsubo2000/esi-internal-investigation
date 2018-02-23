# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Firewall(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 3, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549"
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
    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:40:25Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/7d259276-40ea-450b-9998-a5a3e0118eeb", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549"
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
    "id": "7d259276-40ea-450b-9998-a5a3e0118eeb", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Firewall(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7d259276-40ea-450b-9998-a5a3e0118eeb
```

- Response

```
{
    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:40:25Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/7d259276-40ea-450b-9998-a5a3e0118eeb", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549"
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
    "id": "7d259276-40ea-450b-9998-a5a3e0118eeb", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:40:25Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/7d259276-40ea-450b-9998-a5a3e0118eeb", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "cdde9cfd-a898-4911-b812-b6849f611549"
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
            "value": "FAIL", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-12T07:44:26Z", 
            "last_changed": "2018-02-12T07:41:25Z", 
            "value": 14, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-12T07:44:26Z", 
            "last_changed": "2018-02-12T07:41:26Z", 
            "value": 11, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "7d259276-40ea-450b-9998-a5a3e0118eeb", 
    "resource_type": "ports"
}
```
