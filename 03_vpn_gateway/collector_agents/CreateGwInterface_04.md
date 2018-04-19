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
    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387",
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
                    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387"
                }
            },
            "traffic.out": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "out",
                    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387"
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
    "id": "aa5568e3-f399-474f-9ddb-02c0e583b91b",
    "created_at": "2018-04-16T00:13:04Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aa5568e3-f399-474f-9ddb-02c0e583b91b",
    "type": "virtual_machine_interface",
    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387",
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
                    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387"
                }
            },
            "traffic.out": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "out",
                    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387"
                }
            }
        }
    }
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aa5568e3-f399-474f-9ddb-02c0e583b91b
```

- Response

```
{
    "id": "aa5568e3-f399-474f-9ddb-02c0e583b91b",
    "created_at": "2018-04-16T00:13:04Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aa5568e3-f399-474f-9ddb-02c0e583b91b",
    "type": "virtual_machine_interface",
    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387",
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
                    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387"
                }
            },
            "traffic.out": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "out",
                    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387"
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
    "id": "aa5568e3-f399-474f-9ddb-02c0e583b91b",
    "created_at": "2018-04-16T00:13:04Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aa5568e3-f399-474f-9ddb-02c0e583b91b",
    "type": "virtual_machine_interface",
    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387",
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
                    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387"
                }
            },
            "traffic.out": {
                "metric": "traffic.contrail_bytes",
                "tags": {
                    "direction": "out",
                    "resource_id": "53eeb091-3297-4b9b-a200-b6568567e387"
                }
            }
        }
    },
    "values": [
        {
            "reporter": "contrail_vmi",
            "key": "status",
            "value": "FAIL",
            "last_reported": "2018-04-16T00:14:04Z",
            "last_changed": "2018-04-16T00:14:04Z",
            "fail_counter": 0
        }
    ]
}
```
