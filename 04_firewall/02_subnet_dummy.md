[Return to Previous Page](00_fire_wall.md)

# 2. Clarification of interface in Sequence Diagram "Create Subnet for dummy-net"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_firewall.003.png)


## 2.1. Stored data in etcd after initinalizing gohan

![scope](../images/ESI_Sequence_diagram.002.png)

These are stored data for "heat_templates" in etcd.

* [Checking stored data for "subnet"](../heat_template/subnet.md)
* [Checking stored data for "port"](../heat_template/port.md)



## 2.2. HTTP Methods for RESTful between Gohan and Client

![scope](../images/ESI_Sequence_diagram.003.png)

This is JSON data for "Create Subnet" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/subnets
```
```
{
    "subnet": {
        "description": "dummy subnet for firewall",
        "name": "dummy-subnet",
        "tenant_id": "0f40dffa48614d9baa7eaac7e7532099",
        "tags": {},
        "ip_version": 4,
        "cidr": "10.121.232.0/24",
        "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d"
    }
}
```



## 2.3. Stored data in etcd after receiving HTTP Methods for RESTful

![scope](../images/ESI_Sequence_diagram.004.png)

These are stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/CreateSubnet1_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/CreateSubnet1_02.md)



## 2.4. Stored heat-stack via heat-api

![scope](../images/ESI_Sequence_diagram.005.png)

These are stored heat-stacks for "Create Subnet" in heat-engine.

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet1_01.md)



## 2.5. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json 1244d619-cc55-4bb7-b181-606776ba5e88
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "10.121.232.254",
                "start": "10.121.232.2"
            }
        ],
        "cidr": "10.121.232.0/24",
        "description": "dummy subnet for firewall",
        "dhcp_server_address": "10.121.232.2",
        "dns_nameservers": [],
        "enable_dhcp": true,
        "gateway_ip": "10.121.232.1",
        "host_routes": [],
        "id": "1244d619-cc55-4bb7-b181-606776ba5e88",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "dummy-subnet",
        "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d",
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
$ gohan client port show --output-format json db7b07e7-5fb8-4400-9a64-f3b1df8038f2
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "1244d619-cc55-4bb7-b181-606776ba5e88",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "10.121.232.2",
                "subnet_id": "1244d619-cc55-4bb7-b181-606776ba5e88"
            }
        ],
        "id": "db7b07e7-5fb8-4400-9a64-f3b1df8038f2",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "73b2c401-a1f3-49fb-8612-8c755b37a28d",
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
