# Aira Sadiasa CIS 345 T/Th 10:30-11:45

INTRODUCTION
------------

Mental Anguish is a quiz management system utilizing Tkinter as its GUI. 
You can create, edit, add, delete, search for questions.
The application is able to save and load a list of questions from a txt file. 

FEATURES
------------
Upon opening Mental Anguish, there will be 10 pre-loaded questions. 
You may also load your own questions with the following steps:
1.) Make sure that your .txt file is in the directory 
2.) Call get_questions() and pass your .txt file. Assign this to a variable, question_pool
3.) Call load_file() and pass your question_pool 

-Add 
To create a question, simply fill out the required fields including: question, points, four choices, correct answer, and feedback 
When you click save, the question will automatically be added to the list of questions on the bottom of the screen. 
Simply scroll down to see your question. 

-Edit
To edit an existing question, double click on a question in the list box. 
All fields will automatically be filled in the appropriate box. 
Once you are done editing a question, simply hit save and the edited question will re-appear in the list box. 

-Delete
Select the question you wish to delete from the list box. Then on the upper left corner of the screen, click on the 'Edit' menu, a dropdown menu will appear. Then press 'Delete'. 
The question will be removed from the listbox. 

-Search 
To search for a question, navigate to the Edit menu on the upper left hand of the screen. 
Press 'Search' and you will be brought to a new window. 
Enter the item you wish to search for in the designated entry box. 
In this prorotype, you can only search for one item at a time. 
If you want to search for a question, you may not search for an answer choice or feedback at the same time. 
You must do another search by pressing the 'Clear' button.
From this window you can choose to do the following:
1.) Take the quiz by pressing 'Take quiz' button 
2.) Go back to edit mode, by pressing on the Edit menu and clicking on 'View' 

-Take quiz 
You make begin taking the quiz by the following options: 
1.) Press 'Take quiz' button located on the bottom right of the screen. 
2.) Click on the File menu, press 'New Game'

The quiz is programmed to ask 3 random and unique questions. 
Type your answer in the entry box and hit submit. 
Spelling matters but capitalization does not! 
It's Mental Anguish, we are also testing if you are spelling bee worthy! 
Once you hit submit, the game will give you feedback depending if you get the question right or wrong.
Your current score will also be displayed out of the total points. 
You can keep track of your progress with the progress bar. 
Press the 'Next' button when you are ready to move on to the next question. 
The game will stop once you have answered three questions. 
To play a new game, navigate to the File menu, and press 'New Game'
You can also go back to and of the edit Features by navigating to the Edit menu, and pressing 'View' 
The third option is to navigate to the File menu and press 'Exit Application'. This will quit the entire Mental Anguish application. Sorry to see you go! 