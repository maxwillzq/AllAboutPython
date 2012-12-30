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
#
# @author: psimakov@google.com (Pavel Simakov)


"""All handlers here either serve the cached pages or delegate to real handlers."""

import logging, json

from models.models import Student

import lessons, utils
from utils import StudentHandler
from google.appengine.api import users


"""
Handler for serving course page.
"""
class CourseHandler(StudentHandler):

  def get(self):
    student = self.getEnrolledStudent()
    if student:
      page = self.getOrCreatePage('course_page', lessons.CourseHandler())
      self.serve(page, student.key().name())
    else:
      self.redirect('/preview')


"""
Handler for serving class page.
"""
class UnitHandler(StudentHandler):

  def get(self):
    # Extract incoming args
    c = self.request.get('unit')
    if not c:
      class_id = 1
    else:
      class_id = int(c)

    l = self.request.get('lesson')
    if not l:
      lesson_id = 1
    else:
      lesson_id = int(l)

    # Check for enrollment status
    student = self.getEnrolledStudent()
    if student:
      page = self.getOrCreatePage(
          'lesson%s%s_page' % (class_id, lesson_id), lessons.UnitHandler())
      self.serve(page, student.key().name())
    else:
      self.redirect('/register')


"""
Handler for serving activity page.
"""
class ActivityHandler(StudentHandler):

  def get(self):
    # Extract incoming args
    c = self.request.get('unit')
    if not c:
      class_id = 1
    else:
      class_id = int(c)

    l = self.request.get('lesson')
    if not l:
      lesson_id = 1
    else:
      lesson_id = int(l)

    # Check for enrollment status
    student = self.getEnrolledStudent()
    if student:
      page = self.getOrCreatePage(
          'activity' + str(class_id) + str(lesson_id) + '_page', lessons.ActivityHandler())
      self.serve(page, student.key().name())
    else:
      self.redirect('/register')


"""
Handler for serving assessment page.
"""
class AssessmentHandler(StudentHandler):

  def get(self):
    # Extract incoming args
    n = self.request.get('name')
    if not n:
      n = 'Pre'
    name = n

    # Check for enrollment status
    student = self.getEnrolledStudent()
    if student:
      page = self.getOrCreatePage(
          'assessment' + name + '_page', lessons.AssessmentHandler())
      self.serve(page, student.key().name())
    else:
      self.redirect('/register')


"""
Handler for serving forum page.
"""
class ForumHandler(StudentHandler):

  def get(self):
    # Check for enrollment status
    student = self.getEnrolledStudent()
    if student:
      page = self.getOrCreatePage('forum_page', utils.ForumHandler())
      self.serve(page, student.key().name())
    else:
      self.redirect('/register')


"""
Handler for serving preview page.
"""
class PreviewHandler(StudentHandler):

  def get(self):
    user = users.get_current_user()
    if user:
      if Student.get_enrolled_student_by_email(user.email()):
        self.redirect('/course')
      else:
        page = self.getOrCreatePage('loggedin_preview_page', utils.CoursePreviewHandler())
        self.serve(page, user.email())
    else:
      page = self.getOrCreatePage('anonymous_preview_page', utils.CoursePreviewHandler())
      self.serve(page)

