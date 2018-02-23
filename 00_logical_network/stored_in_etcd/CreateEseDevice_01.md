# Stored data in etcd: Create Ese Device

These are stored data for "heat_templates" in etcd.

* ese_device_existing

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/ese_devices/718148aa-4483-47d5-bbd1-a0e0738dc018
{
    "body": {
        "status": "PENDING_CREATE", 
        "username": "esi", 
        "password": "password", 
        "description": "", 
        "tags": {}, 
        "operational_state": "NO_STATE", 
        "public_ip_address": "10.161.0.33", 
        "hostname": "QFX-NW01", 
        "name": "QFX-NW01", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
        "existing": "existing", 
        "type": "tor", 
        "id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
        "management_ip_address": "10.161.0.33"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:ese_device:718148aa-4483-47d5-bbd1-a0e0738dc018:1:91uyh
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
        "handler": "heat_worker", 
        "job_name": "ese_device:718148aa-4483-47d5-bbd1-a0e0738dc018:1", 
        "dependency": [], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "QFX-NW01", 
                "param": "hostname"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "QFX-NW01", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ae69b52f46ba480bb9636f62736436f4", 
                "param": "tenant_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "10.161.0.33", 
                "param": "device_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "6", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "version"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "ese_device", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:ese_device:718148aa-4483-47d5-bbd1-a0e0738dc018:1:91uyh", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "username": "esi", 
            "description": "", 
            "name": "QFX-NW01", 
            "tags": {}, 
            "existing": "existing", 
            "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
            "hostname": "QFX-NW01", 
            "operational_state": "NO_STATE", 
            "management_ip_address": "10.161.0.33", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "password": "password", 
            "type": "tor", 
            "id": "718148aa-4483-47d5-bbd1-a0e0738dc018", 
            "public_ip_address": "10.161.0.33"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_devices/718148aa-4483-47d5-bbd1-a0e0738dc018
{
    "stack_id": "ese_device_718148aa-4483-47d5-bbd1-a0e0738dc018", 
    "tenant_id": "ae69b52f46ba480bb9636f62736436f4", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "edd4b769-1665-429f-aef4-f428aca34a0b", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": [
                "default-global-system-config", 
                "NWSDP-JNPR-02"
            ], 
            "description": "The FQ name of the physical router.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "7e5c78fa-71c0-427e-947f-586b1fc3c470", 
            "description": "A unique id for the physical router.", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/edd4b769-1665-429f-aef4-f428aca34a0b", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "NWSDP-JNPR-02", 
            "description": "The name of the physical router.", 
            "output_key": "name"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "ese_device:718148aa-4483-47d5-bbd1-a0e0738dc018"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/ese_devices/718148aa-4483-47d5-bbd1-a0e0738dc018
{
    "heat_outputs": [
        {
            "output_value": "edd4b769-1665-429f-aef4-f428aca34a0b", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": [
                "default-global-system-config", 
                "NWSDP-JNPR-02"
            ], 
            "description": "The FQ name of the physical router.", 
            "output_key": "fq_name"
        }, 
        {
            "output_value": "7e5c78fa-71c0-427e-947f-586b1fc3c470", 
            "description": "A unique id for the physical router.", 
            "output_key": "id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/edd4b769-1665-429f-aef4-f428aca34a0b", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }, 
        {
            "output_value": "NWSDP-JNPR-02", 
            "description": "The name of the physical router.", 
            "output_key": "name"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/ese_devices/718148aa-4483-47d5-bbd1-a0e0738dc018
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"edd4b769-1665-429f-aef4-f428aca34a0b\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"default-global-system-config\", \"NWSDP-JNPR-02\"], \"description\": \"The FQ name of the physical router.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"7e5c78fa-71c0-427e-947f-586b1fc3c470\", \"description\": \"A unique id for the physical router.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/edd4b769-1665-429f-aef4-f428aca34a0b\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"NWSDP-JNPR-02\", \"description\": \"The name of the physical router.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```


### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/ese_devices/718148aa-4483-47d5-bbd1-a0e0738dc018
{
    "switch": "UP", 
    "version": 1
}
```
