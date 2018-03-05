# Stored data in etcd: Create Loadbalancer

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
