# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Common Function Gateway(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "version": 2, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
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
    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
    "field_name": "vmi", 
    "created_at": "2018-04-09T04:50:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5b5ef6a3-7444-4443-8c6d-4c66aee1df27", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "virtual_machine_interface", 
    "id": "5b5ef6a3-7444-4443-8c6d-4c66aee1df27", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Common Function Gateway" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5b5ef6a3-7444-4443-8c6d-4c66aee1df27
```

- Response

```
{
    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
    "field_name": "vmi", 
    "created_at": "2018-04-09T04:50:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5b5ef6a3-7444-4443-8c6d-4c66aee1df27", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [], 
    "type": "virtual_machine_interface", 
    "id": "5b5ef6a3-7444-4443-8c6d-4c66aee1df27", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737", 
    "field_name": "vmi", 
    "created_at": "2018-04-09T04:50:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/5b5ef6a3-7444-4443-8c6d-4c66aee1df27", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "f84496b5-dc56-4727-87b1-aa06e2471737"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-04-09T04:51:28Z", 
            "last_changed": "2018-04-09T04:51:28Z", 
            "value": "FAIL", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "5b5ef6a3-7444-4443-8c6d-4c66aee1df27", 
    "resource_type": "ports"
}
```
