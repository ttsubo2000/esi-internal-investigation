# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Update Firewall Interface(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 3, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf"
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
    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:48:40Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/7d227407-399b-4404-9178-f9322665bb38", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf"
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
    "id": "7d227407-399b-4404-9178-f9322665bb38", 
    "resource_type": "ports"
}
```

### This is JSON data for checking "Firewall Interface(virtual_machine_interface)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/7d227407-399b-4404-9178-f9322665bb38
```

- Response

```
{
    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:48:40Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/7d227407-399b-4404-9178-f9322665bb38", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf"
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
    "id": "7d227407-399b-4404-9178-f9322665bb38", 
    "resource_type": "ports"
}
```
and then ...
```
{
    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf", 
    "field_name": "vmi", 
    "created_at": "2018-02-12T07:48:40Z", 
    "properties": {
        "fq_name": "default-domain:admin:f68d0924-ef20-4c1b-ac45-0e6b879af5e7"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 3, 
    "link": "http://collector-agents-se:7070/targets/7d227407-399b-4404-9178-f9322665bb38", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "in", 
                    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.contrail_bytes", 
                "tags": {
                    "direction": "out", 
                    "resource_id": "472879c4-4611-4762-a069-293e0081bcbf"
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
            "last_reported": "2018-02-12T07:51:26Z", 
            "last_changed": "2018-02-12T07:49:26Z", 
            "value": "FAIL", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "virtual_machine_interface", 
    "id": "7d227407-399b-4404-9178-f9322665bb38", 
    "resource_type": "ports"
}
```
