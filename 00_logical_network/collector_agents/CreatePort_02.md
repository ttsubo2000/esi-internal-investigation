# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Port(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "version": 2, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
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
    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
    "field_name": "vmi", 
    "created_at": "2018-02-15T06:55:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/31ac332f-d172-4a39-8fa5-976ada238eff", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "type": "virtual_machine_interface", 
    "id": "31ac332f-d172-4a39-8fa5-976ada238eff", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Port(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/31ac332f-d172-4a39-8fa5-976ada238eff
```

- Response

```
{
    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
    "field_name": "vmi", 
    "created_at": "2018-02-15T06:55:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/31ac332f-d172-4a39-8fa5-976ada238eff", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "values": [], 
    "type": "virtual_machine_interface", 
    "id": "31ac332f-d172-4a39-8fa5-976ada238eff", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b", 
    "field_name": "vmi", 
    "created_at": "2018-02-15T06:55:28Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/31ac332f-d172-4a39-8fa5-976ada238eff", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "fde61b02-9615-4e75-aac0-30a333657c1b"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "values": [
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-15T06:56:28Z", 
            "last_changed": "2018-02-15T06:56:28Z", 
            "value": 14, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-15T06:56:28Z", 
            "last_changed": "2018-02-15T06:56:28Z", 
            "value": 11, 
            "key": "traffic.out", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-15T06:56:28Z", 
            "last_changed": "2018-02-15T06:56:28Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "31ac332f-d172-4a39-8fa5-976ada238eff", 
    "resource_type": "ports"
}
```
