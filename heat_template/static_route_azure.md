# heat_template: static_route_azure
This is heat_template of "static_route_azure" which is provided by gohan via etcd

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/static_route_azure
{
    "body": {
        "handler": "heat_worker", 
        "watch": [], 
        "id": "static_route_azure", 
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  AZURE Gateway Static Route\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n    hidden: true\n  vrf_name:\n    description: Name of VRF to add this static route\n    label: VRF\n    type: string\n  route:\n    description: Static Route definition\n    label: Route\n    type: string\n  next_hop:\n    description: Next hop for the static route\n    label: Next hop\n    type: string\n\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    type: OS::Contrail::NetconfNamedConfigs\n    {% if device == \"secondary\" %}depends_on: netconf_configure_primary{% endif %}\n    properties:\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n      lock_timeout: 3000\n      configs:\n      - config:\n          str_replace:\n            params:\n              $NEXT_HOP:\n                get_param: next_hop\n            template: |\n              next-hop $NEXT_HOP;\n        path:\n          - config_type: tag\n            xml_type: tag\n            tag: routing-instances\n          - config_type: name\n            xml_type: named_tag\n            tag: instance\n            name: { get_param: vrf_name }\n          - config_type: tag\n            xml_type: tag\n            tag: routing-options\n          - config_type: tag\n            xml_type: tag\n            tag: static\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: route\n            name: { get_param: route }\n{% endfor %}\n", 
        "parameter_mappings": {
            "secondary_device_password": "Fazure_gateway+azure_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:password", 
            "route": "Pdestination", 
            "primary_device_password": "Fazure_gateway+azure_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:password", 
            "secondary_device_port": "Fazure_gateway+azure_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ssh_port", 
            "primary_device_ip": "Fazure_gateway+azure_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ip", 
            "heat_timeout": "C60", 
            "next_hop": "Pnexthop", 
            "vrf_name": "Fazure_gateway+azure_gw_id:vrf_name", 
            "primary_device_username": "Fazure_gateway+azure_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:login", 
            "primary_device_port": "Fazure_gateway+azure_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+primary_router_id:ssh_port", 
            "secondary_device_ip": "Fazure_gateway+azure_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:ip", 
            "secondary_device_username": "Fazure_gateway+azure_gw_id:ha_interface+downlink_interface_id:ha_router+ha_router_id:edge_router+secondary_router_id:login"
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* OS::Contrail::NetconfNamedConfigs

```
heat_template_version: 2013-05-23

description: >
  AZURE Gateway Static Route

parameters:
  primary_device_ip:
    description: Ip address that will be used to establish ssh connection to the Primary Device.
    label: Ip address of the device.
    type: string
  primary_device_port:
    description: Port that will be used to establish ssh connection to the Primary Device.
    label: Port of the ssh connection.
    type: number
  primary_device_username:
    description: Name of the user which will be used to log onto the Primary Device.
    label: User name to log on to device.
    type: string
  primary_device_password:
    description: Password of the user which will be used to log onto the Primary Device.
    label: Users password.
    type: string
    hidden: true
  secondary_device_ip:
    description: Ip address that will be used to establish ssh connection to the Secondary Device.
    label: Ip address of the device.
    type: string
  secondary_device_port:
    description: Port that will be used to establish ssh connection to the Secondary Device.
    label: Port of the ssh connection.
    type: number
  secondary_device_username:
    description: Name of the user which will be used to log onto the Secondary Device.
    label: User name to log on to device.
    type: string
  secondary_device_password:
    description: Password of the user which will be used to log onto the Secondary Device.
    label: Users password.
    type: string
    hidden: true
  vrf_name:
    description: Name of VRF to add this static route
    label: VRF
    type: string
  route:
    description: Static Route definition
    label: Route
    type: string
  next_hop:
    description: Next hop for the static route
    label: Next hop
    type: string

resources:
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    type: OS::Contrail::NetconfNamedConfigs
    {% if device == "secondary" %}depends_on: netconf_configure_primary{% endif %}
    properties:
      device_ip:
        get_param: {{ device }}_device_ip
      password:
        get_param: {{ device }}_device_password
      port:
        get_param: {{ device }}_device_port
      username:
        get_param: {{ device }}_device_username
      lock_timeout: 3000
      configs:
      - config:
          str_replace:
            params:
              $NEXT_HOP:
                get_param: next_hop
            template: |
              next-hop $NEXT_HOP;
        path:
          - config_type: tag
            xml_type: tag
            tag: routing-instances
          - config_type: name
            xml_type: named_tag
            tag: instance
            name: { get_param: vrf_name }
          - config_type: tag
            xml_type: tag
            tag: routing-options
          - config_type: tag
            xml_type: tag
            tag: static
          - config_type: named_tag
            xml_type: named_tag
            tag: route
            name: { get_param: route }
{% endfor %}
```
