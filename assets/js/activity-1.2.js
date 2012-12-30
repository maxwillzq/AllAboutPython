// Copyright 2012 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


// Usage instructions: Create a single array variable named 'activity'. This
// represents explanatory text and one or more questions to present to the
// student. Each element in the array should itself be either
//
// -- a string containing a set of complete HTML elements. That is, if the
//    string contains an open HTML tag (such as <form>), it must also have the
//    corresponding close tag (such as </form>). You put the actual question
//    text in a string.
//
// -- a JavaScript object representing the answer information for a question.
//    That is, the object contains properties such as the type of question, a
//    regular expression indicating the correct answer, a string to show in
//    case of either correct or incorrect answers or to show when the student
//    asks for help. For more information on how to specify the object, please
//    see http://code.google.com/p/course-builder/wiki/CreateActivities.

var activity = [

  '<br><br><br>Practice code sample: <iframe src="https://docs.google.com/file/d/0B3YNr_NmMv7US1VFeW05SHY3OU0/preview" width="640" height="480"></iframe><br><br><br>',
  

  { questionType: 'multiple choice',
    choices: [['A', false, 'Please try again.'],
              ['B', false, 'Please try again.'],
              ['C', false, 'Please try again.'],
              ['D', true, 'Correct! Filtering by color would help you view all the books with yellow covers.']]},

  '<br><br><br><img src="assets/img/Image1.3.png" height=450 width=785><p/>',
  '<br><b>2.</b> You want statistics on college loans. If you search using [college loans statistics], you get the image results above. What color would you click to see just the charts and graphs? ',

  { questionType: 'freetext',
    correctAnswerRegex: /white?/i,
    correctAnswerOutput: 'Correct! Many charts, tables, and graphs have white backgrounds, so filtering for white images helps you find them faster.',
    incorrectAnswerOutput: 'Try again. Consider what color would be dominant in images of charts, tables, and graphs. Look at the results above. Each of those sources is traditionally printed on paper.',
    showAnswerOutput: 'Our search expert says: I would click on white in the color grid, since many charts, tables, and graphs have white backgrounds.' },

  '<br><br><br><b>3.</b> What is something you have wanted to find that color filtering might have helped you locate faster? Try it out and share your story in the <a href="LINK_TO_COURSE_FORUM" target="_blank">forum</a>.',

];

