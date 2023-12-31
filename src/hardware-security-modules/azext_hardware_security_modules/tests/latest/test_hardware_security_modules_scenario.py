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
from knack.testsdk import JMESPathCheck


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class HardwareSecurityModulesScenario(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_hardware_security_modules', location='westus')
    def test_hardware_security_modules(self, resource_group):
        self.kwargs.update({
            'vnet': 'testvnet',
            'subnet1': 'hsmsubnet',
            'subnet2': 'GatewaySubnet',
            'public_ip': 'testpublicIp',
            'vnet_gateway': 'testVnetGateway',
            'subscription_id': self.get_subscription_id()
        })
        self.cmd('network vnet create --name {vnet} --resource-group {rg} --address-prefix 10.2.0.0/16 '
                 '--subnet-name compute --subnet-prefix 10.2.0.0/24')
        self.cmd('network vnet subnet create --vnet-name {vnet} --resource-group {rg} --name {subnet1} '
                 '--address-prefixes 10.2.1.0/24 --delegations Microsoft.HardwareSecurityModules/dedicatedHSMs')
        self.cmd('network vnet subnet create --vnet-name {vnet} --resource-group {rg} --name {subnet2} '
                 '--address-prefixes 10.2.255.0/26')
        self.cmd('network public-ip create --name {public_ip} --resource-group {rg}')
        self.cmd('network vnet-gateway create -g {rg} -n {vnet_gateway} --public-ip-address {public_ip} '
                 '--vnet {vnet} --gateway-type ExpressRoute --sku Standard --location westus')

        self.cmd('dedicated-hsm create '
                 '--name hsm1 '
                 '--location westus '
                 '--network-interfaces private-ip-address="10.2.1.5" '
                 '--subnet id=/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vnet}/subnets/{subnet1} '
                 '--stamp-id "stamp1" '
                 '--sku "SafeNet Luna Network HSM A790" '
                 '--tags Dept="hsm" Environment="dogfood" '
                 '--resource-group {rg}',
                 checks=self.check('name', 'hsm1'))

        self.cmd('dedicated-hsm show '
                 '--name hsm1 '
                 '--resource-group {rg}',
                 checks=self.check('name', 'hsm1'))
        self.cmd('dedicated-hsm list '
                 '--resource-group {rg}',
                 checks=self.check('[0].name', 'hsm1'))
        self.cmd('dedicated-hsm update '
                 '--name hsm1 '
                 '--tags Dept="hsm" Environment="dogfood" Slice="A" '
                 '--resource-group {rg}',
                 checks=self.check('tags.Slice', "A"))
        self.cmd('dedicated-hsm delete '
                 '--name hsm1 '
                 '--resource-group {rg} '
                 '-y',
                 checks=[])

        self.cmd('network vnet-gateway delete -g {rg} -n {vnet_gateway}')

    @ResourceGroupPreparer(name_prefix='cli_test_hardware_security_modules_v2', location='eastus')
    def test_hardware_security_modules_v2(self, resource_group):
        self.kwargs.update({
            'vnet1': 'testvnet1',
            'vnet2': 'testvnet2',
            'subnet1': 'hsmsubnet',
            'subnet2': 'hsmsubnet2',
            'subnet3': 'GatewaySubnet',
            'public_ip': 'testpublicIp',
            'vnet_gateway': 'testVnetGateway',
            'subscription_id': self.get_subscription_id()
        })
        self.cmd('network vnet create --name {vnet1} --resource-group {rg} --address-prefix 10.3.0.0/16 '
                 '--subnet-name compute --subnet-prefix 10.3.0.0/24 --tags fastpathenabled="true"')
        self.cmd('network vnet create --name {vnet2} --resource-group {rg} --address-prefix 10.4.0.0/16 '
                 '--subnet-name compute2 --subnet-prefix 10.4.0.0/24 --tags fastpathenabled="true"')
        self.cmd('network vnet subnet create --vnet-name {vnet1} --resource-group {rg} --name {subnet1} '
                 '--address-prefixes 10.3.1.0/24 --delegations Microsoft.HardwareSecurityModules/dedicatedHSMs')
        self.cmd('network vnet subnet create --vnet-name {vnet2} --resource-group {rg} --name {subnet2} '
                 '--address-prefixes 10.4.1.0/24 --delegations Microsoft.HardwareSecurityModules/dedicatedHSMs')
        self.cmd('network vnet subnet create --vnet-name {vnet1} --resource-group {rg} --name {subnet3} '
                 '--address-prefixes 10.3.255.0/26')
        self.cmd('network public-ip create --name {public_ip} --resource-group {rg}')
        self.cmd('network vnet-gateway create -g {rg} -n {vnet_gateway} --public-ip-address {public_ip} '
                 '--vnet {vnet1} --sku Standard --location eastus')

        self.cmd('dedicated-hsm create '
                 '--name hsm1 '
                 '--location eastus '
                 '--network-interfaces private-ip-address="10.3.1.5" '
                 '--subnet id=/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vnet1}/subnets/{subnet1} '
                 '--mgmt-network-interfaces private-ip-address="10.4.1.6" '
                 '--mgmt-network-subnet '
                 'id=/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Network/virtualNetworks/{vnet2}/subnets/{subnet2} '
                 '--stamp-id "stamp2" '
                 '--sku "payShield10K_LMK1_CPS60" '
                 '--tags Dept="hsm" Environment="dogfood" '
                 '--resource-group {rg}',
                 checks=self.check('name', 'hsm1'))
        import time
        time.sleep(900)
        self.cmd('dedicated-hsm show '
                 '--name hsm1 '
                 '--resource-group {rg}',
                 checks=self.check('name', 'hsm1'))
        self.cmd('dedicated-hsm list '
                 '--resource-group {rg}',
                 checks=self.check('[0].name', 'hsm1'))
        self.cmd('dedicated-hsm update '
                 '--name hsm1 '
                 '--tags Dept="hsm" Environment="dogfood" '
                 '--resource-group {rg}')
        self.cmd('dedicated-hsm delete '
                 '--name hsm1 '
                 '--resource-group {rg} '
                 '-y',
                 checks=[])

        self.cmd('network vnet-gateway delete -g {rg} -n {vnet_gateway}')
