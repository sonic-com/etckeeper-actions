#!/usr/bin/python

# Copyright: (c) 2018, Håkon Løvdal <kode@denkule.no>
# GNU General Public License v3.0+ (see gpl.txt, https://tldrlegal.com/l/gpl-3.0 or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):

    TRANSFERS_FILES = False

    def run(self, tmp=None, task_vars=None):
        msg = 'saving uncommitted changes in /etc prior to ansible task run'
        result = self._low_level_execute_command('etckeeper commit "%s"' % msg)
        # In case of no changes the command will fail, but ignore that
        if (result['rc'] == 1) and ('nothing to commit, working tree clean' in result['stdout']):
            result['rc'] = 0
        return result
