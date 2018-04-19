# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 2,
    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
    "field_name": "vmi",
    "type": "virtual_machine_interface",
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    },
    "resource_type": "ports",
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "in",
                    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                }
            },
            "traffic.out": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "out",
                    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                }
            }
        },
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }
}
```

- Response

```
{
    "id": "09f0db4a-16f7-4d25-840f-79436680056e",
    "created_at": "2018-04-16T00:13:04Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/09f0db4a-16f7-4d25-840f-79436680056e",
    "type": "virtual_machine_interface",
    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
    "resource_type": "ports",
    "field_name": "vmi",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 2,
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "vmi"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "in",
                    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                }
            },
            "traffic.out": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "out",
                    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                }
            }
        }
    }
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/09f0db4a-16f7-4d25-840f-79436680056e
```

- Response

```
{
    "id": "09f0db4a-16f7-4d25-840f-79436680056e",
    "created_at": "2018-04-16T00:13:04Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/09f0db4a-16f7-4d25-840f-79436680056e",
    "type": "virtual_machine_interface",
    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
    "resource_type": "ports",
    "field_name": "vmi",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 2,
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "vmi"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "in",
                    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                }
            },
            "traffic.out": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "out",
                    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                }
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "09f0db4a-16f7-4d25-840f-79436680056e",
    "created_at": "2018-04-16T00:13:04Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/09f0db4a-16f7-4d25-840f-79436680056e",
    "type": "virtual_machine_interface",
    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b",
    "resource_type": "ports",
    "field_name": "vmi",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 2,
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "vmi"
            }
        },
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "in",
                    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                }
            },
            "traffic.out": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "out",
                    "resource_id": "5eebab65-bf2f-4ac2-969a-15d6ccbfdd4b"
                }
            }
        }
    },
    "values": [
        {
            "reporter": "contrail_vmi",
            "key": "status",
            "value": "UP",
            "last_reported": "2018-04-16T00:14:04Z",
            "last_changed": "2018-04-16T00:14:04Z",
            "fail_counter": 0
        },
        {
            "reporter": "contrail_vmi",
            "key": "traffic.in",
            "value": 14,
            "last_reported": "2018-04-16T00:14:04Z",
            "last_changed": "2018-04-16T00:14:04Z",
            "fail_counter": 0
        },
        {
            "reporter": "contrail_vmi",
            "key": "traffic.out",
            "value": 11,
            "last_reported": "2018-04-16T00:14:04Z",
            "last_changed": "2018-04-16T00:14:04Z",
            "fail_counter": 0
        }
    ]
}
```
