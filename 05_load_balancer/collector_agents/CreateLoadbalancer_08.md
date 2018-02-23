# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Loadbalancer(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 3, 
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
    "created_at": "2018-02-19T05:21:51Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
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
    "id": "794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Loadbalancer(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/794f28f6-0c97-4a0e-af7a-5696dcd4c3c7
```

- Response

```
{
    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:21:51Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
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
    "id": "794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "a7e5822c-5c04-4c5f-a5ac-b0e0ad50159f", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:21:51Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
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
            "last_reported": "2018-02-19T05:23:32Z", 
            "last_changed": "2018-02-19T05:22:32Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-19T05:23:32Z", 
            "last_changed": "2018-02-19T05:22:32Z", 
            "value": 14, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-19T05:23:32Z", 
            "last_changed": "2018-02-19T05:22:32Z", 
            "value": 11, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "794f28f6-0c97-4a0e-af7a-5696dcd4c3c7", 
    "resource_type": "ports"
}
```
