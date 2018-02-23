# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Firewall(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 3, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
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
    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:44:30Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "type": "virtual_machine_interface", 
    "id": "6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Firewall(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/6eea0aa6-879f-4bec-a9de-97cb607b75bf
```

- Response

```
{
    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:44:30Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [], 
    "type": "virtual_machine_interface", 
    "id": "6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:44:30Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "dea87c7b-b43f-4936-8e32-8995b038b3f8"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "vmi"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [
        {
            "reporter": "contrail_vmi", 
            "last_reported": "2018-02-12T07:46:26Z", 
            "last_changed": "2018-02-12T07:45:26Z", 
            "value": "FAIL", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "6eea0aa6-879f-4bec-a9de-97cb607b75bf", 
    "resource_type": "ports"
}
```
