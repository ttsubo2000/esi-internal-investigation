# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Internet Gateway" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "device_index": "secondary", 
                    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "device_index": "secondary", 
                    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                }
            }
        }
    }, 
    "field_name": "secondary_counter", 
    "type": "igs_counter", 
    "properties": {
        "counter_name_in": "vrf_gw_sample-ha-router-downlink_1025_IN", 
        "counter_name_out": "vrf_gw_sample-ha-router-downlink_1025_OUT", 
        "primary_device_ip": "10.79.5.185", 
        "host": "10.79.5.184", 
        "login": "esi", 
        "password": "***", 
        "port": 830, 
        "secondary_device_ip": "10.79.5.184"
    }, 
    "resource_type": "internet_gateways"
}
```

- Response

```
{
    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
    "field_name": "secondary_counter", 
    "created_at": "2018-04-04T05:00:47Z", 
    "properties": {
        "counter_name_in": "vrf_gw_sample-ha-router-downlink_1025_IN", 
        "counter_name_out": "vrf_gw_sample-ha-router-downlink_1025_OUT", 
        "primary_device_ip": "10.79.5.185", 
        "host": "10.79.5.184", 
        "login": "esi", 
        "password": "***", 
        "port": 830, 
        "secondary_device_ip": "10.79.5.184"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e4609dae-5c88-494a-bdb5-19187026ccfc", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "device_index": "secondary", 
                    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "device_index": "secondary", 
                    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                }
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "type": "igs_counter", 
    "id": "e4609dae-5c88-494a-bdb5-19187026ccfc", 
    "resource_type": "internet_gateways"
}
```

### This is JSON data for checking "Internet Gateway" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e4609dae-5c88-494a-bdb5-19187026ccfc
```

- Response

```
{
    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9", 
    "field_name": "secondary_counter", 
    "created_at": "2018-04-04T05:00:47Z", 
    "properties": {
        "counter_name_in": "vrf_gw_sample-ha-router-downlink_1025_IN", 
        "counter_name_out": "vrf_gw_sample-ha-router-downlink_1025_OUT", 
        "primary_device_ip": "10.79.5.185", 
        "host": "10.79.5.184", 
        "login": "esi", 
        "password": "***", 
        "port": 830, 
        "secondary_device_ip": "10.79.5.184"
    }, 
    "monitorer": "http://collector-agents-se.monitoringrefactordocker_default:7070", 
    "version": 1, 
    "link": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/e4609dae-5c88-494a-bdb5-19187026ccfc", 
    "syncer_properties": {
        "tsdb": {
            "traffic.in": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "in", 
                    "device_index": "secondary", 
                    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                }
            }, 
            "traffic.out": {
                "metric": "traffic.bytes", 
                "tags": {
                    "direction": "out", 
                    "device_index": "secondary", 
                    "resource_id": "f6e8c695-c4c1-4a93-9b7e-1663aee6dec9"
                }
            }
        }
    }, 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "values": [], 
    "type": "igs_counter", 
    "id": "e4609dae-5c88-494a-bdb5-19187026ccfc", 
    "resource_type": "internet_gateways"
}
```
