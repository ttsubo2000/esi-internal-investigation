# Stored data in etcd: Create Firewall

These are stored data for "heat_templates" in etcd.

* firewall_config

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "body": {
        "status": "PENDING_CREATE", 
        "other_username": "", 
        "description": "", 
        "user_username": "user-read", 
        "default_gateway": "192.168.1.1", 
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
        "interfaces": [], 
        "availability_zone": "nova", 
        "admin_username": "user-admin", 
        "networks": [
            {
                "ifname": "dp0s4", 
                "type": "disable"
            }, 
            {
                "ifname": "dp0s5", 
                "type": "disable"
            }
        ], 
        "orchestration_state": "CREATE_IN_PROGRESS", 
        "user_password": "k3cjZ4FNRrkX", 
        "other_password": "", 
        "admin_password": "f5UhAERVGmYS", 
        "firewall_plan_id": "40520774-4f10-4e8c-90fa-550bd4cdf101", 
        "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
        "operational_state": "NO_STATE", 
        "id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
        "name": ""
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/create:heat_worker:firewall:8e4c20be-d221-43f4-8325-0162c1f06166:1:uvr6e
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
        "handler": "heat_worker", 
        "job_name": "firewall:8e4c20be-d221-43f4-8325-0162c1f06166:1", 
        "dependency": [
            "create:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:1:64gpp"
        ], 
        "version": 1, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "192.168.1.1", 
                "param": "default_gateway"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "0f40dffa48614d9baa7eaac7e7532099", 
                "param": "tenant_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "k3cjZ4FNRrkX", 
                "param": "user_password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
                "param": "other_username"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vnf_instance", 
                        "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
                    }
                ], 
                "type": "value", 
                "value": "100.64.193.3", 
                "param": "management_ip"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "user-admin", 
                "param": "admin_username"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "user-read", 
                "param": "user_username"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": 13, 
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
                "value": "", 
                "param": "other_password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "f5UhAERVGmYS", 
                "param": "admin_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "vnf_instance", 
                        "resource_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb"
                    }, 
                    {
                        "resource_type": "vnf_template", 
                        "resource_id": "5a84974a-9d8b-4887-898b-8e3c095e744d"
                    }
                ], 
                "type": "value", 
                "value": {
                    "username": "vfwadmin", 
                    "password": "password"
                }, 
                "param": "credentials"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "8e4c20be-d221-43f4-8325-0162c1f06166", 
                "param": "gohan_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "ifname": "dp0s4", 
                        "type": "disable"
                    }, 
                    {
                        "ifname": "dp0s5", 
                        "type": "disable"
                    }
                ], 
                "param": "networks"
            }
        ], 
        "resource_type": "firewall", 
        "action": "create", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "create:heat_worker:firewall:8e4c20be-d221-43f4-8325-0162c1f06166:1:uvr6e", 
        "resource_input": {
            "status": "PENDING_CREATE", 
            "description": "", 
            "default_gateway": "192.168.1.1", 
            "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
            "interfaces": [], 
            "other_username": "", 
            "admin_username": "user-admin", 
            "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
            "user_username": "user-read", 
            "user_password": "k3cjZ4FNRrkX", 
            "other_password": "", 
            "admin_password": "f5UhAERVGmYS", 
            "orchestration_state": "CREATE_IN_PROGRESS", 
            "availability_zone": "nova", 
            "id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
            "operational_state": "NO_STATE", 
            "networks": [
                {
                    "ifname": "dp0s4", 
                    "type": "disable"
                }, 
                {
                    "ifname": "dp0s5", 
                    "type": "disable"
                }
            ], 
            "firewall_plan_id": "40520774-4f10-4e8c-90fa-550bd4cdf101", 
            "name": ""
        }
    }, 
    0
]
```

### Checking stored data at the point of (3) in etcd

```
/esi-worker/heat_stacks/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "stack_id": "firewall_8e4c20be-d221-43f4-8325-0162c1f06166", 
    "tenant_id": "0f40dffa48614d9baa7eaac7e7532099", 
    "stack_status": "CREATE_COMPLETE", 
    "output": [
        {
            "output_value": "346eb30d-1ae0-4375-a1d6-7d83c699e2d3", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/346eb30d-1ae0-4375-a1d6-7d83c699e2d3", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack CREATE completed successfully", 
    "id": "firewall:8e4c20be-d221-43f4-8325-0162c1f06166"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "heat_outputs": [
        {
            "output_value": "346eb30d-1ae0-4375-a1d6-7d83c699e2d3", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/346eb30d-1ae0-4375-a1d6-7d83c699e2d3", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "CREATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "state": {
        "worker_state": "CREATE_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"346eb30d-1ae0-4375-a1d6-7d83c699e2d3\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/346eb30d-1ae0-4375-a1d6-7d83c699e2d3\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "CREATE_COMPLETE"
    }, 
    "version": 1, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd
```
/monitoring/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "firewall": "UP", 
    "version": 1
}
```
