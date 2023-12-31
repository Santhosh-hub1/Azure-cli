# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import MicrosoftStorageSyncConfiguration
from .operations import Operations
from .operations import StorageSyncServicesOperations
from .operations import SyncGroupsOperations
from .operations import CloudEndpointsOperations
from .operations import ServerEndpointsOperations
from .operations import RegisteredServersOperations
from .operations import WorkflowsOperations
from .operations import OperationStatusOperations
from . import models


class MicrosoftStorageSync(object):
    """Microsoft Storage Sync Service API.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storagesync.operations.Operations
    :ivar storage_sync_services: StorageSyncServicesOperations operations
    :vartype storage_sync_services: azure.mgmt.storagesync.operations.StorageSyncServicesOperations
    :ivar sync_groups: SyncGroupsOperations operations
    :vartype sync_groups: azure.mgmt.storagesync.operations.SyncGroupsOperations
    :ivar cloud_endpoints: CloudEndpointsOperations operations
    :vartype cloud_endpoints: azure.mgmt.storagesync.operations.CloudEndpointsOperations
    :ivar server_endpoints: ServerEndpointsOperations operations
    :vartype server_endpoints: azure.mgmt.storagesync.operations.ServerEndpointsOperations
    :ivar registered_servers: RegisteredServersOperations operations
    :vartype registered_servers: azure.mgmt.storagesync.operations.RegisteredServersOperations
    :ivar workflows: WorkflowsOperations operations
    :vartype workflows: azure.mgmt.storagesync.operations.WorkflowsOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status: azure.mgmt.storagesync.operations.OperationStatusOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MicrosoftStorageSyncConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_sync_services = StorageSyncServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sync_groups = SyncGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cloud_endpoints = CloudEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_endpoints = ServerEndpointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.registered_servers = RegisteredServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflows = WorkflowsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MicrosoftStorageSync
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
