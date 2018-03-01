# Stored data in etcd: Create Ese Device

### Checking stored data at the point of (1) in etcd

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

### Checking stored data at the point of (2) in etcd

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

### Checking stored data at the point of (3) in etcd

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
