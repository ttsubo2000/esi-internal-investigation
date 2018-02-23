# Stored data in etcd: Create Firewall Plan

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/firewall_plans/40520774-4f10-4e8c-90fa-550bd4cdf101
{
    "body": {
        "vendor": "vyatta", 
        "description": "", 
        "vnf_plan_id": "60791395-2267-4553-b115-a38fad3ebf69", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "vnf_template_id": "5a84974a-9d8b-4887-898b-8e3c095e744d", 
        "enabled": true, 
        "version": "3.5R6S3-test", 
        "is_public": true, 
        "id": "40520774-4f10-4e8c-90fa-550bd4cdf101", 
        "name": "Brocade_5600_vRouter_3.5R6S3_2CPU-8GB-2IF"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/firewall_plans/40520774-4f10-4e8c-90fa-550bd4cdf101
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
