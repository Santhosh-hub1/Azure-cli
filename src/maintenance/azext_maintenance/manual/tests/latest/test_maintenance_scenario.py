# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer


def setup(test):
    test.cmd('az vmss create -n "clitestvmss" -g "{rg}"  --instance-count 1 --image "Win2016Datacenter" --data-disk-sizes-gb 2 --admin-password "PasswordCLIMaintenanceRP8!"  --upgrade-policy-mode Automatic ', checks=[])

    # Disable AutomaticUpdates for VM
    test.cmd('az vmss update --name  "clitestvmss"  -g "{rg}"  --set virtualMachineProfile.osProfile.windowsConfiguration.enableAutomaticUpdates=false', checks=[])

    # Enable Health extension, it is required to enable AutomaticOSUpgradePolicy
    test.cmd('az vmss extension set --name ApplicationHealthWindows --publisher Microsoft.ManagedServices --version 1.0 --resource-group "{rg}" --vmss-name  clitestvmss --settings \'{HSProbeSettings}\'', checks=[])

    # Enable AutomaticOSUpgradePolicy
    test.cmd('az vmss update --name "clitestvmss" -g "{rg}" --set UpgradePolicy.AutomaticOSUpgradePolicy.EnableAutomaticOSUpgrade=true', checks=[])

    pass


def step__applyupdates_put_applyupdates_createorupdate(test):
    test.cmd('az maintenance applyupdate create '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "clitestvmss" '
             '--resource-type "virtualMachineScaleSets"',
             checks=[])


def step__applyupdates_get_applyupdates_get(test):
    test.cmd('az maintenance applyupdate show '
             '--name "default" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "clitestvmss" '
             '--resource-type "virtualMachineScaleSets"',
             checks=[])


def step__maintenanceconfigurations_put_maintenanceconfigurations_createorupdateforresource(test):
    test.cmd('az maintenance configuration create '
             '--location "eastus2euap" '
             '--maintenance-scope "OSImage" '
             '--maintenance-window-duration "05:00" '
             '--maintenance-window-expiration-date-time "9999-12-31 00:00" '
             '--maintenance-window-recur-every "Day" '
             '--maintenance-window-start-date-time "2025-09-30 08:00" '
             '--maintenance-window-time-zone "Pacific Standard Time" '
             '--namespace "Microsoft.Maintenance" '
             '--visibility "Custom" '
             '--resource-group "{rg}" '
             '--resource-name "configuration1"',
             checks=[])


def step__maintenanceconfigurations_get_maintenanceconfigurations_getforresource(test):
    test.cmd('az maintenance configuration show '
             '--resource-group "{rg}" '
             '--resource-name "configuration1"',
             checks=[])


def step__maintenanceconfigurations_get_maintenanceconfigurations_list(test):
    test.cmd('az maintenance configuration list',
             checks=[])


def step__maintenanceconfigurations_patch_maintenanceconfigurations_updateforresource(test):
    test.cmd('az maintenance configuration update '
             '--location "eastus2euap" '
             '--maintenance-scope "OSImage" '
             '--maintenance-window-duration "05:00" '
             '--maintenance-window-expiration-date-time "9999-12-31 00:00" '
             '--maintenance-window-recur-every "Day" '
             '--maintenance-window-start-date-time "2025-09-30 08:00" '
             '--maintenance-window-time-zone "Pacific Standard Time" '
             '--namespace "Microsoft.Maintenance" '
             '--visibility "Custom" '
             '--resource-group "{rg}" '
             '--resource-name "configuration1"',
             checks=[])


def step__configurationassignments_put_configurationassignments_createorupdate(test):
    test.cmd('az maintenance assignment create '
             '--maintenance-configuration-id "/subscriptions/{subscription_id}/resourcegroups/{rg}/providers/Microsoft.'
             'Maintenance/maintenanceConfigurations/{MaintenanceConfigurations_2}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "clitestvmss" '
             '--name "{MaintenanceConfigurations_2}" '
             '--resource-type "virtualMachineScaleSets"',
             checks=[])


def step__configurationassignments_get_configurationassignments_list(test):
    test.cmd('az maintenance assignment list '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "clitestvmss" '
             '--resource-type "virtualMachineScaleSets"',
             checks=[])


def step__publicmaintenanceconfigurations_get_publicmaintenanceconfigurations_getforresource(test):
    test.cmd('az maintenance public-configuration show '
             '--resource-name "sql2"',
             checks=[])


def step__publicmaintenanceconfigurations_get_publicmaintenanceconfigurations_list(test):
    test.cmd('az maintenance public-configuration list',
             checks=[])


def step__updates_get_updates_list(test):
    test.cmd('az maintenance update list '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "clitestvmss" '
             '--resource-type "virtualMachineScaleSets"',
             checks=[])


