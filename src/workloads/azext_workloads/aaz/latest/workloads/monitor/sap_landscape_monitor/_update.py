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
    "workloads monitor sap-landscape-monitor update",
    is_preview=True,
)
class Update(AAZCommand):
    """Update a SAP Landscape Monitor Dashboard for the specified subscription, resource group, and resource name.

    :example: Update a SAP Landscape Monitor Dashboard for the specified subscription, resource group, and resource name
        az workloads monitor sap-landscape-monitor update -g <RG-NAME> --monitor-name <monitor-name> --grouping <grouping-details>
    """

    _aaz_info = {
        "version": "2023-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.workloads/monitors/{}/saplandscapemonitor/default", "2023-04-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.monitor_name = AAZStrArg(
            options=["--monitor-name"],
            help="Name of the SAP monitor resource.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.grouping = AAZObjectArg(
            options=["--grouping"],
            arg_group="Properties",
            help="Gets or sets the SID groupings by landscape and Environment.",
            nullable=True,
        )
        _args_schema.top_metrics_thresholds = AAZListArg(
            options=["--top-metrics-thresholds"],
            arg_group="Properties",
            help="Gets or sets the list Top Metric Thresholds for SAP Landscape Monitor Dashboard",
            nullable=True,
            fmt=AAZListArgFormat(
                max_length=50,
            ),
        )

        grouping = cls._args_schema.grouping
        grouping.landscape = AAZListArg(
            options=["landscape"],
            help="Gets or sets the list of landscape to SID mappings.",
            nullable=True,
            fmt=AAZListArgFormat(
                max_length=50,
            ),
        )
        grouping.sap_application = AAZListArg(
            options=["sap-application"],
            help="Gets or sets the list of Sap Applications to SID mappings.",
            nullable=True,
            fmt=AAZListArgFormat(
                max_length=50,
            ),
        )

        landscape = cls._args_schema.grouping.landscape
        landscape.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_sap_landscape_monitor_sid_mapping_update(landscape.Element)

        sap_application = cls._args_schema.grouping.sap_application
        sap_application.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_sap_landscape_monitor_sid_mapping_update(sap_application.Element)

        top_metrics_thresholds = cls._args_schema.top_metrics_thresholds
        top_metrics_thresholds.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.top_metrics_thresholds.Element
        _element.green = AAZFloatArg(
            options=["green"],
            help="Gets or sets the threshold value for Green.",
            nullable=True,
        )
        _element.name = AAZStrArg(
            options=["name"],
            help="Gets or sets the name of the threshold.",
            nullable=True,
        )
        _element.red = AAZFloatArg(
            options=["red"],
            help="Gets or sets the threshold value for Red.",
            nullable=True,
        )
        _element.yellow = AAZFloatArg(
            options=["yellow"],
            help="Gets or sets the threshold value for Yellow.",
            nullable=True,
        )
        return cls._args_schema

    _args_sap_landscape_monitor_sid_mapping_update = None

    @classmethod
    def _build_args_sap_landscape_monitor_sid_mapping_update(cls, _schema):
        if cls._args_sap_landscape_monitor_sid_mapping_update is not None:
            _schema.name = cls._args_sap_landscape_monitor_sid_mapping_update.name
            _schema.top_sid = cls._args_sap_landscape_monitor_sid_mapping_update.top_sid
            return

        cls._args_sap_landscape_monitor_sid_mapping_update = AAZObjectArg(
            nullable=True,
        )

        sap_landscape_monitor_sid_mapping_update = cls._args_sap_landscape_monitor_sid_mapping_update
        sap_landscape_monitor_sid_mapping_update.name = AAZStrArg(
            options=["name"],
            help="Gets or sets the name of the grouping.",
            nullable=True,
        )
        sap_landscape_monitor_sid_mapping_update.top_sid = AAZListArg(
            options=["top-sid"],
            help="Gets or sets the list of SID's.",
            nullable=True,
            fmt=AAZListArgFormat(
                max_length=50,
            ),
        )

        top_sid = cls._args_sap_landscape_monitor_sid_mapping_update.top_sid
        top_sid.Element = AAZStrArg(
            nullable=True,
        )

        _schema.name = cls._args_sap_landscape_monitor_sid_mapping_update.name
        _schema.top_sid = cls._args_sap_landscape_monitor_sid_mapping_update.top_sid

    def _execute_operations(self):
        self.pre_operations()
        self.SapLandscapeMonitorGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.SapLandscapeMonitorCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SapLandscapeMonitorGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/monitors/{monitorName}/sapLandscapeMonitor/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
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
                    "api-version", "2023-04-01",
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
            _UpdateHelper._build_schema_sap_landscape_monitor_read(cls._schema_on_200)

            return cls._schema_on_200

    class SapLandscapeMonitorCreate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/monitors/{monitorName}/sapLandscapeMonitor/default",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "monitorName", self.ctx.args.monitor_name,
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
                    "api-version", "2023-04-01",
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
            _UpdateHelper._build_schema_sap_landscape_monitor_read(cls._schema_on_200_201)

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
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("grouping", AAZObjectType, ".grouping")
                properties.set_prop("topMetricsThresholds", AAZListType, ".top_metrics_thresholds")

            grouping = _builder.get(".properties.grouping")
            if grouping is not None:
                grouping.set_prop("landscape", AAZListType, ".landscape")
                grouping.set_prop("sapApplication", AAZListType, ".sap_application")

            landscape = _builder.get(".properties.grouping.landscape")
            if landscape is not None:
                _UpdateHelper._build_schema_sap_landscape_monitor_sid_mapping_update(landscape.set_elements(AAZObjectType, "."))

            sap_application = _builder.get(".properties.grouping.sapApplication")
            if sap_application is not None:
                _UpdateHelper._build_schema_sap_landscape_monitor_sid_mapping_update(sap_application.set_elements(AAZObjectType, "."))

            top_metrics_thresholds = _builder.get(".properties.topMetricsThresholds")
            if top_metrics_thresholds is not None:
                top_metrics_thresholds.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.topMetricsThresholds[]")
            if _elements is not None:
                _elements.set_prop("green", AAZFloatType, ".green")
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("red", AAZFloatType, ".red")
                _elements.set_prop("yellow", AAZFloatType, ".yellow")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sap_landscape_monitor_sid_mapping_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("name", AAZStrType, ".name")
        _builder.set_prop("topSid", AAZListType, ".top_sid")

        top_sid = _builder.get(".topSid")
        if top_sid is not None:
            top_sid.set_elements(AAZStrType, ".")

    _schema_sap_landscape_monitor_sid_mapping_read = None

    @classmethod
    def _build_schema_sap_landscape_monitor_sid_mapping_read(cls, _schema):
        if cls._schema_sap_landscape_monitor_sid_mapping_read is not None:
            _schema.name = cls._schema_sap_landscape_monitor_sid_mapping_read.name
            _schema.top_sid = cls._schema_sap_landscape_monitor_sid_mapping_read.top_sid
            return

        cls._schema_sap_landscape_monitor_sid_mapping_read = _schema_sap_landscape_monitor_sid_mapping_read = AAZObjectType()

        sap_landscape_monitor_sid_mapping_read = _schema_sap_landscape_monitor_sid_mapping_read
        sap_landscape_monitor_sid_mapping_read.name = AAZStrType()
        sap_landscape_monitor_sid_mapping_read.top_sid = AAZListType(
            serialized_name="topSid",
        )

        top_sid = _schema_sap_landscape_monitor_sid_mapping_read.top_sid
        top_sid.Element = AAZStrType()

        _schema.name = cls._schema_sap_landscape_monitor_sid_mapping_read.name
        _schema.top_sid = cls._schema_sap_landscape_monitor_sid_mapping_read.top_sid

    _schema_sap_landscape_monitor_read = None

    @classmethod
    def _build_schema_sap_landscape_monitor_read(cls, _schema):
        if cls._schema_sap_landscape_monitor_read is not None:
            _schema.id = cls._schema_sap_landscape_monitor_read.id
            _schema.name = cls._schema_sap_landscape_monitor_read.name
            _schema.properties = cls._schema_sap_landscape_monitor_read.properties
            _schema.system_data = cls._schema_sap_landscape_monitor_read.system_data
            _schema.type = cls._schema_sap_landscape_monitor_read.type
            return

        cls._schema_sap_landscape_monitor_read = _schema_sap_landscape_monitor_read = AAZObjectType()

        sap_landscape_monitor_read = _schema_sap_landscape_monitor_read
        sap_landscape_monitor_read.id = AAZStrType(
            flags={"read_only": True},
        )
        sap_landscape_monitor_read.name = AAZStrType(
            flags={"read_only": True},
        )
        sap_landscape_monitor_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        sap_landscape_monitor_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        sap_landscape_monitor_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_sap_landscape_monitor_read.properties
        properties.grouping = AAZObjectType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.top_metrics_thresholds = AAZListType(
            serialized_name="topMetricsThresholds",
        )

        grouping = _schema_sap_landscape_monitor_read.properties.grouping
        grouping.landscape = AAZListType()
        grouping.sap_application = AAZListType(
            serialized_name="sapApplication",
        )

        landscape = _schema_sap_landscape_monitor_read.properties.grouping.landscape
        landscape.Element = AAZObjectType()
        cls._build_schema_sap_landscape_monitor_sid_mapping_read(landscape.Element)

        sap_application = _schema_sap_landscape_monitor_read.properties.grouping.sap_application
        sap_application.Element = AAZObjectType()
        cls._build_schema_sap_landscape_monitor_sid_mapping_read(sap_application.Element)

        top_metrics_thresholds = _schema_sap_landscape_monitor_read.properties.top_metrics_thresholds
        top_metrics_thresholds.Element = AAZObjectType()

        _element = _schema_sap_landscape_monitor_read.properties.top_metrics_thresholds.Element
        _element.green = AAZFloatType()
        _element.name = AAZStrType()
        _element.red = AAZFloatType()
        _element.yellow = AAZFloatType()

        system_data = _schema_sap_landscape_monitor_read.system_data
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

        _schema.id = cls._schema_sap_landscape_monitor_read.id
        _schema.name = cls._schema_sap_landscape_monitor_read.name
        _schema.properties = cls._schema_sap_landscape_monitor_read.properties
        _schema.system_data = cls._schema_sap_landscape_monitor_read.system_data
        _schema.type = cls._schema_sap_landscape_monitor_read.type


__all__ = ["Update"]
