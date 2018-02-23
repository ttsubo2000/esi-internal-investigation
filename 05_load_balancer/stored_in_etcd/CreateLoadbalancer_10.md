# Stored data in etcd: Create Loadbalancer

These are stored data for "heat_templates" in etcd.

* load_balancer

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "body": {
        "status": "PENDING_CREATE", 
        "syslog_servers": [], 
        "description": "", 
        "availability_zone": "nova", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "interfaces": [], 
        "other_username": "", 
        "networks": [], 
        "internet_port_id": "c00e43b8-ebd5-46bc-bc11-9d835b2c36ad", 
        "admin_username": "user-admin", 
        "load_balancer_conf_id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
        "user_username": "user-read", 
        "user_password": "lGxSVYSIdLqu", 
        "other_password": "", 
        "admin_password": "RBvaP4je2j5Q", 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
        "operational_state": "NO_STATE", 
        "id": "b311c470-d878-4fea-8466-a4393938f2d4", 
        "load_balancer_plan_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a", 
        "name": ""
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:1:na8s9
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
        "handler": "heat_worker", 
        "job_name": "load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:1", 
        "dependency": [
            "create:heat_worker:load_balancer_conf:1d2023e1-0cf4-48a1-af42-ab32466b2acb:1:ejvot", 
            "create:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:1:pcx6h"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "load_balancer_conf", 
                        "resource_id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb"
                    }
                ], 
                "type": "value", 
                "value": "1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
                "param": "jinja_force_dependency"
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
                "value": "b311c470-d878-4fea-8466-a4393938f2d4", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "load_balancer", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:1:na8s9", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "operational_state": "NO_STATE", 
            "syslog_servers": [], 
            "description": "", 
            "availability_zone": "nova", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "interfaces": [], 
            "other_username": "", 
            "internet_port_id": "c00e43b8-ebd5-46bc-bc11-9d835b2c36ad", 
            "admin_username": "user-admin", 
            "load_balancer_conf_id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
            "user_username": "user-read", 
            "user_password": "lGxSVYSIdLqu", 
            "other_password": "", 
            "admin_password": "RBvaP4je2j5Q", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "id": "b311c470-d878-4fea-8466-a4393938f2d4", 
            "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
            "networks": [], 
            "load_balancer_plan_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a", 
            "name": ""
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "stack_id": "load_balancer_b311c470-d878-4fea-8466-a4393938f2d4", 
    "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "8a031503-513d-4d7b-ac78-0ac2631fe786", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/8a031503-513d-4d7b-ac78-0ac2631fe786", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "load_balancer:b311c470-d878-4fea-8466-a4393938f2d4"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "heat_outputs": [
        {
            "output_value": "8a031503-513d-4d7b-ac78-0ac2631fe786", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/8a031503-513d-4d7b-ac78-0ac2631fe786", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"8a031503-513d-4d7b-ac78-0ac2631fe786\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/8a031503-513d-4d7b-ac78-0ac2631fe786\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "load_balancer": "UP", 
    "version": 1
}
```