def step__configurationassignments_delete_configurationassignments_delete(test):
    test.cmd('az maintenance assignment delete '
             '--name "{MaintenanceConfigurations_2}" '
             '--provider-name "Microsoft.Compute" '
             '--resource-group "{rg}" '
             '--resource-name "clitestvmss" '
             '--resource-type "virtualMachineScaleSets" '
             '--yes',
             checks=[])


def step__maintenanceconfigurations_delete_maintenanceconfigurations_deleteforresource(test):
    test.cmd('az maintenance configuration delete '
             '--resource-group "{rg}" '
             '--resource-name "configuration1" '
             '--yes',
             checks=[])


def step__maintenanceconfigurations_delete_publicmaintenanceconfigurations_delete(test):
    test.cmd('az maintenance configuration delete '
             '--resource-group "{rg}" '
             '--resource-name "sqlcli" '
             '--yes',
             checks=[])


def step__maintenanceconfigurations_put_publicmaintenanceconfigurations_createorupdateforresource(test):
    test.cmd('az maintenance configuration create '
             '--location "eastus2euap" '
             '--maintenance-scope "SQLDB" '
             '--maintenance-window-duration "05:00" '
             '--maintenance-window-expiration-date-time "9999-12-31 00:00" '
             '--maintenance-window-recur-every "Day" '
             '--maintenance-window-start-date-time "2025-09-30 08:00" '
             '--maintenance-window-time-zone "Pacific Standard Time" '
             '--namespace "Microsoft.Maintenance" '
             '--visibility "Public" '
             '--resource-group "{rg}" '
             '--resource-name "sqlcli" '
             '--extension-properties publicMaintenanceConfigurationId=sqlcli isAvailable=true',
             checks=[])

def step__maintenanceconfigurations_create_maintenanceconfigurations_inguestpatchdefault(test):
    test.cmd('az maintenance configuration create --maintenance-scope InGuestPatch '
        '--maintenance-window-duration "01:00" '
        '--maintenance-window-expiration-date-time "9999-12-31 00:00" '
        '--maintenance-window-recur-every "Day" '
        '--maintenance-window-start-date-time "2022-04-30 08:00" '
        '--maintenance-window-time-zone "Pacific Standard Time" '
        '--resource-group  {rg} '
        '--resource-name clitestmrpconfinguestdefault '
        '--install-patches-linux-parameters package-name-masks-to-exclude=pkg1 '
        ' package-name-masks-to-exclude=pkg2  classifications-to-include=Other  '
        '--reboot-setting IfRequired'
        , checks=[])

def step__maintenanceconfigurations_create_maintenanceconfigurations_inguestpatchadvanced(test):
    test.cmd('az maintenance configuration create --maintenance-scope InGuestPatch '
        '--maintenance-window-duration "01:00" '
        '--maintenance-window-expiration-date-time "9999-12-31 00:00" '
        '--maintenance-window-recur-every "Day" '
        '--maintenance-window-start-date-time "2022-04-30 08:00" '
        '--maintenance-window-time-zone "Pacific Standard Time" '
        '--resource-group  {rg} '
        '--resource-name clitestmrpconfinguestadvanced '
        , checks=[])

def cleanup(test):
    test.cmd('az vmss delete -n "clitestvmss" -g "{rg}"', checks=[])
    pass


def call_scenario(test):
    setup(test)
    step__maintenanceconfigurations_put_maintenanceconfigurations_createorupdateforresource(test)
    step__maintenanceconfigurations_get_maintenanceconfigurations_getforresource(test)
    step__maintenanceconfigurations_get_maintenanceconfigurations_list(test)
    step__maintenanceconfigurations_patch_maintenanceconfigurations_updateforresource(test)
    step__configurationassignments_put_configurationassignments_createorupdate(test)
    step__configurationassignments_get_configurationassignments_list(test)
    step__publicmaintenanceconfigurations_get_publicmaintenanceconfigurations_getforresource(test)
    step__publicmaintenanceconfigurations_get_publicmaintenanceconfigurations_list(test)
    step__updates_get_updates_list(test)
    step__applyupdates_put_applyupdates_createorupdate(test)
    step__applyupdates_get_applyupdates_get(test)
    step__configurationassignments_delete_configurationassignments_delete(test)
    step__maintenanceconfigurations_delete_maintenanceconfigurations_deleteforresource(test)
    step__maintenanceconfigurations_put_publicmaintenanceconfigurations_createorupdateforresource(test)
    step__maintenanceconfigurations_delete_publicmaintenanceconfigurations_delete(test)
    step__maintenanceconfigurations_create_maintenanceconfigurations_inguestpatchdefault(test)
    step__maintenanceconfigurations_create_maintenanceconfigurations_inguestpatchadvanced(test)
    cleanup(test)
