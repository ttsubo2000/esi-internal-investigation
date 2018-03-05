# Stored data in etcd: Update Loadbalancer Interface

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/vnf_instances/398d65ba-0060-456e-b415-5bc954450717
{
    "stack_id": "vnf_instance_398d65ba-0060-456e-b415-5bc954450717", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "47531b14-72e9-439d-8949-fd941457ecde", 
            "description": "A unique id for the nova server.", 
            "output_key": "server_id"
        }, 
        {
            "output_value": "ed1b9e59-0d6f-44d9-83bc-07ba4a236598", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/ed1b9e59-0d6f-44d9-83bc-07ba4a236598", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "vnf_instance:398d65ba-0060-456e-b415-5bc954450717"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/vnf_instances/398d65ba-0060-456e-b415-5bc954450717
{
    "heat_outputs": [
        {
            "output_value": "47531b14-72e9-439d-8949-fd941457ecde", 
            "description": "A unique id for the nova server.", 
            "output_key": "server_id"
        }, 
        {
            "output_value": "ed1b9e59-0d6f-44d9-83bc-07ba4a236598", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/ed1b9e59-0d6f-44d9-83bc-07ba4a236598", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/vnf_instances/398d65ba-0060-456e-b415-5bc954450717
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"47531b14-72e9-439d-8949-fd941457ecde\", \"description\": \"A unique id for the nova server.\", \"output_key\": \"server_id\"}, {\"output_value\": \"ed1b9e59-0d6f-44d9-83bc-07ba4a236598\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/ed1b9e59-0d6f-44d9-83bc-07ba4a236598\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```
