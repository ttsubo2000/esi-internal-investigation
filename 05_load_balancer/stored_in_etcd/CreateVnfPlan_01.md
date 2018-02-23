# Stored data in etcd: Create Vnf Plan

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_plans/043fed11-ce3d-48fb-aa8d-13aad5804d83
{
    "body": {
        "function": "load_balancer", 
        "interface_limit": 5, 
        "vendor": "citrix", 
        "description": "dummy_vnf_plans", 
        "default_interface_number": 3, 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "flavor": "m1.xlarge", 
        "id": "043fed11-ce3d-48fb-aa8d-13aad5804d83", 
        "name": "vLB_plan"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/vnf_plans/043fed11-ce3d-48fb-aa8d-13aad5804d83
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
