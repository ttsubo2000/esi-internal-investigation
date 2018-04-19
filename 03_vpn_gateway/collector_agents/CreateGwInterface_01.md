# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Gw Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
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
    "resource_type": "gw_interfaces",
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
    }
}
```

- Response

```
{
    "id": "8ac03032-a027-4965-b636-32a7b1281bfc",
    "created_at": "2018-04-16T00:12:47Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8ac03032-a027-4965-b636-32a7b1281bfc",
    "type": "vrrp_pool",
    "resource_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
    "resource_type": "gw_interfaces",
    "field_name": "status",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "primary": {
            "host": "10.79.5.185",
            "interface": "ae0.1025",
            "login": "esi",
            "password": "***",
            "port": 830
        },
        "secondary": {
            "host": "10.79.5.184",
            "interface": "ae0.1025",
            "login": "esi",
            "password": "***",
            "port": 830
        },
        "vrid": [
            20
        ]
    },
    "syncer_properties": {
        "etcd": {
            "hold_options": {
                "positive_status": {
                    "primary": "MASTER",
                    "secondary": "BACKUP"
                },
                "time_seconds": 360
            },
            "status": {
                "key": "status"
            }
        }
    }
}
```

### This is JSON data for checking "Gw Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8ac03032-a027-4965-b636-32a7b1281bfc
```

- Response

```
{
    "id": "8ac03032-a027-4965-b636-32a7b1281bfc",
    "created_at": "2018-04-16T00:12:47Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8ac03032-a027-4965-b636-32a7b1281bfc",
    "type": "vrrp_pool",
    "resource_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
    "resource_type": "gw_interfaces",
    "field_name": "status",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "primary": {
            "host": "10.79.5.185",
            "interface": "ae0.1025",
            "login": "esi",
            "password": "***",
            "port": 830
        },
        "secondary": {
            "host": "10.79.5.184",
            "interface": "ae0.1025",
            "login": "esi",
            "password": "***",
            "port": 830
        },
        "vrid": [
            20
        ]
    },
    "syncer_properties": {
        "etcd": {
            "hold_options": {
                "positive_status": {
                    "primary": "MASTER",
                    "secondary": "BACKUP"
                },
                "time_seconds": 360
            },
            "status": {
                "key": "status"
            }
        }
    },
    "values": []
}
```
and then ...
```
{
    "id": "8ac03032-a027-4965-b636-32a7b1281bfc",
    "created_at": "2018-04-16T00:12:47Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8ac03032-a027-4965-b636-32a7b1281bfc",
    "type": "vrrp_pool",
    "resource_id": "3dbcfce5-bca5-4182-991a-c23de685fcf1",
    "resource_type": "gw_interfaces",
    "field_name": "status",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "primary": {
            "host": "10.79.5.185",
            "interface": "ae0.1025",
            "login": "esi",
            "password": "***",
            "port": 830
        },
        "secondary": {
            "host": "10.79.5.184",
            "interface": "ae0.1025",
            "login": "esi",
            "password": "***",
            "port": 830
        },
        "vrid": [
            20
        ]
    },
    "syncer_properties": {
        "etcd": {
            "hold_options": {
                "positive_status": {
                    "primary": "MASTER",
                    "secondary": "BACKUP"
                },
                "time_seconds": 360
            },
            "status": {
                "key": "status"
            }
        }
    },
    "values": [
        {
            "reporter": "VRRPAgent",
            "key": "status",
            "value": {
                "primary": "MASTER",
                "secondary": "BACKUP"
            },
            "last_reported": "2018-04-16T00:13:47Z",
            "last_changed": "2018-04-16T00:13:47Z",
            "fail_counter": 0
        }
    ]
}
```
