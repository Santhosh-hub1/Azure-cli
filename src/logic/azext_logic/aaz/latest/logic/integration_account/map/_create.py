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
    "logic integration-account map create",
)
class Create(AAZCommand):
    """Create an integration account map. If the map is larger than 4 MB, you need to store the map in an Azure blob and use the blob's Shared Access Signature (SAS) URL as the 'contentLink' property value.

    :example: Create map
        az logic integration-account map create -g rg -n map-name --integration-account account-name --map-type Xslt --content-type application/xml --map-content map_content.txt
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/integrationaccounts/{}/maps/{}", "2019-05-01"],
        ]
    }

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
        _args_schema.integration_account = AAZStrArg(
            options=["--integration-account"],
            help="The integration account name.",
            required=True,
        )
        _args_schema.map_name = AAZStrArg(
            options=["-n", "--name", "--map-name"],
            help="The integration account map name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Map"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="Map",
            help="The resource location.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Map",
            help="The resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.content = AAZStrArg(
            options=["--content"],
            arg_group="Properties",
            help="The content.",
        )
        _args_schema.content_type = AAZStrArg(
            options=["--content-type"],
            arg_group="Properties",
            help="The content type.",
        )
        _args_schema.map_type = AAZStrArg(
            options=["--map-type"],
            arg_group="Properties",
            help="The map type.",
            required=True,
            enum={"Liquid": "Liquid", "NotSpecified": "NotSpecified", "Xslt": "Xslt", "Xslt20": "Xslt20", "Xslt30": "Xslt30"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IntegrationAccountMapsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IntegrationAccountMapsCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}",
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
                    "integrationAccountName", self.ctx.args.integration_account,
                    required=True,
                ),
                **self.serialize_url_param(
                    "mapName", self.ctx.args.map_name,
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
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("content", AAZStrType, ".content")
                properties.set_prop("contentType", AAZStrType, ".content_type")
                properties.set_prop("mapType", AAZStrType, ".map_type", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.changed_time = AAZStrType(
                serialized_name="changedTime",
                flags={"read_only": True},
            )
            properties.content = AAZStrType()
            properties.content_link = AAZObjectType(
                serialized_name="contentLink",
            )
            properties.content_type = AAZStrType(
                serialized_name="contentType",
            )
            properties.created_time = AAZStrType(
                serialized_name="createdTime",
                flags={"read_only": True},
            )
            properties.map_type = AAZStrType(
                serialized_name="mapType",
                flags={"required": True},
            )
            properties.parameters_schema = AAZObjectType(
                serialized_name="parametersSchema",
            )

            content_link = cls._schema_on_200_201.properties.content_link
            content_link.content_hash = AAZObjectType(
                serialized_name="contentHash",
            )
            content_link.content_size = AAZIntType(
                serialized_name="contentSize",
                flags={"read_only": True},
            )
            content_link.content_version = AAZStrType(
                serialized_name="contentVersion",
                flags={"read_only": True},
            )
            content_link.uri = AAZStrType()

            content_hash = cls._schema_on_200_201.properties.content_link.content_hash
            content_hash.algorithm = AAZStrType()
            content_hash.value = AAZStrType()

            parameters_schema = cls._schema_on_200_201.properties.parameters_schema
            parameters_schema.ref = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
