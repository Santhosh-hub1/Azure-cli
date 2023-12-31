# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import json
from azext_aks_preview.azuremonitormetrics.constants import DC_API
from azext_aks_preview.azuremonitormetrics.dc.defaults import get_default_dcra_name
from knack.util import CLIError


def create_dcra(cmd, cluster_region, cluster_subscription, cluster_resource_group_name, cluster_name, dcr_resource_id):
    from azure.cli.core.util import send_raw_request
    cluster_resource_id = "/subscriptions/{0}/resourceGroups/{1}/providers/Microsoft.ContainerService/managedClusters/{2}".format(
        cluster_subscription,
        cluster_resource_group_name,
        cluster_name
    )
    dcra_name = get_default_dcra_name(cmd, cluster_region, cluster_name)
    dcra_resource_id = "/subscriptions/{0}/resourceGroups/{1}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{2}".format(
        cluster_subscription,
        cluster_resource_group_name,
        dcra_name
    )
    # only create or delete the association between the DCR and cluster
    association_body = json.dumps({"location": cluster_region,
                                   "properties": {
                                       "dataCollectionRuleId": dcr_resource_id,
                                       "description": "Promtheus data collection association between DCR, DCE and target AKS resource"
                                   }})
    armendpoint = cmd.cli_ctx.cloud.endpoints.resource_manager
    association_url = f"{armendpoint}{cluster_resource_id}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{dcra_name}?api-version={DC_API}"
    try:
        headers = ['User-Agent=azuremonitormetrics.create_dcra']
        send_raw_request(cmd.cli_ctx, "PUT", association_url,
                         body=association_body, headers=headers)
        return dcra_resource_id
    except CLIError as error:
        raise error
