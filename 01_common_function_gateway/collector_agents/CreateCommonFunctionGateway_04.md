# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Common Function Gateway(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "version": 2, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
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
    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
    "field_name": "vmi", 
    "created_at": "2018-04-09T04:50:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9ba38fcf-3f2e-41e5-af92-cb4603c33e62", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
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
    "id": "9ba38fcf-3f2e-41e5-af92-cb4603c33e62", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Common Function Gateway" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9ba38fcf-3f2e-41e5-af92-cb4603c33e62
```

- Response

```
{
    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
    "field_name": "vmi", 
    "created_at": "2018-04-09T04:50:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9ba38fcf-3f2e-41e5-af92-cb4603c33e62", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
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
    "id": "9ba38fcf-3f2e-41e5-af92-cb4603c33e62", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4", 
    "field_name": "vmi", 
    "created_at": "2018-04-09T04:50:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 2, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9ba38fcf-3f2e-41e5-af92-cb4603c33e62", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "343b0257-512e-40e3-b063-8cc13a4b61f4"
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
            "value": 14, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-04-09T04:51:28Z", 
            "last_changed": "2018-04-09T04:51:28Z", 
            "value": 11, 
            "key": "traffic.out", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-04-09T04:51:28Z", 
            "last_changed": "2018-04-09T04:51:28Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "9ba38fcf-3f2e-41e5-af92-cb4603c33e62", 
    "resource_type": "ports"
}
```
