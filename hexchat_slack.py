# hexchat_slack.py -- Plugin for Hexchat to fix the weird voice/devoice
# behaviour of Slack on IRC.
# Copyright (C) <2015>  <Germano Gabbianelli>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# You can install this program by placing it in ~/.config/hexchat/addons. e.g.
# $ (cd ~/.config/hexchat/addons; wget \
#       https://github.com/tyrion/hexchat-slack/raw/master/hexchat_slack.py)

import re
import hexchat

__module_name__ = "slack"
__module_version__ = "1.0"
__module_description__ = "Fix Slack voice/devoice behaviour."

SERVER = 'slack.com'
PATTERN = re.compile(r'^([+-])v$')


def fix_voice(words, words_eol, userdata):
    host = hexchat.get_info('host')
    if not host.endswith(SERVER):
        return

    server = hexchat.get_info('server')
    mode = PATTERN.match(words[3])
    nick = words[4]

    if mode:
        away = ':' if mode.group(1) == '-' else ''
        hexchat.command(
            'RECV :{nick}!{nick}@{server} AWAY {away}'.format(**locals()))
        return hexchat.EAT_ALL


hexchat.hook_server('MODE', fix_voice)

print('Slack plugin loaded (GPLv3)')
