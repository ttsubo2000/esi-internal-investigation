What's etcd_store
==========
etcdで保持しているstore dataを可視化するツールです

使い方
==========
### etcdのstore dataを、dumpします

	$ python etcd_store.py -i etcd-server -p 2379 -f test.dump store


### etcdのdumpファイル内で保持しているキー情報の一覧を確認します

	$ python etcd_store.py -f test.dump lsr

	/gohan/cluster/sync
	/state/common/v1.0/tenants/4b666935e57f4cfcad57249ff1768ffd
	/state/common/v1.0/tenants/a367ed245222497db761a6c0becacab0
	/state/v2.0/reserve_addresses/default
	/state/v2.0/subnets/9b780c04-1848-4577-8f94-9dd3629c4a36
	/state/v2.0/subnets/e8746b84-4406-4b5c-a262-bf728877cfca

	... (snip)

	/config/v2.0/networks/3c466256-abb8-4c2a-a17e-79ff0020e81e
	/config/v2.0/networks/c8f6b5e3-05db-430d-aaec-cb80c5388d95
	/config/v2.0/networks/bf720013-ba37-4e57-9ff1-bd9abf6df077

	... (snip)

	/config/v2.0/heat_stacks/network:222ea63f-fb6f-41d8-90c5-b6aaf91d8e65
	/config/v2.0/heat_stacks/subnet:e8746b84-4406-4b5c-a262-bf728877cfca
	/config/v2.0/heat_stacks/port:25985d45-3b45-41ea-9b89-d9e6d87721db
	/config/v2.0/heat_stacks/network:542fb99d-c873-424b-96a3-c7af49605d05
	/config/v2.0/heat_templates/static_route_internet
	/config/v2.0/heat_templates/internet_gateway
	/config/v2.0/heat_templates/vpn_gateway_monitoring
	/config/v2.0/heat_templates/port
	/config/v2.0/heat_templates/public_ip
	/config/v2.0/heat_templates/vpn_gateway
	/config/v2.0/heat_templates/qos_option_vpn
	/config/v2.0/heat_templates/qos_option_internet
	/config/v2.0/heat_templates/ese_logical_port_monitoring
	/config/v2.0/heat_templates/gw_interface_internet
	/config/v2.0/heat_templates/vpn_interface_monitoring
	/config/v2.0/heat_templates/ese_physical_port_monitoring	


### dumpしたデータを閲覧します

## (1) 通常のstore dataを閲覧する場合

python etcd_store.py -f test.dump get < full-path>をを指定します

Example 1: "/gohan/cluster/sync"を確認する

	$ python etcd_store.py -f test.dump get /gohan/cluster/sync
	"esi-f03-030adbe7ea-ce48-4e5d-8c58-fbb35b0c9b49"


Example 2: "/state/v2.0/subnets/9b780c04-1848-4577-8f94-9dd3629c4a36"を確認する

	$ python etcd_store.py -f test.dump get /state/v2.0/subnets/9b780c04-1848-4577-8f94-9dd3629c4a36
	{
	    "state": {
	        "worker_state": "ACTIVE", 
	        "error": null
	    }, 
	    "version": -1
	}


## (2) heat_stack関連のstore dataを閲覧する場合

python etcd_store.py -f test.dump get_stack < full-path>をを指定します

Example 3: "/config/v2.0/heat_stacks/network:222ea63f-fb6f-41d8-90c5-b6aaf91d8e65"を確認する

	$ python etcd_store.py -f test.dump get_stack /config/v2.0/heat_stacks/network:222ea63f-fb6f-41d8-90c5-b6aaf91d8e65
	{
	    "body": {
	        "output": [], 
	        "stack_id": "", 
	        "tenant_id": "a367ed245222497db761a6c0becacab0", 
	        "last_index": 0, 
	        "stack_status": "DELETE_COMPLETE", 
	        "input": {
	            "tenant_id": "a367ed245222497db761a6c0becacab0", 
	            "id": "222ea63f-fb6f-41d8-90c5-b6aaf91d8e65"
	        }, 
	        "status_reason": "", 
	        "id": "network:222ea63f-fb6f-41d8-90c5-b6aaf91d8e65"
	    }, 
	    "version": 0
	}


