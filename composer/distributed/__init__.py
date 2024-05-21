# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

"""Distributed training"""

from composer.distributed.deepspeed import fix_batch_precision_for_deepspeed, parse_deepspeed_config
from composer.distributed.dist_strategy import DDPSyncStrategy, ddp_sync_context, prepare_ddp_module, prepare_fsdp_module, prepare_tp_module
from composer.distributed.mosaic_fsdp import patch_pytorch, set_fsdp_default, SavePlannerWithDedupFix


__all__ = [
    'fix_batch_precision_for_deepspeed',
    'parse_deepspeed_config',
    'DDPSyncStrategy',
    'ddp_sync_context',
    'prepare_ddp_module',
    'prepare_fsdp_module',
    'prepare_tp_module',
    'patch_pytorch',
    'set_fsdp_default',
    'SavePlannerWithDedupFix',
]
