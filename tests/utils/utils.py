
# -*- coding: utf-8 -*-
#
# This file is part of Inspirehep.
# Copyright (C) 2016 CERN.
#
# Inspirehep is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Inspirehep is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Inspirehep; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.
import json
from json_merger.conflict import Conflict

from inspire_schemas.api import load_schema, validate

"""Pytest utils."""


def assert_ordered_conflicts(conflicts, expected_conflicts):
    # expected conflict is a Conflict class instance
    expected_conflict = [
        json.loads(Conflict(c[0], c[1], c[2]).to_json()) for c in expected_conflicts
    ]

    # order the lists to check if they match
    conflicts = sorted(conflicts, key=lambda c: c['path'])
    expected_conflict = sorted(expected_conflict, key=lambda c: c['path'])

    assert conflicts == expected_conflict


def validate_subschema(obj):
    schema = load_schema('hep')
    key = list(obj.keys())[0]  # python 3 compatibility
    sub_schema = schema['properties'].get(key)
    assert validate(obj.get(key), sub_schema) is None

