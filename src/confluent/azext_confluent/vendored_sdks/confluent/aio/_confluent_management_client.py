# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import ConfluentManagementClientConfiguration
from .operations import MarketplaceAgreementsOperations
from .operations import OrganizationOperationsOperations
from .operations import OrganizationOperations
from .operations import ValidationsOperations
from .. import models


class ConfluentManagementClient(object):
    """ConfluentManagementClient.

    :ivar marketplace_agreements: MarketplaceAgreementsOperations operations
    :vartype marketplace_agreements: azure.mgmt.confluent.aio.operations.MarketplaceAgreementsOperations
    :ivar organization_operations: OrganizationOperationsOperations operations
    :vartype organization_operations: azure.mgmt.confluent.aio.operations.OrganizationOperationsOperations
    :ivar organization: OrganizationOperations operations
    :vartype organization: azure.mgmt.confluent.aio.operations.OrganizationOperations
    :ivar validations: ValidationsOperations operations
    :vartype validations: azure.mgmt.confluent.aio.operations.ValidationsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Microsoft Azure subscription id.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ConfluentManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.marketplace_agreements = MarketplaceAgreementsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.organization_operations = OrganizationOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.organization = OrganizationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.validations = ValidationsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ConfluentManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
