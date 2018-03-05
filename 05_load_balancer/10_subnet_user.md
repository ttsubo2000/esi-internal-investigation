[Return to Previous Page](00_load_balancer.md)

# 10. Clarification of interface in Sequence Diagram "Create Subnet for user-net"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_loadbalancer.011.png)


## 10.1. Gohan

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
        "description": "load_balancer subnet",
        "name": "sample-lb-subnet",
        "tenant_id": "fe3a4a1a72c04479bb6c19c2c0ccba4c",
        "tags": {},
        "ip_version": 4,
        "cidr": "10.225.225.0/24",
        "network_id": "774acf45-316f-4431-b31b-08770b76d761"
    }
}
```
After processing, Gohan has stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/01_Gohan/CreateSubnet3_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/01_Gohan/CreateSubnet3_02.md)


## 10.2. ResourceReader
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

* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/00_ResourceReader/CreateSubnet3_02.md)


## 10.3. JobManager

![scope](../images/ESI_Sequence_diagram.004.png)

### Outline
After converting resource_data to job_data, JobManager has stored it in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/02_JobManager/CreateSubnet3_01.md)


## 10.4. HeatWorker

![scope](../images/ESI_Sequence_diagram.005.png)

### Outline
After fetching job_data, HeatWorker has handled job_data.
And then, HeatWorker has stored the result of handling job_data.

* [Checking stored data for creating "subnet"](stored_in_etcd/03_HeatWorker/CreateSubnet3_01.md)


## 10.5. Heat

![scope](../images/ESI_Sequence_diagram.006.png)

### Outline
Heat has conducted some tasks for "Create Subnet".
As a result, Heat has stored heat-stacks for "Create Subnet".

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet3_01.md)


## 10.6. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json c2c9520b-026d-444a-8db9-c1cb9d71c130
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "10.225.225.254",
                "start": "10.225.225.2"
            }
        ],
        "cidr": "10.225.225.0/24",
        "description": "load_balancer subnet",
        "dhcp_server_address": "10.225.225.2",
        "dns_nameservers": [],
        "enable_dhcp": true,
        "gateway_ip": "10.225.225.1",
        "host_routes": [],
        "id": "c2c9520b-026d-444a-8db9-c1cb9d71c130",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "sample-lb-subnet",
        "network_id": "774acf45-316f-4431-b31b-08770b76d761",
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
$ gohan client port show --output-format json 6b5b32b0-e1fc-430d-9ae0-57306fab7285
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "10.225.225.2",
                "subnet_id": "c2c9520b-026d-444a-8db9-c1cb9d71c130"
            }
        ],
        "id": "6b5b32b0-e1fc-430d-9ae0-57306fab7285",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "774acf45-316f-4431-b31b-08770b76d761",
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
