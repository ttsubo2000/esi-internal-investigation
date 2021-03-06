[Return to Previous Page](00_load_balancer.md)

# 2. Clarification of interface in Sequence Diagram "Create Subnet for dummy-net"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_loadbalancer.003.png)


## 2.1. Gohan

![scope](../images/ESI_Sequence_diagram.002.png)

### Outline
First of all, Gohan has received JSON data for "Create Subnet" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/subnets
```
```
{
    "subnet": {
        "description": "dummy subnet for load_balancer",
        "name": "dummy-subnet",
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",
        "tags": {},
        "ip_version": 4,
        "cidr": "10.121.232.0/24",
        "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f"
    }
}
```
After processing, Gohan has stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/01_Gohan/CreateSubnet1_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/01_Gohan/CreateSubnet1_02.md)


## 2.2. ResourceReader
When ResourceReader has started, it gets all of schemas from Gohan.
After that, these schemas are converted as a template_mappings.
And then, ResourceReader keeps storing template_mappings for following processing.

### Reference
* [Checking schemas in ResourceReader](../memo/schemas.txt)
* [Checking template_mappings in ResourceReader](../memo/template_mappings.md)

![scope](../images/ESI_Sequence_diagram.003.png)

### Outline
After fetching resource_data for "Create Subnet" in etcd, ResourceReader has fetched heat_templates in etcd.

* [Checking stored data for "subnet"](../heat_template/subnet.md)

And then, ResourceReader has stored data as finishing resource

* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/00_ResourceReader/CreateSubnet1_02.md)


## 2.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/02_JobManager/CreateSubnet1_01.md)


## 2.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "subnet"](stored_in_etcd/03_HeatWorker/CreateSubnet1_01.md)


## 2.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Subnet".
As a result, Heat has stored heat-stacks for "Create Subnet".

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet1_01.md)


## 2.6. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json 6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "10.121.232.254",
                "start": "10.121.232.2"
            }
        ],
        "cidr": "10.121.232.0/24",
        "description": "dummy subnet for load_balancer",
        "dhcp_server_address": "10.121.232.2",
        "dns_nameservers": [],
        "enable_dhcp": true,
        "gateway_ip": "10.121.232.1",
        "host_routes": [],
        "id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "dummy-subnet",
        "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f",
        "ntp_servers": [],
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c"
    }
}
```
* Checking another resources via gohan client
```
$ gohan client port show --output-format json 7864794a-fe4f-4aac-91a7-61c103f11f58
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "10.121.232.2",
                "subnet_id": "6f5f33d6-2cfe-47c1-a91a-3f3d44972b1a"
            }
        ],
        "id": "7864794a-fe4f-4aac-91a7-61c103f11f58",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "ce9a7a92-d11a-4fc6-8ae7-18061b62c98f",
        "operational_state": "",
        "orchestration_state": "SYNC_COMPLETE",
        "security_groups": [],
        "segmentation_id": null,
        "segmentation_type": null,
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c"
    }
}
```

[Return to Previous Page](00_load_balancer.md)
