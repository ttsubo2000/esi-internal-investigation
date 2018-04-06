# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "version": 1, 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }, 
            "hold_options": {
                "time_seconds": 360, 
                "positive_status": {
                    "primary": "MASTER", 
                    "secondary": "BACKUP"
                }
            }
        }
    }, 
    "field_name": "status", 
    "type": "vrrp_pool", 
    "properties": {
        "vrid": [
            20
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
    "resource_type": "gw_interfaces"
}
```

- Response

```
{
    "resource_id": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
    "field_name": "status", 
    "created_at": "2018-04-04T05:02:21Z", 
    "properties": {
        "vrid": [
            20
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
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }, 
            "hold_options": {
                "time_seconds": 360, 
                "positive_status": {
                    "primary": "MASTER", 
                    "secondary": "BACKUP"
                }
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "vrrp_pool", 
    "id": "921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
    "resource_type": "gw_interfaces"
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/921a9234-0ae4-44f5-89b0-2f68dcaaae5b
```

- Response

```
{
    "resource_id": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
    "field_name": "status", 
    "created_at": "2018-04-04T05:02:21Z", 
    "properties": {
        "vrid": [
            20
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
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }, 
            "hold_options": {
                "time_seconds": 360, 
                "positive_status": {
                    "primary": "MASTER", 
                    "secondary": "BACKUP"
                }
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [], 
    "type": "vrrp_pool", 
    "id": "921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
    "resource_type": "gw_interfaces"
}
```
and then ...
```
{
    "resource_id": "ce8831fd-d30c-41e3-95de-feaee0b95405", 
    "field_name": "status", 
    "created_at": "2018-04-04T05:02:21Z", 
    "properties": {
        "vrid": [
            20
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
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }, 
            "hold_options": {
                "time_seconds": 360, 
                "positive_status": {
                    "primary": "MASTER", 
                    "secondary": "BACKUP"
                }
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [
        {
            "reporter": "VRRPAgent", 
            "last_reported": "2018-04-04T05:03:21Z", 
            "last_changed": "2018-04-04T05:03:21Z", 
            "value": {
                "primary": "MASTER", 
                "secondary": "BACKUP"
            }, 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "vrrp_pool", 
    "id": "921a9234-0ae4-44f5-89b0-2f68dcaaae5b", 
    "resource_type": "gw_interfaces"
}
```
