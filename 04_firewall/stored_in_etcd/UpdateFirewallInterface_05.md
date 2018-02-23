# Stored data in etcd: Update Firewall Interface

These are stored data for "heat_templates" in etcd.

* firewall_config

### Checking stored data at the point of (1) in etcd

```
/config/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "body": {
        "status": "PENDING_UPDATE", 
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
                "type": "static", 
                "cidr": "24", 
                "ip_address": "10.98.76.3", 
                "ifname": "dp0s4"
            }, 
            {
                "ifname": "dp0s5", 
                "type": "disable"
            }
        ], 
        "orchestration_state": "UPDATE_IN_PROGRESS", 
        "user_password": "k3cjZ4FNRrkX", 
        "other_password": "", 
        "admin_password": "f5UhAERVGmYS", 
        "firewall_plan_id": "40520774-4f10-4e8c-90fa-550bd4cdf101", 
        "vnf_instance_id": "44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb", 
        "operational_state": "INIT", 
        "id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
        "name": ""
    }, 
    "version": 2, 
    "marked_for_deletion": false
}
```

### Checking stored data at the point of (2) in etcd

```
/jobs/all/modify:heat_worker:firewall:8e4c20be-d221-43f4-8325-0162c1f06166:2:qzrbq
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
        "handler": "heat_worker", 
        "job_name": "firewall:8e4c20be-d221-43f4-8325-0162c1f06166:2", 
        "dependency": [
            "modify:heat_worker:firewall_interface:3543155d-0d9a-43a3-ae77-3479cf8a0e4a:2:ur5by", 
            "modify:heat_worker:vnf_instance:44799fe4-6fbf-4a5d-a2bc-ccd45e9f04eb:2:wqq3h"
        ], 
        "version": 2, 
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
                    }, 
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
                "value": 2, 
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
                    }, 
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
                        "ip_address": "10.98.76.3", 
                        "cidr": "24", 
                        "type": "static", 
                        "ifname": "dp0s4"
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
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:firewall:8e4c20be-d221-43f4-8325-0162c1f06166:2:qzrbq", 
        "resource_input": {
            "status": "PENDING_UPDATE", 
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
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "availability_zone": "nova", 
            "id": "8e4c20be-d221-43f4-8325-0162c1f06166", 
            "operational_state": "INIT", 
            "networks": [
                {
                    "ip_address": "10.98.76.3", 
                    "cidr": "24", 
                    "type": "static", 
                    "ifname": "dp0s4"
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
    "stack_status": "UPDATE_COMPLETE", 
    "output": [
        {
            "output_value": "a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "status_reason": "Stack successfully updated", 
    "id": "firewall:8e4c20be-d221-43f4-8325-0162c1f06166"
}
```

### Checking stored data at the point of (4) in etcd

```
/esi-worker/job_state/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "heat_outputs": [
        {
            "output_value": "a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
            "description": "Monitoring Target ID", 
            "output_key": "monitoring_target_id"
        }, 
        {
            "output_value": "http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6", 
            "description": "Monitoring Process Link", 
            "output_key": "monitoring_link"
        }
    ], 
    "orchestration_state": "UPDATE_COMPLETE"
}
```

### Checking stored data at the point of (5) in etcd

```
/state/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "state": {
        "worker_state": "MODIFY_COMPLETED", 
        "heat_outputs": "[{\"output_value\": \"a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6\", \"description\": \"Monitoring Target ID\", \"output_key\": \"monitoring_target_id\"}, {\"output_value\": \"http://collector-agents-se:7070/targets/a5eddd6b-1de5-4199-8c1b-a4e9f3f4eab6\", \"description\": \"Monitoring Process Link\", \"output_key\": \"monitoring_link\"}]", 
        "orchestration_state": "UPDATE_COMPLETE"
    }, 
    "version": 2, 
    "error": ""
}
```

### Checking stored data at the point of (6) in etcd

```
/monitoring/v2.0/firewalls/8e4c20be-d221-43f4-8325-0162c1f06166
{
    "firewall": "UP", 
    "version": 2
}
```
