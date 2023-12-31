# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import CLIError


def reservations_exception_handler(ex):
    from .vendored_sdks.reservations.models import Error
    if isinstance(ex, Error):
        message = ex.error.error.message
        raise CLIError(message)
    raise ex
