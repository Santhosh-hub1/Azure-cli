# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from knack.help_files import helps


helps['confluent'] = """
    type: group
    short-summary: Manage confluent resources
"""

helps['confluent terms'] = """
    type: group
    short-summary: Manage marketplace agreement with confluent. This command group will be deprecated, please use 'az term' instead.
"""

helps['confluent terms list'] = """
    type: command
    short-summary: "List Confluent marketplace agreements in the subscription. This command will be deprecated, please use 'az term show' instead."
    examples:
      - name: MarketplaceAgreements_List
        text: |-
               az confluent terms list
"""

helps['confluent organization create'] = """
    type: command
    short-summary: "Create Organization resource."
    examples:
      - name: Create organization
        text: |-
               az confluent organization create --location "West US" --tags Environment="Dev" --name "myOrganization" \
--resource-group "myResourceGroup" --offer-id "confluent-cloud-azure-prod" --plan-id "confluent-cloud-azure-payg-prod" \
--plan-name "Confluent Cloud - Pay as you Go" --publisher-id "confluentinc" --term-unit "P1M"
"""

helps['confluent organization show'] = """
    type: command
    short-summary: "Get the properties of a specific Organization resource."
    examples:
      - name: Show organization
        text: |-
               az confluent organization show --name "myOrganization" --resource-group "myResourceGroup"
      - name: Show organization using IDs
        text: |-
               az confluent organization show --ids "/subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Confluent/organizations/{myOrganization}"
"""

helps['confluent organization delete'] = """
    type: command
    short-summary: "Delete Organization resource."
    examples:
      - name: Delete organization
        text: |-
               az confluent organization delete --name "myOrganization" --resource-group "myResourceGroup"
      - name: Delete organization using IDs
        text: |-
               az confluent organization delete --ids "/subscriptions/{SubID}/resourceGroups/{ResourceGroup}/providers/Microsoft.Confluent/organizations/{myOrganization}"
"""

helps['confluent offer-detail'] = """
    type: group
    short-summary: Manage confluent offer details
"""

helps['confluent offer-detail show'] = """
    type: command
    short-summary: "Get the offer details for available offers."
    examples:
      - name: Show default offer details
        text: |-
               az confluent offer-detail show
"""
