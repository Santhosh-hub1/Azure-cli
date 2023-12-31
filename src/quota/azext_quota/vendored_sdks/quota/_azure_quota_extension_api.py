# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import AzureQuotaExtensionAPIConfiguration
from .operations import usagesOperations
from .operations import quotaOperations
from .operations import quotarequeststatusOperations
from .operations import quotaoperationOperations
from . import models


class AzureQuotaExtensionAPI(object):
    """Microsoft Azure Quota Resource Provider.

    :ivar usages: usagesOperations operations
    :vartype usages: azure_quota_extension_api.operations.usagesOperations
    :ivar quota: quotaOperations operations
    :vartype quota: azure_quota_extension_api.operations.quotaOperations
    :ivar quotarequeststatus: quotarequeststatusOperations operations
    :vartype quotarequeststatus: azure_quota_extension_api.operations.quotarequeststatusOperations
    :ivar quotaoperation: quotaoperationOperations operations
    :vartype quotaoperation: azure_quota_extension_api.operations.quotaoperationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = AzureQuotaExtensionAPIConfiguration(credential, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.usages = usagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quota = quotaOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quotarequeststatus = quotarequeststatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.quotaoperation = quotaoperationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AzureQuotaExtensionAPI
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
