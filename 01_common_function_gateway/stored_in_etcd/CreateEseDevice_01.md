# Stored data in etcd: Create Ese Device

These are stored data for "heat_templates" in etcd.

* ese_device_existing
* ese_device_monitoring

![scope](../../images/esi_interface.008.png)

These are stored data for "Create Ese Device" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_devices/9f05b260-26ca-46f7-98c3-ad88e411a989
{
    "body": {
        "status": "PENDING_CREATE", 
        "username": "esi", 
        "password": "password", 
        "description": "", 
        "tags": {}, 
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
        "public_ip_address": "10.161.0.34", 
        "hostname": "QFX-NW02", 
        "name": "QFX-NW02", 
        "existing": "existing", 
        "type": "tor", 
        "id": "9f05b260-26ca-46f7-98c3-ad88e411a989", 
        "management_ip_address": "10.161.0.34"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

* Jobs for heat_worker
```
/jobs/all/create:heat_worker:ese_device:9f05b260-26ca-46f7-98c3-ad88e411a989:1:se2z7
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "9f05b260-26ca-46f7-98c3-ad88e411a989", 
        "handler": "heat_worker", 
        "job_name": "ese_device:9f05b260-26ca-46f7-98c3-ad88e411a989:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "QFX-NW02", 
                "param": "hostname"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "QFX-NW02", 
                "param": "name"
            }
        ], 
        "resource_type": "ese_device", 
        "action": "create", 
        "is_last": false, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_device:9f05b260-26ca-46f7-98c3-ad88e411a989:1:se2z7", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "username": "esi", 
            "description": "", 
            "tags": {}, 
            "existing": "existing", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "hostname": "QFX-NW02", 
            "name": "QFX-NW02", 
            "management_ip_address": "10.161.0.34", 
            "password": "password", 
            "type": "tor", 
            "id": "9f05b260-26ca-46f7-98c3-ad88e411a989", 
            "public_ip_address": "10.161.0.34"
        }
    }, 
    0
]
```

* Jobs for monitoring_worker
```
/jobs/all/create:monitoring_worker:ese_device:9f05b260-26ca-46f7-98c3-ad88e411a989:1:8sz98
[
    "monitoring_worker", 
    {
        "is_first": false, 
        "resource_id": "9f05b260-26ca-46f7-98c3-ad88e411a989", 
        "handler": "monitoring_worker", 
        "job_name": "ese_device:9f05b260-26ca-46f7-98c3-ad88e411a989:1", 
        "dependency": [
            "create:heat_worker:ese_device:9f05b260-26ca-46f7-98c3-ad88e411a989:1:se2z7"
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
                "resources": [], 
                "type": "value", 
                "value": "10.161.0.34", 
                "param": "device_ip"
            }
        ], 
        "resource_type": "ese_device", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:monitoring_worker:ese_device:9f05b260-26ca-46f7-98c3-ad88e411a989:1:8sz98", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "username": "esi", 
            "description": "", 
            "tags": {}, 
            "existing": "existing", 
            "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
            "hostname": "QFX-NW02", 
            "name": "QFX-NW02", 
            "management_ip_address": "10.161.0.34", 
            "password": "password", 
            "type": "tor", 
            "id": "9f05b260-26ca-46f7-98c3-ad88e411a989", 
            "public_ip_address": "10.161.0.34"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_devices/9f05b260-26ca-46f7-98c3-ad88e411a989
{
    "stack_id": "ese_device_9f05b260-26ca-46f7-98c3-ad88e411a989", 
    "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": [
                "default-global-system-config", 
                "QFX-NW02"
            ], 
            "description": "The FQ name of the physical router.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "physical_router", 
            "description": "A unique id for the physical router.", 
            "output_key": "id"
        }, 
        {
            "output_value": "dummy", 
            "description": "The name of the physical router.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "ese_device:9f05b260-26ca-46f7-98c3-ad88e411a989"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ese_devices/9f05b260-26ca-46f7-98c3-ad88e411a989
{
    "heat_outputs": [
        {
            "output_value": [
                "default-global-system-config", 
                "QFX-NW02"
            ], 
            "description": "The FQ name of the physical router.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "physical_router", 
            "description": "A unique id for the physical router.", 
            "output_key": "id"
        }, 
        {
            "output_value": "dummy", 
            "description": "The name of the physical router.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (5) in etcd

```
/esi-worker/job_state/v2.0/ese_devices/9f05b260-26ca-46f7-98c3-ad88e411a989
{
    "state_monitoring": {
        "switch": "ACTIVE"
    }, 
    "heat_outputs": [
        {
            "output_value": [
                "default-global-system-config", 
                "QFX-NW02"
            ], 
            "description": "The FQ name of the physical router.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "physical_router", 
            "description": "A unique id for the physical router.", 
            "output_key": "id"
        }, 
        {
            "output_value": "dummy", 
            "description": "The name of the physical router.", 
            "output_key": "name"
        }
    ]
}
```

### Checking stored data at the point of (6) in etcd

```
/state/v2.0/ese_devices/9f05b260-26ca-46f7-98c3-ad88e411a989
{
    "state": {
        "state_monitoring": "{\"switch\": \"ACTIVE\"}", 
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": [\"default-global-system-config\", \"QFX-NW02\"], \"description\": \"The FQ name of the physical router.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"physical_router\", \"description\": \"A unique id for the physical router.\", \"output_key\": \"id\"}, {\"output_value\": \"dummy\", \"description\": \"The name of the physical router.\", \"output_key\": \"name\"}]"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (7) in etcd

```
/monitoring/v2.0/ese_devices/9f05b260-26ca-46f7-98c3-ad88e411a989
{
    "switch": "UP", 
    "version": 1
}
```
