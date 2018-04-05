# Stored data in etcd: Create Edge Router

### Checking stored data at the point of (1) in etcd

```
/esi-worker/heat_stacks/v2.0/edge_routers/cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78
{
    "stack_id": "edge_router_cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78", 
    "tenant_id": "06d6b792b31c40daa546fb0f4e35980d", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "edge_router:cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78"
}
```

### Checking stored data at the point of (2) in etcd

```
/esi-worker/job_state/v2.0/edge_routers/cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78
{
    "heat_outputs": [
        {
            "output_value": "9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9363d0ec-e347-482c-8d0d-da1d8e11ad73", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (3) in etcd

```
/state/v2.0/edge_routers/cbe0fe23-8461-4a71-a7cc-a3a1d8c1fd78
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"9363d0ec-e347-482c-8d0d-da1d8e11ad73\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se.monitoringrefactordocker_default:7070/targets/9363d0ec-e347-482c-8d0d-da1d8e11ad73\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
