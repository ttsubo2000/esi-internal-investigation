# Stored data in etcd: Create Loadbalancer

These are stored data for "heat_templates" in etcd.

* load_balancer_interface

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/load_balancer_interfaces/63121c05-53c3-4cff-9c27-5d4055541a63
{
    "body": {
        "status": "PENDING_CREATE", 
        "type": "management", 
        "name": "Interface 0/1", 
        "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "vnf_interface_id": "9cf64483-bbf1-4e82-ae07-33febf43dbbf", 
        "slot_number": 0, 
        "operational_state": "NO_STATE", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "load_balancer_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
        "ip_address": "100.64.193.3", 
        "id": "63121c05-53c3-4cff-9c27-5d4055541a63"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:load_balancer_interface:63121c05-53c3-4cff-9c27-5d4055541a63:1:cshn1
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "63121c05-53c3-4cff-9c27-5d4055541a63", 
        "handler": "heat_worker", 
        "job_name": "load_balancer_interface:63121c05-53c3-4cff-9c27-5d4055541a63:1", 
        "dependency": [
            "create:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:1:pcx6h", 
            "create:heat_worker:load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:1:na8s9"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": 0, 
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
                "value": "63121c05-53c3-4cff-9c27-5d4055541a63", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "load_balancer_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:load_balancer_interface:63121c05-53c3-4cff-9c27-5d4055541a63:1:cshn1", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "Interface 0/1", 
            "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "load_balancer_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
            "operational_state": "NO_STATE", 
            "ip_address": "100.64.193.3", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "vnf_interface_id": "9cf64483-bbf1-4e82-ae07-33febf43dbbf", 
            "slot_number": 0, 
            "type": "management", 
            "id": "63121c05-53c3-4cff-9c27-5d4055541a63"
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/load_balancer_interfaces/63121c05-53c3-4cff-9c27-5d4055541a63
{
    "stack_id": "load_balancer_interface_63121c05-53c3-4cff-9c27-5d4055541a63", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "130f173c-2799-4337-8ee5-d1a93a9882a9", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "load_balancer_interface:63121c05-53c3-4cff-9c27-5d4055541a63"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/load_balancer_interfaces/63121c05-53c3-4cff-9c27-5d4055541a63
{
    "heat_outputs": [
        {
            "output_value": "130f173c-2799-4337-8ee5-d1a93a9882a9", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/load_balancer_interfaces/63121c05-53c3-4cff-9c27-5d4055541a63
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"130f173c-2799-4337-8ee5-d1a93a9882a9\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/130f173c-2799-4337-8ee5-d1a93a9882a9\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/load_balancer_interfaces/63121c05-53c3-4cff-9c27-5d4055541a63
{
    "interface": "UP", 
    "version": 1
}
```
