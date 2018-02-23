# heat_template: interdc_interface
This is heat_template of "interdc_interface" which is provided by gohan via etcd

![scope](../images/esi_interface.002.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/interdc_interface
{
    "body": {
        "handler": "heat_worker", 
        "watch": [], 
        "id": "interdc_interface", 
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Interdc Interface\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n  primary_device_physical_interface:\n    description: MX physical port on which logical interface will be created\n    label: Underlying physical interface\n    type: string\n  primary_device_downlink_physical_interface:\n    description: MX physical port on which logical downlink interface will be created\n    label: Underlying physical interface\n    type: string\n  secondary_device_physical_interface:\n    description: MX physical port on which logical interface will be created\n    label: Underlying physical interface\n    type: string\n  secondary_device_downlink_physical_interface:\n    description: MX physical port on which downlink logical interface will be created\n    label: Underlying physical interface\n    type: string\n  primary_device_gw_ip:\n    description: IP on primary device\n    label: Inet Address CIDR\n    type: string\n  secondary_device_gw_ip:\n    description: IP on secondary device\n    label: Inet Address CIDR\n    type: string\n  primary_device_priority:\n    type: string\n    label: Primary device priority\n  secondary_device_priority:\n    type: string\n    label: Secondary device priority\n  vrf_name:\n    description: Name of VRF (routing-instance) in MX config\n    label: VRF Name\n    type: string\n  netmask:\n    description: Netmask for gw_ip\n    label: Netmask\n    type: number\n  uplink_vlan_id:\n    description: VLAN ID used on uplink interfaces (same for both primary and secondary device)\n    label: Uplink VLAN ID\n    type: string\n  downlink_vlan_id:\n    description: VLAN ID used on downlink interfaces (same for both primary and secondary device)\n    label: Downlink VLAN ID\n    type: string\n  gw_vip:\n    description: Virtual IP configured on VRRP\n    label: Inet Address CIDR\n    type: string\n  primary_device_gw_ip:\n    description: IP on primary device\n    label: Inet Address CIDR\n    type: string\n  secondary_device_gw_ip:\n    description: IP on secondary device\n    label: Inet Address CIDR\n    type: string\n  vrrp_group:\n    type: string\n    label: VRRP Group\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    type: OS::Contrail::NetconfNamedConfigs\n    properties:\n      lock_timeout: 3000\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n      configs:\n      - config:\n          str_replace:\n            params:\n              $VRRP_GROUP:\n                get_param: vrrp_group\n              $VIP:\n                get_param: gw_vip\n              $PRIORITY:\n                get_param: {{ device }}_device_priority\n              $DOWNLINK_IF:\n                get_param: secondary_device_downlink_physical_interface\n              $DOWNLINK_VLAN_ID:\n                get_param: downlink_vlan_id\n            template: |\n              vrrp-group $VRRP_GROUP {\n                virtual-address $VIP;\n                priority $PRIORITY;\n                track {\n                  interface $DOWNLINK_IF.$DOWNLINK_VLAN_ID {\n                    priority-cost 10;\n                  }\n                }\n              }\n        path:\n        - config_type: tag\n          xml_type: tag\n          tag: interfaces\n        - config_type: name\n          xml_type: named_tag\n          tag: interface\n          name: { get_param: {{ device }}_device_physical_interface }\n        - config_type: named_tag\n          xml_type: named_tag\n          tag: unit\n          name: { get_param: uplink_vlan_id }\n        - config_type: tag\n          xml_type: tag\n          tag: family\n        - config_type: tag\n          xml_type: tag\n          tag: inet\n        - config_type: named_tag\n          xml_type: named_tag\n          tag: address\n          name:\n            str_replace:\n              params:\n                $DEVICE_IP:\n                  get_param: {{ device }}_device_gw_ip\n                $NETMASK:\n                  get_param: netmask\n              template: |\n                $DEVICE_IP/$NETMASK\n{% endfor %}\n", 
        "parameter_mappings": {
            "secondary_device_physical_interface": {
                "field": "name", 
                "path": [
                    "interdc_gw_id", 
                    "interdc_service_id", 
                    "uplink_interface_id", 
                    "secondary_interface_id"
                ]
            }, 
            "primary_device_password": {
                "field": "password", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_gw_ip": {
                "field": "secondary_ipv4"
            }, 
            "primary_device_downlink_physical_interface": {
                "field": "name", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "primary_interface_id"
                ]
            }, 
            "gw_vip": {
                "field": "gw_vipv4"
            }, 
            "primary_device_ip": {
                "field": "ip", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_username": {
                "field": "login", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "downlink_vlan_id": {
                "field": "downlink_vlan_id", 
                "path": [
                    "interdc_gw_id"
                ]
            }, 
            "primary_device_physical_interface": {
                "field": "name", 
                "path": [
                    "interdc_gw_id", 
                    "interdc_service_id", 
                    "uplink_interface_id", 
                    "primary_interface_id"
                ]
            }, 
            "netmask": {
                "field": "netmask"
            }, 
            "secondary_device_downlink_physical_interface": {
                "field": "name", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "secondary_interface_id"
                ]
            }, 
            "primary_device_gw_ip": {
                "field": "primary_ipv4"
            }, 
            "vrrp_group": {
                "field": "vrid"
            }, 
            "primary_device_priority": {
                "constant": 105
            }, 
            "secondary_device_port": {
                "field": "ssh_port", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "secondary_device_password": {
                "field": "password", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "uplink_vlan_id": {
                "field": "uplink_vlan_id", 
                "path": [
                    "interdc_gw_id"
                ]
            }, 
            "heat_timeout": {
                "constant": 60
            }, 
            "vrf_name": {
                "field": "vrf_name", 
                "path": [
                    "interdc_gw_id"
                ]
            }, 
            "primary_device_username": {
                "field": "login", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_priority": {
                "constant": 100
            }, 
            "primary_device_port": {
                "field": "ssh_port", 
                "path": [
                    "interdc_gw_id", 
                    "downlink_interface_id", 
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_ip": {
                "field": "ip", 
                "path": [
                    "interdc_gw_id", 
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

* OS::Contrail::NetconfNamedConfigs

```
heat_template_version: 2013-05-23

description: >
  Interdc Interface

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
  primary_device_physical_interface:
    description: MX physical port on which logical interface will be created
    label: Underlying physical interface
    type: string
  primary_device_downlink_physical_interface:
    description: MX physical port on which logical downlink interface will be created
    label: Underlying physical interface
    type: string
  secondary_device_physical_interface:
    description: MX physical port on which logical interface will be created
    label: Underlying physical interface
    type: string
  secondary_device_downlink_physical_interface:
    description: MX physical port on which downlink logical interface will be created
    label: Underlying physical interface
    type: string
  primary_device_gw_ip:
    description: IP on primary device
    label: Inet Address CIDR
    type: string
  secondary_device_gw_ip:
    description: IP on secondary device
    label: Inet Address CIDR
    type: string
  primary_device_priority:
    type: string
    label: Primary device priority
  secondary_device_priority:
    type: string
    label: Secondary device priority
  vrf_name:
    description: Name of VRF (routing-instance) in MX config
    label: VRF Name
    type: string
  netmask:
    description: Netmask for gw_ip
    label: Netmask
    type: number
  uplink_vlan_id:
    description: VLAN ID used on uplink interfaces (same for both primary and secondary device)
    label: Uplink VLAN ID
    type: string
  downlink_vlan_id:
    description: VLAN ID used on downlink interfaces (same for both primary and secondary device)
    label: Downlink VLAN ID
    type: string
  gw_vip:
    description: Virtual IP configured on VRRP
    label: Inet Address CIDR
    type: string
  primary_device_gw_ip:
    description: IP on primary device
    label: Inet Address CIDR
    type: string
  secondary_device_gw_ip:
    description: IP on secondary device
    label: Inet Address CIDR
    type: string
  vrrp_group:
    type: string
    label: VRRP Group
resources:
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    type: OS::Contrail::NetconfNamedConfigs
    properties:
      lock_timeout: 3000
      device_ip:
        get_param: {{ device }}_device_ip
      password:
        get_param: {{ device }}_device_password
      port:
        get_param: {{ device }}_device_port
      username:
        get_param: {{ device }}_device_username
      configs:
      - config:
          str_replace:
            params:
              $VRRP_GROUP:
                get_param: vrrp_group
              $VIP:
                get_param: gw_vip
              $PRIORITY:
                get_param: {{ device }}_device_priority
              $DOWNLINK_IF:
                get_param: secondary_device_downlink_physical_interface
              $DOWNLINK_VLAN_ID:
                get_param: downlink_vlan_id
            template: |
              vrrp-group $VRRP_GROUP {
                virtual-address $VIP;
                priority $PRIORITY;
                track {
                  interface $DOWNLINK_IF.$DOWNLINK_VLAN_ID {
                    priority-cost 10;
                  }
                }
              }
        path:
        - config_type: tag
          xml_type: tag
          tag: interfaces
        - config_type: name
          xml_type: named_tag
          tag: interface
          name: { get_param: {{ device }}_device_physical_interface }
        - config_type: named_tag
          xml_type: named_tag
          tag: unit
          name: { get_param: uplink_vlan_id }
        - config_type: tag
          xml_type: tag
          tag: family
        - config_type: tag
          xml_type: tag
          tag: inet
        - config_type: named_tag
          xml_type: named_tag
          tag: address
          name:
            str_replace:
              params:
                $DEVICE_IP:
                  get_param: {{ device }}_device_gw_ip
                $NETMASK:
                  get_param: netmask
              template: |
                $DEVICE_IP/$NETMASK
{% endfor %}
```

### (2) Notes for Code of Heat Plugin in contrail-heat
* contrail-heat/contrail_heat/resources/netconf_named.py

```
class ContrailNetconfNamedConfigs(netconf.ContrailNetconf):

    ConfigEntity = collections.namedtuple('ConfigEntity',
                                          'path config')

    PROPERTIES = (
        DEVICE_IP, USERNAME, PASSWORD, PORT, CONFIGS, ON_UPDATE, LOCK_TIMEOUT
    ) = (
        'device_ip', 'username', 'password', 'port', 'configs', 'on_update',
        'lock_timeout'
    )

    CONFIG_KEYS = (PATH, CONFIG, ADDITIONAL_COMMANDS) = (
        'path', 'config', 'additional_commands')

    PATH_KEYS = (
        CONFIG_TYPE, XML_TYPE, TAG, NAME
    ) = (
        "config_type", "xml_type", "tag", "name",
    )

    path_schema = properties.Schema(
        properties.Schema.MAP,
        schema={
            CONFIG_TYPE: properties.Schema(
                properties.Schema.STRING,
                _('Type of node in juniper cli format'),
                constraints=[
                    constraints.AllowedValues(['tag', 'named_tag', 'name']),
                ],
                default='tag'
            ),
            XML_TYPE: properties.Schema(
                properties.Schema.STRING,
                _('Type of node in netconf xml'),
                constraints=[
                    constraints.AllowedValues(['tag', 'named_tag']),
                ],
                default='tag'
            ),
            TAG: properties.Schema(
                properties.Schema.STRING,
                _('Tag value for path'),
                default=''
            ),
            NAME: properties.Schema(
                properties.Schema.STRING,
                _('Name value for path'),
                default=''
            ),
        })

    properties_schema = {
        DEVICE_IP: properties.Schema(
            properties.Schema.STRING,
            _('Ip address of the device.'),
            required=True,
        ),
        USERNAME: properties.Schema(
            properties.Schema.STRING,
            _('User name to log on to device.'),
            required=True,
            update_allowed=True
        ),
        PASSWORD: properties.Schema(
            properties.Schema.STRING,
            _('Users password.'),
            required=True,
            update_allowed=True
        ),
        PORT: properties.Schema(
            properties.Schema.INTEGER,
            _('Port of the ssh connection.'),
            default=22,
            update_allowed=True
        ),
        ON_UPDATE: properties.Schema(
            properties.Schema.STRING,
            _("JUNOS action run on update. "
              "Default action is to delete old config "
              "and apply new. "
              "Rest of them are action passed to netconf as "
              "action parameter on load_configuration."),
            constraints=[
                constraints.AllowedValues(
                    ['delete-and-create', 'merge', 'override',
                     'replace', 'update']),
            ],
            default='delete-and-create',
            update_allowed=False
        ),
        CONFIGS: properties.Schema(
            properties.Schema.LIST,
            _('A list of named config entities (ex. interfaces, '
              'routing-policies, etc.)'),
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    PATH: properties.Schema(
                        properties.Schema.LIST,
                        _('Path of config in config tree.'),
                        required=True,
                        schema=path_schema,
                        update_allowed=False,
                    ),
                    CONFIG: properties.Schema(
                        properties.Schema.STRING,
                        _('Config in junos cli format.'),
                        required=True,
                        update_allowed=True,
                    ),
                    ADDITIONAL_COMMANDS: properties.Schema(
                        properties.Schema.STRING,
                        _("Additional JUNOS CLI commands to"
                          " run after create."),
                        required=False,
                    ),
                }
            ),
            required=True,
            update_allowed=True
        ),
        LOCK_TIMEOUT: properties.Schema(
            properties.Schema.INTEGER,
            _('Timeout on trying to get the config lock in seconds.'),
            default=120,
            update_allowed=True
        ),
    }

    XML_EDIT_CONFIG = '''
                 <edit-config>
                   <target>
                     <candidate/>
                   </target>
                   <default-operation>none</default-operation>
                   <config>
                     <configuration>
                       {config}
                     </configuration>
                   </config>
                 </edit-config>'''

    update_allowed_keys = ('Properties',)

    # templates for building xml and config strings
    _xml_open_templates = {
        "tag": "<{tag}{operation}>",
        "named_tag": """<{tag}{operation}>
        <name><![CDATA[{name}]]></name>""",
    }
    _xml_close_templates = collections.defaultdict(lambda: "</{tag}>")

    _config_templates = {
        "tag": "{tag}",
        "name": "{name}",
        "named_tag": "{tag} {name}",
    }

    class TreeNode(object):
        def __init__(self, path_element):
            self.path_element = path_element
            self.children = []
            self.value = None

    NOT_FOUND_PATTERNS = [
        re.compile("^Referenced filter '.+' is not defined$", re.I),
        re.compile("^statement not found: .+$", re.I)]

    def _is_not_found_error(self, rpc_error):
        message = rpc_error.message
        for pattern in self.NOT_FOUND_PATTERNS:
            if pattern.search(message) is not None:
                return True
        return False

    def _build_config_tree(self, configs):
        root = []
        for conf in configs:
            curr_node = root
            new_node = None
            if not conf.path:
                raise ValueError(_("Tree for config is empty"))
            for path_element in conf.path:
                found = False
                for node in curr_node:
                    if node.path_element == path_element:
                        curr_node = node.children
                        found = True
                        break
                if not found:
                    new_node = self.TreeNode(path_element)
                    curr_node.append(new_node)
                    curr_node = new_node.children
            if not new_node:
                raise ValueError(_("You are trying to overwrite other config "
                                 "from this stack."))
            new_node.value = conf.config
        return root

    def _build_config_string(self, tree):
        result = []
        for node in tree:
            path_el = node.path_element
            result.append(self._config_templates[
                path_el["config_type"]].format(tag=path_el.get("tag"),
                                               name=path_el.get("name")))
            if node.children:
                if node.value:
                    # we don't allow this as it will make deletion harder
                    # and it may be even easier to just
                    # insert child's config in parent's config
                    raise ValueError(_(
                        "You can't add a child to the parent created "
                        "in this stack. If you need this "
                        "insert child config as "
                        "string in parent config."))
                result.append(' {{\n{} }}\n'.format(
                              self._build_config_string(node.children)))
            elif node.value:
                result.append(' {{\n{} }}\n'.format(node.value))
            else:
                # no children or value - we don't need to open scope,
                # just add statement
                result.append(";\n")
        return ''.join(result)

    def _build_xml_string(self, tree, operation=""):
        result = []
        for node in tree:
            path_el = node.path_element
            template_args = collections.defaultdict(
                str, tag=path_el.get("tag"), name=path_el.get("name"))
            if not node.children:
                template_args["operation"] = operation
            result.append(string.Formatter().vformat(
                self._xml_open_templates[path_el["xml_type"]], (),
                template_args))
            if node.children:
                result.append(self._build_xml_string(node.children, operation))
            result.append(string.Formatter().vformat(
                self._xml_close_templates[path_el["xml_type"]], (),
                template_args))
            LOG.info(result)
        return ''.join(result)

    def _create_config(self):
        configs = self._get_configs()
        tree = self._build_config_tree(configs)
        return self._build_config_string(tree)

    def _create_delete_rpcs(self):
        configs = self._get_configs()
        xmls = []
        for config in configs:
            tree = self._build_config_tree([config])
            xmls.append(self._build_xml_string(tree, " operation=\"delete\""))
        rpcs = []
        for xml in xmls:
            rpcs.append(self.XML_EDIT_CONFIG.format(config=xml))
        return rpcs

    def _get_configs(self):
        return [self.ConfigEntity(p[self.PATH],
                                  p[self.CONFIG])
                for p in self.properties[self.CONFIGS]]

    def _execute_additional_commands(self, manager):
        cmds = '\n'.join(p[self.ADDITIONAL_COMMANDS]
                         for p in self.properties[self.CONFIGS]
                         if bool(p[self.ADDITIONAL_COMMANDS]))
        if cmds:
            manager.load_configuration(target="candidate",
                                    config=cmds,
                                    format='text',
                                    action="set")

    def _create(self, manager, config, action='merge'):
        # merge is default action for load_configuration

        LOG.info('Constructed netconf create payload for %s: %s',
                 self.properties[self.DEVICE_IP], config)
        manager.load_configuration(target="candidate",
                                   action=action,
                                   config=config,
                                   format='text')
        self._execute_additional_commands(manager)

    def _delete(self, manager, configs):
        LOG.info('Constructed netconf delete rpcs %s: %s',
                 self.properties[self.DEVICE_IP], '\n'.join(configs))
        for config in configs:
            try:
                manager.rpc(config)
            except RPCError as e:
                if not self._is_not_found_error(e):
                    raise
                else:
                    LOG.warn("Resource not found for config: \n %s \n."
                             "  Skipping...", config)

    def _update(self, manager, delete_configs, new_config):
        if self.properties[self.ON_UPDATE] == 'delete-and-create':
            LOG.debug("Running delete-and-create.")
            self._delete(manager, delete_configs)
            self._create(manager, new_config)
        else:
            LOG.debug("Running update with action %s",
                      self.properties[self.ON_UPDATE])
            self._create(manager, new_config,
                         action=self.properties[self.ON_UPDATE])

    def handle_create(self):
        self.resource_id_set(str(uuid.uuid4()))
        config = self._create_config()
        self._client.execute_in_transaction(self._create, config)

    def handle_update(self, json_snippet=None, tmpl_diff=None, prop_diff=None):
        if not prop_diff:
            LOG.info("No update required.")
            return

        # create cmd to remove old config
        delete_configs = self._create_delete_rpcs()

        self.properties = json_snippet.properties(self.properties_schema,
                                                  self.context)

        # create updated config
        new_config = self._create_config()
        # execute delete and create with single commit
        self._client.execute_in_transaction(
                self._update, delete_configs, new_config)

    def handle_delete(self):
        configs = self._create_delete_rpcs()
        self._client.execute_in_transaction(self._delete, configs)


def resource_mapping():
    return {
        'OS::Contrail::NetconfNamedConfigs': ContrailNetconfNamedConfigs,
    }
```

### (3) Memo for myself ...
* It looks that master branch is not used in repository of "contrail-heat".
* The codes of processing via netconf is included in repository of "esi-python-modules".

![scope](../memo/Intenal_processing_fornetconf.001.png)
