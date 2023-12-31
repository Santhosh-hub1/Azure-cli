# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "dns-resolver forwarding-rule update",
)
class Update(AAZCommand):
    """Update a forwarding rule in a DNS forwarding ruleset.

    :example: Update forwarding rule in a DNS forwarding ruleset
        az dns-resolver forwarding-rule update --ruleset-name "sampleDnsForwardingRuleset" --name "sampleForwardingRule" --forwarding-rule-state "Disabled" --metadata additionalProp2="value2" --resource-group "sampleResourceGroup"
    """

    _aaz_info = {
        "version": "2022-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/dnsforwardingrulesets/{}/forwardingrules/{}", "2022-07-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = False

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.if_match = AAZStrArg(
            options=["--if-match"],
            help="ETag of the resource. Omit this value to always overwrite the current resource. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.",
        )
        _args_schema.ruleset_name = AAZStrArg(
            options=["--ruleset-name"],
            help="The name of the DNS forwarding ruleset.",
            required=True,
            id_part="name",
        )
        _args_schema.forwarding_rule_name = AAZStrArg(
            options=["-n", "--name", "--forwarding-rule-name"],
            help="The name of the forwarding rule.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.forwarding_rule_state = AAZStrArg(
            options=["--forwarding-rule-state"],
            help="The state of forwarding rule.",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.metadata = AAZDictArg(
            options=["--metadata"],
            help="Metadata attached to the forwarding rule. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...",
            nullable=True,
        )
        _args_schema.target_dns_servers = AAZListArg(
            options=["--target-dns-servers"],
            help={"short-summary": "DNS servers to forward the DNS query to.", "long-summary": "Usage: --target-dns-servers [{ip-address:XX,port:XX}]\nip-address: DNS server IP address.\nport: DNS server port.\nMultiple actions can be specified by using more than one --target-dns-servers argument."},
        )

        metadata = cls._args_schema.metadata
        metadata.Element = AAZStrArg(
            nullable=True,
        )

        target_dns_servers = cls._args_schema.target_dns_servers
        target_dns_servers.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.target_dns_servers.Element
        _element.ip_address = AAZStrArg(
            options=["ip-address"],
            help="DNS server IP address.",
        )
        _element.port = AAZIntArg(
            options=["port"],
            help="DNS server port.",
            nullable=True,
        )

        # define Arg Group "Properties"
        return cls._args_schema

    def _execute_operations(self):
        self.ForwardingRulesGet(ctx=self.ctx)()
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.ForwardingRulesCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ForwardingRulesGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "dnsForwardingRulesetName", self.ctx.args.ruleset_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "forwardingRuleName", self.ctx.args.forwarding_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _build_schema_forwarding_rule_read(cls._schema_on_200)

            return cls._schema_on_200

    class ForwardingRulesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsForwardingRulesets/{dnsForwardingRulesetName}/forwardingRules/{forwardingRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "dnsForwardingRulesetName", self.ctx.args.ruleset_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "forwardingRuleName", self.ctx.args.forwarding_rule_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "If-Match", self.ctx.args.if_match,
                ),
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _build_schema_forwarding_rule_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("forwardingRuleState", AAZStrType, ".forwarding_rule_state")
                properties.set_prop("metadata", AAZDictType, ".metadata")
                properties.set_prop("targetDnsServers", AAZListType, ".target_dns_servers", typ_kwargs={"flags": {"required": True}})

            metadata = _builder.get(".properties.metadata")
            if metadata is not None:
                metadata.set_elements(AAZStrType, ".")

            target_dns_servers = _builder.get(".properties.targetDnsServers")
            if target_dns_servers is not None:
                target_dns_servers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.targetDnsServers[]")
            if _elements is not None:
                _elements.set_prop("ipAddress", AAZStrType, ".ip_address", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("port", AAZIntType, ".port")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


_schema_forwarding_rule_read = None


def _build_schema_forwarding_rule_read(_schema):
    global _schema_forwarding_rule_read
    if _schema_forwarding_rule_read is not None:
        _schema.etag = _schema_forwarding_rule_read.etag
        _schema.id = _schema_forwarding_rule_read.id
        _schema.name = _schema_forwarding_rule_read.name
        _schema.properties = _schema_forwarding_rule_read.properties
        _schema.system_data = _schema_forwarding_rule_read.system_data
        _schema.type = _schema_forwarding_rule_read.type
        return

    _schema_forwarding_rule_read = AAZObjectType()

    forwarding_rule_read = _schema_forwarding_rule_read
    forwarding_rule_read.etag = AAZStrType(
        flags={"read_only": True},
    )
    forwarding_rule_read.id = AAZStrType(
        flags={"read_only": True},
    )
    forwarding_rule_read.name = AAZStrType(
        flags={"read_only": True},
    )
    forwarding_rule_read.properties = AAZObjectType(
        flags={"required": True, "client_flatten": True},
    )
    forwarding_rule_read.system_data = AAZObjectType(
        serialized_name="systemData",
        flags={"read_only": True},
    )
    forwarding_rule_read.type = AAZStrType(
        flags={"read_only": True},
    )

    properties = _schema_forwarding_rule_read.properties
    properties.domain_name = AAZStrType(
        serialized_name="domainName",
        flags={"required": True},
    )
    properties.forwarding_rule_state = AAZStrType(
        serialized_name="forwardingRuleState",
    )
    properties.metadata = AAZDictType()
    properties.provisioning_state = AAZStrType(
        serialized_name="provisioningState",
        flags={"read_only": True},
    )
    properties.target_dns_servers = AAZListType(
        serialized_name="targetDnsServers",
        flags={"required": True},
    )

    metadata = _schema_forwarding_rule_read.properties.metadata
    metadata.Element = AAZStrType()

    target_dns_servers = _schema_forwarding_rule_read.properties.target_dns_servers
    target_dns_servers.Element = AAZObjectType()

    _element = _schema_forwarding_rule_read.properties.target_dns_servers.Element
    _element.ip_address = AAZStrType(
        serialized_name="ipAddress",
        flags={"required": True},
    )
    _element.port = AAZIntType()

    system_data = _schema_forwarding_rule_read.system_data
    system_data.created_at = AAZStrType(
        serialized_name="createdAt",
        flags={"read_only": True},
    )
    system_data.created_by = AAZStrType(
        serialized_name="createdBy",
        flags={"read_only": True},
    )
    system_data.created_by_type = AAZStrType(
        serialized_name="createdByType",
        flags={"read_only": True},
    )
    system_data.last_modified_at = AAZStrType(
        serialized_name="lastModifiedAt",
        flags={"read_only": True},
    )
    system_data.last_modified_by = AAZStrType(
        serialized_name="lastModifiedBy",
        flags={"read_only": True},
    )
    system_data.last_modified_by_type = AAZStrType(
        serialized_name="lastModifiedByType",
        flags={"read_only": True},
    )

    _schema.etag = _schema_forwarding_rule_read.etag
    _schema.id = _schema_forwarding_rule_read.id
    _schema.name = _schema_forwarding_rule_read.name
    _schema.properties = _schema_forwarding_rule_read.properties
    _schema.system_data = _schema_forwarding_rule_read.system_data
    _schema.type = _schema_forwarding_rule_read.type


__all__ = ["Update"]
