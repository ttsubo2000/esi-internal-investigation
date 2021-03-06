# Stored data in etcd: Update Loadbalancer Interface

```
/jobs/all/modify:heat_worker:load_balancer_conf:1d2023e1-0cf4-48a1-af42-ab32466b2acb:2:ykx6w
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
        "handler": "heat_worker", 
        "job_name": "load_balancer_conf:1d2023e1-0cf4-48a1-af42-ab32466b2acb:2", 
        "dependency": [
            "modify:heat_worker:vnf_instance:398d65ba-0060-456e-b415-5bc954450717:2:0wakm"
        ], 
        "version": 2, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
                "param": "other_password"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "", 
                "param": "other_username"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": {
                    "ip_address": "100.64.193.4", 
                    "mask": "255.255.255.0"
                }, 
                "param": "internet_port"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
                "param": "default_gateway"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "lGxSVYSIdLqu", 
                "param": "user_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "load_balancer_plan", 
                        "resource_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a"
                    }, 
                    {
                        "resource_type": "load_balancer_plan", 
                        "resource_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a"
                    }
                ], 
                "type": "value", 
                "value": "LA-0001969526-49522", 
                "param": "license_code"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "load_balancer_plan", 
                        "resource_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a"
                    }, 
                    {
                        "resource_type": "vnf_template", 
                        "resource_id": "f2123d79-e953-4b61-8aee-a217bee284af"
                    }, 
                    {
                        "resource_type": "load_balancer_plan", 
                        "resource_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a"
                    }, 
                    {
                        "resource_type": "vnf_template", 
                        "resource_id": "f2123d79-e953-4b61-8aee-a217bee284af"
                    }
                ], 
                "type": "value", 
                "value": {}, 
                "param": "init_config"
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
                "value": 10, 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "100.64.193.1", 
                "param": "management_gateway"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "RBvaP4je2j5Q", 
                "param": "admin_password"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "load_balancer_plan", 
                        "resource_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a"
                    }, 
                    {
                        "resource_type": "vnf_template", 
                        "resource_id": "f2123d79-e953-4b61-8aee-a217bee284af"
                    }, 
                    {
                        "resource_type": "load_balancer_plan", 
                        "resource_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a"
                    }, 
                    {
                        "resource_type": "vnf_template", 
                        "resource_id": "f2123d79-e953-4b61-8aee-a217bee284af"
                    }
                ], 
                "type": "value", 
                "value": {
                    "username": "vlbadmin", 
                    "password": "password"
                }, 
                "param": "credentials"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "load_balancer_plan", 
                        "resource_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a"
                    }, 
                    {
                        "resource_type": "load_balancer_plan", 
                        "resource_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a"
                    }
                ], 
                "type": "value", 
                "value": {
                    "edition": "Standard", 
                    "size": "10"
                }, 
                "param": "model"
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
                "type": "output_key", 
                "value": {
                    "output_key": "server_id", 
                    "resource_type": "vnf_instance", 
                    "resource_id": "398d65ba-0060-456e-b415-5bc954450717"
                }, 
                "param": "server_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "ip_address": "100.64.193.3", 
                        "cidr": "100.64.193.0/24", 
                        "type": "user"
                    }, 
                    {
                        "ip_address": "10.225.225.3", 
                        "cidr": "10.225.225.0/24", 
                        "type": "user"
                    }, 
                    {
                        "ip_address": "10.121.232.4", 
                        "cidr": "10.121.232.0/24", 
                        "type": "dummy"
                    }
                ], 
                "param": "networks"
            }
        ], 
        "resource_type": "load_balancer_conf", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:load_balancer_conf:1d2023e1-0cf4-48a1-af42-ab32466b2acb:2:ykx6w", 
        "resource_input": {
            "status": "PENDING_UPDATE", 
            "description": "", 
            "internet_port": {
                "ip_address": "100.64.193.4", 
                "mask": "255.255.255.0"
            }, 
            "default_gateway": null, 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "user_password": "lGxSVYSIdLqu", 
            "other_username": "", 
            "admin_username": "user-admin", 
            "vnf_instance_id": "398d65ba-0060-456e-b415-5bc954450717", 
            "user_username": "user-read", 
            "management_gateway": "100.64.193.1", 
            "admin_password": "RBvaP4je2j5Q", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "id": "1d2023e1-0cf4-48a1-af42-ab32466b2acb", 
            "other_password": "", 
            "networks": [
                {
                    "ip_address": "100.64.193.3", 
                    "cidr": "100.64.193.0/24", 
                    "type": "user"
                }, 
                {
                    "ip_address": "10.225.225.3", 
                    "cidr": "10.225.225.0/24", 
                    "type": "user"
                }, 
                {
                    "ip_address": "10.121.232.4", 
                    "cidr": "10.121.232.0/24", 
                    "type": "dummy"
                }
            ], 
            "load_balancer_plan_id": "f2fcb624-bac7-4601-a444-007d4a01bc6a", 
            "name": ""
        }
    }, 
    0
]
```
