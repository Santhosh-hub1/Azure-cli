# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class ControllerState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of dnc controller resource.
    """

    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    PROVISIONING = "Provisioning"

class DelegatedSubnetState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of dnc delegated subnet resource.
    """

    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    PROVISIONING = "Provisioning"

class OrchestratorInstanceState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current state of orchestratorInstance resource.
    """

    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    PROVISIONING = "Provisioning"

class OrchestratorKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of workbook. Choices are user and shared.
    """

    KUBERNETES = "Kubernetes"

class Origin(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system"
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class ResourceIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity used for orchestrator cluster. Type 'SystemAssigned' will use an
    implicitly created identity orchestrator clusters
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"
