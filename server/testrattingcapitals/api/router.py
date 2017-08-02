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

from flask import Flask
from flask_restful import Api

from testrattingcapitals.api.controllers.health_controller import HealthController
from testrattingcapitals.api.controllers.latest_controller import LatestController


def setup_routes(app, api):
    if not isinstance(app, Flask):
        TypeError('app must be of type ', type(Flask))
    if not isinstance(api, Api):
        TypeError('api must be of type ', type(Api))

    api.add_resource(HealthController, '/', '/health')
    api.add_resource(LatestController, '/api/v2/latest')
