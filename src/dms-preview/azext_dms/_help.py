# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

helps['dms project create'] = """
    type: command
    short-summary: Create a migration project which can contain multiple tasks.
    long-summary: |
        The following project configurations are supported:
            -) source -> target
            1) SQL -> SQLDB
            2) PostgreSQL -> AzureDbForPostgreSQL
            3) MongoDB -> MongoDB (for migrating to Cosmos DB via their MongoDB API)

    parameters:
        - name: --source-platform
          type: string
          short-summary: >
            The type of server for the source database. The supported types are: SQL, PostgreSQL, MongoDB.
        - name: --target-platform
          type: string
          short-summary: >
            The type of service for the target database. The supported types are: SQLDB, AzureDbForPostgreSQL, MongoDB.
    examples:
        - name: Create a SQL to SQLDB project for a DMS instance.
          text: >
            az dms project create -l westus -n sqlproject -g myresourcegroup --service-name mydms --source-platform SQL --target-platform SQLDB --tags tagName1=tagValue1 tagWithNoValue
        - name: Create a PostgreSql to AzureDbForPostgreSql project for a DMS instance.
          text: >
            az dms project create -l westus -n pgproject -g myresourcegroup --service-name mydms --source-platform PostgreSQL --target-platform AzureDbForPostgreSQL --tags tagName1=tagValue1 tagWithNoValue
"""

