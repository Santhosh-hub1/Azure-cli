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
    "automation python3-package create",
)
class Create(AAZCommand):
    """Create or Update the python 3 package identified by package name.

    :example: Add Python3 Package to automation account
        az automation python3-package create --automation-account-name "MyAutomationAccount" --resource-group "MyResourceGroup" --name "PackageName" --content-link "uri=https://PackageUri.com"
    """

    _aaz_info = {
        "version": "2022-08-08",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.automation/automationaccounts/{}/python3packages/{}", "2022-08-08"],
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
        _args_schema.automation_account_name = AAZStrArg(
            options=["--automation-account-name"],
            help="The name of the automation account.",
            required=True,
            id_part="name",
        )
        _args_schema.package_name = AAZStrArg(
            options=["-n", "--name", "--package-name"],
            help="The name of python package.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Gets or sets the tags attached to the resource.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.content_link = AAZObjectArg(
            options=["--content-link"],
            arg_group="Properties",
            help="Gets or sets the module content link.",
            required=True,
        )

        content_link = cls._args_schema.content_link
        content_link.content_hash = AAZObjectArg(
            options=["content-hash"],
            help="Gets or sets the hash.",
        )
        content_link.uri = AAZStrArg(
            options=["uri"],
            help="Gets or sets the uri of the runbook content.",
        )
        content_link.version = AAZStrArg(
            options=["version"],
            help="Gets or sets the version of the content.",
        )

        content_hash = cls._args_schema.content_link.content_hash
        content_hash.algorithm = AAZStrArg(
            options=["algorithm"],
            help="Gets or sets the content hash algorithm used to hash the content.",
            required=True,
        )
        content_hash.value = AAZStrArg(
            options=["value"],
            help="Gets or sets expected hash value of the content.",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.Python3PackageCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    # @register_callback
    def pre_operations(self):
        pass

    # @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class Python3PackageCreateOrUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/python3Packages/{packageName}",
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
                    "automationAccountName", self.ctx.args.automation_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "packageName", self.ctx.args.package_name,
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
                    "api-version", "2022-08-08",
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
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("contentLink", AAZObjectType, ".content_link", typ_kwargs={"flags": {"required": True}})

            content_link = _builder.get(".properties.contentLink")
            if content_link is not None:
                content_link.set_prop("contentHash", AAZObjectType, ".content_hash")
                content_link.set_prop("uri", AAZStrType, ".uri")
                content_link.set_prop("version", AAZStrType, ".version")

            content_hash = _builder.get(".properties.contentLink.contentHash")
            if content_hash is not None:
                content_hash.set_prop("algorithm", AAZStrType, ".algorithm", typ_kwargs={"flags": {"required": True}})
                content_hash.set_prop("value", AAZStrType, ".value", typ_kwargs={"flags": {"required": True}})

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
            _schema_on_200_201.etag = AAZStrType()
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.activity_count = AAZIntType(
                serialized_name="activityCount",
            )
            properties.content_link = AAZObjectType(
                serialized_name="contentLink",
            )
            properties.creation_time = AAZStrType(
                serialized_name="creationTime",
            )
            properties.description = AAZStrType()
            properties.error = AAZObjectType()
            properties.is_composite = AAZBoolType(
                serialized_name="isComposite",
            )
            properties.is_global = AAZBoolType(
                serialized_name="isGlobal",
            )
            properties.last_modified_time = AAZStrType(
                serialized_name="lastModifiedTime",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.size_in_bytes = AAZIntType(
                serialized_name="sizeInBytes",
            )
            properties.version = AAZStrType()

            content_link = cls._schema_on_200_201.properties.content_link
            content_link.content_hash = AAZObjectType(
                serialized_name="contentHash",
            )
            content_link.uri = AAZStrType()
            content_link.version = AAZStrType()

            content_hash = cls._schema_on_200_201.properties.content_link.content_hash
            content_hash.algorithm = AAZStrType(
                flags={"required": True},
            )
            content_hash.value = AAZStrType(
                flags={"required": True},
            )

            error = cls._schema_on_200_201.properties.error
            error.code = AAZStrType()
            error.message = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


__all__ = ["Create"]
