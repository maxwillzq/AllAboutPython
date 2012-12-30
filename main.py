# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import appengine_config, webapp2
from controllers import servings, sites, utils, assessments
from webapp2 import WSGIApplication, Route

#inject './lib' dir in the path so that we can simple
#do "import ndb" or whatever there 's in the app lib dir
if 'lib' not in sys.path:
	sys.path[0:0] = ['lib']

# webapp2 config
app_config = {}

# FIXME: set to 'False' before going live
debug = True

urls = [
  ('/', servings.CourseHandler),
  ('/activity', servings.ActivityHandler),
  ('/announcements', utils.AnnouncementsHandler),
  ('/answer', assessments.AnswerHandler),
  ('/assessment', servings.AssessmentHandler),
  ('/course', servings.CourseHandler),
  ('/forum', servings.ForumHandler),
  ('/preview', servings.PreviewHandler),
  ('/register', utils.RegisterHandler),
  ('/student/editstudent', utils.StudentEditStudentHandler),
  ('/student/home', utils.StudentProfileHandler),
  ('/student/unenroll', utils.StudentUnenrollHandler),
  ('/unit', servings.UnitHandler),]

sites.ApplicationRequestHandler.bind(urls)

routes =[]
routes.extend([(r'(.*)', sites.ApplicationRequestHandler)])

app = WSGIApplication(routes,config=app_config,debug=debug)

