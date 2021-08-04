# Copyright (c) 2021 SAP SE or an SAP affiliate company.
# All rights reserved.
# This file is licensed under the Apache Software License, v. 2 except as noted otherwise in the LICENSE file.
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import dataclasses
import enum
import typing


@dataclasses.dataclass(frozen=True)
class WhiteSourceApiExtensionWebsocketWSConfig:
    apiKey: str
    extraWsConfig: typing.Dict
    productToken: str
    projectName: str
    requesterEmail: str
    userKey: str
    wssUrl: str


@dataclasses.dataclass(frozen=True)
class WhiteSourceApiExtensionWebsocketMetadata:
    chunkSize: int
    length: int


@dataclasses.dataclass(frozen=True)
class WhiteSourceApiExtensionWebsocketContract:
    metadata: WhiteSourceApiExtensionWebsocketMetadata
    wsConfig: WhiteSourceApiExtensionWebsocketWSConfig


class WhiteSourceApiExtensionStatusCodeReasons(enum.IntEnum):
    CONTRACT_VIOLATION = 4000
    CHUNK_SIZE_TOO_BIG = 4001
    BINARY_CORRUPTED = 4002
