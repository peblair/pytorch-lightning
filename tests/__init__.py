# Copyright The PyTorch Lightning team.
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
import os

import numpy as np
import torch

from pytorch_lightning.utilities import (
    _APEX_AVAILABLE,
    _NATIVE_AMP_AVAILABLE,
    _TORCH_LOWER_EQUAL_1_4,
    _TORCH_QUANTIZE_AVAILABLE,
)
from tests.helpers.skipif import SkipIf

_TEST_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_TEST_ROOT)
_TEMP_PATH = os.path.join(_PROJECT_ROOT, 'test_temp')
DATASETS_PATH = os.path.join(_PROJECT_ROOT, 'Datasets')
LEGACY_PATH = os.path.join(_PROJECT_ROOT, 'legacy')

# todo: this setting `PYTHONPATH` may not be used by other evns like Conda for import packages
if _PROJECT_ROOT not in os.getenv('PYTHONPATH', ""):
    splitter = ":" if os.environ.get("PYTHONPATH", "") else ""
    os.environ['PYTHONPATH'] = f'{_PROJECT_ROOT}{splitter}{os.environ.get("PYTHONPATH", "")}'

# generate a list of random seeds for each test
RANDOM_PORTS = list(np.random.randint(12000, 19000, 1000))

if not os.path.isdir(_TEMP_PATH):
    os.mkdir(_TEMP_PATH)

_SKIPIF_PT_LE_1_4 = SkipIf(condition=_TORCH_LOWER_EQUAL_1_4, reason="test pytorch > 1.4")
_SKIPIF_NO_GPU = SkipIf(condition=not torch.cuda.is_available(), reason="test requires any GPU machine")
_SKIPIF_NO_GPUS = SkipIf(condition=torch.cuda.device_count() < 2, reason="test requires multi-GPU machine")
_SKIPIF_NO_AMP = SkipIf(condition=not _NATIVE_AMP_AVAILABLE, reason="test requires native AMP")
_SKIPIF_NO_APEX = SkipIf(condition=not _APEX_AVAILABLE, reason="test requires APEX")
_SKIPIF_NO_PT_QUANT = SkipIf(
    condition=not _TORCH_QUANTIZE_AVAILABLE, reason="PyTorch quantization is needed for this test"
)
