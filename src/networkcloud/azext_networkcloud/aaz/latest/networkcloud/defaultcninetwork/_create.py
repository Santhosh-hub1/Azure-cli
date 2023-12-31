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
    "networkcloud defaultcninetwork create",
    is_experimental=True,
)
class Create(AAZCommand):
    """Create a new default CNI network or update the properties of the existing default CNI network.

    :example: Create or update default CNI network
        az networkcloud defaultcninetwork create --name "defaultCniNetworkName" --extended-location name="/subscriptions/subscriptionId/resourceGroups/resourceGroupName/providers/Microsoft.ExtendedLocation/customLocations/clusterExtendedLocationName" type="CustomLocation" --location "location" --cni-bgp-configuration "{bgpPeers:[{asNumber:64497,peerIp:'203.0.113.254'}],communityAdvertisements:[{communities:['64512','100'],subnetPrefix:'192.0.2.0/27'}],serviceExternalPrefixes:['192.0.2.0/28'],serviceLoadBalancerPrefixes:['192.0.2.16/28']}" --ip-allocation-type "DualStack" --ipv4-connected-prefix "203.0.113.0/24" --ipv6-connected-prefix "2001:db8:0:3::/64" --l3-isolation-domain-id "/subscriptions/subscriptionId/resourceGroups/resourceGroupName/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/l3IsolationDomainName" --vlan 12 --tags key1="myvalue1" key2="myvalue2" --resource-group "resourceGroupName"
    """

    _aaz_info = {
        "version": "2022-12-12-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/defaultcninetworks/{}", "2022-12-12-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.default_cni_network_name = AAZStrArg(
            options=["-n", "--name", "--default-cni-network-name"],
            help="The name of the default CNI network.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "DefaultCniNetworkParameters"

        _args_schema = cls._args_schema
        _args_schema.extended_location = AAZObjectArg(
            options=["--extended-location"],
            arg_group="DefaultCniNetworkParameters",
            help="The extended location of the cluster associated with the resource.",
            required=True,
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="DefaultCniNetworkParameters",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="DefaultCniNetworkParameters",
            help="Resource tags.",
        )

        extended_location = cls._args_schema.extended_location
        extended_location.name = AAZStrArg(
            options=["name"],
            help="The resource ID of the extended location on which the resource will be created.",
            required=True,
        )
        extended_location.type = AAZStrArg(
            options=["type"],
            help="The extended location type, for example, CustomLocation.",
            required=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.cni_bgp_configuration = AAZObjectArg(
            options=["--cni-bgp-configuration"],
            arg_group="Properties",
            help="The Calico BGP configuration.",
        )
        _args_schema.ip_allocation_type = AAZStrArg(
            options=["--ip-allocation-type"],
            arg_group="Properties",
            help="The type of the IP address allocation.",
            default="DualStack",
            enum={"DualStack": "DualStack", "IPV4": "IPV4", "IPV6": "IPV6"},
        )
        _args_schema.ipv4_connected_prefix = AAZStrArg(
            options=["--ipv4-connected-prefix"],
            arg_group="Properties",
            help="The IPV4 prefix (CIDR) assigned to this default CNI network. It is required when the IP allocation type is IPV4 or DualStack.",
        )
        _args_schema.ipv6_connected_prefix = AAZStrArg(
            options=["--ipv6-connected-prefix"],
            arg_group="Properties",
            help="The IPV6 prefix (CIDR) assigned to this default CNI network. It is required when the IP allocation type is IPV6 or DualStack.",
        )
        _args_schema.l3_isolation_domain_id = AAZStrArg(
            options=["--l3-isolation-domain-id"],
            arg_group="Properties",
            help="The resource ID of the Network Fabric l3IsolationDomain.",
            required=True,
        )
        _args_schema.vlan = AAZIntArg(
            options=["--vlan"],
            arg_group="Properties",
            help="The VLAN from the l3IsolationDomain that is used for this network.",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=4094,
                minimum=1,
            ),
        )

        cni_bgp_configuration = cls._args_schema.cni_bgp_configuration
        cni_bgp_configuration.bgp_peers = AAZListArg(
            options=["bgp-peers"],
            help="The list of BgpPeer entities that the Hybrid AKS cluster will peer with in addition to peering that occurs automatically with the switch fabric.",
        )
        cni_bgp_configuration.community_advertisements = AAZListArg(
            options=["community-advertisements"],
            help="The list of prefix community advertisement properties. Each prefix community specifies a prefix, and the communities that should be associated with that prefix when it is announced.",
        )
        cni_bgp_configuration.node_mesh_password = AAZStrArg(
            options=["node-mesh-password"],
            help="The password of the Calico node mesh. It defaults to a randomly-generated string when not provided.",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9]{0,80}$",
                max_length=80,
            ),
        )
        cni_bgp_configuration.service_external_prefixes = AAZListArg(
            options=["service-external-prefixes"],
            help="The subnet blocks in CIDR format for Kubernetes service external IPs to be advertised over BGP.",
        )
        cni_bgp_configuration.service_load_balancer_prefixes = AAZListArg(
            options=["service-load-balancer-prefixes"],
            help="The subnet blocks in CIDR format for Kubernetes load balancers. Load balancer IPs will only be advertised if they are within one of these blocks.",
        )

        bgp_peers = cls._args_schema.cni_bgp_configuration.bgp_peers
        bgp_peers.Element = AAZObjectArg()

        _element = cls._args_schema.cni_bgp_configuration.bgp_peers.Element
        _element.as_number = AAZIntArg(
            options=["as-number"],
            help="The ASN (Autonomous System Number) of the BGP peer.",
            required=True,
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=0,
            ),
        )
        _element.password = AAZStrArg(
            options=["password"],
            help="The password for this peering neighbor. It defaults to no password if not specified.",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9]{0,80}$",
                max_length=80,
            ),
        )
        _element.peer_ip = AAZStrArg(
            options=["peer-ip"],
            help="The IPv4 or IPv6 address to peer with the associated CNI Network. The IP version type will drive a peering with the same version type from the Default CNI Network. For example, IPv4 to IPv4 or IPv6 to IPv6.",
            required=True,
        )

        community_advertisements = cls._args_schema.cni_bgp_configuration.community_advertisements
        community_advertisements.Element = AAZObjectArg()

        _element = cls._args_schema.cni_bgp_configuration.community_advertisements.Element
        _element.communities = AAZListArg(
            options=["communities"],
            help="The list of community strings to announce with this prefix.",
            required=True,
        )
        _element.subnet_prefix = AAZStrArg(
            options=["subnet-prefix"],
            help="The subnet in CIDR format for which properties should be advertised.",
            required=True,
        )

        communities = cls._args_schema.cni_bgp_configuration.community_advertisements.Element.communities
        communities.Element = AAZStrArg()

        service_external_prefixes = cls._args_schema.cni_bgp_configuration.service_external_prefixes
        service_external_prefixes.Element = AAZStrArg()

        service_load_balancer_prefixes = cls._args_schema.cni_bgp_configuration.service_load_balancer_prefixes
        service_load_balancer_prefixes.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.DefaultCniNetworksCreateOrUpdate(ctx=self.ctx)()
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

    class DefaultCniNetworksCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/defaultCniNetworks/{defaultCniNetworkName}",
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
                    "defaultCniNetworkName", self.ctx.args.default_cni_network_name,
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
                    "api-version", "2022-12-12-preview",
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
            _builder.set_prop("extendedLocation", AAZObjectType, ".extended_location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            extended_location = _builder.get(".extendedLocation")
            if extended_location is not None:
                extended_location.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                extended_location.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("cniBgpConfiguration", AAZObjectType, ".cni_bgp_configuration")
                properties.set_prop("ipAllocationType", AAZStrType, ".ip_allocation_type")
                properties.set_prop("ipv4ConnectedPrefix", AAZStrType, ".ipv4_connected_prefix")
                properties.set_prop("ipv6ConnectedPrefix", AAZStrType, ".ipv6_connected_prefix")
                properties.set_prop("l3IsolationDomainId", AAZStrType, ".l3_isolation_domain_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("vlan", AAZIntType, ".vlan", typ_kwargs={"flags": {"required": True}})

            cni_bgp_configuration = _builder.get(".properties.cniBgpConfiguration")
            if cni_bgp_configuration is not None:
                cni_bgp_configuration.set_prop("bgpPeers", AAZListType, ".bgp_peers")
                cni_bgp_configuration.set_prop("communityAdvertisements", AAZListType, ".community_advertisements")
                cni_bgp_configuration.set_prop("nodeMeshPassword", AAZStrType, ".node_mesh_password", typ_kwargs={"flags": {"secret": True}})
                cni_bgp_configuration.set_prop("serviceExternalPrefixes", AAZListType, ".service_external_prefixes")
                cni_bgp_configuration.set_prop("serviceLoadBalancerPrefixes", AAZListType, ".service_load_balancer_prefixes")

            bgp_peers = _builder.get(".properties.cniBgpConfiguration.bgpPeers")
            if bgp_peers is not None:
                bgp_peers.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.cniBgpConfiguration.bgpPeers[]")
            if _elements is not None:
                _elements.set_prop("asNumber", AAZIntType, ".as_number", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("password", AAZStrType, ".password", typ_kwargs={"flags": {"secret": True}})
                _elements.set_prop("peerIp", AAZStrType, ".peer_ip", typ_kwargs={"flags": {"required": True}})

            community_advertisements = _builder.get(".properties.cniBgpConfiguration.communityAdvertisements")
            if community_advertisements is not None:
                community_advertisements.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.cniBgpConfiguration.communityAdvertisements[]")
            if _elements is not None:
                _elements.set_prop("communities", AAZListType, ".communities", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("subnetPrefix", AAZStrType, ".subnet_prefix", typ_kwargs={"flags": {"required": True}})

            communities = _builder.get(".properties.cniBgpConfiguration.communityAdvertisements[].communities")
            if communities is not None:
                communities.set_elements(AAZStrType, ".")

            service_external_prefixes = _builder.get(".properties.cniBgpConfiguration.serviceExternalPrefixes")
            if service_external_prefixes is not None:
                service_external_prefixes.set_elements(AAZStrType, ".")

            service_load_balancer_prefixes = _builder.get(".properties.cniBgpConfiguration.serviceLoadBalancerPrefixes")
            if service_load_balancer_prefixes is not None:
                service_load_balancer_prefixes.set_elements(AAZStrType, ".")

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
            _schema_on_200_201.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
                flags={"required": True},
            )
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200_201.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            properties.cni_as_number = AAZIntType(
                serialized_name="cniAsNumber",
                flags={"read_only": True},
            )
            properties.cni_bgp_configuration = AAZObjectType(
                serialized_name="cniBgpConfiguration",
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.fabric_bgp_peers = AAZListType(
                serialized_name="fabricBgpPeers",
                flags={"read_only": True},
            )
            properties.hybrid_aks_clusters_associated_ids = AAZListType(
                serialized_name="hybridAksClustersAssociatedIds",
                flags={"read_only": True},
            )
            properties.interface_name = AAZStrType(
                serialized_name="interfaceName",
                flags={"read_only": True},
            )
            properties.ip_allocation_type = AAZStrType(
                serialized_name="ipAllocationType",
            )
            properties.ipv4_connected_prefix = AAZStrType(
                serialized_name="ipv4ConnectedPrefix",
            )
            properties.ipv6_connected_prefix = AAZStrType(
                serialized_name="ipv6ConnectedPrefix",
            )
            properties.l3_isolation_domain_id = AAZStrType(
                serialized_name="l3IsolationDomainId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.vlan = AAZIntType(
                flags={"required": True},
            )

            cni_bgp_configuration = cls._schema_on_200_201.properties.cni_bgp_configuration
            cni_bgp_configuration.bgp_peers = AAZListType(
                serialized_name="bgpPeers",
            )
            cni_bgp_configuration.community_advertisements = AAZListType(
                serialized_name="communityAdvertisements",
            )
            cni_bgp_configuration.service_external_prefixes = AAZListType(
                serialized_name="serviceExternalPrefixes",
            )
            cni_bgp_configuration.service_load_balancer_prefixes = AAZListType(
                serialized_name="serviceLoadBalancerPrefixes",
            )

            bgp_peers = cls._schema_on_200_201.properties.cni_bgp_configuration.bgp_peers
            bgp_peers.Element = AAZObjectType()
            _CreateHelper._build_schema_bgp_peer_read(bgp_peers.Element)

            community_advertisements = cls._schema_on_200_201.properties.cni_bgp_configuration.community_advertisements
            community_advertisements.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.cni_bgp_configuration.community_advertisements.Element
            _element.communities = AAZListType(
                flags={"required": True},
            )
            _element.subnet_prefix = AAZStrType(
                serialized_name="subnetPrefix",
                flags={"required": True},
            )

            communities = cls._schema_on_200_201.properties.cni_bgp_configuration.community_advertisements.Element.communities
            communities.Element = AAZStrType()

            service_external_prefixes = cls._schema_on_200_201.properties.cni_bgp_configuration.service_external_prefixes
            service_external_prefixes.Element = AAZStrType()

            service_load_balancer_prefixes = cls._schema_on_200_201.properties.cni_bgp_configuration.service_load_balancer_prefixes
            service_load_balancer_prefixes.Element = AAZStrType()

            fabric_bgp_peers = cls._schema_on_200_201.properties.fabric_bgp_peers
            fabric_bgp_peers.Element = AAZObjectType()
            _CreateHelper._build_schema_bgp_peer_read(fabric_bgp_peers.Element)

            hybrid_aks_clusters_associated_ids = cls._schema_on_200_201.properties.hybrid_aks_clusters_associated_ids
            hybrid_aks_clusters_associated_ids.Element = AAZStrType()

            system_data = cls._schema_on_200_201.system_data
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

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    _schema_bgp_peer_read = None

    @classmethod
    def _build_schema_bgp_peer_read(cls, _schema):
        if cls._schema_bgp_peer_read is not None:
            _schema.as_number = cls._schema_bgp_peer_read.as_number
            _schema.peer_ip = cls._schema_bgp_peer_read.peer_ip
            return

        cls._schema_bgp_peer_read = _schema_bgp_peer_read = AAZObjectType()

        bgp_peer_read = _schema_bgp_peer_read
        bgp_peer_read.as_number = AAZIntType(
            serialized_name="asNumber",
            flags={"required": True},
        )
        bgp_peer_read.peer_ip = AAZStrType(
            serialized_name="peerIp",
            flags={"required": True},
        )

        _schema.as_number = cls._schema_bgp_peer_read.as_number
        _schema.peer_ip = cls._schema_bgp_peer_read.peer_ip


__all__ = ["Create"]
