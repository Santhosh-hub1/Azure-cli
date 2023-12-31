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
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    resource_group_name_type,
)
from azure.cli.core.commands.validators import (
    validate_file_or_dict,
)

from azext_datafactory.action import (
    AddFactoryVstsConfiguration,
    AddFactoryGitHubConfiguration,
)


def load_arguments(self, _):
    # DataFactory
    with self.argument_context("datafactory create") as c:
        c.argument(
            "factory_vsts_configuration",
            options_list=["--vsts-config", "--factory-vsts-configuration"],
            action=AddFactoryVstsConfiguration,
            nargs="+",
            help="Factory's VSTS repo information.",
            arg_group="RepoConfiguration",
        )
        c.argument(
            "factory_git_hub_configuration",
            options_list=["--github-config", "--factory-git-hub-configuration"],
            action=AddFactoryGitHubConfiguration,
            nargs="+",
            help="Factory's GitHub repo information.",
            arg_group="RepoConfiguration",
        )

    with self.argument_context("datafactory configure-factory-repo") as c:
        c.argument(
            "factory_vsts_configuration",
            options_list=["--vsts-config", "--factory-vsts-configuration"],
            action=AddFactoryVstsConfiguration,
            nargs="+",
            help="Factory's VSTS repo information.",
            arg_group="RepoConfiguration",
        )
        c.argument(
            "factory_git_hub_configuration",
            options_list=["--github-config", "--factory-git-hub-configuration"],
            action=AddFactoryGitHubConfiguration,
            nargs="+",
            help="Factory's GitHub repo information.",
            arg_group="RepoConfiguration",
        )

    # Data Flows
    with self.argument_context("datafactory data-flow show") as c:
        c.argument("resource_group_name", resource_group_name_type)
        c.argument(
            "factory_name",
            options_list=["--factory-name", "-f"],
            type=str,
            help="The factory name.",
            id_part="name",
        )
        c.argument(
            "data_flow_name",
            options_list=["--name", "-n", "--data-flow-name"],
            type=str,
            help="The data flow name.",
            id_part="child_name_1",
        )
        c.argument(
            "if_none_match",
            type=str,
            help="ETag of the pipeline entity. Should only be specified for get. If "
            "the ETag matches the existing entity tag, or if * was provided, then no content will be returned.",
        )

    with self.argument_context("datafactory data-flow list") as c:
        c.argument("resource_group_name", resource_group_name_type)
        c.argument(
            "factory_name",
            options_list=["--factory-name", "-f"],
            type=str,
            help="The factory name.",
            id_part=None,
        )

    with self.argument_context("datafactory data-flow delete") as c:
        c.argument("resource_group_name", resource_group_name_type)
        c.argument(
            "factory_name",
            options_list=["--factory-name", "-f"],
            type=str,
            help="The factory name.",
            id_part="name",
        )
        c.argument(
            "data_flow_name",
            options_list=["--name", "-n", "--data-flow-name"],
            type=str,
            help="The data flow name.",
            id_part="child_name_1",
        )

    with self.argument_context("datafactory data-flow create") as c:
        c.argument("resource_group_name", resource_group_name_type)
        c.argument(
            "factory_name",
            options_list=["--factory-name", "-f"],
            type=str,
            help="The factory name.",
            id_part="name",
        )
        c.argument(
            "data_flow_name",
            options_list=["--name", "-n", "--data-flow-name"],
            type=str,
            help="The data flow name.",
            id_part="child_name_1",
        )
        c.argument("properties", type=validate_file_or_dict)
        c.argument(
            "flow_type",
            options_list=["--flow-type", "-t"],
            type=str,
            help="The data flow type. Valid choices: MappingDataFlow, Flowlet",
        )
        c.argument(
            "if_match",
            type=str,
            help="ETag of the data flow entity.  Should only be specified for update, for "
            "which it should match existing entity or can be * for unconditional update.",
        )

    with self.argument_context("datafactory data-flow update") as c:
        c.argument("resource_group_name", resource_group_name_type)
        c.argument(
            "factory_name",
            options_list=["--factory-name", "-f"],
            type=str,
            help="The factory name.",
            id_part="name",
        )
        c.argument(
            "data_flow_name",
            options_list=["--name", "-n", "--data-flow-name"],
            type=str,
            help="The data flow name.",
            id_part="child_name_1",
        )
        c.argument("properties", type=validate_file_or_dict)
        c.argument(
            "if_match",
            type=str,
            help="ETag of the data flow entity.  Should only be specified for update, for "
            "which it should match existing entity or can be * for unconditional update.",
        )