helps['dms project task create'] = """
    type: command
    short-summary: Create and start a migration task.
    long-summary: |
        The following task configurations are supported:
            -) source -> target :: task type
            1) SQL -> SQLDB :: OfflineMigration
            2) PostgreSQL -> AzureDbForPostgreSQL :: OnlineMigration
            3) MongoDB -> MongoDB (for migrating to Cosmos DB via their MongoDB API) :: OfflineMigration

    parameters:
        - name: --task-type
          type: string
          short-summary: >
            The type of data movement the task will support. The supported types are: OnlineMigration, OfflineMigration. If not provided, will default to OfflineMigration for SQL, MongoDB and OnlineMigration for PostgreSQL.
        - name: --database-options-json
          type: string
          short-summary: >
            Database and table information. This can be either a JSON-formatted string or the location to a file containing the JSON object. See examples below for the format.
          long-summary: >
            For SQL we support per table migrations. To use this, specify the tables names in the 'table_map' as below.
            You can also set the source as read only.
              [
                  {
                      "name": "source database",
                      "target_database_name": "target database",
                      "make_source_db_read_only": false|true,
                      "table_map": {
                          "schema.SourceTableName1": "schema.TargetTableName1",
                          "schema.SourceTableName2": "schema.TargetTableName2",
                          ...n
                      }
                  },
                  ...n
              ]

            For PostgreSQL, the format of the database options JSON object.
              [
                  {
                      "name": "source database",
                      "target_database_name": "target database",
                      // Used for manipulating the underlying migration engine.
                      // Only provide if instructed to do so or if you really know what you are doing.
                      "migrationSetting": {
                          "setting1": "value1",
                          ...n
                      },
                      // Used for manipulating the underlying migration engine.
                      // Only provide if instructed to do so or if you really know what you are doing.
                      "sourceSetting": {
                          "setting1": "value1",
                          ...n
                      },
                      // Used for manipulating the underlying migration engine.
                      // Only provide if instructed to do so or if you really know what you are doing.
                      "targetSetting": {
                          "setting1": "value1",
                          ...n
                      },
                      // Optional parameter to list tables that you want included in the migration.
                      "selectedTables": [
                          "schemaName1.tableName1",
                          ...n
                      ]
                  },
                  ...n
              ]

            For MongoDB we support per collection migrations. To use this, specify the collections inside the database object as below.
              {
                  // set to zero to get the default boost during migration (recommended)
                  "boostRUs": 0,
                  // "OneTime" or "Continuous", only "OneTime" is currently supported
                  "replication": "OneTime",
                  // Set to null to use maximum resources available.
                  "throttling": {
                      // percentage of the CPU to try to avoid using
                      "minFreeCpu": 25,
                      // amount of RAM (in MBs) to try to avoid using
                      "minFreeMemoryMb": 1024,
                      // max number of collections to migrate at a time
                      "maxParallelism": 2
                  },
                  "databases": {
                      "database_name": {
                          // see https://docs.microsoft.com/th-th/azure/cosmos-db/request-units,     ||
                          // set to null to use default
                          // or 0 if throughput should not be provisioned at the database level
                          "targetRUs": 0,
                          "collections": {
                              "collection_name_1": {
                                  // Whether the target database/collection will be deleted if exists
                                  "canDelete": true,
                                  // set to null if target should not be sharded
                                  // or to copy the shard key from source (if exists)
                                  "shardKey": null,
                                  // set to null to use default (recommended)
                                  "targetRUs": null
                              },
                              "collection_name_2": {
                                  "canDelete": true,
                                  "shardKey": {
                                      "fields": [
                                          {
                                              "name": "field_name",
                                              // accepts "Forward", "Reverse", or "Hashed" but CosmosDB only accepts a single-field, hashed shard key
                                              "order": "Forward"
                                          },
                                          ...n
                                      ],
                                      // whether shard key is unique
                                      // see https://docs.microsoft.com/azure/cosmos-db/partition-data
                                      "isUnique": false
                                  },
                                  "targetRUs": 10000
                              },
                              ...n
                          }
                      },
                      ...n
                  }
              }

        - name: --source-connection-json
          type: string
          short-summary: >
            The connection information to the source server. This can be either a JSON-formatted string or the location to a file containing the JSON object. See examples below for the format.
          long-summary: |
            The format of the connection JSON object for SQL connections.
              {
                  "userName": "user name",    // if this is missing or null, you will be prompted
                  "password": null,           // if this is missing or null (highly recommended) you will be prompted
                  "dataSource": "server name[,port]",
                  "authentication": "SqlAuthentication|WindowsAuthentication",
                  "encryptConnection": true,      // highly recommended to leave as true
                  "trustServerCertificate": false  // highly recommended to leave as false
              }

            The format of the connection JSON object for PostgreSQL connections.
              {
                  "userName": "user name",    // if this is missing or null, you will be prompted
                  "password": null,           // if this is missing or null (highly recommended) you will be prompted
                  "serverName": "server name",
                  "databaseName": "database name", // if this is missing, it will default to the 'postgres' database
                  "port": 5432,                // if this is missing, it will default to 5432
                  "encryptConnection": true,      // highly recommended to leave as true
                  "trustServerCertificate": false  // highly recommended to leave as false
              }

            The format of the connection JSON object for MongoDB connections.
              {
                  "userName": null,   // if this is missing or null, you will be prompted
                  "password": null,   // if this is missing or null (highly recommended) you will be prompted
                  "connectionString": "mongodb://hostOrIp:port"
              }

        - name: --target-connection-json
          type: string
          short-summary: >
            The connection information to the target server. This can be either a JSON-formatted string or the location to a file containing the JSON object. See 'source-connection-json' for examples of connection formats.
        - name: --enable-data-integrity-validation
          type: bool
          short-summary: >
            For SQL only. Whether to perform a checksum based data integrity validation between source and target for the selected database and tables.
        - name: --enable-query-analysis-validation
          type: bool
          short-summary: >
            For SQL only. Whether to perform a quick and intelligent query analysis by retrieving queries from the source database and
            executing them in the target. The result will have execution statistics for executions in source and target databases
            for the extracted queries.
        - name: --enable-schema-validation
          type: bool
          short-summary: >
            For SQL only. Whether to compare the schema information between source and target.
        - name: --validate-only
          type: bool
          short-summary: >
            For MongoDB to Cosmos DB only. Whether to run validation only and NOT run migration. It is mandatory to run a 'validate only' task before attempting an actual migration. Once the validation is complete, pass the name of this 'validate only' task to a new task's 'validated task name' argument.
        - name: --validated-task-name
          type: string
          short-summary: >
            (For MongoDB to Cosmos DB only) When running a migration it is neceaary to pass in the name of a previously run 'validate only' task.
    examples:
        - name: Create and start a SQL Task which performs no validation checks.
          text: >
            az dms project task create --database-options-json C:\\CliFiles\\databaseOptions.json -n mytask --project-name myproject -g myresourcegroup --service-name mydms --source-connection-json '{'dataSource': 'myserver', 'authentication': 'SqlAuthentication', 'encryptConnection': 'true', 'trustServerCertificate': 'true'}' --target-connection-json C:\\CliFiles\\targetConnection.json --task-type offlinemigration
        - name: Create and start a SQL Task which performs all validation checks.
          text: >
            az dms project task create --database-options-json C:\\CliFiles\\databaseOptions.json -n mytask --project-name myproject -g myresourcegroup --service-name mydms --source-connection-json C:\\CliFiles\\sourceConnection.json --target-connection-json C:\\CliFiles\\targetConnection.json --enable-data-integrity-validation --enable-query-analysis-validation --enable-schema-validation --task-type offlinemigration
"""

helps['dms project task cancel'] = """
    type: command
    short-summary: This command is being deprecated. Use the stop command instead.
    long-summary: |
        To keep a more consistent experience with Azure's portal UI use:
            az dms project task stop

    parameters:
        - name: --object-name
          type: string
          short-summary: >
            Supported by MongoDB migrations only.
            The qualified name of the database or collection you wish to stop. Leave blank to stop the entire migration.
"""

helps['dms project task restart'] = """
    type: command
    short-summary: Restart either the entire migration or just a specified object. Currently only supported by MongoDB migrations.
    long-summary: |
        To see the result of the request, please use the 'task show' command:
            az dms project task show ... --expand command

    parameters:
        - name: --object-name
          type: string
          short-summary: >
            The qualified name of the database or collection you wish to restart. Leave blank to restart the entire migration.
"""

helps['dms project task stop'] = """
    type: command
    short-summary: Stops the task, or stops migration on the specified object (MongoDB migrations only).
    long-summary: |
        To see the result of the request, please use the 'task show' command:
            az dms project task show ... --expand command

    parameters:
        - name: --object-name
          type: string
          short-summary: >
            Supported by MongoDB migrations only.
            The qualified name of the database or collection you wish to stop. Leave blank to stop the entire migration.
"""
