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
    "remote-rendering-account update",
    is_preview=True,
)
class Update(AAZCommand):
    """Update a Remote Rendering Account.

    :example: Update remote rendering account
        az remote-rendering-account update -n "MyAccount" --tags hero="romeo" heroine="juliet" --resource-group "MyResourceGroup"
    """

    _aaz_info = {
        "version": "2021-03-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.mixedreality/remoterenderingaccounts/{}", "2021-03-01-preview"],
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
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of an Mixed Reality Account.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[-\w\._\(\)]+$",
                max_length=90,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.storage_account_name = AAZStrArg(
            options=["--storage-account-name"],
            arg_group="Properties",
            help="The name of the storage account associated with this accountId",
        )

        # define Arg Group "RemoteRenderingAccount"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="RemoteRenderingAccount",
            help="The identity associated with this account",
        )
        cls._build_args_identity_update(_args_schema.identity)
        _args_schema.kind = AAZObjectArg(
            options=["--kind"],
            arg_group="RemoteRenderingAccount",
            help="The kind of account, if supported",
        )
        cls._build_args_sku_update(_args_schema.kind)
        _args_schema.sku = AAZObjectArg(
            options=["--sku"],
            arg_group="RemoteRenderingAccount",
            help="The sku associated with this account",
        )
        cls._build_args_sku_update(_args_schema.sku)
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="RemoteRenderingAccount",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    _args_identity_update = None

    @classmethod
    def _build_args_identity_update(cls, _schema):
        if cls._args_identity_update is not None:
            _schema.type = cls._args_identity_update.type
            return

        cls._args_identity_update = AAZObjectArg()

        identity_update = cls._args_identity_update
        identity_update.type = AAZStrArg(
            options=["type"],
            help="The identity type.",
            enum={"SystemAssigned": "SystemAssigned"},
        )

        _schema.type = cls._args_identity_update.type

    _args_sku_update = None

    @classmethod
    def _build_args_sku_update(cls, _schema):
        if cls._args_sku_update is not None:
            _schema.capacity = cls._args_sku_update.capacity
            _schema.family = cls._args_sku_update.family
            _schema.name = cls._args_sku_update.name
            _schema.size = cls._args_sku_update.size
            _schema.tier = cls._args_sku_update.tier
            return

        cls._args_sku_update = AAZObjectArg()

        sku_update = cls._args_sku_update
        sku_update.capacity = AAZIntArg(
            options=["capacity"],
            help="If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.",
        )
        sku_update.family = AAZStrArg(
            options=["family"],
            help="If the service has different generations of hardware, for the same SKU, then that can be captured here.",
        )
        sku_update.name = AAZStrArg(
            options=["name"],
            help="The name of the SKU. Ex - P3. It is typically a letter+number code",
            required=True,
        )
        sku_update.size = AAZStrArg(
            options=["size"],
            help="The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. ",
        )
        sku_update.tier = AAZStrArg(
            options=["tier"],
            help="This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.",
            enum={"Basic": "Basic", "Free": "Free", "Premium": "Premium", "Standard": "Standard"},
        )

        _schema.capacity = cls._args_sku_update.capacity
        _schema.family = cls._args_sku_update.family
        _schema.name = cls._args_sku_update.name
        _schema.size = cls._args_sku_update.size
        _schema.tier = cls._args_sku_update.tier

    def _execute_operations(self):
        self.pre_operations()
        self.RemoteRenderingAccountsUpdate(ctx=self.ctx)()
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

    class RemoteRenderingAccountsUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts/{accountName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accountName", self.ctx.args.name,
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
                    "api-version", "2021-03-01-preview",
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
            _UpdateHelper._build_schema_identity_update(_builder.set_prop("identity", AAZObjectType, ".identity"))
            _UpdateHelper._build_schema_sku_update(_builder.set_prop("kind", AAZObjectType, ".kind"))
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _UpdateHelper._build_schema_sku_update(_builder.set_prop("sku", AAZObjectType, ".sku"))
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("storageAccountName", AAZStrType, ".storage_account_name")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _UpdateHelper._build_schema_identity_read(_schema_on_200.identity)
            _schema_on_200.kind = AAZObjectType()
            _UpdateHelper._build_schema_sku_read(_schema_on_200.kind)
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.plan = AAZObjectType()
            _UpdateHelper._build_schema_identity_read(_schema_on_200.plan)
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType()
            _UpdateHelper._build_schema_sku_read(_schema_on_200.sku)
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.account_domain = AAZStrType(
                serialized_name="accountDomain",
                flags={"read_only": True},
            )
            properties.account_id = AAZStrType(
                serialized_name="accountId",
                flags={"read_only": True},
            )
            properties.storage_account_name = AAZStrType(
                serialized_name="storageAccountName",
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_identity_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("type", AAZStrType, ".type")

    @classmethod
    def _build_schema_sku_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("capacity", AAZIntType, ".capacity")
        _builder.set_prop("family", AAZStrType, ".family")
        _builder.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("size", AAZStrType, ".size")
        _builder.set_prop("tier", AAZStrType, ".tier")

    _schema_identity_read = None

    @classmethod
    def _build_schema_identity_read(cls, _schema):
        if cls._schema_identity_read is not None:
            _schema.principal_id = cls._schema_identity_read.principal_id
            _schema.tenant_id = cls._schema_identity_read.tenant_id
            _schema.type = cls._schema_identity_read.type
            return

        cls._schema_identity_read = _schema_identity_read = AAZObjectType()

        identity_read = _schema_identity_read
        identity_read.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity_read.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity_read.type = AAZStrType()

        _schema.principal_id = cls._schema_identity_read.principal_id
        _schema.tenant_id = cls._schema_identity_read.tenant_id
        _schema.type = cls._schema_identity_read.type

    _schema_sku_read = None

    @classmethod
    def _build_schema_sku_read(cls, _schema):
        if cls._schema_sku_read is not None:
            _schema.capacity = cls._schema_sku_read.capacity
            _schema.family = cls._schema_sku_read.family
            _schema.name = cls._schema_sku_read.name
            _schema.size = cls._schema_sku_read.size
            _schema.tier = cls._schema_sku_read.tier
            return

        cls._schema_sku_read = _schema_sku_read = AAZObjectType()

        sku_read = _schema_sku_read
        sku_read.capacity = AAZIntType()
        sku_read.family = AAZStrType()
        sku_read.name = AAZStrType(
            flags={"required": True},
        )
        sku_read.size = AAZStrType()
        sku_read.tier = AAZStrType()

        _schema.capacity = cls._schema_sku_read.capacity
        _schema.family = cls._schema_sku_read.family
        _schema.name = cls._schema_sku_read.name
        _schema.size = cls._schema_sku_read.size
        _schema.tier = cls._schema_sku_read.tier


__all__ = ["Update"]
