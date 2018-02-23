# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Update Firewall Interface(firewall_config)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "version": 2, 
    "syncer_properties": {
        "tsdb": {
            "cpu.user": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "user", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "cpu.system": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "system", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "memory.available": {
                "metric": "memory.kbytes", 
                "tags": {
                    "type": "available", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "tcp.passive": {
                "metric": "tcp.connections", 
                "tags": {
                    "open": "passive", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "memory.total": {
                "metric": "memory.kbytes", 
                "tags": {
                    "type": "total", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "cpu.idle": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "idle", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "tcp.active": {
                "metric": "tcp.connections", 
                "tags": {
                    "open": "active", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "firewall"
            }
        }
    }, 
    "field_name": "firewall", 
    "type": "snmp_device_fw", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3"
    }, 
    "resource_type": "firewalls"
}
```

- Response

```
{
    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
    "field_name": "firewall", 
    "created_at": "2018-02-12T07:49:11Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
    "syncer_properties": {
        "tsdb": {
            "cpu.system": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "system", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "cpu.user": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "user", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "memory.available": {
                "metric": "memory.kbytes", 
                "tags": {
                    "type": "available", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "tcp.passive": {
                "metric": "tcp.connections", 
                "tags": {
                    "open": "passive", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "memory.total": {
                "metric": "memory.kbytes", 
                "tags": {
                    "type": "total", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "cpu.idle": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "idle", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "tcp.active": {
                "metric": "tcp.connections", 
                "tags": {
                    "open": "active", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "firewall"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "type": "snmp_device_fw", 
    "id": "a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
    "resource_type": "firewalls"
}
```

### This is JSON data for checking "Firewall Interface(firewall_config)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6
```

- Response

```
{
    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
    "field_name": "firewall", 
    "created_at": "2018-02-12T07:49:11Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
    "syncer_properties": {
        "tsdb": {
            "cpu.system": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "system", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "cpu.user": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "user", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "memory.available": {
                "metric": "memory.kbytes", 
                "tags": {
                    "type": "available", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "tcp.passive": {
                "metric": "tcp.connections", 
                "tags": {
                    "open": "passive", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "memory.total": {
                "metric": "memory.kbytes", 
                "tags": {
                    "type": "total", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "cpu.idle": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "idle", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "tcp.active": {
                "metric": "tcp.connections", 
                "tags": {
                    "open": "active", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "firewall"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [], 
    "type": "snmp_device_fw", 
    "id": "a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
    "resource_type": "firewalls"
}
```
and then ...
```
{
    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
    "field_name": "firewall", 
    "created_at": "2018-02-12T07:49:11Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 2, 
    "link": "http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
    "syncer_properties": {
        "tsdb": {
            "cpu.system": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "system", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "cpu.user": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "user", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "memory.available": {
                "metric": "memory.kbytes", 
                "tags": {
                    "type": "available", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "tcp.passive": {
                "metric": "tcp.connections", 
                "tags": {
                    "open": "passive", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "memory.total": {
                "metric": "memory.kbytes", 
                "tags": {
                    "type": "total", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "cpu.idle": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "idle", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }, 
            "tcp.active": {
                "metric": "tcp.connections", 
                "tags": {
                    "open": "active", 
                    "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "firewall"
            }
        }
    }, 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "values": [
        {
            "reporter": "SnmpDeviceAgent", 
            "last_reported": "2018-02-12T07:51:11Z", 
            "last_changed": "2018-02-12T07:50:11Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device_fw", 
    "id": "a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
    "resource_type": "firewalls"
}
```
