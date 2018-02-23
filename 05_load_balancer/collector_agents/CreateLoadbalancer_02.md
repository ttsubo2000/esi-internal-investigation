# HTTP Methods for RESTful between heat-engine and CollectorAgents
  
### These are stored data for "Create Loadbalancer(load_balancer)" in HTTP Methods from heat-engine.

- Request

```
POST http://collector-agents-se.monitoringrefactordocker_default:7070/targets
```
```
{
    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "version": 1, 
    "syncer_properties": {
        "tsdb": {
            "cpu.usage": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "usage", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "http.request": {
                "metric": "http.request.connections", 
                "tags": {
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "tcp.server": {
                "metric": "tcp.connections", 
                "tags": {
                    "owner": "server", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "tcp.client": {
                "metric": "tcp.connections", 
                "tags": {
                    "owner": "client", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "memory.usage": {
                "metric": "memory.percents", 
                "tags": {
                    "type": "usage", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "load_balancer"
            }
        }
    }, 
    "field_name": "load_balancer", 
    "type": "snmp_device_lb", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3"
    }, 
    "resource_type": "load_balancers"
}
```

- Response

```
{
    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
    "field_name": "load_balancer", 
    "created_at": "2018-02-19T05:21:58Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/8a031503-513d-4d7b-ac78-0ac2631fe786", 
    "syncer_properties": {
        "tsdb": {
            "cpu.usage": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "usage", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "http.request": {
                "metric": "http.request.connections", 
                "tags": {
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "tcp.server": {
                "metric": "tcp.connections", 
                "tags": {
                    "owner": "server", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "tcp.client": {
                "metric": "tcp.connections", 
                "tags": {
                    "owner": "client", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "memory.usage": {
                "metric": "memory.percents", 
                "tags": {
                    "type": "usage", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "load_balancer"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "type": "snmp_device_lb", 
    "id": "8a031503-513d-4d7b-ac78-0ac2631fe786", 
    "resource_type": "load_balancers"
}
```

### This is JSON data for checking "Loadbalancer(load_balancer)" in HTTP Methods from heat-engine.

- Request

```
GET http://collector-agents-se.monitoringrefactordocker_default:7070/targets/8a031503-513d-4d7b-ac78-0ac2631fe786
```

- Response

```
{
    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
    "field_name": "load_balancer", 
    "created_at": "2018-02-19T05:21:58Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/8a031503-513d-4d7b-ac78-0ac2631fe786", 
    "syncer_properties": {
        "tsdb": {
            "cpu.usage": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "usage", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "http.request": {
                "metric": "http.request.connections", 
                "tags": {
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "tcp.server": {
                "metric": "tcp.connections", 
                "tags": {
                    "owner": "server", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "tcp.client": {
                "metric": "tcp.connections", 
                "tags": {
                    "owner": "client", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "memory.usage": {
                "metric": "memory.percents", 
                "tags": {
                    "type": "usage", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "load_balancer"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "values": [], 
    "type": "snmp_device_lb", 
    "id": "8a031503-513d-4d7b-ac78-0ac2631fe786", 
    "resource_type": "load_balancers"
}
```
and then ...
```
{
    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
    "field_name": "load_balancer", 
    "created_at": "2018-02-19T05:21:58Z", 
    "properties": {
        "community_name": "***", 
        "device_ip": "100.64.193.3"
    }, 
    "monitorer": "http://collector-agents-se:7070", 
    "version": 1, 
    "link": "http://collector-agents-se:7070/targets/8a031503-513d-4d7b-ac78-0ac2631fe786", 
    "syncer_properties": {
        "tsdb": {
            "cpu.usage": {
                "metric": "cpu.percents", 
                "tags": {
                    "type": "usage", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "http.request": {
                "metric": "http.request.connections", 
                "tags": {
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "tcp.server": {
                "metric": "tcp.connections", 
                "tags": {
                    "owner": "server", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "tcp.client": {
                "metric": "tcp.connections", 
                "tags": {
                    "owner": "client", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }, 
            "memory.usage": {
                "metric": "memory.percents", 
                "tags": {
                    "type": "usage", 
                    "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                }
            }
        }, 
        "etcd": {
            "status": {
                "key": "load_balancer"
            }
        }
    }, 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "values": [
        {
            "reporter": "SnmpDeviceAgent", 
            "last_reported": "2018-02-19T05:25:58Z", 
            "last_changed": "2018-02-19T05:22:58Z", 
            "value": "UP", 
            "key": "status", 
            "fail_counter": 0
        }
    ], 
    "type": "snmp_device_lb", 
    "id": "8a031503-513d-4d7b-ac78-0ac2631fe786", 
    "resource_type": "load_balancers"
}
```
