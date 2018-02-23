[Return to Previous Page](00_internet_gateway.md)

# 13. Clarification of interface in Sequence Diagram "Create Subnet"
You can see the relations of "Subnet" as following.

![Subnet](resource/gohan_investigate_for_inetgw.014.png)

## 13.1. Sequence Diagram between gohan and etcd
This is a diagram that has been described as interfaces for "Subnet" between gohan and etcd.

* Initinalizing gohan ...
* Receiving HTTP Methods for Creating Resource ...

![Create Subnet](diag/ESI_Sequence_Diagram_for_Internet_Gateway.016.png)

## 13.2. Stored data in etcd after initinalizing gohan
These are stored data for "heat_templates" in etcd.

* [Checking stored data for "subnet"](../heat_template/subnet.md)
* [Checking stored data for "port"](../heat_template/port.md)
* [Checking stored data for "port_monitoring"](../heat_template/port_monitoring.md)

## 13.3. HTTP Methods for RESTful between Gohan and Client
This is JSON data for "Create Subnet" in HTTP Methods from client.

* Checking JSON data at post method
```
POST /v2.0/subnets
```
```
{
    "subnet": {
        "description": "Sample Subnet",
        "name": "sample-subnet",
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f",
        "tags": {},
        "ip_version": 4,
        "cidr": "172.16.101.0/24",
        "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0"
    }
}
```
![scope](../images/esi_interface.004.png)


## 13.4. Stored data in etcd after receiving HTTP Methods for RESTful
These are stored data for "Create Subnet" in etcd.

* [Checking stored data for creating "subnet"](stored_in_etcd/CreateSubnet_01.md)
* [Checking stored data for creating "port(dhcp)"](stored_in_etcd/CreateSubnet_02.md)

![scope](../images/esi_interface.005.png)


## 13.5. Stored heat-stack via heat-api
These are stored heat-stacks for "Create Subnet" in heat-engine.

* [Checking heat-stack of "subnet"](heat-stack/CreateSubnet_01.md)

![scope](../images/esi_interface.006.png)


## 13.6. Stored resource in gohan
As a result, checking resources regarding of "Subnet" in gohan.

* Checking the target of resources via gohan client
```
$ gohan client subnet show --output-format json a510f785-7758-4ce5-8fd4-c107d11b8e40
{
    "subnet": {
        "allocation_pools": [
            {
                "end": "172.16.101.254",
                "start": "172.16.101.2"
            }
        ],
        "cidr": "172.16.101.0/24",
        "description": "Sample Subnet",
        "dhcp_server_address": "172.16.101.2",
        "dns_nameservers": [],
        "enable_dhcp": true,
        "gateway_ip": "172.16.101.1",
        "host_routes": [],
        "id": "a510f785-7758-4ce5-8fd4-c107d11b8e40",
        "ip_version": 4,
        "ipv6_address_mode": null,
        "ipv6_ra_mode": null,
        "name": "sample-subnet",
        "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",
        "ntp_servers": [],
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
    }
}
```
* Checking another resources via gohan client
```
$ gohan client port show --output-format json 0cd64eb2-32e8-4069-b5e4-9b718aa61b76
{
    "port": {
        "admin_state_up": true,
        "allowed_address_pairs": [],
        "attached": false,
        "binding:vif_type": "vrouter",
        "description": "DHCP Server Port",
        "device_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40",
        "device_owner": "network:dhcp",
        "ese_logical_port_id": null,
        "fake_delete": false,
        "fixed_ips": [
            {
                "ip_address": "172.16.101.2",
                "subnet_id": "a510f785-7758-4ce5-8fd4-c107d11b8e40"
            }
        ],
        "id": "0cd64eb2-32e8-4069-b5e4-9b718aa61b76",
        "mac_address": "00:00:5e:00:01:00",
        "managed_by_service": false,
        "name": "dhcp-server-port",
        "network_id": "52d7bef8-aa17-45c3-b63e-6a0e504603f0",
        "segmentation_id": null,
        "segmentation_type": null,
        "status": "ACTIVE",
        "tags": {},
        "tenant_id": "0b576f6f4cbf414f829cd12f008bf08f"
    }
}
```

[Return to Previous Page](00_internet_gateway.md)
