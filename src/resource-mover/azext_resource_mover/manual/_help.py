# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps

helps['resource-mover'] = """
    type: group
    short-summary: Manage Resource Mover Service API
"""

helps['resource-mover move-collection'] = """
    type: group
    short-summary: Manage move-collection
"""

helps['resource-mover move-collection list'] = """
    type: command
    short-summary: "List details of the move-collections."
    examples:
      - name: List all move-collections.
        text: |-
               az resource-mover move-collection list
      - name: List all move-collections by resource group.
        text: |-
               az resource-mover move-collection list -g MyResourceGroup
"""

helps['resource-mover move-collection show'] = """
    type: command
    short-summary: "Get the details of a move-collection."
    examples:
      - name: Show information about a move-collection.
        text: |-
               az resource-mover move-collection show --name MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection create'] = """
    type: command
    short-summary: "Create a move-collection."
    parameters:
      - name: --identity
        short-summary: "Define the MSI properties of the move-collection."
        long-summary: |
            Usage: --identity type=XX principal-id=XX tenant-id=XX

            type: The type of identity used for the resource mover service.
            principal-id: The principal id.
            tenant-id: The tenant id.
    examples:
      - name: Create a move-collection with system assigned identity.
        text: |-
               az resource-mover move-collection create --identity type=SystemAssigned --location eastus2 \
--source-region eastus --target-region westus --name MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection update'] = """
    type: command
    short-summary: "Update a move-collection."
    parameters:
      - name: --identity
        short-summary: "Define the MSI properties of the move-collection."
        long-summary: |
            Usage: --identity type=XX principal-id=XX tenant-id=XX

            type: The type of identity used for the resource mover service.
            principal-id: The principal id.
            tenant-id: The tenant id.
    examples:
      - name: Update a move-collection.
        text: |-
               az resource-mover move-collection update --identity type=SystemAssigned --tags key1=value1 --name \
MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection delete'] = """
    type: command
    short-summary: "Delete a move-collection."
    examples:
      - name: Delete a move-collection.
        text: |-
               az resource-mover move-collection delete --name MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection bulk-remove'] = """
    type: command
    short-summary: "Remove the set of move-resources from move-collection."
    examples:
      - name: Remove a move-resource in a move-collection.
        text: |-
               az resource-mover move-collection bulk-remove --move-resources "/subscriptions/subID/resourceGroups/myRG/\
providers/Microsoft.Migrate/MoveCollections/movecollection1/MoveResources/moveresource1" --validate-only false --name \
MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection commit'] = """
    type: command
    short-summary: "Commit the set of resources. The commit operation is triggered on the move-resources in the move-state \
'CommitPending' or 'CommitFailed', on a successful completion the move-resource's move-state do a transition to Committed."
    examples:
      - name: Commit a move-resource.
        text: |-
               az resource-mover move-collection commit --move-resources "/subscriptions/subID/resourceGroups/myRG/provi\
ders/Microsoft.Migrate/MoveCollections/movecollection1/MoveResources/moveresource1" --validate-only false --name \
MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection discard'] = """
    type: command
    short-summary: "Discard the set of resources. The discard operation is triggered on the move-resources in the move-state \
'CommitPending' or 'DiscardFailed', on a successful completion the move-resource's move-state do a transition to MovePending."
    examples:
      - name: Discard a remove-resource.
        text: |-
               az resource-mover move-collection discard --move-resources "/subscriptions/subID/resourceGroups/myRG/prov\
iders/Microsoft.Migrate/MoveCollections/movecollection1/MoveResources/moveresource1" --validate-only false --name \
MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection initiate-move'] = """
    type: command
    short-summary: "Move the set of resources. The move operation is triggered after the move-resources are in the move-state \
'MovePending' or 'MoveFailed', on a successful completion the move-resource's move-state do a transition to CommitPending."
    examples:
      - name: Move the set of resources.
        text: |-
               az resource-mover move-collection initiate-move --move-resources "/subscriptions/subID/resourceGroups/myRG\
/providers/Microsoft.Migrate/MoveCollections/movecollection1/MoveResources/moveresource1" --validate-only false \
--name MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection list-required-for'] = """
    type: command
    short-summary: "List the move-resources for which an arm resource is required for."
    examples:
      - name: List the move-resources for which an arm resource is required for.
        text: |-
               az resource-mover move-collection list-required-for --name MyMoveCollection --resource-group MyResourceGroup \
--source-id "/subscriptions/subID/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/nic1"
"""

helps['resource-mover move-collection prepare'] = """
    type: command
    short-summary: "Prepare the set of resources. The prepare operation is on the move-resources that are in the move-state \
'PreparePending' or 'PrepareFailed', on a successful completion the move-resource's move-state do a transition to MovePending."
    examples:
      - name: Prepare a move-resource.
        text: |-
               az resource-mover move-collection prepare --move-resources "/subscriptions/subID/resourceGroups/myRG/prov\
iders/Microsoft.Migrate/MoveCollections/movecollection1/MoveResources/moveresource1" --validate-only false --name \
MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection resolve-dependency'] = """
    type: command
    short-summary: "Compute, resolve and validate the dependencies of the move-resources in the move-collection."
    examples:
      - name: Resolve the dependency of the move-resources.
        text: |-
               az resource-mover move-collection resolve-dependency --name MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-collection wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the move-collection is met.
    examples:
      - name: Pause executing next line of CLI script until the move-collection is successfully \
