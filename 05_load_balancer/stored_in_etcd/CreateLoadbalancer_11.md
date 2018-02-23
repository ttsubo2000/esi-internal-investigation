# Stored data in etcd: Create Loadbalancer

These are stored data for "heat_templates" in etcd.

* load_balancer_interface

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "body": {
        "status": "PENDING_CREATE", 
        "name": "Interface 1/1", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "vnf_interface_id": "3f1be05a-6cae-4f5e-9985-15f6f714d8dc", 
        "load_balancer_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
        "operational_state": "NO_STATE", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "slot_number": 1, 
        "type": "user", 
        "id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c:1:sougr
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
        "handler": "heat_worker", 
        "job_name": "load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c:1", 
        "dependency": [
            "create:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:1:pcx6h", 
            "create:heat_worker:load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:1:na8s9"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": 1, 
                "param": "jinja_slot_number"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
                "param": "tenant_id"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "load_balancer", 
                        "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4"
                    }, 
                    {
                        "resource_type": "vnf_instance", 
                        "resource_id": "398d65ba-0060-456e-b415-5bc954450717"
                    }
                ], 
                "type": "value", 
                "value": "100.64.193.3", 
                "param": "management_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 3, 
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
                "value": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "load_balancer_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c:1:sougr", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "Interface 1/1", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "slot_number": 1, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "vnf_interface_id": "3f1be05a-6cae-4f5e-9985-15f6f714d8dc", 
            "load_balancer_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
            "type": "user", 
            "id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "stack_id": "load_balancer_interface_24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "2da66917-604c-4076-8c21-79da05f6479e", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/2da66917-604c-4076-8c21-79da05f6479e", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "heat_outputs": [
        {
            "output_value": "2da66917-604c-4076-8c21-79da05f6479e", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/2da66917-604c-4076-8c21-79da05f6479e", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"2da66917-604c-4076-8c21-79da05f6479e\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/2da66917-604c-4076-8c21-79da05f6479e\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "interface": "UP", 
    "version": 1
}
```
