# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# pylint: disable=protected-access

# pylint: disable=no-self-use


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddFilterableProperties(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.filterable_properties = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            v = properties[k]

            d[k] = v[0]

        return d


class AddRegisteredFeatures(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddRegisteredFeatures, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'name':
                d['name'] = v[0]

            elif kl == 'state':
                d['state'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter registered-features. All possible keys are: name,'
                    ' state'.format(k)
                )

        return d


class AddShippingAddress(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.shipping_address = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'street-address1':
                d['street_address1'] = v[0]

            elif kl == 'street-address2':
                d['street_address2'] = v[0]

            elif kl == 'street-address3':
                d['street_address3'] = v[0]

            elif kl == 'city':
                d['city'] = v[0]

            elif kl == 'state-or-province':
                d['state_or_province'] = v[0]

            elif kl == 'country':
                d['country'] = v[0]

            elif kl == 'postal-code':
                d['postal_code'] = v[0]

            elif kl == 'zip-extended-code':
                d['zip_extended_code'] = v[0]

            elif kl == 'company-name':
                d['company_name'] = v[0]

            elif kl == 'address-type':
                d['address_type'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter shipping-address. All possible keys are:'
                    ' street-address1, street-address2, street-address3, city, state-or-province, country, postal-code,'
                    ' zip-extended-code, company-name, address-type'.format(k)
                )

        return d


class AddContactDetails(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.contact_details = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'contact-name':
                d['contact_name'] = v[0]

            elif kl == 'phone':
                d['phone'] = v[0]

            elif kl == 'phone-extension':
                d['phone_extension'] = v[0]

            elif kl == 'mobile':
                d['mobile'] = v[0]

            elif kl == 'email-list':
                d['email_list'] = v

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter contact-details. All possible keys are: contact-name,'
                    ' phone, phone-extension, mobile, email-list'.format(k)
                )

        return d


class AddNotificationPreferences(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddNotificationPreferences, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'stage-name':
                d['stage_name'] = v[0]

            elif kl == 'send-notification':
                d['send_notification'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter notification-preferences. All possible keys are:'
                    ' stage-name, send-notification'.format(k)
                )

        return d


class AddTransportPreferences(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.transport_preferences = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'preferred-shipment-type':
                d['preferred_shipment_type'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter transport-preferences. All possible keys are:'
                    ' preferred-shipment-type'.format(k)
                )

        return d


class AddEncryptionPreferences(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.encryption_preferences = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'double-encryption-status':
                d['double_encryption_status'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter encryption-preferences. All possible keys are:'
                    ' double-encryption-status'.format(k)
                )

        return d


class AddManagementResourcePreferences(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.management_resource_preferences = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'preferred-management-resource-id':
                d['preferred_management_resource_id'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter management-resource-preferences. All possible keys'
                    ' are: preferred-management-resource-id'.format(k)
                )

        return d
