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
    "billing-benefits savings-plan-order savings-plan update",
)
class Update(AAZCommand):
    """Update savings plan.

    :example: Update display name
        az billing-benefits savings-plan-order savings-plan update --savings-plan-order-id 30000000-aaaa-bbbb-cccc-200000000017 --savings-plan-id 30000000-aaaa-bbbb-cccc-200000000019 --display-name "cliTest"

    :example: Update savings plan applied scope to "Shared"
        az billing-benefits savings-plan-order savings-plan update --savings-plan-order-id 30000000-aaaa-bbbb-cccc-200000000017 --savings-plan-id 30000000-aaaa-bbbb-cccc-200000000019 --applied-scope-type Shared

    :example: Update savings plan applied scope to "Single"
        az billing-benefits savings-plan-order savings-plan update --savings-plan-order-id 30000000-aaaa-bbbb-cccc-200000000017 --savings-plan-id 30000000-aaaa-bbbb-cccc-200000000019 --applied-scope-type Single --applied-scope-prop "{subscription-id:/subscriptions/30000000-aaaa-bbbb-cccc-200000000004}"

    :example: Update savings plan applied scope to "Single" resource group
        az billing-benefits savings-plan-order savings-plan update --savings-plan-order-id 30000000-aaaa-bbbb-cccc-200000000017 --savings-plan-id 30000000-aaaa-bbbb-cccc-200000000019 --applied-scope-type Single --applied-scope-prop "{subscription-id:/subscriptions/30000000-aaaa-bbbb-cccc-200000000004/resourceGroups/rgName}"

    :example: Update savings plan applied scope to "ManagementGroup"
        az billing-benefits savings-plan-order savings-plan update --savings-plan-order-id 30000000-aaaa-bbbb-cccc-200000000017 --savings-plan-id 30000000-aaaa-bbbb-cccc-200000000019 --applied-scope-type ManagementGroup --applied-scope-prop "{tenantId:10000000-aaaa-bbbb-cccc-20000000006,managementGroupId:/providers/Microsoft.Management/managementGroups/TestRg}"

    :example: Update savings plan renewal setting
        az billing-benefits savings-plan-order savings-plan update --savings-plan-order-id 30000000-aaaa-bbbb-cccc-200000000017 --savings-plan-id 30000000-aaaa-bbbb-cccc-200000000019 --renew true --renew-properties "{purchase-properties:{applied-scope-type:Shared,billing-plan:P1M,billing-scope-id:/subscriptions/30000000-aaaa-bbbb-cccc-200000000015,commitment:{amount:10.0,currency-code:USD,grain:Hourly},display-name:name1,renew:true,term:P1Y,sku:Compute_Savings_Plan}}"
    """

    _aaz_info = {
        "version": "2022-11-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billingbenefits/savingsplanorders/{}/savingsplans/{}", "2022-11-01"],
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
        _args_schema.savings_plan_id = AAZStrArg(
            options=["--savings-plan-id"],
            help="ID of the savings plan",
            required=True,
        )
        _args_schema.savings_plan_order_id = AAZStrArg(
            options=["--savings-plan-order-id"],
            help="Order ID of the savings plan",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.applied_scope_prop = AAZObjectArg(
            options=["--applied-scope-prop"],
            arg_group="Properties",
            help="Properties specific to applied scope type. Not required if not applicable.",
        )
        cls._build_args_applied_scope_properties_update(_args_schema.applied_scope_prop)
        _args_schema.applied_scope_type = AAZStrArg(
            options=["--applied-scope-type"],
            arg_group="Properties",
            help="Type of the Applied Scope.",
            enum={"ManagementGroup": "ManagementGroup", "Shared": "Shared", "Single": "Single"},
        )
        _args_schema.display_name = AAZStrArg(
            options=["--display-name"],
            arg_group="Properties",
            help="Display name",
        )
        _args_schema.renew = AAZBoolArg(
            options=["--renew"],
            arg_group="Properties",
            help="Setting this to true will automatically purchase a new benefit on the expiration date time.",
            default=False,
        )
        _args_schema.renew_properties = AAZObjectArg(
            options=["--renew-properties"],
            arg_group="Properties",
        )

        renew_properties = cls._args_schema.renew_properties
        renew_properties.purchase_properties = AAZObjectArg(
            options=["purchase-properties"],
        )

        purchase_properties = cls._args_schema.renew_properties.purchase_properties
        purchase_properties.applied_scope_properties = AAZObjectArg(
            options=["applied-scope-properties"],
        )
        cls._build_args_applied_scope_properties_update(purchase_properties.applied_scope_properties)
        purchase_properties.applied_scope_type = AAZStrArg(
            options=["applied-scope-type"],
            help="Type of the Applied Scope.",
            enum={"ManagementGroup": "ManagementGroup", "Shared": "Shared", "Single": "Single"},
        )
        purchase_properties.billing_plan = AAZStrArg(
            options=["billing-plan"],
            help="Represents the billing plan in ISO 8601 format. Required only for monthly billing plans.",
            enum={"P1M": "P1M"},
        )
        purchase_properties.billing_scope_id = AAZStrArg(
            options=["billing-scope-id"],
            help="Subscription that will be charged for purchasing the benefit",
        )
        purchase_properties.commitment = AAZObjectArg(
            options=["commitment"],
            help="Commitment towards the benefit.",
        )
        purchase_properties.display_name = AAZStrArg(
            options=["display-name"],
            help="Friendly name of the savings plan",
        )
        purchase_properties.renew = AAZBoolArg(
            options=["renew"],
            help="Setting this to true will automatically purchase a new benefit on the expiration date time.",
            default=False,
        )
        purchase_properties.term = AAZStrArg(
            options=["term"],
            help="Represent benefit term in ISO 8601 format.",
            enum={"P1Y": "P1Y", "P3Y": "P3Y", "P5Y": "P5Y"},
        )
        purchase_properties.sku = AAZStrArg(
            options=["sku"],
            help="Name of the SKU to be applied",
        )

        commitment = cls._args_schema.renew_properties.purchase_properties.commitment
        commitment.amount = AAZFloatArg(
            options=["amount"],
        )
        commitment.currency_code = AAZStrArg(
            options=["currency-code"],
            help="The ISO 4217 3-letter currency code for the currency used by this purchase record.",
        )
        commitment.grain = AAZStrArg(
            options=["grain"],
            help="Commitment grain.",
            enum={"Hourly": "Hourly"},
        )
        return cls._args_schema

    _args_applied_scope_properties_update = None

    @classmethod
    def _build_args_applied_scope_properties_update(cls, _schema):
        if cls._args_applied_scope_properties_update is not None:
            _schema.display_name = cls._args_applied_scope_properties_update.display_name
            _schema.management_group_id = cls._args_applied_scope_properties_update.management_group_id
            _schema.resource_group_id = cls._args_applied_scope_properties_update.resource_group_id
            _schema.subscription_id = cls._args_applied_scope_properties_update.subscription_id
            _schema.tenant_id = cls._args_applied_scope_properties_update.tenant_id
            return

        cls._args_applied_scope_properties_update = AAZObjectArg()

        applied_scope_properties_update = cls._args_applied_scope_properties_update
        applied_scope_properties_update.display_name = AAZStrArg(
            options=["display-name"],
            help="Display name",
        )
        applied_scope_properties_update.management_group_id = AAZStrArg(
            options=["management-group-id"],
            help="Fully-qualified identifier of the management group where the benefit must be applied.",
        )
        applied_scope_properties_update.resource_group_id = AAZStrArg(
            options=["resource-group-id"],
            help="Fully-qualified identifier of the resource group.",
        )
        applied_scope_properties_update.subscription_id = AAZStrArg(
            options=["subscription-id"],
            help="Fully-qualified identifier of the subscription.",
        )
        applied_scope_properties_update.tenant_id = AAZStrArg(
            options=["tenant-id"],
            help="Tenant ID where the benefit is applied.",
        )

        _schema.display_name = cls._args_applied_scope_properties_update.display_name
        _schema.management_group_id = cls._args_applied_scope_properties_update.management_group_id
        _schema.resource_group_id = cls._args_applied_scope_properties_update.resource_group_id
        _schema.subscription_id = cls._args_applied_scope_properties_update.subscription_id
        _schema.tenant_id = cls._args_applied_scope_properties_update.tenant_id

    def _execute_operations(self):
        self.pre_operations()
        self.SavingsPlanUpdate(ctx=self.ctx)()
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

    class SavingsPlanUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)
            if session.http_response.status_code in [202]:
                return self.on_202(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.BillingBenefits/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "savingsPlanId", self.ctx.args.savings_plan_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "savingsPlanOrderId", self.ctx.args.savings_plan_order_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-11-01",
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
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                _UpdateHelper._build_schema_applied_scope_properties_update(properties.set_prop("appliedScopeProperties", AAZObjectType, ".applied_scope_prop"))
                properties.set_prop("appliedScopeType", AAZStrType, ".applied_scope_type")
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("renew", AAZBoolType, ".renew")
                properties.set_prop("renewProperties", AAZObjectType, ".renew_properties")

            renew_properties = _builder.get(".properties.renewProperties")
            if renew_properties is not None:
                renew_properties.set_prop("purchaseProperties", AAZObjectType, ".purchase_properties")

            purchase_properties = _builder.get(".properties.renewProperties.purchaseProperties")
            if purchase_properties is not None:
                purchase_properties.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
                purchase_properties.set_prop("sku", AAZObjectType)

            properties = _builder.get(".properties.renewProperties.purchaseProperties.properties")
            if properties is not None:
                _UpdateHelper._build_schema_applied_scope_properties_update(properties.set_prop("appliedScopeProperties", AAZObjectType, ".applied_scope_properties"))
                properties.set_prop("appliedScopeType", AAZStrType, ".applied_scope_type")
                properties.set_prop("billingPlan", AAZStrType, ".billing_plan")
                properties.set_prop("billingScopeId", AAZStrType, ".billing_scope_id")
                properties.set_prop("commitment", AAZObjectType, ".commitment")
                properties.set_prop("displayName", AAZStrType, ".display_name")
                properties.set_prop("renew", AAZBoolType, ".renew")
                properties.set_prop("term", AAZStrType, ".term")

            commitment = _builder.get(".properties.renewProperties.purchaseProperties.properties.commitment")
            if commitment is not None:
                commitment.set_prop("amount", AAZFloatType, ".amount")
                commitment.set_prop("currencyCode", AAZStrType, ".currency_code")
                commitment.set_prop("grain", AAZStrType, ".grain")

            sku = _builder.get(".properties.renewProperties.purchaseProperties.sku")
            if sku is not None:
                sku.set_prop("name", AAZStrType, ".sku")

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
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType(
                flags={"required": True},
            )
            _UpdateHelper._build_schema_sku_read(_schema_on_200.sku)
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            _UpdateHelper._build_schema_applied_scope_properties_read(properties.applied_scope_properties)
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.benefit_start_time = AAZStrType(
                serialized_name="benefitStartTime",
            )
            properties.billing_account_id = AAZStrType(
                serialized_name="billingAccountId",
                flags={"read_only": True},
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_profile_id = AAZStrType(
                serialized_name="billingProfileId",
                flags={"read_only": True},
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.commitment = AAZObjectType()
            _UpdateHelper._build_schema_commitment_read(properties.commitment)
            properties.customer_id = AAZStrType(
                serialized_name="customerId",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.display_provisioning_state = AAZStrType(
                serialized_name="displayProvisioningState",
                flags={"read_only": True},
            )
            properties.effective_date_time = AAZStrType(
                serialized_name="effectiveDateTime",
                flags={"read_only": True},
            )
            properties.expiry_date_time = AAZStrType(
                serialized_name="expiryDateTime",
                flags={"read_only": True},
            )
            properties.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.purchase_date_time = AAZStrType(
                serialized_name="purchaseDateTime",
                flags={"read_only": True},
            )
            properties.renew = AAZBoolType()
            properties.renew_destination = AAZStrType(
                serialized_name="renewDestination",
            )
            properties.renew_properties = AAZObjectType(
                serialized_name="renewProperties",
            )
            properties.renew_source = AAZStrType(
                serialized_name="renewSource",
            )
            properties.term = AAZStrType()
            properties.user_friendly_applied_scope_type = AAZStrType(
                serialized_name="userFriendlyAppliedScopeType",
                flags={"read_only": True},
            )
            properties.utilization = AAZObjectType(
                flags={"read_only": True},
            )

            extended_status_info = cls._schema_on_200.properties.extended_status_info
            extended_status_info.message = AAZStrType()
            extended_status_info.status_code = AAZStrType(
                serialized_name="statusCode",
            )

            renew_properties = cls._schema_on_200.properties.renew_properties
            renew_properties.purchase_properties = AAZObjectType(
                serialized_name="purchaseProperties",
            )

            purchase_properties = cls._schema_on_200.properties.renew_properties.purchase_properties
            purchase_properties.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            purchase_properties.sku = AAZObjectType()
            _UpdateHelper._build_schema_sku_read(purchase_properties.sku)

            properties = cls._schema_on_200.properties.renew_properties.purchase_properties.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            _UpdateHelper._build_schema_applied_scope_properties_read(properties.applied_scope_properties)
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.commitment = AAZObjectType()
            _UpdateHelper._build_schema_commitment_read(properties.commitment)
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.effective_date_time = AAZStrType(
                serialized_name="effectiveDateTime",
                flags={"read_only": True},
            )
            properties.renew = AAZBoolType()
            properties.term = AAZStrType()

            utilization = cls._schema_on_200.properties.utilization
            utilization.aggregates = AAZListType()
            utilization.trend = AAZStrType(
                flags={"read_only": True},
            )

            aggregates = cls._schema_on_200.properties.utilization.aggregates
            aggregates.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.utilization.aggregates.Element
            _element.grain = AAZFloatType(
                flags={"read_only": True},
            )
            _element.grain_unit = AAZStrType(
                serialized_name="grainUnit",
                flags={"read_only": True},
            )
            _element.value = AAZFloatType(
                flags={"read_only": True},
            )
            _element.value_unit = AAZStrType(
                serialized_name="valueUnit",
                flags={"read_only": True},
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

            return cls._schema_on_200

        def on_202(self, session):
            pass


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_applied_scope_properties_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("displayName", AAZStrType, ".display_name")
        _builder.set_prop("managementGroupId", AAZStrType, ".management_group_id")
        _builder.set_prop("resourceGroupId", AAZStrType, ".resource_group_id")
        _builder.set_prop("subscriptionId", AAZStrType, ".subscription_id")
        _builder.set_prop("tenantId", AAZStrType, ".tenant_id")

    _schema_applied_scope_properties_read = None

    @classmethod
    def _build_schema_applied_scope_properties_read(cls, _schema):
        if cls._schema_applied_scope_properties_read is not None:
            _schema.display_name = cls._schema_applied_scope_properties_read.display_name
            _schema.management_group_id = cls._schema_applied_scope_properties_read.management_group_id
            _schema.resource_group_id = cls._schema_applied_scope_properties_read.resource_group_id
            _schema.subscription_id = cls._schema_applied_scope_properties_read.subscription_id
            _schema.tenant_id = cls._schema_applied_scope_properties_read.tenant_id
            return

        cls._schema_applied_scope_properties_read = _schema_applied_scope_properties_read = AAZObjectType()

        applied_scope_properties_read = _schema_applied_scope_properties_read
        applied_scope_properties_read.display_name = AAZStrType(
            serialized_name="displayName",
        )
        applied_scope_properties_read.management_group_id = AAZStrType(
            serialized_name="managementGroupId",
        )
        applied_scope_properties_read.resource_group_id = AAZStrType(
            serialized_name="resourceGroupId",
        )
        applied_scope_properties_read.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )
        applied_scope_properties_read.tenant_id = AAZStrType(
            serialized_name="tenantId",
        )

        _schema.display_name = cls._schema_applied_scope_properties_read.display_name
        _schema.management_group_id = cls._schema_applied_scope_properties_read.management_group_id
        _schema.resource_group_id = cls._schema_applied_scope_properties_read.resource_group_id
        _schema.subscription_id = cls._schema_applied_scope_properties_read.subscription_id
        _schema.tenant_id = cls._schema_applied_scope_properties_read.tenant_id

    _schema_commitment_read = None

    @classmethod
    def _build_schema_commitment_read(cls, _schema):
        if cls._schema_commitment_read is not None:
            _schema.amount = cls._schema_commitment_read.amount
            _schema.currency_code = cls._schema_commitment_read.currency_code
            _schema.grain = cls._schema_commitment_read.grain
            return

        cls._schema_commitment_read = _schema_commitment_read = AAZObjectType()

        commitment_read = _schema_commitment_read
        commitment_read.amount = AAZFloatType()
        commitment_read.currency_code = AAZStrType(
            serialized_name="currencyCode",
        )
        commitment_read.grain = AAZStrType()

        _schema.amount = cls._schema_commitment_read.amount
        _schema.currency_code = cls._schema_commitment_read.currency_code
        _schema.grain = cls._schema_commitment_read.grain

    _schema_sku_read = None

    @classmethod
    def _build_schema_sku_read(cls, _schema):
        if cls._schema_sku_read is not None:
            _schema.name = cls._schema_sku_read.name
            return

        cls._schema_sku_read = _schema_sku_read = AAZObjectType()

        sku_read = _schema_sku_read
        sku_read.name = AAZStrType()

        _schema.name = cls._schema_sku_read.name


__all__ = ["Update"]
