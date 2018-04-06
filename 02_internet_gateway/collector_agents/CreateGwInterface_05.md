# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "version": 2, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
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
    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
    "field_name": "vmi", 
    "created_at": "2018-04-04T05:02:39Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1b86504e-571f-4d8f-a3c5-a960a747e093", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
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
    "id": "1b86504e-571f-4d8f-a3c5-a960a747e093", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1b86504e-571f-4d8f-a3c5-a960a747e093
```

- Response

```
{
    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
    "field_name": "vmi", 
    "created_at": "2018-04-04T05:02:39Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1b86504e-571f-4d8f-a3c5-a960a747e093", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
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
    "id": "1b86504e-571f-4d8f-a3c5-a960a747e093", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a", 
    "field_name": "vmi", 
    "created_at": "2018-04-04T05:02:39Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/1b86504e-571f-4d8f-a3c5-a960a747e093", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "f3867a99-de18-4512-8e94-f9aaa7b05c3a"
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
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-04-04T05:03:38Z", 
            "last_changed": "2018-04-04T05:03:38Z", 
            "value": 14, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-04-04T05:03:38Z", 
            "last_changed": "2018-04-04T05:03:38Z", 
            "value": 11, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "1b86504e-571f-4d8f-a3c5-a960a747e093", 
    "resource_type": "ports"
}
```
