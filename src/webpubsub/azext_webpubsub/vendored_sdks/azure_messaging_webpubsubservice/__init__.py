# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

__all__ = ["build_authentication_token", "WebPubSubServiceClient"]

from copy import deepcopy
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

import jwt
import six

import azure.core.credentials as corecredentials
import azure.core.pipeline as corepipeline
import azure.core.pipeline.policies as corepolicies
import azure.core.pipeline.transport as coretransport


# Temporary location for types that eventually graduate to Azure Core
from .core import rest as corerest
from ._version import VERSION as _VERSION
from ._policies import JwtCredentialPolicy
from ._utils import UTC as _UTC

if TYPE_CHECKING:
    from azure.core.pipeline.policies import HTTPPolicy, SansIOHTTPPolicy
    from typing import Any, List, cast, Type, TypeVar

    ClientType = TypeVar("ClientType", bound="WebPubSubServiceClient")


def _parse_connection_string(connection_string, **kwargs):
    for segment in connection_string.split(";"):
        if "=" in segment:
            key, value = segment.split("=", maxsplit=1)
            key = key.lower()
            if key not in ("version", ):
                kwargs.setdefault(key, value)
        elif segment:
            raise ValueError(
                "Malformed connection string - expected 'key=value', found segment '{}' in '{}'".format(
                    segment, connection_string
                )
            )

    if "endpoint" not in kwargs:
        raise ValueError("connection_string missing 'endpoint' field")

    if "accesskey" not in kwargs:
        raise ValueError("connection_string missing 'accesskey' field")

    return kwargs

def build_authentication_token(endpoint, hub, **kwargs):
    """Build an authentication token for the given endpoint, hub using the provided key.

    :keyword endpoint: connetion string or HTTP or HTTPS endpoint for the WebPubSub service instance.
    :type endpoint: ~str
    :keyword hub: The hub to give access to.
    :type hub: ~str
    :keyword accesskey: Key to sign the token with. Required if endpoint is not a connection string
    :type accesskey: ~str
    :keyword ttl: Optional ttl timedelta for the token. Default is 1 hour.
    :type ttl: ~datetime.timedelta
    :keyword user: Optional user name (subject) for the token. Default is no user.
    :type user: ~str
    :keyword roles: Roles for the token.
    :type roles: typing.List[str]. Default is no roles.
    :returns: ~dict containing the web socket endpoint, the token and a url with the generated access token.
    :rtype: ~dict


    Example:
    >>> build_authentication_token(endpoint='https://contoso.com/api/webpubsub', hub='theHub', key='123')
    {
        'baseUrl': 'wss://contoso.com/api/webpubsub/client/hubs/theHub',
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ...',
        'url': 'wss://contoso.com/api/webpubsub/client/hubs/theHub?access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ...'
    }
    """
    if 'accesskey' not in kwargs:
        kwargs = _parse_connection_string(endpoint, **kwargs)
        endpoint = kwargs.pop('endpoint')

    user = kwargs.pop("user", None)
    key = kwargs.pop("accesskey")
    ttl = kwargs.pop("ttl", timedelta(hours=1))
    roles = kwargs.pop("roles", [])
    endpoint = endpoint.lower()
    if not endpoint.startswith("http://") and not endpoint.startswith("https://"):
        raise ValueError(
            "Invalid endpoint: '{}' has unknown scheme - expected 'http://' or 'https://'".format(
                endpoint
            )
        )

    # Ensure endpoint has no trailing slash
    endpoint = endpoint.rstrip("/")

    # Switch from http(s) to ws(s) scheme
    client_endpoint = "ws" + endpoint[4:]
    client_url = "{}/client/hubs/{}".format(client_endpoint, hub)
    audience = "{}/client/hubs/{}".format(endpoint, hub)

    payload = {
        "aud": audience,
        "iat": datetime.now(tz=_UTC),
        "exp": datetime.now(tz=_UTC) + ttl,
    }
    if user:
        payload["sub"] = user
    if roles:
        payload["role"] = roles

    token = six.ensure_str(jwt.encode(payload, key, algorithm="HS256"))
    return {
        "baseUrl": client_url,
        "token": token,
        "url": "{}?access_token={}".format(client_url, token),
    }


class WebPubSubServiceClient(object):
    def __init__(self, endpoint, credential, **kwargs):
        # type: (str, corecredentials.AzureKeyCredential, Any) -> None
        """Create a new WebPubSubServiceClient instance

        :param endpoint: Endpoint to connect to.
        :type endpoint: ~str
        :param credential: Credentials to use to connect to endpoint.
        :type credential: ~azure.core.credentials.AzureKeyCredential
        :keyword api_version: Api version to use when communicating with the service.
        :type api_version: str
        :keyword user: User to connect as. Optional.
        :type user: ~str
        """
        self.endpoint = endpoint.rstrip("/")
        transport = kwargs.pop("transport", None) or coretransport.RequestsTransport(
            **kwargs
        )
        kwargs.setdefault(
            "sdk_moniker", "messaging-webpubsubservice/{}".format(_VERSION)
        )
        policies = [
            corepolicies.HeadersPolicy(**kwargs),
            corepolicies.UserAgentPolicy(**kwargs),
            corepolicies.RetryPolicy(**kwargs),
            corepolicies.ProxyPolicy(**kwargs),
            corepolicies.CustomHookPolicy(**kwargs),
            corepolicies.RedirectPolicy(**kwargs),
            JwtCredentialPolicy(credential, kwargs.get("user", None)),
            corepolicies.NetworkTraceLoggingPolicy(**kwargs),
        ]  # type: Any
        self._pipeline = corepipeline.Pipeline(
            transport,
            policies,
        )  # type: corepipeline.Pipeline

    @classmethod
    def from_connection_string(cls, connection_string, **kwargs):
        # type: (Type[ClientType], str, Any) -> ClientType
        """Create a new WebPubSubServiceClient from a connection string.

        :param connection_string: Connection string
        :type connection_string: ~str
        :rtype: WebPubSubServiceClient
        """
        kwargs = _parse_connection_string(connection_string, **kwargs)

        kwargs["credential"] = corecredentials.AzureKeyCredential(
            kwargs.pop("accesskey")
        )
        return cls(**kwargs)

    def __repr__(self):
        return "<WebPubSubServiceClient> endpoint:'{}'".format(self.endpoint)

    def _format_url(self, url):
        # type: (str) -> str
        assert self.endpoint[-1] != "/", "My endpoint should not have a trailing slash"
        return "/".join([self.endpoint, url.lstrip("/")])

    def send_request(self, http_request, **kwargs):
        # type: (corerest.HttpRequest, Any) -> corerest.HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.messaging.webpubsub.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from azure.messaging.webpubsub.rest import build_healthapi_get_health_status_request
        >>> request = build_healthapi_get_health_status_request(api_version)
        <HttpRequest [HEAD], url: '/api/health'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/llcwiki

        For advanced cases, you can also create your own :class:`~azure.messaging.webpubsub.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.messaging.webpubsub.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.messaging.webpubsub.core.rest.HttpResponse
        """
        request_copy = deepcopy(http_request)
        request_copy.url = self._format_url(request_copy.url)

        # can't do StreamCOntextManager yet. This client doesn't have a pipeline client,
        # StreamContextManager requires a pipeline client. WIll look more into it
        # if kwargs.pop("stream_response", False):
        #     return corerest._StreamContextManager(
        #         client=self._client,
        #         request=request_copy,
        #     )
        pipeline_response = self._pipeline.run(request_copy._internal_request, **kwargs) # pylint: disable=protected-access
        response = corerest.HttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response,
        )
        response.read()
        return response
