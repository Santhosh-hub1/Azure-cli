# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements, protected-access

from knack.log import get_logger
from azext_amlfs.aaz.latest.amlfs import Create as _AmlfsCreate

logger = get_logger(__name__)


class AmlfsCreate(_AmlfsCreate):
    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        from azure.cli.core.aaz import AAZResourceIdArg, AAZResourceIdArgFormat, AAZListArg
        args_schema = super()._build_arguments_schema(*args, **kwargs)
        args_schema.mi_user_assigned = AAZListArg(
            options=["--mi-user-assigned"],
            help="Space separated resource IDs to add user-assigned identities.",
        )
        args_schema.mi_user_assigned.Element = AAZResourceIdArg(
            fmt=AAZResourceIdArgFormat(template="/subscriptions/{subscription}/resourceGroups/{resource_group}"
                                                "/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{}")
        )
        args_schema.identity._registered = False
        return args_schema

    def pre_operations(self):
        from azure.cli.core.aaz import has_value
        args = self.ctx.args
        if has_value(self.ctx.args.mi_user_assigned):
            args.identity.type = "UserAssigned"
            user_assigned_identities = {}
            for identity in args.mi_user_assigned:
                user_assigned_identities.update({
                    identity.to_serialized_data(): {}
                })
            args.identity.user_assigned_identities = user_assigned_identities
