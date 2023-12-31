# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_purview_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_purview.vendored_sdks.purview import PurviewManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   PurviewManagementClient)


def cf_account(cli_ctx, *_):
    return cf_purview_cl(cli_ctx).accounts


def cf_default_account(cli_ctx, *_):
    return cf_purview_cl(cli_ctx).default_accounts
