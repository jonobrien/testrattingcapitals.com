#!/usr/bin/env python3
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
import logging
import os
import signal
import sys

logger = logging.getLogger('testrattingcapitals')

app = Flask(__name__)

def configure_logging():
    logger.setLevel(int(os.getenv('LOG_LEVEL', logging.DEBUG)))
    stdio = logging.StreamHandler(sys.stdout)
    stdio.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(stdio)

configure_logging()
    
logger.info('testrattingcapitals api started')

@app.route('/')
def health():
    return 'OK'