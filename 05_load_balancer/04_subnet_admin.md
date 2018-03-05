[Return to Previous Page](00_load_balancer.md)

# 4. Clarification of interface in Sequence Diagram "Create Subnet for admin-net"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_loadbalancer.005.png)


## 4.1. Gohan

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
        "description": "adminpod subnet",
        "name": "adminpod-subnet",
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",
        "tags": {},
        "ip_version": 4,
        "cidr": "100.64.193.0/24",
        "network_id": "168c1535-9001-49c7-bb05-21844570a83c",
        "host_routes": [
            {
                "destination": "172.26.10.0/24",
                "nexthop": "100.64.193.1"
            }
        ]
    }
}
```
After processing, Gohan has stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/01_Gohan/CreateSubnet2_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/01_Gohan/CreateSubnet2_02.md)


## 4.2. ResourceReader
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

* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/00_ResourceReader/CreateSubnet2_02.md)


## 4.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/02_JobManager/CreateSubnet2_01.md)


## 4.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "subnet"](stored_in_etcd/03_HeatWorker/CreateSubnet2_01.md)


## 4.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Subnet".
As a result, Heat has stored heat-stacks for "Create Subnet".

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet2_01.md)


## 4.6. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json 707847d0-89d9-4b98-93a2-8b376709c5f3
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "100.64.193.254",
                "start": "100.64.193.2"
            }
        ],
        "cidr": "100.64.193.0/24",
        "description": "adminpod subnet",
        "dhcp_server_address": "100.64.193.2",
        "dns_nameservers": [],
        "enable_dhcp": true,
        "gateway_ip": "100.64.193.1",
        "host_routes": [
            {
                "destination": "172.26.10.0/24",
                "nexthop": "100.64.193.1"
            }
        ],
        "id": "707847d0-89d9-4b98-93a2-8b376709c5f3",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "adminpod-subnet",
        "network_id": "168c1535-9001-49c7-bb05-21844570a83c",
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
$ gohan client port show --output-format json ff724cd0-02ef-42e0-9510-1ea784ddaa8c
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "707847d0-89d9-4b98-93a2-8b376709c5f3",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "100.64.193.2",
                "subnet_id": "707847d0-89d9-4b98-93a2-8b376709c5f3"
            }
        ],
        "id": "ff724cd0-02ef-42e0-9510-1ea784ddaa8c",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "168c1535-9001-49c7-bb05-21844570a83c",
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
