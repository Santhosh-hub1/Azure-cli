# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "storage-mover agent",
)
class __CMDGroup(AAZCommandGroup):
    """Manage Agent resource, which references a hybrid compute machine that can run jobs.
    """
    pass


__all__ = ["__CMDGroup"]
