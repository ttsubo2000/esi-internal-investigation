# Stored data in etcd: Create Loadbalancer Plan

No stored data for "heat_templates" in etcd.

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/load_balancer_plans/f2fcb624-bac7-4601-a444-007d4a01bc6a
{
    "body": {
        "vendor": "citrix", 
        "description": "", 
        "license_code": "LA-0001969526-49522", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "vnf_template_id": "f2123d79-e953-4b61-8aee-a217bee284af", 
        "vnf_plan_id": "043fed11-ce3d-48fb-aa8d-13aad5804d83", 
        "enabled": true, 
        "maximum_syslog_servers": 2, 
        "version": "10.5-57.7", 
        "is_public": true, 
        "model": {
            "edition": "Standard", 
            "size": "10"
        }, 
        "id": "f2fcb624-bac7-4601-a444-007d4a01bc6a", 
        "name": "Citrix_NetScaler_VPX_10.5-57.7_Standard_Edition_50Mbps_2CPU-8GB-4IF"
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/load_balancer_plans/f2fcb624-bac7-4601-a444-007d4a01bc6a
{
    "state": {
        "worker_state": "READ_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```
