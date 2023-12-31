# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import ScenarioTest, record_only


class BillingBenefitsScenario(ScenarioTest):
    def _validate_savings_plan_order(self, order):
        self.assertIsNotNone(order)
        self.assertIsNotNone(order['id'])
        self.assertIsNotNone(order['name'])
        self.assertEqual(
            order['type'], 'microsoft.billingbenefits/savingsPlanOrders')
        self.assertIsNotNone(order['provisioningState'])
        self.assertIsNotNone(order['billingScopeId'])
        self.assertIsNotNone(order['savingsPlans'])
        self.assertGreater(len(order['savingsPlans']), 0)
        self.assertIsNotNone(order['expiryDateTime'])
        self.assertIsNotNone(order['term'])
        self.assertIsNotNone(order['displayName'])
        self.assertIsNotNone(order['benefitStartTime'])
        self.assertIsNotNone(order['billingProfileId'])
        self.assertIsNotNone(order['billingAccountId'])
        self.assertIsNotNone(order['expiryDateTime'])
        self.assertIsNotNone(order['sku'])
        self.assertEqual(
            order['sku']['name'], 'Compute_Savings_Plan')

    def _validate_savings_plan_item(self, item):
        self.assertIsNotNone(item)
        self.assertIsNotNone(item['id'])
        self.assertIsNotNone(item['name'])
        self.assertEqual(
            item['type'], 'microsoft.billingbenefits/savingsPlanOrders/savingsPlans')
        self.assertIsNotNone(item['provisioningState'])
        self.assertIsNotNone(item['expiryDateTime'])
        self.assertIsNotNone(item['purchaseDateTime'])
        self.assertIsNotNone(item['benefitStartTime'])
        self.assertIsNotNone(item['effectiveDateTime'])
        self.assertIsNotNone(item['commitment'])
        self.assertIsNotNone(item['commitment']['grain'])
        self.assertEqual(item['commitment']['grain'], 'Hourly')
        self.assertIsNotNone(item['commitment']['amount'])
        self.assertGreater(item['commitment']['amount'], 0)
        self.assertIsNotNone(item['commitment']['currencyCode'])
        self.assertEqual(item['commitment']['currencyCode'], 'USD')
        self.assertIsNotNone(item['term'])
        self.assertEqual(
            item['type'], 'microsoft.billingbenefits/savingsPlanOrders/savingsPlans')

    def _validate_reservation_order_alias(self, response):
        self.assertIsNotNone(response)
        self.assertEqual(
            response['id'], '/providers/Microsoft.BillingBenefits/reservationOrderAliases/TestNameRo')
        self.assertEqual(response['name'], 'TestNameRo')
        self.assertEqual(
            response['type'], 'Microsoft.BillingBenefits/reservationOrderAliases')
        self.assertEqual(response['location'], 'westus')
        self.assertIsNotNone(response['sku'])
        self.assertEqual(response['sku']['name'], 'Standard_B1ls')
        self.assertEqual(response['quantity'], 1)
        self.assertIsNotNone(response['reservationOrderId'])
        self.assertIsNotNone(response['billingScopeId'])
        self.assertEqual(response['renew'], False)
        self.assertEqual(response['billingPlan'], 'P1M')
        self.assertEqual(response['reservedResourceType'], 'VirtualMachines')
        self.assertEqual(response['appliedScopeType'], 'Shared')
        self.assertEqual(response['displayName'], 'TestNameRo')
        self.assertEqual(response['provisioningState'], 'Created')
        self.assertEqual(response['term'], 'P1Y')

    def _validate_savings_plan_order_alias(self, response):
        self.assertIsNotNone(response)
        self.assertEqual(
            response['id'], '/providers/Microsoft.BillingBenefits/savingsPlanOrderAliases/TestNameSO2')
        self.assertEqual(response['name'], 'TestNameSO2')
        self.assertEqual(
            response['type'], 'Microsoft.BillingBenefits/savingsPlanOrderAliases')
        self.assertIsNotNone(response['sku'])
        self.assertEqual(response['sku']['name'], 'Compute_Savings_Plan')
        self.assertIsNotNone(response['commitment'])
        self.assertEqual(response['commitment']['grain'], 'Hourly')
        self.assertEqual(response['commitment']['currencyCode'], 'USD')
        self.assertEqual(response['commitment']['amount'], 10)
        self.assertIsNotNone(response['savingsPlanOrderId'])
        self.assertIsNotNone(response['billingScopeId'])
        self.assertEqual(response['billingPlan'], 'P1M')
        self.assertEqual(response['appliedScopeType'], 'Shared')
        self.assertEqual(response['displayName'], 'TestNameSO2')
        self.assertEqual(response['provisioningState'], 'Created')
        self.assertEqual(response['term'], 'P1Y')

    @record_only()
    def test_billing_benefits_validate_purchase(self):
        purchase_item = '{applied-scope-type:Shared,billing-plan:P1M,billing-scope-id:eef82110-c91b-4395-9420-fcfcbefc5a47,display-name:name1,sku:Compute_Savings_Plan,term:P1Y,commitment:{amount:10.0,currency-code:USD,grain:Hourly}}'
        purchase_items = '[{}]'.format(purchase_item)
        self.kwargs.update({
            'benefits': purchase_items
        })
        response = self.cmd(
            'billing-benefits validate-purchase --benefits {benefits}').get_output_in_json()
        self.assertIsNotNone(response)
        self.assertIsNotNone(response['benefits'])
        self.assertGreater(len(response['benefits']), 0)
        for item in response['benefits']:
            self.assertIsNotNone(item['valid'])
            self.assertTrue(item['valid'])

    @record_only()
    def test_reservation_order_alias(self):
        self.kwargs.update({
            'reservation_order_alias_name': "TestNameRo",
            'location': "westus",
            'applied_scope_type': "Shared",
            'billing_plan': "P1M",
            'billing_scope_id': "/subscriptions/eef82110-c91b-4395-9420-fcfcbefc5a47",
            'display_name': "TestNameRo",
            'quantity': "1",
            'renew': "false",
            'reserved_resource_type': "VirtualMachines",
            'sku': "Standard_B1ls",
            'term': "P1Y",
        })
        response = self.cmd('billing-benefits reservation-order-aliases create --order-alias-name {reservation_order_alias_name} --location {location} --applied-scope-type {applied_scope_type} '
                            '--billing-plan {billing_plan} --billing-scope-id {billing_scope_id} --display-name {display_name} --quantity {quantity} --renew {renew} --reserved-resource-type {reserved_resource_type} --sku {sku} --term {term}').get_output_in_json()

        self._validate_reservation_order_alias(response)

        response2 = self.cmd(
            'billing-benefits reservation-order-aliases show --order-alias-name {reservation_order_alias_name}').get_output_in_json()
        self._validate_reservation_order_alias(response2)

    @record_only()
    def test_billing_benefits_list_savings_plan(self):
        savings_plan_list = self.cmd(
            'billing-benefits savings-plan list').get_output_in_json()
        self.assertIsNotNone(savings_plan_list)
        for item in savings_plan_list:
            self._validate_savings_plan_item(item)

    @record_only()
    def test_billing_benefits_elevate_savings_plan_order(self):
        self.kwargs.update({
            'order_id': '23792c39-712d-449e-9c45-795a0363a9bd'
        })
        response = self.cmd(
            'billing-benefits savings-plan-order elevate --savings-plan-order-id {order_id}').get_output_in_json()
        self.assertIsNotNone(response['roleDefinitionId'])
        self.assertIsNotNone(response['principalId'])
        self.assertIsNotNone(response['scope'])
        self.assertIsNotNone(response['id'])
        self.assertIsNotNone(response['name'])

    @record_only()
    def test_billing_benefits_savings_plan_order_list(self):
        response = self.cmd(
            'az billing-benefits savings-plan-order list').get_output_in_json()
        self.assertIsNotNone(response)
        for item in response:
            self._validate_savings_plan_order(item)

    @record_only()
    def test_billing_benefits_savings_plan_order_get(self):
        self.kwargs.update({
            'order_id': '91636c5c-051b-4c19-afd7-2b774259d49f'
        })
        response = self.cmd(
            'az billing-benefits savings-plan-order show --savings-plan-order-id {order_id}').get_output_in_json()
        self.assertIsNotNone(response)
        self._validate_savings_plan_order(response)

        # Test 'expand'
        response1 = self.cmd(
            'az billing-benefits savings-plan-order show --savings-plan-order-id {order_id} --expand schedule').get_output_in_json()
        self.assertIsNotNone(response1)
        self._validate_savings_plan_order(response1)
        self.assertIsNotNone(response1['planInformation'])
        self.assertIsNotNone(
            response1['planInformation']['pricingCurrencyTotal'])
        self.assertEqual(response1['planInformation']
                         ['pricingCurrencyTotal']['currencyCode'], 'USD')
        self.assertGreater(response1['planInformation']
                           ['pricingCurrencyTotal']['amount'], 0)
        self.assertIsNotNone(response1['planInformation']['startDate'])
        self.assertIsNotNone(
            response1['planInformation']['nextPaymentDueDate'])
        self.assertIsNotNone(response1['planInformation']['transactions'])
        self.assertGreater(
            len(response1['planInformation']['transactions']), 0)
        for item in response1['planInformation']['transactions']:
            self.assertIsNotNone(item['dueDate'])
            self.assertIsNotNone(item['status'])
            self.assertIsNotNone(item['pricingCurrencyTotal'])

    @record_only()
    def test_billing_benefits_savings_plan_list_items_in_order(self):
        self.kwargs.update({
            'order_id': '91636c5c-051b-4c19-afd7-2b774259d49f'
        })
        response = self.cmd(
            'az billing-benefits savings-plan-order savings-plan list --savings-plan-order-id {order_id}').get_output_in_json()
        self.assertIsNotNone(response)
        for item in response:
            self._validate_savings_plan_item(item)

    @record_only()
    def test_billing_benefits_savings_plan_get_item(self):
        self.kwargs.update({
            'order_id': '683ae71d-f43a-4b76-bb26-9a6ffef80030',
            'item_id': 'ce6eaefe-3abe-4961-8455-1e8b1e041a6f'
        })
        response = self.cmd(
            'az billing-benefits savings-plan-order savings-plan show --savings-plan-order-id {order_id} --savings-plan-id {item_id}').get_output_in_json()
        self._validate_savings_plan_item(response)

        # Test 'expand'
        response1 = self.cmd(
            'az billing-benefits savings-plan-order savings-plan show --savings-plan-order-id {order_id} --savings-plan-id {item_id} --expand renewProperties').get_output_in_json()
        self._validate_savings_plan_item(response1)
        self.assertIsNotNone(response1['renewProperties'])
        self.assertIsNotNone(
            response1['renewProperties']['purchaseProperties'])
        self.assertIsNotNone(
            response1['renewProperties']['purchaseProperties']['sku'])
        self.assertEqual(
            response1['renewProperties']['purchaseProperties']['sku']['name'], 'Compute_Savings_Plan')
        self.assertIsNotNone(
            response1['renewProperties']['purchaseProperties']['billingScopeId'])
        self.assertEqual(response1['renewProperties']
                         ['purchaseProperties']['term'], 'P1Y')
        self.assertEqual(response1['renewProperties']
                         ['purchaseProperties']['billingPlan'], 'Monthly')
        self.assertEqual(response1['renewProperties']
                         ['purchaseProperties']['displayName'], 'name1')
        self.assertEqual(
            response1['renewProperties']['purchaseProperties']['appliedScopeType'], 'Shared')
        self.assertIsNotNone(
            response1['renewProperties']['purchaseProperties']['commitment'])
        self.assertEqual(
            response1['renewProperties']['purchaseProperties']['commitment']['grain'], 'Hourly')
        self.assertEqual(
            response1['renewProperties']['purchaseProperties']['commitment']['currencyCode'], 'USD')
        self.assertGreater(
            response1['renewProperties']['purchaseProperties']['commitment']['amount'], 0)

    @record_only()
    def test_billing_benefits_savings_plan_item_update(self):
        self.kwargs.update({
            'order_id': '683ae71d-f43a-4b76-bb26-9a6ffef80030',
            'item_id': 'ce6eaefe-3abe-4961-8455-1e8b1e041a6f',
            'name': 'newName1',
            'renew': 'true',
            'renew_properties': '{purchase-properties:{applied-scope-type:Shared,billing-plan:P1M,billing-scope-id:/subscriptions/eef82110-c91b-4395-9420-fcfcbefc5a47,commitment:{amount:10.0,currency-code:USD,grain:Hourly},display-name:name1,renew:true,term:P1Y,sku:Compute_Savings_Plan}}',
            'scope': 'Single',
            'scope_properties': '{subscription-id:/subscriptions/eef82110-c91b-4395-9420-fcfcbefc5a47}'
        })

        # First get the item for original state
        response = self.cmd(
            'az billing-benefits savings-plan-order savings-plan show --savings-plan-order-id {order_id} --savings-plan-id {item_id}').get_output_in_json()
        self.assertIsNotNone(response)
        self.assertNotEqual(response['renew'], True)
        self.assertNotEqual(response['appliedScopeType'], 'Single')
        self.assertNotEqual(response['displayName'], 'newName1')

        response1 = self.cmd(
            'az billing-benefits savings-plan-order savings-plan update --savings-plan-order-id {order_id} --savings-plan-id {item_id} --display-name {name} --renew {renew} --renew-properties {renew_properties} --applied-scope-type {scope} --applied-scope-prop {scope_properties}').get_output_in_json()
        self.assertIsNotNone(response1)

        # Then get the item after update to verify
        response2 = self.cmd(
            'az billing-benefits savings-plan-order savings-plan show --savings-plan-order-id {order_id} --savings-plan-id {item_id} --expand renewProperties').get_output_in_json()
        self.assertIsNotNone(response2)
        self.assertEqual(response2['renew'], True)
        self.assertEqual(response2['appliedScopeType'], 'Single')
        self.assertEqual(response2['displayName'], 'newName1')
        self.assertIsNotNone(response2['appliedScopeProperties'])
        self.assertIsNotNone(
            response2['appliedScopeProperties']['subscriptionId'])
        self.assertIsNotNone(
            response2['appliedScopeProperties']['displayName'])
        self.assertIsNotNone(response2['renewProperties'])
        self.assertIsNotNone(
            response2['renewProperties']['purchaseProperties'])
        self.assertIsNotNone(
            response2['renewProperties']['purchaseProperties']['sku'])
        self.assertEqual(
            response2['renewProperties']['purchaseProperties']['sku']['name'], 'Compute_Savings_Plan')
        self.assertIsNotNone(
            response2['renewProperties']['purchaseProperties']['billingScopeId'])
        self.assertEqual(response2['renewProperties']
                         ['purchaseProperties']['term'], 'P1Y')
        self.assertEqual(response2['renewProperties']
                         ['purchaseProperties']['billingPlan'], 'Monthly')
        self.assertEqual(response2['renewProperties']
                         ['purchaseProperties']['displayName'], 'name1')
        self.assertEqual(
            response2['renewProperties']['purchaseProperties']['appliedScopeType'], 'Shared')
        self.assertIsNotNone(
            response2['renewProperties']['purchaseProperties']['commitment'])
        self.assertEqual(
            response2['renewProperties']['purchaseProperties']['commitment']['grain'], 'Hourly')
        self.assertEqual(
            response2['renewProperties']['purchaseProperties']['commitment']['currencyCode'], 'USD')
        self.assertGreater(
            response2['renewProperties']['purchaseProperties']['commitment']['amount'], 0)

    @record_only()
    def test_billing_benefits_savings_plan_item_validate_update(self):
        benefit = '{applied-scope-type:Shared,display-name:newName2}'
        benefits = '[{}]'.format(benefit)
        self.kwargs.update({
            'order_id': '683ae71d-f43a-4b76-bb26-9a6ffef80030',
            'item_id': 'ce6eaefe-3abe-4961-8455-1e8b1e041a6f',
            'benefits': benefits
        })

        response = self.cmd(
            'az billing-benefits savings-plan-order savings-plan validate-update --savings-plan-order-id {order_id} --savings-plan-id {item_id} --benefits {benefits}').get_output_in_json()
        self.assertIsNotNone(response)
        self.assertIsNotNone(response['benefits'])
        self.assertGreater(len(response['benefits']), 0)
        for item in response['benefits']:
            self.assertIsNotNone(item['valid'])
            self.assertTrue(item['valid'])

    @record_only()
    def test_savings_plan_order_alias(self):
        commitment = '{amount:10,currency-code:USD,grain:Hourly}'
        self.kwargs.update({
            'order_alias_name': "TestNameSO2",
            'applied_scope_type': "Shared",
            'billing_plan': "P1M",
            'billing_scope_id': "/subscriptions/eef82110-c91b-4395-9420-fcfcbefc5a47",
            'display_name': "TestNameSO2",
            'commitment': commitment,
            'sku': "Compute_Savings_Plan",
            'term': "P1Y",
        })
        response = self.cmd(
            'billing-benefits savings-plan-order-aliases create --order-alias-name {order_alias_name} --applied-scope-type {applied_scope_type} --billing-plan {billing_plan} --billing-scope-id {billing_scope_id} --commitment {commitment} --display-name {display_name} --term {term} --sku {sku}').get_output_in_json()

        self._validate_savings_plan_order_alias(response)

        response2 = self.cmd(
            'billing-benefits savings-plan-order-aliases show --order-alias-name {order_alias_name}').get_output_in_json()
        self._validate_savings_plan_order_alias(response2)
