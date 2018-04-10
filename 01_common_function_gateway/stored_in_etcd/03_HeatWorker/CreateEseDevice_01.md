# Stored data in etcd: Create Ese Device

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/ese_devices/cc214b6a-2f09-4094-b7cd-a9590f64b854
{
    "stack_id": "ese_device_cc214b6a-2f09-4094-b7cd-a9590f64b854", 
    "tenant_id": "c583ce78843344adbe5fd20f13620274", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
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
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
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
    "id": "ese_device:cc214b6a-2f09-4094-b7cd-a9590f64b854"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/ese_devices/cc214b6a-2f09-4094-b7cd-a9590f64b854
{
    "heat_outputs": [
        {
            "output_value": "2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
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
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/2762cfcb-575c-45cc-a07b-ca19f5b007cd", 
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
/state/v2.0/ese_devices/cc214b6a-2f09-4094-b7cd-a9590f64b854
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"2762cfcb-575c-45cc-a07b-ca19f5b007cd\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": [\"default-global-system-config\", \"NWSDP-JNPR-02\"], \"description\": \"The FQ name of the physical router.\", \"output_key\": \"fq_name\"}, {\"output_value\": \"7e5c78fa-71c0-427e-947f-586b1fc3c470\", \"description\": \"A unique id for the physical router.\", \"output_key\": \"id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/2762cfcb-575c-45cc-a07b-ca19f5b007cd\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}, {\"output_value\": \"NWSDP-JNPR-02\", \"description\": \"The name of the physical router.\", \"output_key\": \"name\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
