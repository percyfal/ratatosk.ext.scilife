# Copyright (c) 2013 Per Unneberg
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import os
import ratatosk.ext.scilife
# Define configuration file locations for predefined workflows
config_dict = {
    'ratatosk' : os.path.join(ratatosk.ext.scilife.__path__[0], os.pardir, os.pardir, os.pardir, "config", "scilife", "ratatosk.yaml"),
    'seqcap' : os.path.join(ratatosk.ext.scilife.__path__[0], os.pardir, os.pardir, os.pardir, "config", "scilife", "align_seqcap.yaml"),
    'haloplex' : os.path.join(ratatosk.ext.scilife.__path__[0], os.pardir, os.pardir, os.pardir, "config", "scilife", "haloplex.yaml"),
    }