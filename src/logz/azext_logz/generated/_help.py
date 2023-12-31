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


helps['logz'] = '''
    type: group
    short-summary: Manage Microsoft Logz
'''

helps['logz monitor'] = """
    type: group
    short-summary: Manage monitor with logz
"""

helps['logz monitor list'] = """
    type: command
    short-summary: "List all monitors under the specified resource group. And List all monitors under the specified \
subscription."
    examples:
      - name: Monitors_ListByResourceGroup
        text: |-
               az logz monitor list --resource-group "myResourceGroup"
      - name: Monitors_List
        text: |-
               az logz monitor list
"""

helps['logz monitor show'] = """
    type: command
    short-summary: "Get the properties of a specific monitor resource."
    examples:
      - name: Monitors_Get
        text: |-
               az logz monitor show --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz monitor create'] = """
    type: command
    short-summary: "Create a monitor resource. This create operation can take upto 10 minutes to complete."
    parameters:
      - name: --org-properties
        long-summary: |
            Usage: --org-properties company-name=XX enterprise-app-id=XX single-sign-on-url=XX

            company-name: Name of the Logz organization.
            enterprise-app-id: The Id of the Enterprise App used for Single sign on.
            single-sign-on-url: The login URL specific to this Logz Organization.
      - name: --user-info
        long-summary: |
            Usage: --user-info first-name=XX last-name=XX email-address=XX phone-number=XX

            first-name: First Name of the user
            last-name: Last Name of the user
            email-address: Email of the user used by Logz for contacting them if needed
            phone-number: Phone number of the user used by Logz for contacting them if needed
      - name: --plan-data
        long-summary: |
            Usage: --plan-data usage-type=XX billing-cycle=XX plan-details=XX effective-date=XX

            usage-type: different usage type like PAYG/COMMITTED. this could be enum
            billing-cycle: different billing cycles like MONTHLY/WEEKLY. this could be enum
            plan-details: plan id as published by Logz
            effective-date: date when plan was applied
    examples:
      - name: Monitors_Create
        text: |-
               az logz monitor create --name "myMonitor" --location "West US" --plan-data billing-cycle="Monthly" \
effective-date="2019-08-30T15:14:33+02:00" plan-details="logzapitestplan" usage-type="Committed" --user-info \
email-address="alice@microsoft.com" first-name="Alice" last-name="Bob" phone-number="123456" --tags Environment="Dev" \
--resource-group "myResourceGroup"
"""

helps['logz monitor update'] = """
    type: command
    short-summary: "Update a monitor resource."
    examples:
      - name: Monitors_Update
        text: |-
               az logz monitor update --name "myMonitor" --monitoring-status "Enabled" --tags Environment="Dev" \
--resource-group "myResourceGroup"
"""

helps['logz monitor delete'] = """
    type: command
    short-summary: "Delete a monitor resource. This delete operation can take upto 10 minutes to complete."
    examples:
      - name: Monitors_Delete
        text: |-
               az logz monitor delete --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz monitor list-payload'] = """
    type: command
    short-summary: "Returns the payload that needs to be passed in the request body for installing Logz.io agent on a \
VM."
    examples:
      - name: MainAccount_VMHosts_Payload
        text: |-
               az logz monitor list-payload --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz monitor list-resource'] = """
    type: command
    short-summary: "List the resources currently being monitored by the Logz monitor resource."
    examples:
      - name: MonitoredResources_List
        text: |-
               az logz monitor list-resource --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz monitor list-role'] = """
    type: command
    short-summary: "List the user's roles configured on Logz.io side for the account corresponding to the monitor \
resource."
    examples:
      - name: MainAccount_VMHosts_Update
        text: |-
               az logz monitor list-role --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz monitor list-vm'] = """
    type: command
    short-summary: "List the compute resources currently being monitored by the Logz main account resource."
    examples:
      - name: MainAccount_VMHosts_List
        text: |-
               az logz monitor list-vm --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz monitor update-vm'] = """
    type: command
    short-summary: "Sending request to update the collection when Logz.io agent has been installed on a VM for a given \
monitor."
    parameters:
      - name: --vm-resource-ids
        short-summary: "Request of a list vm host update operation."
        long-summary: |
            Usage: --vm-resource-ids id=XX agent-version=XX

            id: Request of a list vm host update operation.
            agent-version: Version of the Logz agent installed on the VM.

            Multiple actions can be specified by using more than one --vm-resource-ids argument.
    examples:
      - name: MainAccount_VMHosts_Update
        text: |-
               az logz monitor update-vm --name "myMonitor" --state "Install" --resource-group "myResourceGroup"
