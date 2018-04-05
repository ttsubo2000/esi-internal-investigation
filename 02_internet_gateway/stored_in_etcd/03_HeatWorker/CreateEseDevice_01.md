# Stored data in etcd: Create Ese Device

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_devices/3fb53223-b614-46b6-92e8-25c3bcbed214
{
    "stack_id": "ese_device_3fb53223-b614-46b6-92e8-25c3bcbed214", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
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
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
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
    "id": "ese_device:3fb53223-b614-46b6-92e8-25c3bcbed214"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_devices/3fb53223-b614-46b6-92e8-25c3bcbed214
{
    "heat_outputs": [
        {
            "output_value": "bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
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
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bd8bbbcc-b175-4ea2-bfce-9821677d4da4", 
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
/state/v2.0/ese_devices/3fb53223-b614-46b6-92e8-25c3bcbed214
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"bd8bbbcc-b175-4ea2-bfce-9821677d4da4\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"default-global-system-config\", \"NWSDP-JNPR-02\"], \"description\": \"The FQ name of the physical router.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"7e5c78fa-71c0-427e-947f-586b1fc3c470\", \"description\": \"A unique id for the physical router.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/bd8bbbcc-b175-4ea2-bfce-9821677d4da4\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"NWSDP-JNPR-02\", \"description\": \"The name of the physical router.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
