# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class DefaultAccountsOperations:
    """DefaultAccountsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.purview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        scope_tenant_id: str,
        scope_type: Union[str, "models.ScopeType"],
        scope: Optional[str] = None,
        **kwargs
    ) -> "models.DefaultAccountPayload":
        """Gets the default account information set for the scope.

        Get the default account for the scope.

        :param scope_tenant_id: The tenant ID.
        :type scope_tenant_id: str
        :param scope_type: The scope for the default account.
        :type scope_type: str or ~azure.mgmt.purview.models.ScopeType
        :param scope: The Id of the scope object, for example if the scope is "Subscription" then it is
         the ID of that subscription.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DefaultAccountPayload, or the result of cls(response)
        :rtype: ~azure.mgmt.purview.models.DefaultAccountPayload
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DefaultAccountPayload"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-07-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['scopeTenantId'] = self._serialize.query("scope_tenant_id", scope_tenant_id, 'str')
        query_parameters['scopeType'] = self._serialize.query("scope_type", scope_type, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponseModel, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DefaultAccountPayload', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Purview/getDefaultAccount'}  # type: ignore

    async def set(
        self,
        default_account_payload: "models.DefaultAccountPayload",
        **kwargs
    ) -> "models.DefaultAccountPayload":
        """Sets the default account for the scope.

        Sets the default account for the scope.

        :param default_account_payload: The payload containing the default account information and the
         scope.
        :type default_account_payload: ~azure.mgmt.purview.models.DefaultAccountPayload
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DefaultAccountPayload, or the result of cls(response)
        :rtype: ~azure.mgmt.purview.models.DefaultAccountPayload
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DefaultAccountPayload"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-07-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.set.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(default_account_payload, 'DefaultAccountPayload')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponseModel, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DefaultAccountPayload', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    set.metadata = {'url': '/providers/Microsoft.Purview/setDefaultAccount'}  # type: ignore

    async def remove(
        self,
        scope_tenant_id: str,
        scope_type: Union[str, "models.ScopeType"],
        scope: Optional[str] = None,
        **kwargs
    ) -> None:
        """Removes the default account from the scope.

        Removes the default account from the scope.

        :param scope_tenant_id: The tenant ID.
        :type scope_tenant_id: str
        :param scope_type: The scope for the default account.
        :type scope_type: str or ~azure.mgmt.purview.models.ScopeType
        :param scope: The Id of the scope object, for example if the scope is "Subscription" then it is
         the ID of that subscription.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-07-01"
        accept = "application/json"

        # Construct URL
        url = self.remove.metadata['url']  # type: ignore

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['scopeTenantId'] = self._serialize.query("scope_tenant_id", scope_tenant_id, 'str')
        query_parameters['scopeType'] = self._serialize.query("scope_type", scope_type, 'str')
        if scope is not None:
            query_parameters['scope'] = self._serialize.query("scope", scope, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponseModel, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    remove.metadata = {'url': '/providers/Microsoft.Purview/removeDefaultAccount'}  # type: ignore
