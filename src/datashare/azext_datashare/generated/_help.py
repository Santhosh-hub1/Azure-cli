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


helps['datashare'] = '''
    type: group
    short-summary: Manage Data Share
'''

helps['datashare account'] = """
    type: group
    short-summary: Manage account with datashare
"""

helps['datashare account list'] = """
    type: command
    short-summary: "List Accounts in ResourceGroup And List Accounts in Subscription."
    examples:
      - name: Accounts_ListByResourceGroup
        text: |-
               az datashare account list --resource-group "SampleResourceGroup"
      - name: Accounts_ListBySubscription
        text: |-
               az datashare account list
"""

helps['datashare account show'] = """
    type: command
    short-summary: "Get an account."
    examples:
      - name: Accounts_Get
        text: |-
               az datashare account show --name "Account1" --resource-group "SampleResourceGroup"
"""

helps['datashare account create'] = """
    type: command
    short-summary: "Create an account."
    examples:
      - name: Accounts_Create
        text: |-
               az datashare account create --location "West US 2" --tags tag1="Red" tag2="White" --name "Account1" \
--resource-group "SampleResourceGroup"
"""

helps['datashare account update'] = """
    type: command
    short-summary: "Patch an account."
    examples:
      - name: Accounts_Update
        text: |-
               az datashare account update --name "Account1" --tags tag1="Red" tag2="White" --resource-group \
"SampleResourceGroup"
"""

helps['datashare account delete'] = """
    type: command
    short-summary: "DeleteAccount."
    examples:
      - name: Accounts_Delete
        text: |-
               az datashare account delete --name "Account1" --resource-group "SampleResourceGroup"
"""

