[Return to Previous Page](00_fire_wall.md)

# 10. Clarification of interface in Sequence Diagram "Create Subnet for user-net"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_firewall.011.png)


## 10.1. Stored data in etcd after initinalizing gohan

![scope](../images/ESI_Sequence_diagram.002.png)

These are stored data for "heat_templates" in etcd.

* [Checking stored data for "subnet"](../heat_template/subnet.md)
* [Checking stored data for "port"](../heat_template/port.md)



## 10.2. HTTP Methods for RESTful between Gohan and Client

![scope](../images/ESI_Sequence_diagram.003.png)

This is JSON data for "Create Subnet" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/subnets
```
```
{
    "subnet": {
        "description": "firewall subnet",
        "name": "sample-fw-subnet",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
        "tags": {},
        "ip_version": 4,
        "cidr": "10.98.76.0/24",
        "network_id": "82712b89-c35c-4276-83cb-818860d41f9e"
    }
}
```



## 10.3. Stored data in etcd after receiving HTTP Methods for RESTful

![scope](../images/ESI_Sequence_diagram.004.png)

These are stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/CreateSubnet3_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/CreateSubnet3_02.md)



## 10.4. Stored heat-stack via heat-api

![scope](../images/ESI_Sequence_diagram.005.png)

These are stored heat-stacks for "Create Subnet" in heat-engine.

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet3_01.md)



## 10.5. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json a11785e2-0c2b-4131-9144-349155f958f5
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "10.98.76.254",
                "start": "10.98.76.2"
            }
        ],
        "cidr": "10.98.76.0/24",
        "description": "firewall subnet",
        "dhcp_server_address": "10.98.76.2",
        "dns_nameservers": [],
        "enable_dhcp": true,
        "gateway_ip": "10.98.76.1",
        "host_routes": [],
        "id": "a11785e2-0c2b-4131-9144-349155f958f5",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "sample-fw-subnet",
        "network_id": "82712b89-c35c-4276-83cb-818860d41f9e",
        "ntp_servers": [],
        "orchestration_state": "CREATE_COMPLETE",
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
    }
}
```
* Checking another resources via gohan client
```
$ gohan client port show --output-format json c18705d5-e40a-4bb7-94da-3dc9a93b32e5
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "a11785e2-0c2b-4131-9144-349155f958f5",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "10.98.76.2",
                "subnet_id": "a11785e2-0c2b-4131-9144-349155f958f5"
            }
        ],
        "id": "c18705d5-e40a-4bb7-94da-3dc9a93b32e5",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "82712b89-c35c-4276-83cb-818860d41f9e",
        "operational_state": "",
        "orchestration_state": "SYNC_COMPLETE",
        "security_groups": [],
        "segmentation_id": null,
        "segmentation_type": null,
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099"
    }
}
```

[Return to Previous Page](00_fire_wall.md)
