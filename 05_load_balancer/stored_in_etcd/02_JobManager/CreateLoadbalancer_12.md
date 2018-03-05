# Stored data in etcd: Create Loadbalancer

```
/jobs/all/create:heat_worker:load_balancer_interface:7f2bef0a-26f3-4ec9-89de-1aee7f04f998:1:rika0
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998", 
        "handler": "heat_worker", 
        "job_name": "load_balancer_interface:7f2bef0a-26f3-4ec9-89de-1aee7f04f998:1", 
        "dependency": [
            "create:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:1:pcx6h", 
            "create:heat_worker:load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:1:na8s9"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": 2, 
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
                "value": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "load_balancer_interface", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:load_balancer_interface:7f2bef0a-26f3-4ec9-89de-1aee7f04f998:1:rika0", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "name": "Interface 1/2", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "slot_number": 2, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "vnf_interface_id": "848a926b-40ec-455a-a87c-e960c56b3dba", 
            "load_balancer_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
            "type": "user", 
            "id": "7f2bef0a-26f3-4ec9-89de-1aee7f04f998"
        }
    }, 
    0
]
```
