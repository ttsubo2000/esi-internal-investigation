# Stored data in etcd: Update Loadbalancer Interface

These are stored data for "heat_templates" in etcd.

* load_balancer

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "body": {
        "syslog_servers": [], 
        "availability_zone": "nova", 
        "user_password": "lGxSVYSIdLqu", 
        "other_password": "", 
        "id": "b311c470-d878-4fea-8466-a4393938f2d4", 
        "networks": [], 
        "load_balancer_plan_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a", 
        "internet_port_id": "c00e43b8-ebd5-46bc-bc11-9d835b2c36ad", 
        "load_balancer_conf_id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
        "admin_password": "RBvaP4je2j5Q", 
        "status": "PENDING_UPDATE", 
        "description": "", 
        "default_gateway": null, 
        "interfaces": [], 
        "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
        "user_username": "user-read", 
        "name": "", 
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
        "other_username": "", 
        "admin_username": "user-admin", 
        "operational_state": "INIT", 
        "orchestration_state": "UPDATE_IN_PROGRESS"
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/modify:heat_worker:load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:2:rvx91
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "b311c470-d878-4fea-8466-a4393938f2d4", 
        "handler": "heat_worker", 
        "job_name": "load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:2", 
        "dependency": [
            "modify:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:2:0wakm", 
            "modify:heat_worker:load_balancer_conf:1d2023e1-0cf4-48a1-af42-ab32466b2acb:2:ykx6w"
        ], 
        "version": 2, 
        "params": [
            {
                "resources": [
                    {
                        "resource_type": "load_balancer_conf", 
                        "resource_id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb"
                    }, 
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
                "value": "b311c470-d878-4fea-8466-a4393938f2d4", 
                "param": "gohan_id"
            }
        ], 
        "resource_type": "load_balancer", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:load_balancer:b311c470-d878-4fea-8466-a4393938f2d4:2:rvx91", 
        "resource_input": {
            "syslog_servers": [], 
            "availability_zone": "nova", 
            "user_password": "lGxSVYSIdLqu", 
            "networks": [], 
            "other_password": "", 
            "id": "b311c470-d878-4fea-8466-a4393938f2d4", 
            "load_balancer_plan_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a", 
            "internet_port_id": "c00e43b8-ebd5-46bc-bc11-9d835b2c36ad", 
            "load_balancer_conf_id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
            "admin_password": "RBvaP4je2j5Q", 
            "status": "PENDING_UPDATE", 
            "description": "", 
            "default_gateway": null, 
            "interfaces": [], 
            "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
            "user_username": "user-read", 
            "name": "", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "other_username": "", 
            "admin_username": "user-admin", 
            "operational_state": "INIT", 
            "orchestration_state": "UPDATE_IN_PROGRESS"
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
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "668aabd6-71fe-4e0a-9842-421dce35d777", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/668aabd6-71fe-4e0a-9842-421dce35d777", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "load_balancer:b311c470-d878-4fea-8466-a4393938f2d4"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "heat_outputs": [
        {
            "output_value": "668aabd6-71fe-4e0a-9842-421dce35d777", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/668aabd6-71fe-4e0a-9842-421dce35d777", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"668aabd6-71fe-4e0a-9842-421dce35d777\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/668aabd6-71fe-4e0a-9842-421dce35d777\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/load_balancers/b311c470-d878-4fea-8466-a4393938f2d4
{
    "load_balancer": "UP", 
    "version": 2
}
```
