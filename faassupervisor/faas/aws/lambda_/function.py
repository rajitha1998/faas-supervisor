# Copyright (C) GRyCAP - I3M - UPV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import faassupervisor.utils as utils

class LambdaInstance():

    def __init__(self, context):
        self.context = context
        self.request_id = context.aws_request_id
        utils.set_environment_variable('AWS_LAMBDA_REQUEST_ID', context.aws_request_id)
        self.memory = int(context.memory_limit_in_mb)
        self.arn = context.invoked_function_arn
        self.function_name = context.function_name
        self.log_group_name = self.context.log_group_name
        self.log_stream_name = self.context.log_stream_name  
        self.permanent_folder = "/var/task"

    def get_invocation_remaining_seconds(self):
        return int(self.context.get_remaining_time_in_millis() / 1000) - int(utils.get_environment_variable('TIMEOUT_THRESHOLD'))
    