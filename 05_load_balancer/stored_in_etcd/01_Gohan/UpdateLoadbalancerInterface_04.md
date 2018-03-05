# Stored data in etcd: Update Loadbalancer Interface

```
/config/v2.0/load_balancer_confs/1d2023e1-0cf4-48a1-af42-ab32466b2acb
{
    "body": {
        "status": "PENDING_UPDATE", 
        "description": "", 
        "internet_port": {
            "mask": "255.255.255.0", 
            "ip_address": "100.64.193.4"
        }, 
        "default_gateway": null, 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "user_password": "lGxSVYSIdLqu", 
        "other_username": "", 
        "admin_username": "user-admin", 
        "networks": [
            {
                "type": "user", 
                "cidr": "100.64.193.0/24", 
                "ip_address": "100.64.193.3"
            }, 
            {
                "type": "user", 
                "cidr": "10.225.225.0/24", 
                "ip_address": "10.225.225.3"
            }, 
            {
                "type": "dummy", 
                "cidr": "10.121.232.0/24", 
                "ip_address": "10.121.232.4"
            }
        ], 
        "user_username": "user-read", 
        "management_gateway": "100.64.193.1", 
        "admin_password": "RBvaP4je2j5Q", 
        "orchestration_state": "UPDATE_IN_PROGRESS", 
        "other_password": "", 
        "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
        "id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
        "load_balancer_plan_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a", 
        "name": ""
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```