"""

helps['logz monitor wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the logz monitor is met.
    examples:
      - name: Pause executing next line of CLI script until the logz monitor is successfully created.
        text: |-
               az logz monitor wait --name "myMonitor" --resource-group "myResourceGroup" --created
      - name: Pause executing next line of CLI script until the logz monitor is successfully deleted.
        text: |-
               az logz monitor wait --name "myMonitor" --resource-group "myResourceGroup" --deleted
"""

helps['logz rule'] = """
    type: group
    short-summary: Manage tag rule with logz
"""

helps['logz rule list'] = """
    type: command
    short-summary: "List the tag rules for a given monitor resource."
    examples:
      - name: TagRules_List
        text: |-
               az logz rule list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz rule show'] = """
    type: command
    short-summary: "Get a tag rule set for a given monitor resource."
    examples:
      - name: TagRules_Get
        text: |-
               az logz rule show --monitor-name "myMonitor" --resource-group "myResourceGroup" --rule-set-name \
"default"
"""

helps['logz rule create'] = """
    type: command
    short-summary: "Create a tag rule set for a given monitor resource."
    parameters:
      - name: --filtering-tags
        short-summary: "List of filtering tags to be used for capturing logs. This only takes effect if \
SendActivityLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the \
rules will apply to the list of all available resources. If Include actions are specified, the rules will only include \
resources with the associated tags."
        long-summary: |
            Usage: --filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.

            Multiple actions can be specified by using more than one --filtering-tags argument.
    examples:
      - name: TagRules_CreateOrUpdate
        text: |-
               az logz rule create --monitor-name "myMonitor" --filtering-tags name="Environment" action="Include" \
value="Prod" --filtering-tags name="Environment" action="Exclude" value="Dev" --send-aad-logs false \
--send-activity-logs true --send-subscription-logs true --resource-group "myResourceGroup" --rule-set-name "default"
"""

helps['logz rule update'] = """
    type: command
    short-summary: "Update a tag rule set for a given monitor resource."
    parameters:
      - name: --filtering-tags
        short-summary: "List of filtering tags to be used for capturing logs. This only takes effect if \
SendActivityLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the \
rules will apply to the list of all available resources. If Include actions are specified, the rules will only include \
resources with the associated tags."
        long-summary: |
            Usage: --filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.

            Multiple actions can be specified by using more than one --filtering-tags argument.
"""

helps['logz rule delete'] = """
    type: command
    short-summary: "Delete a tag rule set for a given monitor resource."
    examples:
      - name: TagRules_Delete
        text: |-
               az logz rule delete --monitor-name "myMonitor" --resource-group "myResourceGroup" --rule-set-name \
"default"
"""

helps['logz sso'] = """
    type: group
    short-summary: Manage single sign on with logz
"""

helps['logz sso list'] = """
    type: command
    short-summary: "List the single sign-on configurations for a given monitor resource."
    examples:
      - name: SingleSignOnConfigurations_List
        text: |-
               az logz sso list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz sso show'] = """
    type: command
    short-summary: "Gets the Logz single sign-on resource for the given Monitor."
    examples:
      - name: SingleSignOnConfigurations_Get
        text: |-
               az logz sso show --configuration-name "default" --monitor-name "myMonitor" --resource-group \
"myResourceGroup"
"""

helps['logz sso create'] = """
    type: command
    short-summary: "Configures single-sign-on for this resource. This operation can take upto 10 minutes to complete."
    parameters:
      - name: --properties
        long-summary: |
            Usage: --properties single-sign-on-state=XX enterprise-app-id=XX single-sign-on-url=XX

            single-sign-on-state: Various states of the SSO resource
            enterprise-app-id: The Id of the Enterprise App used for Single sign-on.
            single-sign-on-url: The login URL specific to this Logz Organization.
    examples:
      - name: SingleSignOnConfigurations_CreateOrUpdate
        text: |-
               az logz sso create --configuration-name "default" --monitor-name "myMonitor" --properties \
