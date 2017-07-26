# testrattingcapitals.com

A digital Wall of Shame for the EVE Online group TEST Alliance Please Ignore.

Reads in a stream of all "kill" events in EVE Online and stores interesting 
(read: hilariously embarassing) ones.

Version 2.0.0 is under active development and not ready for release. Check out
version 1 on the master branch for now - it's what's live at
[testrattingcapitals.com](https://testrattingcapitals.com).

## Services

* **daemon** _(python)_ reads in kill events from [zKillboard
  RedisQ](https://github.com/zKillboard/RedisQ), persists ones we identify as
  interesting
* **cacher** _(python)_  runs a predefined set of queries and stores the
  results in redis for consumption by a REST api
* **api** _(python)_ anonymous public REST API
* **webclient** _(javascript)_ web client to render results

## Docker images

* [daemon](https://hub.docker.com/r/tonymke/testrattingcapitals-daemon/)
* [reprocessor](https://hub.docker.com/r/tonymke/testrattingcapitals-reprocessor/)

## License

AGPLv3. See LICENSE.txt

    testrattingcapitals.com is free software: you can redistribute it and/or
    modify it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    Foobar is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
