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
from azure.cli.core.azclierror import InvalidArgumentValueError


class AddStatus(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.status = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise InvalidArgumentValueError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'code':
                d['code'] = v[0]

            elif kl == 'level':
                d['level'] = v[0]

            elif kl == 'display-status':
                d['display_status'] = v[0]

            elif kl == 'message':
                d['message'] = v[0]

            elif kl == 'time':
                d['time'] = v[0]

            else:
                raise InvalidArgumentValueError(
                    'Unsupported Key {} is provided for parameter status. All possible keys are: code, level,'
                    ' display-status, message, time'.format(k)
                )

        return d


class AddConnectionState(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.connection_state = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise InvalidArgumentValueError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'status':
                d['status'] = v[0]

            elif kl == 'description':
                d['description'] = v[0]

            else:
                raise InvalidArgumentValueError(
                    'Unsupported Key {} is provided for parameter connection-state. All possible keys are: status,'
                    ' description'.format(k)
                )

        return d
