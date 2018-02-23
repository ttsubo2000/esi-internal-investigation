# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Update Loadbalancer Interface(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 6, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
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
    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:26:05Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 6, 
    "link": "http://collector-agents-se:7070/targets/d78c0cfb-8677-4ea3-9acb-fa6c5a39847d", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "type": "virtual_machine_interface", 
    "id": "d78c0cfb-8677-4ea3-9acb-fa6c5a39847d", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Loadbalancer Interface(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/d78c0cfb-8677-4ea3-9acb-fa6c5a39847d
```

- Response

```
{
    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:26:05Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 6, 
    "link": "http://collector-agents-se:7070/targets/d78c0cfb-8677-4ea3-9acb-fa6c5a39847d", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "values": [], 
    "type": "virtual_machine_interface", 
    "id": "d78c0cfb-8677-4ea3-9acb-fa6c5a39847d", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:26:05Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 6, 
    "link": "http://collector-agents-se:7070/targets/d78c0cfb-8677-4ea3-9acb-fa6c5a39847d", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "values": [
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-19T05:28:32Z", 
            "last_changed": "2018-02-19T05:27:32Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-19T05:28:32Z", 
            "last_changed": "2018-02-19T05:27:32Z", 
            "value": 14, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-19T05:28:32Z", 
            "last_changed": "2018-02-19T05:27:32Z", 
            "value": 11, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "d78c0cfb-8677-4ea3-9acb-fa6c5a39847d", 
    "resource_type": "ports"
}
```