enterprise-app-id="00000000-0000-0000-0000-000000000000" single-sign-on-state="Enable" single-sign-on-url=null \
--resource-group "myResourceGroup"
"""

helps['logz sso update'] = """
    type: command
    short-summary: "Configures single-sign-on for this resource. This operation can take upto 10 minutes to complete."
    parameters:
      - name: --properties
        long-summary: |
            Usage: --properties single-sign-on-state=XX enterprise-app-id=XX single-sign-on-url=XX

            single-sign-on-state: Various states of the SSO resource
            enterprise-app-id: The Id of the Enterprise App used for Single sign-on.
            single-sign-on-url: The login URL specific to this Logz Organization.
"""

helps['logz sso wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the logz sso is met.
    examples:
      - name: Pause executing next line of CLI script until the logz sso is successfully created.
        text: |-
               az logz sso wait --configuration-name "default" --monitor-name "myMonitor" --resource-group \
"myResourceGroup" --created
      - name: Pause executing next line of CLI script until the logz sso is successfully updated.
        text: |-
               az logz sso wait --configuration-name "default" --monitor-name "myMonitor" --resource-group \
"myResourceGroup" --updated
"""

helps['logz sub-account'] = """
    type: group
    short-summary: Manage sub account with logz
"""

helps['logz sub-account list'] = """
    type: command
    short-summary: "List the sub account under a given monitor resource."
    examples:
      - name: SubAccount_List
        text: |-
               az logz sub-account list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['logz sub-account show'] = """
    type: command
    short-summary: "Get a sub account under a given monitor resource."
    examples:
      - name: SubAccount_Get
        text: |-
               az logz sub-account show --monitor-name "myMonitor" --resource-group "myResourceGroup" --name \
"SubAccount1"
"""

helps['logz sub-account create'] = """
    type: command
    short-summary: "Create sub account under a given monitor resource. This create operation can take upto 10 minutes \
to complete."
    parameters:
      - name: --org-properties
        long-summary: |
            Usage: --org-properties company-name=XX enterprise-app-id=XX single-sign-on-url=XX

            company-name: Name of the Logz organization.
            enterprise-app-id: The Id of the Enterprise App used for Single sign on.
            single-sign-on-url: The login URL specific to this Logz Organization.
      - name: --user-info
        long-summary: |
            Usage: --user-info first-name=XX last-name=XX email-address=XX phone-number=XX

            first-name: First Name of the user
            last-name: Last Name of the user
            email-address: Email of the user used by Logz for contacting them if needed
            phone-number: Phone number of the user used by Logz for contacting them if needed
      - name: --plan-data
        long-summary: |
            Usage: --plan-data usage-type=XX billing-cycle=XX plan-details=XX effective-date=XX

            usage-type: different usage type like PAYG/COMMITTED. this could be enum
            billing-cycle: different billing cycles like MONTHLY/WEEKLY. this could be enum
            plan-details: plan id as published by Logz
            effective-date: date when plan was applied
    examples:
      - name: subAccount_Create
        text: |-
               az logz sub-account create --monitor-name "myMonitor" --type "Microsoft.Logz/monitors" --location "West \
US" --monitoring-status "Enabled" --tags Environment="Dev" --resource-group "myResourceGroup" --name "SubAccount1"
"""

helps['logz sub-account update'] = """
    type: command
    short-summary: "Update a monitor resource."
    examples:
      - name: SubAccount_Update
        text: |-
               az logz sub-account update --monitor-name "myMonitor" --monitoring-status "Enabled" --tags \
Environment="Dev" --resource-group "myResourceGroup" --name "SubAccount1"
"""

helps['logz sub-account delete'] = """
    type: command
    short-summary: "Delete a sub account resource. This delete operation can take upto 10 minutes to complete."
    examples:
      - name: SubAccount_Delete
        text: |-
               az logz sub-account delete --monitor-name "myMonitor" --resource-group "myResourceGroup" --name \
"someName"
"""

helps['logz sub-account list-payload'] = """
    type: command
    short-summary: "Returns the payload that needs to be passed as a request for installing Logz.io agent on a VM."
    examples:
      - name: SubAccount_VMHosts_Payload
        text: |-
               az logz sub-account list-payload --monitor-name "myMonitor" --resource-group "myResourceGroup" --name \
"SubAccount1"
"""

helps['logz sub-account list-resource'] = """
    type: command
    short-summary: "List the resources currently being monitored by the Logz sub account resource."
    examples:
      - name: SubAccount_MonitoredResources_List
        text: |-
               az logz sub-account list-resource --monitor-name "myMonitor" --resource-group "myResourceGroup" --name \
