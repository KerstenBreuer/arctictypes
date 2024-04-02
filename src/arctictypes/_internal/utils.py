# Copyright 2024 Kersten Henrik Breuer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utilities"""

# Check if Pydantic v2 is installed and store the result in a constant:
PYDANTIC_V2_INSTALLED = False
PYDANTIC_VERSION_PREFIX = "2."
try:
    from pydantic import __version__ as pydantic_version
    from pydantic_core import __version__ as pydantic_core_version
except ImportError:
    pass
else:
    if pydantic_version.startswith(
        PYDANTIC_VERSION_PREFIX
    ) and pydantic_core_version.startswith(PYDANTIC_VERSION_PREFIX):
        PYDANTIC_V2_INSTALLED = True