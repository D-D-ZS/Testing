#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

steps = yaml.safe_load(open("../config/steps.yml"))


def pytest_collection_modifyitems(session, config, items:list):
    # print(items)
    new_items = []
    for step in steps:
        for item in items:
            if step in item.nodeid:
                item.add_marker(step)
                new_items.append(item)
    items[:] = new_items