"SubAccount1"
"""

helps['logz sub-account list-vm'] = """
    type: command
    short-summary: "List the compute resources currently being monitored by the Logz sub account resource."
    examples:
      - name: SubAccount_VMHosts_List
        text: |-
               az logz sub-account list-vm --monitor-name "myMonitor" --resource-group "myResourceGroup" --name \
"SubAccount1"
"""

helps['logz sub-account update-vm'] = """
    type: command
    short-summary: "Sending request to update the collection when Logz.io agent has been installed on a VM for a given \
monitor."
    parameters:
      - name: --vm-resource-ids
        short-summary: "Request of a list vm host update operation."
        long-summary: |
            Usage: --vm-resource-ids id=XX agent-version=XX

            id: Request of a list vm host update operation.
            agent-version: Version of the Logz agent installed on the VM.

            Multiple actions can be specified by using more than one --vm-resource-ids argument.
    examples:
      - name: SubAccount_VMHosts_Update
        text: |-
               az logz sub-account update-vm --monitor-name "myMonitor" --state "Install" --resource-group \
"myResourceGroup" --name "SubAccount1"
"""

helps['logz sub-account wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the logz sub-account is met.
    examples:
      - name: Pause executing next line of CLI script until the logz sub-account is successfully created.
        text: |-
               az logz sub-account wait --monitor-name "myMonitor" --resource-group "myResourceGroup" --name \
"SubAccount1" --created
      - name: Pause executing next line of CLI script until the logz sub-account is successfully deleted.
        text: |-
               az logz sub-account wait --monitor-name "myMonitor" --resource-group "myResourceGroup" --name \
"SubAccount1" --deleted
"""

helps['logz sub-rule'] = """
    type: group
    short-summary: Manage sub account tag rule with logz
"""

helps['logz sub-rule list'] = """
    type: command
    short-summary: "List the tag rules for a given sub account resource."
    examples:
      - name: SubAccountTagRules_List
        text: |-
               az logz sub-rule list --monitor-name "myMonitor" --resource-group "myResourceGroup" --sub-account-name \
"SubAccount1"
"""

helps['logz sub-rule show'] = """
    type: command
    short-summary: "Get a tag rule set for a given monitor resource."
    examples:
      - name: SubAccountTagRules_Get
        text: |-
               az logz sub-rule show --monitor-name "myMonitor" --resource-group "myResourceGroup" --rule-set-name \
"default" --sub-account-name "SubAccount1"
"""

helps['logz sub-rule create'] = """
    type: command
    short-summary: "Create a tag rule set for a given sub account resource."
    parameters:
      - name: --filtering-tags
        short-summary: "List of filtering tags to be used for capturing logs. This only takes effect if \
SendActivityLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the \
rules will apply to the list of all available resources. If Include actions are specified, the rules will only include \
resources with the associated tags."
        long-summary: |
            Usage: --filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.

            Multiple actions can be specified by using more than one --filtering-tags argument.
    examples:
      - name: SubAccountTagRules_CreateOrUpdate
        text: |-
               az logz sub-rule create --monitor-name "myMonitor" --filtering-tags name="Environment" action="Include" \
value="Prod" --filtering-tags name="Environment" action="Exclude" value="Dev" --send-aad-logs false \
--send-activity-logs true --send-subscription-logs true --resource-group "myResourceGroup" --rule-set-name "default" \
--sub-account-name "SubAccount1"
"""

helps['logz sub-rule update'] = """
    type: command
    short-summary: "Update a tag rule set for a given sub account resource."
    parameters:
      - name: --filtering-tags
        short-summary: "List of filtering tags to be used for capturing logs. This only takes effect if \
SendActivityLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the \
rules will apply to the list of all available resources. If Include actions are specified, the rules will only include \
resources with the associated tags."
        long-summary: |
            Usage: --filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.

            Multiple actions can be specified by using more than one --filtering-tags argument.
"""

helps['logz sub-rule delete'] = """
    type: command
    short-summary: "Delete a tag rule set for a given monitor resource."
    examples:
      - name: TagRules_Delete
        text: |-
               az logz sub-rule delete --monitor-name "myMonitor" --resource-group "myResourceGroup" --rule-set-name \
"default" --sub-account-name "SubAccount1"
"""
