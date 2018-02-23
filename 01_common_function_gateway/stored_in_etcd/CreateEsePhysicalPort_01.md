# Stored data in etcd: Create Ese Physical Port

These are stored data for "heat_templates" in etcd.

* ese_physical_port_existing
* ese_physical_port_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Ese Physical Port" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_physical_ports/976156ef-05b4-47f4-9497-a36531563a08
{
    "body": {
        "status": "PENDING_CREATE", 
        "connected_port_owner": "mx_downlink", 
        "name": "xe-0/0/3", 
        "tags": {}, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "existing": "new", 
        "connected_port_id": "", 
        "ese_device_id": "9f05b260-26ca-46f7-98c3-ad88e411a989", 
        "id": "976156ef-05b4-47f4-9497-a36531563a08", 
        "description": ""
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:ese_physical_port:976156ef-05b4-47f4-9497-a36531563a08:1:4w58i
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "976156ef-05b4-47f4-9497-a36531563a08", 
        "handler": "heat_worker", 
        "job_name": "ese_physical_port:976156ef-05b4-47f4-9497-a36531563a08:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/3", 
                "param": "physical_port_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "9f05b260-26ca-46f7-98c3-ad88e411a989"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "ese_device", 
                    "resource_id": "9f05b260-26ca-46f7-98c3-ad88e411a989"
                }, 
                "param": "physical_device"
            }
        ], 
        "resource_type": "ese_physical_port", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_physical_port:976156ef-05b4-47f4-9497-a36531563a08:1:4w58i", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_port_owner": "mx_downlink", 
            "tags": {}, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "description": "", 
            "existing": "new", 
            "connected_port_id": "", 
            "ese_device_id": "9f05b260-26ca-46f7-98c3-ad88e411a989", 
            "id": "976156ef-05b4-47f4-9497-a36531563a08", 
            "name": "xe-0/0/3"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ese_physical_port:976156ef-05b4-47f4-9497-a36531563a08:1:vr0kv
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "976156ef-05b4-47f4-9497-a36531563a08", 
        "handler": "monitoring_worker", 
        "job_name": "ese_physical_port:976156ef-05b4-47f4-9497-a36531563a08:1", 
        "dependency": [
            "create:heat_worker:ese_physical_port:976156ef-05b4-47f4-9497-a36531563a08:1:4w58i"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "ESE_NODE_COMMUNITY", 
                "param": "community_name"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "ese_device", 
                        "resource_id": "9f05b260-26ca-46f7-98c3-ad88e411a989"
                    }
                ], 
                "type": "value", 
                "value": "10.161.0.34", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "xe-0/0/3", 
                "param": "name"
            }
        ], 
        "resource_type": "ese_physical_port", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ese_physical_port:976156ef-05b4-47f4-9497-a36531563a08:1:vr0kv", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "connected_port_owner": "mx_downlink", 
            "tags": {}, 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "description": "", 
            "existing": "new", 
            "connected_port_id": "", 
            "ese_device_id": "9f05b260-26ca-46f7-98c3-ad88e411a989", 
            "id": "976156ef-05b4-47f4-9497-a36531563a08", 
            "name": "xe-0/0/3"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_physical_ports/976156ef-05b4-47f4-9497-a36531563a08
{
    "stack_id": "ese_physical_port_976156ef-05b4-47f4-9497-a36531563a08", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "dddddddd-dddd-dddd-dddd-dddddddddddd", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": null, 
            "output_error": "'ContrailPhysicalInterface' object has no attribute 'pi_uuid'", 
            "description": "The name of the physical interface.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "ese_physical_port:976156ef-05b4-47f4-9497-a36531563a08"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ese_physical_ports/976156ef-05b4-47f4-9497-a36531563a08
{
    "heat_outputs": [
        {
            "output_value": "dddddddd-dddd-dddd-dddd-dddddddddddd", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": null, 
            "output_error": "'ContrailPhysicalInterface' object has no attribute 'pi_uuid'", 
            "description": "The name of the physical interface.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/ese_physical_ports/976156ef-05b4-47f4-9497-a36531563a08
{
    "state_monitoring": {
        "port": "ACTIVE"
    }, 
    "heat_outputs": [
        {
            "output_value": "dddddddd-dddd-dddd-dddd-dddddddddddd", 
            "description": "A unique id for the physical interface", 
            "output_key": "id"
        }, 
        {
            "output_value": null, 
            "output_error": "'ContrailPhysicalInterface' object has no attribute 'pi_uuid'", 
            "description": "The name of the physical interface.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/ese_physical_ports/976156ef-05b4-47f4-9497-a36531563a08
{
    "state": {
        "state_monitoring": "{\"port\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"dddddddd-dddd-dddd-dddd-dddddddddddd\", \"description\": \"A unique id for the physical interface\", \"output_key\": \"id\"}, {\"output_value\": null, \"output_error\": \"'ContrailPhysicalInterface' object has no attribute 'pi_uuid'\", \"description\": \"The name of the physical interface.\", \"output_key\": \"name\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/ese_physical_ports/976156ef-05b4-47f4-9497-a36531563a08
{
    "version": 1, 
    "port": "UP"
}
```
