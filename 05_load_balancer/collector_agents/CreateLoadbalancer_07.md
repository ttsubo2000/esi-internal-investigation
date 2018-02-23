# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Loadbalancer(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 3, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
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
    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:21:38Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/9914421e-bc09-46d0-bd4f-e2b3d9f31bff", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
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
    "id": "9914421e-bc09-46d0-bd4f-e2b3d9f31bff", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Loadbalancer(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9914421e-bc09-46d0-bd4f-e2b3d9f31bff
```

- Response

```
{
    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:21:38Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/9914421e-bc09-46d0-bd4f-e2b3d9f31bff", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
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
    "id": "9914421e-bc09-46d0-bd4f-e2b3d9f31bff", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:21:38Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/9914421e-bc09-46d0-bd4f-e2b3d9f31bff", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "db3bff62-cf93-48ce-8d6b-cfb2f7fd7dfc"
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
            "value": "FAIL", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "9914421e-bc09-46d0-bd4f-e2b3d9f31bff", 
    "resource_type": "ports"
}
```
