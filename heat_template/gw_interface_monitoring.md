# monitoring_template: gw_interface_monitoring
This is monitoring_template of "gw_interface_monitoring" which is provided by gohan via etcd

![scope](../images/esi_interface.003.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/gw_interface_monitoring
{
    "body": {
        "handler": "monitoring_worker", 
        "watch": [], 
        "id": "gw_interface_monitoring", 
        "template_file": "primary:\n  type: vrrp_session\n  host: {{ primary_device_ip }}\n  port: {{ primary_device_port }}\n  login: {{ primary_device_login }}\n  password: {{ primary_device_password }}\n  interface: {{ primary_logical_interface_name }}\n  wanted_status: master\n  vrid: {{ vrid }}\n  timeout: 360\nsecondary:\n  type: vrrp_session\n  host: {{ secondary_device_ip }}\n  port: {{ secondary_device_port }}\n  login: {{ secondary_device_login }}\n  password: {{ secondary_device_password }}\n  interface: {{ secondary_logical_interface_name }}\n  wanted_status: backup\n  vrid: {{ vrid }}\n  timeout: 360\ndb_mappings:\n- mapped_id: {{primary_device_ip}}-{{primary_logical_interface_name}}\n  relation: {{service_type}}_primary\n- mapped_id: {{secondary_device_ip}}-{{secondary_logical_interface_name}}\n  relation: {{service_type}}_secondary\n", 
        "parameter_mappings": {
            "secondary_device_password": {
                "field": "password", 
                "path": [
                    {
                        "concatenate": [
                            {
                                "field": "service_type"
                            }, 
                            "_gw_id"
                        ]
                    }, 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "secondary_logical_interface_name": {
                "else_mapping": {
                    "field": "secondary_logical_downlink_interface_name", 
                    "path": [
                        {
                            "concatenate": [
                                {
                                    "field": "service_type"
                                }, 
                                "_gw_id"
                            ]
                        }
                    ]
                }, 
                "if_mapping": {
                    "equal": [
                        {
                            "field": "service_type"
                        }, 
                        "internet"
                    ]
                }, 
                "then_mapping": {
                    "field": "secondary_logical_interface_name", 
                    "path": [
                        {
                            "concatenate": [
                                {
                                    "field": "service_type"
                                }, 
                                "_gw_id"
                            ]
                        }
                    ]
                }
            }, 
            "primary_logical_interface_name": {
                "else_mapping": {
                    "field": "primary_logical_downlink_interface_name", 
                    "path": [
                        {
                            "concatenate": [
                                {
                                    "field": "service_type"
                                }, 
                                "_gw_id"
                            ]
                        }
                    ]
                }, 
                "if_mapping": {
                    "equal": [
                        {
                            "field": "service_type"
                        }, 
                        "internet"
                    ]
                }, 
                "then_mapping": {
                    "field": "primary_logical_interface_name", 
                    "path": [
                        {
                            "concatenate": [
                                {
                                    "field": "service_type"
                                }, 
                                "_gw_id"
                            ]
                        }
                    ]
                }
            }, 
            "vrid": {
                "field": "vrid"
            }, 
            "secondary_device_port": {
                "field": "ssh_port", 
                "path": [
                    {
                        "concatenate": [
                            {
                                "field": "service_type"
                            }, 
                            "_gw_id"
                        ]
                    }, 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "primary_device_ip": {
                "field": "ip", 
                "path": [
                    {
                        "concatenate": [
                            {
                                "field": "service_type"
                            }, 
                            "_gw_id"
                        ]
                    }, 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "primary_device_password": {
                "field": "password", 
                "path": [
                    {
                        "concatenate": [
                            {
                                "field": "service_type"
                            }, 
                            "_gw_id"
                        ]
                    }, 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_login": {
                "field": "login", 
                "path": [
                    {
                        "concatenate": [
                            {
                                "field": "service_type"
                            }, 
                            "_gw_id"
                        ]
                    }, 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "service_type": {
                "field": "service_type"
            }, 
            "primary_device_login": {
                "field": "login", 
                "path": [
                    {
                        "concatenate": [
                            {
                                "field": "service_type"
                            }, 
                            "_gw_id"
                        ]
                    }, 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "primary_device_port": {
                "field": "ssh_port", 
                "path": [
                    {
                        "concatenate": [
                            {
                                "field": "service_type"
                            }, 
                            "_gw_id"
                        ]
                    }, 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_ip": {
                "field": "ip", 
                "path": [
                    {
                        "concatenate": [
                            {
                                "field": "service_type"
                            }, 
                            "_gw_id"
                        ]
                    }, 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }
        }
    }, 
    "version": 1, 
    "marked_for_deletion": false
}
```
You can see the retreiving of "template_file" as "Heat Template".

* vrrp_session

```
primary:
  type: vrrp_session
  host: {{ primary_device_ip }}
  port: {{ primary_device_port }}
  login: {{ primary_device_login }}
  password: {{ primary_device_password }}
  interface: {{ primary_logical_interface_name }}
  wanted_status: master
  vrid: {{ vrid }}
  timeout: 360
secondary:
  type: vrrp_session
  host: {{ secondary_device_ip }}
  port: {{ secondary_device_port }}
  login: {{ secondary_device_login }}
  password: {{ secondary_device_password }}
  interface: {{ secondary_logical_interface_name }}
  wanted_status: backup
  vrid: {{ vrid }}
  timeout: 360
db_mappings:
- mapped_id: {{primary_device_ip}}-{{primary_logical_interface_name}}
  relation: {{service_type}}_primary
- mapped_id: {{secondary_device_ip}}-{{secondary_logical_interface_name}}
  relation: {{service_type}}_secondary
```

### (2) Notes for Code of Monitoring-Worker Plugin in esi-worker
* esi-worker/esi_worker/workers/monitoring_worker/resource_plugins/vrrp_session.py

```
class VRRPSessionPlugin(MonitoringWorkerPlugin):
    TYPE = {
        "vrrp_session": "monitor_igs_interface"
    }

    REQUIRED_PROPS = ['host', 'port', 'login', 'password', 'interface', 'vrid']

    BACKEND_SKIPPED_PROPS = ['wanted_status']

    DEFAULT_PROPS = {
        "wanted_status": "master",
    }

    @staticmethod
    def get_vrrp_info(manager):
        cmd = '<get-vrrp-information></get-vrrp-information>'
        return manager.rpc(cmd)

    def _get_status_once(self, props):
        rpc_timeout = self._worker_conf.getint('monitoring',
                                               'netconf_rpc_timeout')
        client = NCClient(props["host"], props["port"],
                          props["login"], props["password"],
                          rpc_timeout=rpc_timeout)
        logger.debug("Waiting for the VRRP on interface %s with vrid %s"
                     " to start...",
                     props["interface"], props["vrid"])
        try:
            response = client.execute(self.get_vrrp_info, max_retries=1)
        except Exception as e:
            logger.debug(e.message)
            raise ResourcePingException()

        interface = self._get_interface(response, props["interface"],
                                        props["vrid"])
        status = interface.find("vrrp-state").text
        logger.debug(
            "VRRP on {} has status {}".format(props["interface"], status))
        return status

    @staticmethod
    def _retry_on_result(result, params):
        return result != params['wanted_status']

    @staticmethod
    def _get_interface(response, if_name, vrid):
        for interface in response.find('vrrp-information').findall(
                'vrrp-interface'):
            if interface.find("interface").text == if_name and \
               interface.find("group").text == str(vrid):
                return interface
        logger.debug(
            'Interface "{}" with vrid "{}" not found!'.format(if_name, vrid))
        raise ResourcePingException()
```

### (3) Memo for myself ...
