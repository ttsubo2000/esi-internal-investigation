# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Vpn Interface" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "field_name": "status",
    "type": "bgp_pool",
    "properties": {
        "instance": "vrf_gw_sample-ha-router-downlink_1025",
        "primary": {
            "peer_address": "192.168.8.1",
            "login": "esi",
            "password": "***",
            "host": "10.79.5.185",
            "port": 830
        },
        "secondary": {
            "peer_address": "192.168.8.5",
            "login": "esi",
            "password": "***",
            "host": "10.79.5.184",
            "port": 830
        }
    },
    "resource_type": "vpn_interfaces",
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }
        }
    }
}
```

- Response

```
{
    "id": "34b9de21-40c0-46f1-afa5-787220cc5ed2",
    "created_at": "2018-04-16T00:10:07Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/34b9de21-40c0-46f1-afa5-787220cc5ed2",
    "type": "bgp_pool",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "status",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "instance": "vrf_gw_sample-ha-router-downlink_1025",
        "primary": {
            "host": "10.79.5.185",
            "login": "esi",
            "password": "***",
            "peer_address": "192.168.8.1",
            "port": 830
        },
        "secondary": {
            "host": "10.79.5.184",
            "login": "esi",
            "password": "***",
            "peer_address": "192.168.8.5",
            "port": 830
        }
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }
        }
    }
}
```

### This is JSON data for checking "Vpn Interface" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/34b9de21-40c0-46f1-afa5-787220cc5ed2
```

- Response

```
{
    "id": "34b9de21-40c0-46f1-afa5-787220cc5ed2",
    "created_at": "2018-04-16T00:10:07Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/34b9de21-40c0-46f1-afa5-787220cc5ed2",
    "type": "bgp_pool",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "status",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "instance": "vrf_gw_sample-ha-router-downlink_1025",
        "primary": {
            "host": "10.79.5.185",
            "login": "esi",
            "password": "***",
            "peer_address": "192.168.8.1",
            "port": 830
        },
        "secondary": {
            "host": "10.79.5.184",
            "login": "esi",
            "password": "***",
            "peer_address": "192.168.8.5",
            "port": 830
        }
    },
    "syncer_properties": {
        "etcd": {
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
    "id": "34b9de21-40c0-46f1-afa5-787220cc5ed2",
    "created_at": "2018-04-16T00:10:07Z",
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070",
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/34b9de21-40c0-46f1-afa5-787220cc5ed2",
    "type": "bgp_pool",
    "resource_id": "07d4f1fc-5142-4fae-b115-627fc009e222",
    "resource_type": "vpn_interfaces",
    "field_name": "status",
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef",
    "version": 1,
    "properties": {
        "instance": "vrf_gw_sample-ha-router-downlink_1025",
        "primary": {
            "host": "10.79.5.185",
            "login": "esi",
            "password": "***",
            "peer_address": "192.168.8.1",
            "port": 830
        },
        "secondary": {
            "host": "10.79.5.184",
            "login": "esi",
            "password": "***",
            "peer_address": "192.168.8.5",
            "port": 830
        }
    },
    "syncer_properties": {
        "etcd": {
            "status": {
                "key": "status"
            }
        }
    },
    "values": [
        {
            "reporter": "BGPAgent",
            "key": "status",
            "value": {
                "primary": "ESTABLISHED",
                "secondary": "ESTABLISHED"
            },
            "last_reported": "2018-04-16T00:11:07Z",
            "last_changed": "2018-04-16T00:11:07Z",
            "fail_counter": 0
        }
    ]
}
```
