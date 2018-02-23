# heat_template: common_function
This is heat_template of "common_function" which is provided by gohan via etcd

![scope](../images/esi_interface.002.png)

### (1) Stored data in etcd
These are stored data for "heat_templates" in etcd.
```
/config/v2.0/heat_templates/common_function
{
    "body": {
        "handler": "heat_worker", 
        "watch": [], 
        "id": "common_function", 
        "template_file": "heat_template_version: 2013-05-23\n\ndescription: >\n  Common Function\n\nparameters:\n  primary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Primary Device.\n    label: Ip address of the device.\n    type: string\n  primary_device_port:\n    description: Port that will be used to establish ssh connection to the Primary Device.\n    label: Port of the ssh connection.\n    type: number\n  primary_device_username:\n    description: Name of the user which will be used to log onto the Primary Device.\n    label: User name to log on to device.\n    type: string\n  primary_device_password:\n    description: Password of the user which will be used to log onto the Primary Device.\n    label: Users password.\n    type: string\n  primary_vrrp_ip:\n    description: Local ip in VRRP group on primary device.\n    label: Primary VRRP ip.\n    type: string\n  secondary_device_ip:\n    description: Ip address that will be used to establish ssh connection to the Secondary Device.\n    label: Ip address of the device.\n    type: string\n  secondary_device_port:\n    description: Port that will be used to establish ssh connection to the Secondary Device.\n    label: Port of the ssh connection.\n    type: number\n  secondary_device_username:\n    description: Name of the user which will be used to log onto the Secondary Device.\n    label: User name to log on to device.\n    type: string\n  secondary_device_password:\n    description: Password of the user which will be used to log onto the Secondary Device.\n    label: Users password.\n    type: string\n  secondary_vrrp_ip:\n    description: Local ip in VRRP group on secondary device.\n    label: Secondary VRRP ip.\n    type: string\n  netmask:\n    description: Netmask used in link local network.\n    label: Link-local netmask.\n    type: string\n\nresources:\n{% for device in [\"primary\", \"secondary\"] %}\n  netconf_configure_{{ device }}:\n    properties:\n      lock_timeout: 3000\n      configs:\n      - config: \"\"\n        path:\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: groups\n            name: {{ jinja_vrrp_group_name }}\n          - config_type: tag\n            xml_type: tag\n            tag: interfaces\n          - config_type: name\n            xml_type: named_tag\n            tag: interface\n            name: <*>\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: unit\n            name: <*>\n          - config_type: tag\n            xml_type: tag\n            tag: family\n          - config_type: tag\n            xml_type: tag\n            tag: inet\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: address\n            name:\n              str_replace:\n                params:\n                  $VIP:\n                    get_param: {{ device }}_vrrp_ip\n                  $NETMASK:\n                    get_param: netmask\n                template: |\n                  $VIP/$NETMASK\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: vrrp-group\n            name: {{ jinja_vrid }}\n          - config_type: named_tag\n            xml_type: named_tag # FIXME: this is probably not true, as far as i can see we don't support that in plugin at all :(\n            tag: virtual-address\n            name: {{ jinja_link_local_ip_address }}\n      - config: |\n          from {\n            destination-address {\n              {{ jinja_link_local_ip_address }}/32;\n            }\n          }\n          then {\n            translated {\n              translation-type {\n                dnat-44;\n              }\n            }\n          }\n        path:\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: groups\n            name: {{ jinja_dnat_group_name }}\n          - config_type: tag\n            xml_type: tag\n            tag: services\n          - config_type: tag\n            xml_type: tag\n            tag: nat\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: rule\n            name: <*>\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: term\n            name: {{ jinja_service_number }}\n      - config: |\n          services {\n            nat {\n              pool <*> {\n                address {{ jinja_shared_ip_address }}/32;\n              }\n            }\n          }\n        path:\n          - config_type: named_tag\n            xml_type: named_tag\n            tag: groups\n            name: {{ jinja_dnat_pool_group_name }}-{{ jinja_service_number }}\n      device_ip:\n        get_param: {{ device }}_device_ip\n      password:\n        get_param: {{ device }}_device_password\n      port:\n        get_param: {{ device }}_device_port\n      username:\n        get_param: {{ device }}_device_username\n    type: OS::Contrail::NetconfNamedConfigs\n{% endfor %}\n", 
        "parameter_mappings": {
            "jinja_dnat_pool_group_name": {
                "field": "dnat_pool_group_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "primary_vrrp_ip": {
                "field": "primary_vrrp_ip"
            }, 
            "jinja_dnat_group_name": {
                "field": "dnat_group_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "secondary_vrrp_ip": {
                "field": "secondary_vrrp_ip"
            }, 
            "secondary_device_ip": {
                "field": "ip", 
                "path": [
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "primary_device_port": {
                "field": "ssh_port", 
                "path": [
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "netmask": {
                "field": "link_local_netmask", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "jinja_shared_ip_address": {
                "field": "shared_ip_address"
            }, 
            "primary_device_ip": {
                "field": "ip", 
                "path": [
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "secondary_device_password": {
                "field": "password", 
                "path": [
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "heat_timeout": "C60", 
            "primary_device_username": {
                "field": "login", 
                "path": [
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "primary_device_password": {
                "field": "password", 
                "path": [
                    "ha_router_id", 
                    "primary_router_id"
                ]
            }, 
            "jinja_service_number": {
                "field": "common_function_number"
            }, 
            "secondary_device_username": {
                "field": "login", 
                "path": [
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "jinja_vrrp_group_name": {
                "field": "vrrp_group_name", 
                "path": [
                    "common_function_pool_id"
                ]
            }, 
            "secondary_device_port": {
                "field": "ssh_port", 
                "path": [
                    "ha_router_id", 
                    "secondary_router_id"
                ]
            }, 
            "jinja_vrid": {
                "field": "vrid"
            }, 
            "jinja_link_local_ip_address": {
                "field": "link_local_ip_address"
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
  Common Function

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
  primary_vrrp_ip:
    description: Local ip in VRRP group on primary device.
    label: Primary VRRP ip.
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
  secondary_vrrp_ip:
    description: Local ip in VRRP group on secondary device.
    label: Secondary VRRP ip.
    type: string
  netmask:
    description: Netmask used in link local network.
    label: Link-local netmask.
    type: string

resources:
{% for device in ["primary", "secondary"] %}
  netconf_configure_{{ device }}:
    properties:
      lock_timeout: 3000
      configs:
      - config: ""
        path:
          - config_type: named_tag
            xml_type: named_tag
            tag: groups
            name: {{ jinja_vrrp_group_name }}
          - config_type: tag
            xml_type: tag
            tag: interfaces
          - config_type: name
            xml_type: named_tag
            tag: interface
            name: <*>
          - config_type: named_tag
            xml_type: named_tag
            tag: unit
            name: <*>
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
                  $VIP:
                    get_param: {{ device }}_vrrp_ip
                  $NETMASK:
                    get_param: netmask
                template: |
                  $VIP/$NETMASK
          - config_type: named_tag
            xml_type: named_tag
            tag: vrrp-group
            name: {{ jinja_vrid }}
          - config_type: named_tag
            xml_type: named_tag # FIXME: this is probably not true, as far as i can see we don't support that in plugin at all :(
            tag: virtual-address
            name: {{ jinja_link_local_ip_address }}
      - config: |
          from {
            destination-address {
              {{ jinja_link_local_ip_address }}/32;
            }
          }
          then {
            translated {
              translation-type {
                dnat-44;
              }
            }
          }
        path:
          - config_type: named_tag
            xml_type: named_tag
            tag: groups
            name: {{ jinja_dnat_group_name }}
          - config_type: tag
            xml_type: tag
            tag: services
          - config_type: tag
            xml_type: tag
            tag: nat
          - config_type: named_tag
            xml_type: named_tag
            tag: rule
            name: <*>
          - config_type: named_tag
            xml_type: named_tag
            tag: term
            name: {{ jinja_service_number }}
      - config: |
          services {
            nat {
              pool <*> {
                address {{ jinja_shared_ip_address }}/32;
              }
            }
          }
        path:
          - config_type: named_tag
            xml_type: named_tag
            tag: groups
            name: {{ jinja_dnat_pool_group_name }}-{{ jinja_service_number }}
      device_ip:
        get_param: {{ device }}_device_ip
      password:
        get_param: {{ device }}_device_password
      port:
        get_param: {{ device }}_device_port
      username:
        get_param: {{ device }}_device_username
    type: OS::Contrail::NetconfNamedConfigs
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
