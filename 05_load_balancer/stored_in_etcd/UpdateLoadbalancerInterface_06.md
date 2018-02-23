# Stored data in etcd: Update Loadbalancer Interface

These are stored data for "heat_templates" in etcd.

* load_balancer_interface

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "body": {
        "status": "PENDING_UPDATE", 
        "type": "user", 
        "description": null, 
        "network_id": "774acf45-316f-4431-b31b-08770b76d761", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "vnf_interface_id": "3f1be05a-6cae-4f5e-9985-15f6f714d8dc", 
        "slot_number": 1, 
        "operational_state": "INIT", 
        "orchestration_state": "UPDATE_IN_PROGRESS", 
        "load_balancer_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
        "virtual_ip_address": null, 
        "virtual_ip_properties": null, 
        "ip_address": "10.225.225.3", 
        "id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
        "name": "Interface 1/1"
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/modify:heat_worker:load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c:2:mzlsm
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
        "handler": "heat_worker", 
        "job_name": "load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c:2", 
        "dependency": [
            "modify:heat_worker:load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:2:rvx91", 
            "modify:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:2:0wakm"
        ], 
        "version": 2, 
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
                    }, 
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
                "value": 2, 
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
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c:2:mzlsm", 
        "resource_input": {
            "status": "PENDING_UPDATE", 
            "virtual_ip_properties": null, 
            "description": null, 
            "network_id": "774acf45-316f-4431-b31b-08770b76d761", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "load_balancer_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
            "operational_state": "INIT", 
            "ip_address": "10.225.225.3", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "vnf_interface_id": "3f1be05a-6cae-4f5e-9985-15f6f714d8dc", 
            "slot_number": 1, 
            "virtual_ip_address": null, 
            "type": "user", 
            "id": "24580bfc-32f4-4c0f-8e8a-c7288497aa7c", 
            "name": "Interface 1/1"
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
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "load_balancer_interface:24580bfc-32f4-4c0f-8e8a-c7288497aa7c"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "heat_outputs": [
        {
            "output_value": "9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/9fc3003a-56fd-4a6c-9cac-0c1ab74f11c8\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/load_balancer_interfaces/24580bfc-32f4-4c0f-8e8a-c7288497aa7c
{
    "interface": "UP", 
    "version": 2
}
```
