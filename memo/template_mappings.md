### self.template_mappings

```
{
    "heat_worker": {
        "load_balancer_syslog_server": "Cload_balancer_syslog_server", 
        "aws_interface": "Caws_interface", 
        "static_route": "ACstatic_route_&Pservice_type", 
        "internet_gateway": "Cinternet_gateway", 
        "gcp_gateway": "Cgcp_gateway", 
        "load_balancer_interface": "Cload_balancer_interface", 
        "azure_gateway": "Cazure_gateway", 
        "public_ip": "Cpublic_ip", 
        "ese_logical_port": "Cese_logical_port", 
        "gcp_interface": "Cgcp_interface", 
        "interdc_interface": "Cinterdc_interface", 
        "vpn_gateway": "Cvpn_gateway", 
        "vpn_interface": "Cvpn_interface", 
        "edge_router": "Cedge_router", 
        "ese_device": "ACese_device_&Pexisting", 
        "subnet": "Csubnet", 
        "network": "Cnetwork", 
        "local_subnet": "Cese_logical_port", 
        "er_physical_interface": "Cer_physical_interface", 
        "port": {
            "else_mapping": {
                "constant": "port"
            }, 
            "if_mapping": {
                "regexp": [
                    {
                        "field": "device_owner"
                    }, 
                    {
                        "constant": "network:dhcp|network:empty"
                    }
                ]
            }, 
            "then_mapping": {
                "constant": null
            }
        }, 
        "firewall": "Cfirewall_config", 
        "load_balancer_conf": "Cload_balancer_conf", 
        "load_balancer": "Cload_balancer", 
        "gw_interface": "ACgw_interface_&Pservice_type", 
        "ese_physical_port": "ACese_physical_port_&Pexisting", 
        "firewall_interface": "Cfirewall_interface", 
        "common_function_gateway": "Ccommon_function_gateway", 
        "aws_gateway": "Caws_gateway", 
        "azure_interface": "Cazure_interface", 
        "vnf_instance": "Cvnf_instance", 
        "interdc_gateway": "Cinterdc_gateway"
    }, 
    "monitoring_worker": {}
}
```
