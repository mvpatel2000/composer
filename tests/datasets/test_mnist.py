# Copyright 2022 MosaicML Composer authors
# SPDX-License-Identifier: Apache-2.0

import pytest

from composer.datasets import build_synthetic_mnist_dataloader


@pytest.mark.parametrize('is_train', [False, True])
def test_mnist_shape_length(is_train):
    batch_size = 1
    loader = build_synthetic_mnist_dataloader(global_batch_size=batch_size, is_train=is_train)

    samples = [_ for _ in loader]
    if is_train:
        assert len(samples) == 60000 // batch_size
    else:
        assert len(samples) == 10000 // batch_size

    assert samples[0][0].shape == (1, 1, 28, 28)