helps['datashare account wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datashare account is met.
    examples:
      - name: Pause executing next line of CLI script until the datashare account is successfully created.
        text: |-
               az datashare account wait --name "Account1" --resource-group "SampleResourceGroup" --created
      - name: Pause executing next line of CLI script until the datashare account is successfully deleted.
        text: |-
               az datashare account wait --name "Account1" --resource-group "SampleResourceGroup" --deleted
"""

helps['datashare consumer-invitation'] = """
    type: group
    short-summary: Manage consumer invitation with datashare
"""

helps['datashare consumer-invitation show'] = """
    type: command
    short-summary: "Get an invitation."
    examples:
      - name: ConsumerInvitations_Get
        text: |-
               az datashare consumer-invitation show --invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" --location \
"East US 2"
"""

helps['datashare consumer-invitation list-invitation'] = """
    type: command
    short-summary: "Lists invitations."
    examples:
      - name: ConsumerInvitations_ListInvitations
        text: |-
               az datashare consumer-invitation list-invitation
"""

helps['datashare consumer-invitation reject-invitation'] = """
    type: command
    short-summary: "Reject an invitation."
    examples:
      - name: ConsumerInvitations_RejectInvitation
        text: |-
               az datashare consumer-invitation reject-invitation --invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03\
" --location "East US 2"
"""

helps['datashare data-set'] = """
    type: group
    short-summary: Manage data set with datashare
"""

helps['datashare data-set list'] = """
    type: command
    short-summary: "List DataSets in a share."
    examples:
      - name: DataSets_ListByShare
        text: |-
               az datashare data-set list --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-name "Share1"
"""

helps['datashare data-set show'] = """
    type: command
    short-summary: "Get a DataSet in a share."
    examples:
      - name: DataSets_Get
        text: |-
               az datashare data-set show --account-name "Account1" --name "Dataset1" --resource-group \
"SampleResourceGroup" --share-name "Share1"
"""

helps['datashare data-set create'] = """
    type: command
    short-summary: "Create a DataSet."
    examples:
      - name: DataSets_Create
        text: |-
               az datashare data-set create --account-name "Account1" --data-set "{\\"kind\\":\\"Blob\\",\\"properties\
\\":{\\"containerName\\":\\"C1\\",\\"filePath\\":\\"file21\\",\\"resourceGroup\\":\\"SampleResourceGroup\\",\\"storageA\
ccountName\\":\\"storage2\\",\\"subscriptionId\\":\\"433a8dfd-e5d5-4e77-ad86-90acdc75eb1a\\"}}" --name "Dataset1" \
--resource-group "SampleResourceGroup" --share-name "Share1"
      - name: DataSets_KustoCluster_Create
        text: |-
               az datashare data-set create --account-name "Account1" --data-set "{\\"kind\\":\\"KustoCluster\\",\\"pro\
perties\\":{\\"kustoClusterResourceId\\":\\"/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleRe\
sourceGroup/providers/Microsoft.Kusto/clusters/Cluster1\\"}}" --name "Dataset1" --resource-group "SampleResourceGroup" \
--share-name "Share1"
      - name: DataSets_KustoDatabase_Create
        text: |-
               az datashare data-set create --account-name "Account1" --data-set "{\\"kind\\":\\"KustoDatabase\\",\\"pr\
operties\\":{\\"kustoDatabaseResourceId\\":\\"/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/Sample\
ResourceGroup/providers/Microsoft.Kusto/clusters/Cluster1/databases/Database1\\"}}" --name "Dataset1" --resource-group \
"SampleResourceGroup" --share-name "Share1"
      - name: DataSets_KustoTable_Create
        text: |-
               az datashare data-set create --account-name "Account1" --data-set "{\\"kind\\":\\"KustoTable\\",\\"prope\
rties\\":{\\"kustoDatabaseResourceId\\":\\"/subscriptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleRes\
ourceGroup/providers/Microsoft.Kusto/clusters/Cluster1/databases/Database1\\",\\"tableLevelSharingProperties\\":{\\"ext\
ernalTablesToExclude\\":[\\"test11\\",\\"test12\\"],\\"externalTablesToInclude\\":[\\"test9\\",\\"test10\\"],\\"materia\
lizedViewsToExclude\\":[\\"test7\\",\\"test8\\"],\\"materializedViewsToInclude\\":[\\"test5\\",\\"test6\\"],\\"tablesTo\
Exclude\\":[\\"test3\\",\\"test4\\"],\\"tablesToInclude\\":[\\"test1\\",\\"test2\\"]}}}" --name "Dataset1" \
--resource-group "SampleResourceGroup" --share-name "Share1"
      - name: DataSets_SqlDBTable_Create
        text: |-
               az datashare data-set create --account-name "Account1" --data-set "{\\"kind\\":\\"SqlDBTable\\",\\"prope\
rties\\":{\\"databaseName\\":\\"SqlDB1\\",\\"schemaName\\":\\"dbo\\",\\"sqlServerResourceId\\":\\"/subscriptions/433a8d\
fd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleResourceGroup/providers/Microsoft.Sql/servers/Server1\\",\\"tableNa\
me\\":\\"Table1\\"}}" --name "Dataset1" --resource-group "SampleResourceGroup" --share-name "Share1"
      - name: DataSets_SqlDWTable_Create
        text: |-
               az datashare data-set create --account-name "Account1" --data-set "{\\"kind\\":\\"SqlDWTable\\",\\"prope\
rties\\":{\\"dataWarehouseName\\":\\"DataWarehouse1\\",\\"schemaName\\":\\"dbo\\",\\"sqlServerResourceId\\":\\"/subscri\
ptions/433a8dfd-e5d5-4e77-ad86-90acdc75eb1a/resourceGroups/SampleResourceGroup/providers/Microsoft.Sql/servers/Server1\
\\",\\"tableName\\":\\"Table1\\"}}" --name "Dataset1" --resource-group "SampleResourceGroup" --share-name "Share1"
      - name: DataSets_SynapseWorkspaceSqlPoolTable_Create
        text: |-
               az datashare data-set create --account-name "sourceAccount" --data-set "{\\"kind\\":\\"SynapseWorkspaceS\
qlPoolTable\\",\\"properties\\":{\\"synapseWorkspaceSqlPoolTableResourceId\\":\\"/subscriptions/0f3dcfc3-18f8-4099-b381\
-8353e19d43a7/resourceGroups/SampleResourceGroup/providers/Microsoft.Synapse/workspaces/ExampleWorkspace/sqlPools/Examp\
leSqlPool/schemas/dbo/tables/table1\\"}}" --name "dataset1" --resource-group "SampleResourceGroup" --share-name \
"share1"
"""

helps['datashare data-set delete'] = """
    type: command
    short-summary: "Delete a DataSet in a share."
    examples:
      - name: DataSets_Delete
        text: |-
               az datashare data-set delete --account-name "Account1" --name "Dataset1" --resource-group \
"SampleResourceGroup" --share-name "Share1"
"""

helps['datashare data-set wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datashare data-set is met.
    examples:
      - name: Pause executing next line of CLI script until the datashare data-set is successfully deleted.
        text: |-
               az datashare data-set wait --account-name "Account1" --name "Dataset1" --resource-group \
"SampleResourceGroup" --share-name "Share1" --deleted
"""

helps['datashare data-set-mapping'] = """
    type: group
    short-summary: Manage data set mapping with datashare
"""

helps['datashare data-set-mapping list'] = """
    type: command
    short-summary: "List DataSetMappings in a share subscription."
    examples:
      - name: DataSetMappings_ListByShareSubscription
        text: |-
               az datashare data-set-mapping list --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-subscription-name "ShareSubscription1"
"""

helps['datashare data-set-mapping show'] = """
    type: command
    short-summary: "Get a DataSetMapping in a shareSubscription."
    examples:
      - name: DataSetMappings_Get
        text: |-
               az datashare data-set-mapping show --account-name "Account1" --name "DatasetMapping1" --resource-group \
"SampleResourceGroup" --share-subscription-name "ShareSubscription1"
"""

helps['datashare data-set-mapping create'] = """
    type: command
    short-summary: "Create a DataSetMapping."
    parameters:
      - name: --adls-gen2-file-data-set-mapping
        short-summary: "An ADLS Gen2 file data set mapping."
        long-summary: |
            Usage: --adls-gen2-file-data-set-mapping data-set-id=XX file-path=XX file-system=XX output-type=XX \
resource-group=XX storage-account-name=XX subscription-id=XX kind=XX

            data-set-id: Required. The id of the source data set.
            file-path: Required. File path within the file system.
            file-system: Required. File system to which the file belongs.
            output-type: Type of output file
            resource-group: Required. Resource group of storage account.
            storage-account-name: Required. Storage account name of the source data set.
            subscription-id: Required. Subscription id of storage account.
            kind: Required. Kind of data set mapping.
      - name: --adls-gen2-file-system-data-set-mapping
        short-summary: "An ADLS Gen2 file system data set mapping."
        long-summary: |
            Usage: --adls-gen2-file-system-data-set-mapping data-set-id=XX file-system=XX resource-group=XX \
storage-account-name=XX subscription-id=XX kind=XX

            data-set-id: Required. The id of the source data set.
            file-system: Required. The file system name.
            resource-group: Required. Resource group of storage account.
            storage-account-name: Required. Storage account name of the source data set.
            subscription-id: Required. Subscription id of storage account.
            kind: Required. Kind of data set mapping.
      - name: --adls-gen2-folder-data-set-mapping
        short-summary: "An ADLS Gen2 folder data set mapping."
        long-summary: |
            Usage: --adls-gen2-folder-data-set-mapping data-set-id=XX file-system=XX folder-path=XX resource-group=XX \
storage-account-name=XX subscription-id=XX kind=XX

            data-set-id: Required. The id of the source data set.
            file-system: Required. File system to which the folder belongs.
            folder-path: Required. Folder path within the file system.
            resource-group: Required. Resource group of storage account.
            storage-account-name: Required. Storage account name of the source data set.
            subscription-id: Required. Subscription id of storage account.
            kind: Required. Kind of data set mapping.
      - name: --blob-container-data-set-mapping
        short-summary: "A Blob container data set mapping."
        long-summary: |
            Usage: --blob-container-data-set-mapping container-name=XX data-set-id=XX resource-group=XX \
storage-account-name=XX subscription-id=XX kind=XX

            container-name: Required. BLOB Container name.
            data-set-id: Required. The id of the source data set.
            resource-group: Required. Resource group of storage account.
            storage-account-name: Required. Storage account name of the source data set.
            subscription-id: Required. Subscription id of storage account.
            kind: Required. Kind of data set mapping.
      - name: --blob-data-set-mapping
        short-summary: "A Blob data set mapping."
        long-summary: |
            Usage: --blob-data-set-mapping container-name=XX data-set-id=XX file-path=XX output-type=XX \
resource-group=XX storage-account-name=XX subscription-id=XX kind=XX

            container-name: Required. Container that has the file path.
            data-set-id: Required. The id of the source data set.
            file-path: Required. File path within the source data set
            output-type: File output type
            resource-group: Required. Resource group of storage account.
            storage-account-name: Required. Storage account name of the source data set.
            subscription-id: Required. Subscription id of storage account.
            kind: Required. Kind of data set mapping.
      - name: --blob-folder-data-set-mapping
        short-summary: "A Blob folder data set mapping."
        long-summary: |
            Usage: --blob-folder-data-set-mapping container-name=XX data-set-id=XX prefix=XX resource-group=XX \
storage-account-name=XX subscription-id=XX kind=XX

            container-name: Required. Container that has the file path.
            data-set-id: Required. The id of the source data set.
            prefix: Required. Prefix for blob folder
            resource-group: Required. Resource group of storage account.
            storage-account-name: Required. Storage account name of the source data set.
            subscription-id: Required. Subscription id of storage account.
            kind: Required. Kind of data set mapping.
      - name: --kusto-cluster-data-set-mapping
        short-summary: "A Kusto cluster data set mapping"
        long-summary: |
            Usage: --kusto-cluster-data-set-mapping data-set-id=XX kusto-cluster-resource-id=XX kind=XX

            data-set-id: Required. The id of the source data set.
            kusto-cluster-resource-id: Required. Resource id of the sink kusto cluster.
            kind: Required. Kind of data set mapping.
      - name: --kusto-database-data-set-mapping
        short-summary: "A Kusto database data set mapping"
        long-summary: |
            Usage: --kusto-database-data-set-mapping data-set-id=XX kusto-cluster-resource-id=XX kind=XX

            data-set-id: Required. The id of the source data set.
            kusto-cluster-resource-id: Required. Resource id of the sink kusto cluster.
            kind: Required. Kind of data set mapping.
      - name: --kusto-table-data-set-mapping
        short-summary: "A Kusto database data set mapping"
        long-summary: |
            Usage: --kusto-table-data-set-mapping data-set-id=XX kusto-cluster-resource-id=XX kind=XX

            data-set-id: Required. The id of the source data set.
            kusto-cluster-resource-id: Required. Resource id of the sink kusto cluster.
            kind: Required. Kind of data set mapping.
      - name: --sqldb-table-data-set-mapping
        short-summary: "A SQL DB Table data set mapping."
        long-summary: |
            Usage: --sqldb-table-data-set-mapping database-name=XX data-set-id=XX schema-name=XX \
sql-server-resource-id=XX table-name=XX kind=XX

            database-name: Required. DatabaseName name of the sink data set
            data-set-id: Required. The id of the source data set.
            schema-name: Required. Schema of the table. Default value is dbo.
            sql-server-resource-id: Required. Resource id of SQL server
            table-name: Required. SQL DB table name.
            kind: Required. Kind of data set mapping.
      - name: --sqldw-table-data-set-mapping
        short-summary: "A SQL DW Table data set mapping."
        long-summary: |
            Usage: --sqldw-table-data-set-mapping data-set-id=XX data-warehouse-name=XX schema-name=XX \
sql-server-resource-id=XX table-name=XX kind=XX

            data-set-id: Required. The id of the source data set.
            data-warehouse-name: Required. DataWarehouse name of the source data set
            schema-name: Required. Schema of the table. Default value is dbo.
            sql-server-resource-id: Required. Resource id of SQL server
            table-name: Required. SQL DW table name.
            kind: Required. Kind of data set mapping.
      - name: --synapse-workspace-sql-pool-table-data-set-mapping
        short-summary: "A Synapse Workspace Sql Pool Table data set mapping"
        long-summary: |
            Usage: --synapse-workspace-sql-pool-table-data-set-mapping data-set-id=XX synapse-workspace-sql-pool-table-\
resource-id=XX kind=XX

            data-set-id: Required. The id of the source data set.
            synapse-workspace-sql-pool-table-resource-id: Required. Resource id of the Synapse Workspace SQL Pool \
Table
            kind: Required. Kind of data set mapping.
    examples:
      - name: DataSetMappings_SqlDWDataSetToAdlsGen2File_Create
        text: |-
               az datashare data-set-mapping create --account-name "Account1" --adls-gen2-file-data-set-mapping \
data-set-id="a08f184b-0567-4b11-ba22-a1199336d226" file-path="file21" file-system="fileSystem" output-type="Csv" \
resource-group="SampleResourceGroup" storage-account-name="storage2" subscription-id="433a8dfd-e5d5-4e77-ad86-90acdc75e\
b1a" --name "DatasetMapping1" --resource-group "SampleResourceGroup" --share-subscription-name "ShareSubscription1"
"""

helps['datashare data-set-mapping delete'] = """
    type: command
    short-summary: "Delete a DataSetMapping in a shareSubscription."
    examples:
      - name: DataSetMappings_Delete
        text: |-
               az datashare data-set-mapping delete --account-name "Account1" --name "DatasetMapping1" \
--resource-group "SampleResourceGroup" --share-subscription-name "ShareSubscription1"
"""

helps['datashare email-registration'] = """
    type: group
    short-summary: Manage email registration with datashare
"""

helps['datashare email-registration activate-email'] = """
    type: command
    short-summary: "Activate the email registration for the current tenant."
    examples:
      - name: EmailRegistrations_ActivateEmail
        text: |-
               az datashare email-registration activate-email --activation-code "djsfhakj2lekowd3wepfklpwe9lpflcd" \
--location "East US 2"
"""

helps['datashare email-registration register-email'] = """
    type: command
    short-summary: "Register an email for the current tenant."
    examples:
      - name: EmailRegistrations_RegisterEmail
        text: |-
               az datashare email-registration register-email --location "East US 2"
"""

helps['datashare invitation'] = """
    type: group
    short-summary: Manage invitation with datashare
"""

helps['datashare invitation list'] = """
    type: command
    short-summary: "List invitations in a share."
    examples:
      - name: Invitations_ListByShare
        text: |-
               az datashare invitation list --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-name "Share1"
"""

helps['datashare invitation show'] = """
    type: command
    short-summary: "Get an invitation in a share."
    examples:
      - name: Invitations_Get
        text: |-
               az datashare invitation show --account-name "Account1" --name "Invitation1" --resource-group \
"SampleResourceGroup" --share-name "Share1"
"""

helps['datashare invitation create'] = """
    type: command
    short-summary: "Create an invitation."
    examples:
      - name: Invitations_Create
        text: |-
               az datashare invitation create --account-name "Account1" --expiration-date \
"2020-08-26T22:33:24.5785265Z" --target-email "receiver@microsoft.com" --name "Invitation1" --resource-group \
"SampleResourceGroup" --share-name "Share1"
"""

helps['datashare invitation delete'] = """
    type: command
    short-summary: "Delete an invitation in a share."
    examples:
      - name: Invitations_Delete
        text: |-
               az datashare invitation delete --account-name "Account1" --name "Invitation1" --resource-group \
"SampleResourceGroup" --share-name "Share1"
"""

helps['datashare list'] = """
    type: command
    short-summary: "List shares in an account."
    examples:
      - name: Shares_ListByAccount
        text: |-
               az datashare list --account-name "Account1" --resource-group "SampleResourceGroup"
"""

helps['datashare show'] = """
    type: command
    short-summary: "Get a share."
    examples:
      - name: Shares_Get
        text: |-
               az datashare show --account-name "Account1" --resource-group "SampleResourceGroup" --name "Share1"
"""

helps['datashare create'] = """
    type: command
    short-summary: "Create a share."
    examples:
      - name: Shares_Create
        text: |-
               az datashare create --account-name "Account1" --resource-group "SampleResourceGroup" --description \
"share description" --share-kind "CopyBased" --terms "Confidential" --name "Share1"
"""

helps['datashare delete'] = """
    type: command
    short-summary: "Delete a share."
    examples:
      - name: Shares_Delete
        text: |-
               az datashare delete --account-name "Account1" --resource-group "SampleResourceGroup" --name "Share1"
"""

helps['datashare list-synchronization'] = """
    type: command
    short-summary: "List synchronizations of a share."
    examples:
      - name: Shares_ListSynchronizations
        text: |-
               az datashare list-synchronization --account-name "Account1" --resource-group "SampleResourceGroup" \
--name "Share1"
"""

helps['datashare list-synchronization-detail'] = """
    type: command
    short-summary: "List synchronization details."
    examples:
      - name: Shares_ListSynchronizationDetails
        text: |-
               az datashare list-synchronization-detail --account-name "Account1" --resource-group \
"SampleResourceGroup" --name "Share1" --synchronization-id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb"
"""

helps['datashare wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datashare is met.
    examples:
      - name: Pause executing next line of CLI script until the datashare is successfully deleted.
        text: |-
               az datashare wait --account-name "Account1" --resource-group "SampleResourceGroup" --name "Share1" \
--deleted
"""

helps['datashare provider-share-subscription'] = """
    type: group
    short-summary: Manage provider share subscription with datashare
"""

helps['datashare provider-share-subscription list'] = """
    type: command
    short-summary: "List share subscriptions in a provider share."
    examples:
      - name: ProviderShareSubscriptions_ListByShare
        text: |-
               az datashare provider-share-subscription list --account-name "Account1" --resource-group \
"SampleResourceGroup" --share-name "Share1"
"""

helps['datashare provider-share-subscription show'] = """
    type: command
    short-summary: "Get share subscription in a provider share."
    examples:
      - name: ProviderShareSubscriptions_GetByShare
        text: |-
               az datashare provider-share-subscription show --account-name "Account1" --provider-share-subscription-id\
 "4256e2cf-0f82-4865-961b-12f83333f487" --resource-group "SampleResourceGroup" --share-name "Share1"
"""

helps['datashare provider-share-subscription adjust'] = """
    type: command
    short-summary: "Adjust a share subscription's expiration date in a provider share."
    examples:
      - name: ProviderShareSubscriptions_Adjust
        text: |-
               az datashare provider-share-subscription adjust --account-name "Account1" --expiration-date \
"2020-12-26T22:33:24.5785265Z" --provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" \
--resource-group "SampleResourceGroup" --share-name "Share1"
"""

helps['datashare provider-share-subscription reinstate'] = """
    type: command
    short-summary: "Reinstate share subscription in a provider share."
    examples:
      - name: ProviderShareSubscriptions_Reinstate
        text: |-
               az datashare provider-share-subscription reinstate --account-name "Account1" --expiration-date \
"2020-12-26T22:33:24.5785265Z" --provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" \
--resource-group "SampleResourceGroup" --share-name "Share1"
"""

helps['datashare provider-share-subscription revoke'] = """
    type: command
    short-summary: "Revoke share subscription in a provider share."
    examples:
      - name: ProviderShareSubscriptions_Revoke
        text: |-
               az datashare provider-share-subscription revoke --account-name "Account1" \
--provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" --resource-group "SampleResourceGroup" \
--share-name "Share1"
"""

helps['datashare provider-share-subscription wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datashare provider-share-subscription is \
met.
    examples:
      - name: Pause executing next line of CLI script until the datashare provider-share-subscription is successfully \
created.
        text: |-
               az datashare provider-share-subscription wait --account-name "Account1" --provider-share-subscription-id\
 "4256e2cf-0f82-4865-961b-12f83333f487" --resource-group "SampleResourceGroup" --share-name "Share1" --created
"""

helps['datashare share-subscription'] = """
    type: group
    short-summary: Manage share subscription with datashare
"""

helps['datashare share-subscription list'] = """
    type: command
    short-summary: "List share subscriptions in an account."
    examples:
      - name: ShareSubscriptions_ListByAccount
        text: |-
               az datashare share-subscription list --account-name "Account1" --resource-group "SampleResourceGroup"
"""

helps['datashare share-subscription show'] = """
    type: command
    short-summary: "Get a shareSubscription in an account."
    examples:
      - name: ShareSubscriptions_Get
        text: |-
               az datashare share-subscription show --account-name "Account1" --resource-group "SampleResourceGroup" \
--name "ShareSubscription1"
"""

helps['datashare share-subscription create'] = """
    type: command
    short-summary: "Create a shareSubscription in an account."
    examples:
      - name: ShareSubscriptions_Create
        text: |-
               az datashare share-subscription create --account-name "Account1" --resource-group "SampleResourceGroup" \
--expiration-date "2020-08-26T22:33:24.5785265Z" --invitation-id "12345678-1234-1234-12345678abd" \
--source-share-location "eastus2" --name "ShareSubscription1"
"""

helps['datashare share-subscription delete'] = """
    type: command
    short-summary: "Delete a shareSubscription in an account."
    examples:
      - name: ShareSubscriptions_Delete
        text: |-
               az datashare share-subscription delete --account-name "Account1" --resource-group "SampleResourceGroup" \
--name "ShareSubscription1"
"""

helps['datashare share-subscription cancel-synchronization'] = """
    type: command
    short-summary: "Request to cancel a synchronization."
    examples:
      - name: ShareSubscriptions_CancelSynchronization
        text: |-
               az datashare share-subscription cancel-synchronization --account-name "Account1" --resource-group \
"SampleResourceGroup" --name "ShareSubscription1" --synchronization-id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb"
"""

helps['datashare share-subscription list-source-share-synchronization-setting'] = """
    type: command
    short-summary: "Get synchronization settings set on a share."
    examples:
      - name: ShareSubscriptions_ListSourceShareSynchronizationSettings
        text: |-
               az datashare share-subscription list-source-share-synchronization-setting --account-name "Account1" \
--resource-group "SampleResourceGroup" --name "ShareSub1"
"""

helps['datashare share-subscription list-synchronization'] = """
    type: command
    short-summary: "List synchronizations of a share subscription."
    examples:
      - name: ShareSubscriptions_ListSynchronizations
        text: |-
               az datashare share-subscription list-synchronization --account-name "Account1" --resource-group \
"SampleResourceGroup" --name "ShareSub1"
"""

helps['datashare share-subscription list-synchronization-detail'] = """
    type: command
    short-summary: "List synchronization details."
    examples:
      - name: ShareSubscriptions_ListSynchronizationDetails
        text: |-
               az datashare share-subscription list-synchronization-detail --account-name "Account1" --resource-group \
"SampleResourceGroup" --name "ShareSub1" --synchronization-id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb"
"""

helps['datashare share-subscription synchronize'] = """
    type: command
    short-summary: "Initiate a copy."
    examples:
      - name: ShareSubscriptions_Synchronize
        text: |-
               az datashare share-subscription synchronize --account-name "Account1" --resource-group \
"SampleResourceGroup" --name "ShareSubscription1" --synchronization-mode "Incremental"
"""

helps['datashare share-subscription wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datashare share-subscription is met.
    examples:
      - name: Pause executing next line of CLI script until the datashare share-subscription is successfully deleted.
        text: |-
               az datashare share-subscription wait --account-name "Account1" --resource-group "SampleResourceGroup" \
--name "ShareSubscription1" --deleted
      - name: Pause executing next line of CLI script until the datashare share-subscription is successfully created.
        text: |-
               az datashare share-subscription wait --account-name "Account1" --resource-group "SampleResourceGroup" \
--name "ShareSubscription1" --created
"""

helps['datashare consumer-source-data-set'] = """
    type: group
    short-summary: Manage consumer source data set with datashare
"""

helps['datashare consumer-source-data-set list'] = """
    type: command
    short-summary: "Get source dataSets of a shareSubscription."
    examples:
      - name: ConsumerSourceDataSets_ListByShareSubscription
        text: |-
               az datashare consumer-source-data-set list --account-name "Account1" --resource-group \
"SampleResourceGroup" --share-subscription-name "Share1"
"""

helps['datashare synchronization-setting'] = """
    type: group
    short-summary: Manage synchronization setting with datashare
"""

helps['datashare synchronization-setting list'] = """
    type: command
    short-summary: "List synchronizationSettings in a share."
    examples:
      - name: SynchronizationSettings_ListByShare
        text: |-
               az datashare synchronization-setting list --account-name "Account1" --resource-group \
"SampleResourceGroup" --share-name "Share1"
"""

helps['datashare synchronization-setting show'] = """
    type: command
    short-summary: "Get a synchronizationSetting in a share."
    examples:
      - name: SynchronizationSettings_Get
        text: |-
               az datashare synchronization-setting show --account-name "Account1" --resource-group \
"SampleResourceGroup" --share-name "Share1" --name "SynchronizationSetting1"
"""

helps['datashare synchronization-setting create'] = """
    type: command
    short-summary: "Create a synchronizationSetting."
    parameters:
      - name: --scheduled-synchronization-setting
        short-summary: "A type of synchronization setting based on schedule"
        long-summary: |
            Usage: --scheduled-synchronization-setting recurrence-interval=XX synchronization-time=XX kind=XX

            recurrence-interval: Required. Recurrence Interval
            synchronization-time: Required. Synchronization time
            kind: Required. Kind of synchronization setting.
    examples:
      - name: SynchronizationSettings_Create
        text: |-
               az datashare synchronization-setting create --account-name "Account1" --resource-group \
"SampleResourceGroup" --share-name "Share1" --scheduled-synchronization-setting recurrence-interval="Day" \
synchronization-time="2018-11-14T04:47:52.9614956Z" --name "Dataset1"
"""

helps['datashare synchronization-setting delete'] = """
    type: command
    short-summary: "Delete a synchronizationSetting in a share."
    examples:
      - name: SynchronizationSettings_Delete
        text: |-
               az datashare synchronization-setting delete --account-name "Account1" --resource-group \
"SampleResourceGroup" --share-name "Share1" --name "SynchronizationSetting1"
"""

helps['datashare synchronization-setting wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datashare synchronization-setting is met.
    examples:
      - name: Pause executing next line of CLI script until the datashare synchronization-setting is successfully \
deleted.
        text: |-
               az datashare synchronization-setting wait --account-name "Account1" --resource-group \
"SampleResourceGroup" --share-name "Share1" --name "SynchronizationSetting1" --deleted
"""

helps['datashare trigger'] = """
    type: group
    short-summary: Manage trigger with datashare
"""

helps['datashare trigger list'] = """
    type: command
    short-summary: "List Triggers in a share subscription."
    examples:
      - name: Triggers_ListByShareSubscription
        text: |-
               az datashare trigger list --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-subscription-name "ShareSubscription1"
"""

helps['datashare trigger show'] = """
    type: command
    short-summary: "Get a Trigger in a shareSubscription."
    examples:
      - name: Triggers_Get
        text: |-
               az datashare trigger show --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-subscription-name "ShareSubscription1" --name "Trigger1"
"""

helps['datashare trigger create'] = """
    type: command
    short-summary: "Create a Trigger."
    parameters:
      - name: --scheduled-trigger
        short-summary: "A type of trigger based on schedule"
        long-summary: |
            Usage: --scheduled-trigger recurrence-interval=XX synchronization-mode=XX synchronization-time=XX kind=XX

            recurrence-interval: Required. Recurrence Interval
            synchronization-mode: Synchronization mode
            synchronization-time: Required. Synchronization time
            kind: Required. Kind of synchronization on trigger.
    examples:
      - name: Triggers_Create
        text: |-
               az datashare trigger create --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-subscription-name "ShareSubscription1" --scheduled-trigger recurrence-interval="Day" \
synchronization-mode="Incremental" synchronization-time="2018-11-14T04:47:52.9614956Z" --name "Trigger1"
"""

helps['datashare trigger delete'] = """
    type: command
    short-summary: "Delete a Trigger in a shareSubscription."
    examples:
      - name: Triggers_Delete
        text: |-
               az datashare trigger delete --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-subscription-name "ShareSubscription1" --name "Trigger1"
"""

helps['datashare trigger wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the datashare trigger is met.
    examples:
      - name: Pause executing next line of CLI script until the datashare trigger is successfully created.
        text: |-
               az datashare trigger wait --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-subscription-name "ShareSubscription1" --name "Trigger1" --created
      - name: Pause executing next line of CLI script until the datashare trigger is successfully deleted.
        text: |-
               az datashare trigger wait --account-name "Account1" --resource-group "SampleResourceGroup" \
--share-subscription-name "ShareSubscription1" --name "Trigger1" --deleted
"""
