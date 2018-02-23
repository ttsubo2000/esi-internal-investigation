# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Loadbalancer(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 3, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c"
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
    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:17:31Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/cc987cdf-428c-446c-a390-540c5af4449d", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c"
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
    "id": "cc987cdf-428c-446c-a390-540c5af4449d", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Loadbalancer(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cc987cdf-428c-446c-a390-540c5af4449d
```

- Response

```
{
    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:17:31Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/cc987cdf-428c-446c-a390-540c5af4449d", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c"
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
    "id": "cc987cdf-428c-446c-a390-540c5af4449d", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
    "field_name": "vmi", 
    "created_at": "2018-02-19T05:17:31Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/cc987cdf-428c-446c-a390-540c5af4449d", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c"
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
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-19T05:21:32Z", 
            "last_changed": "2018-02-19T05:18:31Z", 
            "value": 14, 
            "key": "traffic.in", 
            "fail_counter": 0
        }, 
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-19T05:21:32Z", 
            "last_changed": "2018-02-19T05:18:32Z", 
            "value": 11, 
            "key": "traffic.out", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "cc987cdf-428c-446c-a390-540c5af4449d", 
    "resource_type": "ports"
}
```
