# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Common Function Gateway" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "version": 1, 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }, 
            "hold_options": {
                "time_seconds": 360, 
                "positive_status": {
                    "secondary_vrid1": "BACKUP", 
                    "secondary_vrid2": "BACKUP", 
                    "primary_vrid2": "MASTER", 
                    "primary_vrid1": "MASTER"
                }
            }
        }
    }, 
    "field_name": "status", 
    "type": "vrrp_pool", 
    "properties": {
        "vrid": [
            41, 
            42
        ], 
        "primary": {
            "interface": "ae0.1025", 
            "login": "esi", 
            "password": "***", 
            "host": "10.79.5.185", 
            "port": 830
        }, 
        "secondary": {
            "interface": "ae0.1025", 
            "login": "esi", 
            "password": "***", 
            "host": "10.79.5.184", 
            "port": 830
        }
    }, 
    "resource_type": "common_function_gateways"
}
```

- Response

```
{
    "resource_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
    "field_name": "status", 
    "created_at": "2018-04-09T04:50:20Z", 
    "properties": {
        "vrid": [
            41, 
            42
        ], 
        "primary": {
            "interface": "ae0.1025", 
            "host": "10.79.5.185", 
            "password": "***", 
            "login": "esi", 
            "port": 830
        }, 
        "secondary": {
            "interface": "ae0.1025", 
            "host": "10.79.5.184", 
            "password": "***", 
            "login": "esi", 
            "port": 830
        }
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }, 
            "hold_options": {
                "time_seconds": 360, 
                "positive_status": {
                    "secondary_vrid1": "BACKUP", 
                    "secondary_vrid2": "BACKUP", 
                    "primary_vrid2": "MASTER", 
                    "primary_vrid1": "MASTER"
                }
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "type": "vrrp_pool", 
    "id": "cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
    "resource_type": "common_function_gateways"
}
```

### This is JSON data for checking "Common Function Gateway" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e
```

- Response

```
{
    "resource_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
    "field_name": "status", 
    "created_at": "2018-04-09T04:50:20Z", 
    "properties": {
        "vrid": [
            41, 
            42
        ], 
        "primary": {
            "interface": "ae0.1025", 
            "host": "10.79.5.185", 
            "password": "***", 
            "login": "esi", 
            "port": 830
        }, 
        "secondary": {
            "interface": "ae0.1025", 
            "host": "10.79.5.184", 
            "password": "***", 
            "login": "esi", 
            "port": 830
        }
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }, 
            "hold_options": {
                "time_seconds": 360, 
                "positive_status": {
                    "secondary_vrid1": "BACKUP", 
                    "secondary_vrid2": "BACKUP", 
                    "primary_vrid2": "MASTER", 
                    "primary_vrid1": "MASTER"
                }
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [], 
    "type": "vrrp_pool", 
    "id": "cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
    "resource_type": "common_function_gateways"
}
```
and then ...
```
{
    "resource_id": "f649736d-1920-41eb-96af-d4e4fe192d0e", 
    "field_name": "status", 
    "created_at": "2018-04-09T04:50:20Z", 
    "properties": {
        "vrid": [
            41, 
            42
        ], 
        "primary": {
            "interface": "ae0.1025", 
            "host": "10.79.5.185", 
            "password": "***", 
            "login": "esi", 
            "port": 830
        }, 
        "secondary": {
            "interface": "ae0.1025", 
            "host": "10.79.5.184", 
            "password": "***", 
            "login": "esi", 
            "port": 830
        }
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }, 
            "hold_options": {
                "time_seconds": 360, 
                "positive_status": {
                    "secondary_vrid1": "BACKUP", 
                    "secondary_vrid2": "BACKUP", 
                    "primary_vrid2": "MASTER", 
                    "primary_vrid1": "MASTER"
                }
            }
        }
    }, 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "values": [
        {
            "reporter": "VRRPAgent", 
            "last_reported": "2018-04-09T04:51:20Z", 
            "last_changed": "2018-04-09T04:51:20Z", 
            "value": {
                "secondary_vrid1": "BACKUP", 
                "secondary_vrid2": "BACKUP", 
                "primary_vrid2": "MASTER", 
                "primary_vrid1": "MASTER"
            }, 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "vrrp_pool", 
    "id": "cfb54c6f-43cf-4e35-aff8-e2c2ec8adc7e", 
    "resource_type": "common_function_gateways"
}
```