deleted.
        text: |-
               az resource-mover move-collection wait --name MyMoveCollection --resource-group MyResourceGroup --deleted
      - name: Pause executing next line of CLI script until the move-collection is successfully \
created.
        text: |-
               az resource-mover move-collection wait --name MyMoveCollection --resource-group MyResourceGroup --created
"""

helps['resource-mover move-resource'] = """
    type: group
    short-summary: Manage move-resource
"""

helps['resource-mover move-resource list'] = """
    type: command
    short-summary: "List the move-resources in a move-collection."
    examples:
      - name: List the move-resources in a move-collection.
        text: |-
               az resource-mover move-resource list --move-collection-name MyMoveCollection --resource-group MyResourceGroup
"""

helps['resource-mover move-resource show'] = """
    type: command
    short-summary: "Get the details of a move-resource."
    examples:
      - name: Get the details of a move-resource.
        text: |-
               az resource-mover move-resource show --move-collection-name MyMoveCollection --name \
MyMoveResource --resource-group MyResourceGroup
"""

helps['resource-mover move-resource add'] = """
    type: command
    short-summary: "Create or update a move-resource to the move-collection."
    parameters:
      - name: --depends-on-overrides
        short-summary: "The move-resource dependencies overrides."
        long-summary: |
            Usage: --depends-on-overrides id=XX target-id=XX

            id: The ARM ID of the dependent resource.
            target-id: The resource ARM ID of either the move-resource or the resource ARM ID of the \
dependent resource.

            Multiple actions can be specified by using more than one --depends-on-overrides argument.
    examples:
      - name: Add a vNet as a move-resource to the move-collection.
        text: |-
               az resource-mover move-resource add --resource-group MyResourceGroup --move-collection-name MyMoveCollection --name MoveResourceName
               --source-id "/subscriptions/subID/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/MyVNet"
               --resource-settings '{
                   "resourceType": "Microsoft.Network/virtualNetworks",
                   "targetResourceName": "MyVNet-target"
               }'

      - name: Add a vNet as a move-resource to the move-collection.
        text: |-
               az resource-mover move-resource add --resource-group MyResourceGroup --move-collection-name MyMoveCollection --name MoveResourceName
               --source-id "/subscriptions/subID/resourceGroups/myRG/providers/Microsoft.Network/virtualNetworks/MyVNet"
               --resource-settings @resource-settings.json

      - name: Add a VM as a move-resource to the move-collection.
        text: |-
               az resource-mover move-resource add --resource-group MyResourceGroup --move-collection-name MyMoveCollection --name MoveResourceName
               --source-id "/subscriptions/subID/resourceGroups/eastusRG/providers/Microsoft.Compute/virtualMachines/MyVM"
               --depends-on-overrides id="/subscriptions/subID/resourceGroups/eastusRG/providers/Microsoft.Network/networkInterfaces/MyNIC" target-id="/subscriptions/subID/resourceGroups/westusRG/providers/Microsoft.Network/networkInterfaces/MyNIC"
               --resource-settings '{
                   "resourceType": "Microsoft.Compute/virtualMachines",
                   "targetAvailabilitySetId": "/subscriptions/subID/resourceGroups/eastusRG/providers/Microsoft.Compute/availabilitySets/MyAVSet",
                   "targetAvailabilityZone": "2",
                   "targetResourceName": "MyVM-target",
                   "targetVmSize": null,
                   "userManagedIdentities": [/subscriptions/subid/resourceGroups/eastusRG/providers/Microsoft.ManagedIdentity/userAssignedIdentities/umi1]
               }'
"""

helps['resource-mover move-resource delete'] = """
    type: command
    short-summary: "Delete a move-resource from the move-collection."
    examples:
      - name: Delete a move-resource from the move-collection.
        text: |-
               az resource-mover move-resource delete --move-collection-name MyMoveCollection --name \
MyMoveResource --resource-group MyResourceGroup
"""

helps['resource-mover move-resource wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the move-resource is met.
    examples:
      - name: Pause executing next line of CLI script until the move-resource is successfully created.
        text: |-
               az resource-mover move-resource wait --move-collection-name MyMoveCollection --name \
MyMoveResource --resource-group MyResourceGroup --created
      - name: Pause executing next line of CLI script until the move-resource is successfully deleted.
        text: |-
               az resource-mover move-resource wait --move-collection-name MyMoveCollection --name \
MyMoveResource --resource-group MyResourceGroup --deleted
"""

helps['resource-mover move-collection list-unresolved-dependency'] = """
    type: command
    short-summary: "List the details of the unresolved dependencies in a move-collection."
    examples:
      - name: List the unresolved dependencies.
        text: |-
               az resource-mover move-collection list-unresolved-dependency --move-collection-name MyMoveCollection \
--resource-group MyResourceGroup
"""
