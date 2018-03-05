# Stored data in etcd: Create Loadbalancer

```
/jobs/all/modify:heat_worker:port:ddc14be4-3480-4e97-a978-817b18f9904c:2:6xpec
[
    "heat_worker", 
    {
        "is_first": true, 
        "resource_id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
        "handler": "heat_worker", 
        "job_name": "port:ddc14be4-3480-4e97-a978-817b18f9904c:2", 
        "dependency": [], 
        "version": 2, 
        "params": [
            {
                "resources": [], 
                "type": "value", 
                "value": false, 
                "param": "jinja_attached"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "network", 
                        "resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
                    }, 
                    {
                        "resource_type": "network", 
                        "resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
                    }
                ], 
                "type": "output_key", 
                "value": {
                    "output_key": "id", 
                    "resource_type": "network", 
                    "resource_id": "168c1535-9001-49c7-bb05-21844570a83c"
                }, 
                "param": "virtual_network"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "47531b14-72e9-439d-8949-fd941457ecde", 
                "param": "virtual_machine"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ddc14be4-3480-4e97-a978-817b18f9904c", 
                "param": "name"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": true, 
                "param": "admin_state_up"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
                "param": "tenant_id"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "13", 
                "param": "heat_timeout"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [], 
                "param": "virtual_machine_interface_allowed_address_pairs"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "fa:16:3e:cf:b0:c4", 
                "param": "virtual_machine_interface_mac_address"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "compute:nova", 
                "param": "device_owner"
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
                "value": [], 
                "param": "security_groups"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
                "param": "jinja_force_dependency_gw_interface"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": [
                    {
                        "subnet_id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
                        "ip_address": "100.64.193.3"
                    }
                ], 
                "param": "jinja_fixed_ips"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": null, 
                "param": "jinja_force_dependency_cfg"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "compute:nova", 
                "param": "jinja_device_owner"
            }, 
            {
                "resources": [
                    {
                        "resource_type": "subnet", 
                        "resource_id": "707847d0-89d9-4b98-93a2-8b376709c5f3"
                    }, 
                    {
                        "resource_type": "subnet", 
                        "resource_id": "707847d0-89d9-4b98-93a2-8b376709c5f3"
                    }
                ], 
                "type": "list", 
                "value": [
                    {
                        "param": "jinja_subnets", 
                        "type": "output_key", 
                        "value": {
                            "output_key": "id", 
                            "resource_type": "subnet", 
                            "resource_id": "707847d0-89d9-4b98-93a2-8b376709c5f3"
                        }, 
                        "resources": []
                    }
                ], 
                "param": "jinja_subnets"
            }, 
            {
                "resources": [], 
                "type": "value", 
                "value": "ddc14be4-3480-4e97-a978-817b18f9904c", 
                "param": "uuid"
            }
        ], 
        "resource_type": "port", 
        "action": "modify", 
        "is_last": true, 
        "on_failure": "fail", 
        "id": "modify:heat_worker:port:ddc14be4-3480-4e97-a978-817b18f9904c:2:6xpec", 
        "resource_input": {
            "ese_logical_port_id": null, 
            "allowed_address_pairs": [], 
            "device_owner": "compute:nova", 
            "fake_delete": true, 
            "fixed_ips": [
                {
                    "subnet_id": "707847d0-89d9-4b98-93a2-8b376709c5f3", 
                    "ip_address": "100.64.193.3"
                }
            ], 
            "id": "ddc14be4-3480-4e97-a978-817b18f9904c", 
            "security_groups": [], 
            "binding:vif_type": "vrouter", 
            "mac_address": "fa:16:3e:cf:b0:c4", 
            "status": "PENDING_UPDATE", 
            "description": "", 
            "tags": {}, 
            "segmentation_id": 0, 
            "device_id": "47531b14-72e9-439d-8949-fd941457ecde", 
            "name": "load_balancer-management-port", 
            "managed_by_service": false, 
            "network_id": "168c1535-9001-49c7-bb05-21844570a83c", 
            "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c", 
            "admin_state_up": true, 
            "attached": false, 
            "operational_state": "NO_STATE", 
            "orchestration_state": "UPDATE_IN_PROGRESS", 
            "segmentation_type": "flat"
        }
    }, 
    0
]
```
