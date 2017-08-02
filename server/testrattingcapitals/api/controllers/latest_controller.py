"""
  Copyright (c) 2016-2017 Tony Lechner and contributors

  testrattingcapitals.com is free software: you can redistribute it and/or
  modify it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, either version 3 of the
  License, or (at your option) any later version.

  testrattingcapitals.com is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License
  along with testrattingcapitals.com.  If not, see
  <http://www.gnu.org/licenses/>.
"""

from flask import jsonify
from flask_restful import Resource
import os

from testrattingcapitals import cache_service
from testrattingcapitals.processors import \
    all_processor, \
    deployment_bad_dragon_processor, \
    ratting_capital_processor, \
    vni_processor

PROCESSORS = [
    deployment_bad_dragon_processor,
    ratting_capital_processor,
    vni_processor,
]

if os.getenv('PERSIST_ALL'):
    PROCESSORS.append(all_processor)


class LatestController(Resource):
    def get(self):
        result = dict()
        for proc in PROCESSORS:
            result[proc.TRACKING_LABEL] = {
                'kill': cache_service.get_latest_for_tracking_label(
                    proc.TRACKING_LABEL
                )
            }
        return jsonify(result)