Example 4: "/config/v2.0/heat_templates/port"を確認する

	$ python etcd_store.py -f test.dump get_stack /config/v2.0/heat_templates/port
	-------- [template_file] -------
	heat_template_version: 2013-05-23

	description: >
	  Virtual Machine Interface Template

	parameters:
	  uuid:
	    type: string
	    label: Backend Virtual Machine Interface UUID
	    description: A unique id for the Virtual Machine Interface.
	  name:
	    type: string
	    label: Physical Interface ID
	    description: A unique id for the Physical Interface.
	  virtual_machine_interface_allowed_address_pairs:
	    type: json
	    label: Virtual machine interface allowed address pairs.
	  virtual_machine_interface_mac_address:
	    type: string
	    default: "fe:ff:ff:ff:ff:ff"
	    label: Virtual machine interface mac address.
	  virtual_network:
	    type: string
	    label: Virtual Network.
	  virtual_machine:
	    type: string
	    label: Virtual Machine.
	    default: ""
	  device_owner:
	    type: string
	    label: Device Owner
	    default: ""
	  admin_state_up:
	    type: boolean
	    label: Admin state up
	    default: true

	resources:
	  virtual_machine_interface:
	    type: OS::Contrail::VirtualMachineInterface
	    properties:
	      uuid: { get_param: uuid }
	      name: { get_param: name }
	      virtual_machine_interface_allowed_address_pairs: { get_param: virtual_machine_interface_allowed_address_pairs }
	      virtual_machine_interface_mac_addresses: [ { get_param: virtual_machine_interface_mac_address } ]
	      virtual_networks: [ { get_param: virtual_network } ]
	      virtual_machine: { get_param: virtual_machine }
	      device_owner: { get_param: device_owner }
	      admin_state_up: { get_param: admin_state_up }

	{% for fixed_ip in jinja_fixed_ips %}
	{% set instance_ip_id = 'instance_ip_' + (loop.index0|string) %}
	  {{ instance_ip_id }}:
	    type: OS::Contrail::InstanceIp
	    properties:
	      name:
	        str_replace:
	          template: '%name%_%zone%_%ip%'
	          params:
	            "%name%": { get_param: name }
	            "%zone%": {{ fixed_ip.subnet_id }}
	            "%ip%": {{ fixed_ip.ip_address }}
	      ip_address: {{ fixed_ip.ip_address }}
	      subnet_id: {{ jinja_subnets[loop.index0] }}
	      network_id: { get_param: virtual_network }
	      virtual_machine_interfaces: [ { get_resource: virtual_machine_interface } ]
	{% endfor %}

	outputs:
	  id:
	    description: A unique id for the virtual machine interface.
	    value: { get_resource: virtual_machine_interface }
	  mac_address:
	    description: Virtual machine interface mac address.
	    value: { get_attr: [virtual_machine_interface, virtual_machine_interface_mac_addresses] }
	  allowed_address_pairs:
	    description: Virtual machine allowed address pairs.
	    value: { get_attr: [virtual_machine_interface, virtual_machine_interface_allowed_address_pairs] }
	  virtual_network:
	    description: Virtual network.
	    value: { get_attr: [virtual_machine_interface, virtual_networks] }
	  fq_name:
	    description: Fully Qualified Name of the VMI
	    value: { get_attr: [virtual_machine_interface, fq_name] }

	-------- [template_file] -------
	{
	    "body": {
	        "handler": "heat_worker", 
	        "watch": [], 
	        "id": "port", 
	        "template_file": "... snip (Please check the above)", 
	        "parameter_mappings": {
	            "virtual_machine": "Pdevice_id", 
	            "uuid": "Pid", 
	            "admin_state_up": "Padmin_state_up", 
	            "virtual_machine_interface_allowed_address_pairs": "Pallowed_address_pairs", 
	            "virtual_machine_interface_mac_address": "Pmac_address", 
	            "device_owner": "Pdevice_owner", 
	            "jinja_fixed_ips": "Pfixed_ips", 
	            "virtual_network": "Mnetwork:network_id:id", 
	            "jinja_subnets": {
	                "for_mapping": {
	                    "path": [
	                        {
	                            "type": "subnet", 
	                            "id": "subnet_id"
	                        }
	                    ], 
	                    "output_key": "id"
	                }, 
	                "for_field": "fixed_ips"
	            }, 
	            "name": "Pid"
	        }
	    }, 
	    "version": 0
	}
