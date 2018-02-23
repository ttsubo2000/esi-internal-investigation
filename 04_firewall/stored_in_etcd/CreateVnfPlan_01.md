# Stored data in etcd: Create Vnf Plan

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/vnf_plans/60791395-2267-4553-b115-a38fad3ebf69
{
    "body": {
        "function": "firewall", 
        "interface_limit": 3, 
        "vendor": "vyatta", 
        "description": "vyatta-2CPU-2IF", 
        "default_interface_number": 3, 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "flavor": "m1.large", 
        "id": "60791395-2267-4553-b115-a38fad3ebf69", 
        "name": "vyatta-2CPU-2IF"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/vnf_plans/60791395-2267-4553-b115-a38fad3ebf69
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
