# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Update Loadbalancer Interface(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 3, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992"
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
    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:25:52Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/45700507-166d-48af-b4e9-de9b8902d253", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992"
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
    "id": "45700507-166d-48af-b4e9-de9b8902d253", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Loadbalancer Interface(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/45700507-166d-48af-b4e9-de9b8902d253
```

- Response

```
{
    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:25:52Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/45700507-166d-48af-b4e9-de9b8902d253", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992"
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
    "id": "45700507-166d-48af-b4e9-de9b8902d253", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:25:52Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/45700507-166d-48af-b4e9-de9b8902d253", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "23464cbc-d910-430a-93f7-3776ea07f992"
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
            "last_changed": "2018-02-19T05:26:32Z", 
            "value": "FAIL", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "45700507-166d-48af-b4e9-de9b8902d253", 
    "resource_type": "ports"
}
```
