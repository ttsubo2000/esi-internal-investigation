### self._relations
  
```
{
    "load_balancer_syslog_server": {
        "load_balancer_id": "load_balancer"
    }, 
    "aws_interface": {
        "aws_gw_id": "aws_gateway"
    }, 
    "vnf_interface": {
        "network_id": "network", 
        "port_id": "port", 
        "vnf_instance_id": "vnf_instance"
    }, 
    "vpn_interface": {
        "vpn_gw_id": "vpn_gateway"
    }, 
    "billing_resource": {
        "parent_billing_id": "billing_resource"
    }, 
    "public_ip_pool": {
        "ha_router_id": "ha_router", 
        "internet_service_id": "internet_service"
    }, 
    "interdc_service": {}, 
    "gcp_gateway": {
        "downlink_interface_id": "ha_interface", 
        "gcp_service_id": "gcp_service", 
        "qos_option_id": "qos_option", 
        "uplink_interface_id": "ha_interface"
    }, 
    "load_balancer_interface": {
        "network_id": "network", 
        "vnf_interface_id": "vnf_interface", 
        "load_balancer_id": "load_balancer"
    }, 
    "azure_gateway": {
        "downlink_interface_id": "ha_interface", 
        "azure_service_id": "azure_service", 
        "uplink_interface_id": "ha_interface", 
        "qos_option_id": "qos_option"
    }, 
    "public_ip": {
        "ip_pool_id": "public_ip_pool", 
        "suspended_public_ip_id": "suspended_public_ip", 
        "internet_gw_id": "internet_gateway"
    }, 
    "ese_logical_port": {
        "network_id": "network", 
        "ese_physical_port_id": "ese_physical_port"
    }, 
    "gcp_interface": {
        "gcp_gw_id": "gcp_gateway"
    }, 
    "interdc_interface": {
        "interdc_gw_id": "interdc_gateway"
    }, 
    "common_function_pool": {}, 
    "vpn_gateway": {
        "downlink_interface_id": "ha_interface", 
        "vpn_service_id": "vpn_service", 
        "uplink_interface_id": "ha_interface", 
        "qos_option_id": "qos_option"
    }, 
    "static_route": {
        "interdc_gw_id": "interdc_gateway", 
        "internet_gw_id": "internet_gateway", 
        "gcp_gw_id": "gcp_gateway", 
        "vpn_gw_id": "vpn_gateway", 
        "azure_gw_id": "azure_gateway", 
        "public_ip_id": "public_ip", 
        "aws_gw_id": "aws_gateway"
    }, 
    "qos_option": {
        "vpn_service_id": "vpn_service", 
        "aws_service_id": "aws_service", 
        "internet_service_id": "internet_service", 
        "interdc_service_id": "interdc_service", 
        "gcp_service_id": "gcp_service", 
        "ha_router_id": "ha_router", 
        "azure_service_id": "azure_service"
    }, 
    "colocation_space": {}, 
    "port": {
        "network_id": "network"
    }, 
    "physical_port": {}, 
    "ese_device": {
        "location": "location"
    }, 
    "subnet": {
        "network_id": "network"
    }, 
    "common_function_gateway": {
        "downlink_interface_id": "ha_interface", 
        "common_function_pool_id": "common_function_pool"
    }, 
    "load_balancer_plan": {
        "vnf_template_id": "vnf_template", 
        "vnf_plan_id": "vnf_plan"
    }, 
    "monitoring": {}, 
    "network": {}, 
    "local_subnet": {
        "ese_logical_port_id": "ese_logical_port", 
        "network_id": "network"
    }, 
    "suspended_public_ip": {
        "ip_pool_id": "public_ip_pool"
    }, 
    "er_physical_interface": {
        "connected_ese_port_id": "ese_physical_port", 
        "device_id": "edge_router"
    }, 
    "namespace": {}, 
    "tenant_connection": {}, 
    "event": {}, 
    "hosting_physical_link": {
        "type_b_physical_port_id": "physical_port", 
        "type_a_physical_port_id": "physical_port", 
        "type_b_ese_physical_port_id": "ese_physical_port", 
        "type_a_ese_physical_port_id": "ese_physical_port", 
        "colocation_space_id": "colocation_space"
    }, 
    "internet_gateway": {
        "downlink_interface_id": "ha_interface", 
        "associated_uplink_id": "ha_interface", 
        "internet_service_id": "internet_service", 
        "qos_option_id": "qos_option"
    }, 
    "edge_router": {}, 
    "aws_service": {}, 
    "reserve_address": {}, 
    "policy": {}, 
    "billing_usage": {
        "tenant_id": "tenant"
    }, 
    "location": {}, 
    "load_balancer": {
        "vnf_instance_id": "vnf_instance", 
        "load_balancer_plan_id": "load_balancer_plan", 
        "load_balancer_conf_id": "load_balancer_conf"
    }, 
    "gw_interface": {
        "interdc_gw_id": "interdc_gateway", 
        "network_id": "network", 
        "internet_gw_id": "internet_gateway", 
        "gcp_gw_id": "gcp_gateway", 
        "aws_gw_id": "aws_gateway", 
        "azure_gw_id": "azure_gateway", 
        "public_ip_id": "public_ip", 
        "vpn_gw_id": "vpn_gateway"
    }, 
    "vnf_plan": {}, 
    "gcp_service": {}, 
    "colocation_logical_link": {
        "network_id": "network", 
        "type_a_port_id": "port", 
        "colocation_physical_link_id": "colocation_physical_link", 
        "type_b_port_id": "port"
    }, 
    "quota": {}, 
    "load_balancer_conf": {
        "load_balancer_plan_id": "load_balancer_plan", 
        "vnf_instance_id": "vnf_instance"
    }, 
    "firewall_plan": {
        "vnf_template_id": "vnf_template", 
        "vnf_plan_id": "vnf_plan"
    }, 
    "nat_ip_pool": {
        "ha_router_id": "ha_router", 
        "common_function_pool_id": "common_function_pool"
    }, 
    "ese_physical_port": {
        "ese_device_id": "ese_device"
    }, 
    "monitoring_history": {}, 
    "neutron_extension": {}, 
    "vnf_template": {}, 
    "ha_router": {
        "primary_router_id": "edge_router", 
        "secondary_router_id": "edge_router"
    }, 
    "tenant": {}, 
    "hosting_logical_link": {
        "network_id": "network", 
        "type_a_port_id": "port", 
        "type_b_port_id": "port", 
        "hosting_physical_link_id": "hosting_physical_link"
    }, 
    "colocation_physical_link": {
        "type_b_physical_port_id": "physical_port", 
        "type_a_physical_port_id": "physical_port", 
        "type_b_ese_physical_port_id": "ese_physical_port", 
        "type_a_ese_physical_port_id": "ese_physical_port", 
        "colocation_space_id": "colocation_space"
    }, 
    "aws_gateway": {
        "downlink_interface_id": "ha_interface", 
        "qos_option_id": "qos_option", 
        "uplink_interface_id": "ha_interface", 
        "aws_service_id": "aws_service"
    }, 
    "azure_service": {}, 
    "azure_interface": {
        "azure_gw_id": "azure_gateway"
    }, 
    "extension": {}, 
    "ha_interface": {
        "ha_router_id": "ha_router", 
        "primary_interface_id": "er_physical_interface", 
        "secondary_interface_id": "er_physical_interface"
    }, 
    "firewall": {
        "firewall_plan_id": "firewall_plan", 
        "vnf_instance_id": "vnf_instance"
    }, 
    "vpn_service": {}, 
    "server": {}, 
    "worker_data": {}, 
    "vnf_instance": {
        "vnf_template_id": "vnf_template", 
        "vnf_plan_id": "vnf_plan"
    }, 
    "security_group": {}, 
    "interdc_gateway": {
        "downlink_interface_id": "ha_interface", 
        "uplink_interface_id": "ha_interface", 
        "interdc_service_id": "interdc_service", 
        "qos_option_id": "qos_option"
    }, 
    "heat_template": {}, 
    "schema": {}, 
    "firewall_interface": {
        "network_id": "network", 
        "firewall_id": "firewall", 
        "vnf_interface_id": "vnf_interface"
    }, 
    "common_function": {
        "ha_router_id": "ha_router", 
        "common_function_pool_id": "common_function_pool"
    }, 
    "internet_service": {}
}
```
