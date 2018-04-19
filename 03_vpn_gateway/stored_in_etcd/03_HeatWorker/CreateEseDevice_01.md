# Stored data in etcd: Create Ese Device

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_devices/4d8371c0-1b91-4818-a6e7-26425178e5d4
{
    "stack_id": "ese_device_4d8371c0-1b91-4818-a6e7-26425178e5d4", 
    "tenant_id": "b3e3095c0a5b4383805efe9cf2a6b5ef", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "aeaad149-357c-41b9-b408-6304c5d3396c", 
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
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aeaad149-357c-41b9-b408-6304c5d3396c", 
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
    "id": "ese_device:4d8371c0-1b91-4818-a6e7-26425178e5d4"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_devices/4d8371c0-1b91-4818-a6e7-26425178e5d4
{
    "heat_outputs": [
        {
            "output_value": "aeaad149-357c-41b9-b408-6304c5d3396c", 
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
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aeaad149-357c-41b9-b408-6304c5d3396c", 
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
/state/v2.0/ese_devices/4d8371c0-1b91-4818-a6e7-26425178e5d4
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"aeaad149-357c-41b9-b408-6304c5d3396c\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"default-global-system-config\", \"NWSDP-JNPR-02\"], \"description\": \"The FQ name of the physical router.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"7e5c78fa-71c0-427e-947f-586b1fc3c470\", \"description\": \"A unique id for the physical router.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/aeaad149-357c-41b9-b408-6304c5d3396c\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"NWSDP-JNPR-02\", \"description\": \"The name of the physical router.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
