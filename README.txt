##############################################################################
USER MANUAL

##############################################################################
CONTENTS
------------------------------------------------------------------------------

1.0 - General Instructions

2.0 - Create a New Domain
2.1 - Create a T/F Node
  2.1.1 - Default Statement 
2.2 - Create a Multiple Choice Node
2.3 - Question Creation
  2.3.1 - Question Order

3.0 - Existing Domain
3.1 - Edit Domain Menu
3.2 - Query Domain
  3.2.1 - Question Answering
3.3 - Outcome
  3.3.1 - Report
3.4 - Edit Domain
  3.4.1 - Edit non-leaf node
  3.4.2 - Save
3.5 - Visualise Domain

##############################################################################
1.0 - GENERAL INSTRUCTIONS
------------------------------------------------------------------------------
- Pressing 'START' on the welcome screen will bring you to the main menu and 
allow you to use the application.

- You can go back to the menu at any time but if you are in the middle of 
querying, creating or editing a domain etc your progress in this will be lost.

##############################################################################
2.0 - CREATE A NEW DOMAIN 
------------------------------------------------------------------------------
- After initialising the creation of a new legal domain you must first specify
a name for the domain. This name cannot contain spaces in order to function
properly. 
e.g. if your domain name is Wild Animals, write it as WildAnimals

2.1 - Create a T/F Node
------------------------------------------------------------------------------
- Create this kind of node if you are creating a non-leaf factor and you want
any questions to instantiate the base-level factors to be answered 'Yes' or 'No'.

- You do not need to create nodes for base-level factors, only non-leaf factors.
The base-level factor nodes will be generated for you. The exception is if you
wish the base-level factor to be determined by multiple choice then refer to 2.2.

- First set a name for the node, the name must not contain any spaces. For the
visualisation feature to work properly do not use names which are too long, under
25 characters is best.
e.g. if your node name is Visibility of Item, write it as VisibilityOfItem

- You can then set acceptance conditions and statements.

- Each acceptance condition must have an accompanying statement to be printed
when it is accepted.

- Each acceptance condition must consist of other nodes, which may have been created
previously or not, with the logical operators and, or, not between them.
e.g. Assault and not Trespass

- You may also use brackets in order to make the logical expressions clearer so
long as there are spaces between the brackets and the nodes/logical conditions.
e.g. ( OwnsLand and Resident ) or Convention or Capture

- It is also possible to create a reject condition using the keyword 'reject'.
This keyword means that if the acceptance condition is satisfied the node will
not be added to the factors in the case.
e.g. reject Licence and RestrictedArea

- There must always be a node named Decide in the domain which which
may be created at any time. This node should give the final outcome of the case.

- Press add condition when you have entered your acceptance condition and statement.
This will cause what you have entered to disappear and you can then enter another
acceptance condition and statement if needed. 

2.1.1 - Default Statement 
------------------------------------------------------------------------------
- This statement will be displayed in the outcome if the acceptance condition
is not met.

- Press add statement when you have entered this.

- Press END if you have added all the nodes otherwise add a T/F node or a multi 
node - 2.3 will detail the next screen.

2.2 - Create a Multiple Choice Node
------------------------------------------------------------------------------
- Create this kind of node if you are creating a base-level factor which you
want to instantiate with a multiple choice question.
e.g. If the vehicle is an automobile, is it a: car, mobile home

- To refer to setting the name, acceptance and statement boxes refer to 2.1.

- The only exception to the above is the setting of the acceptance conditions.
The tokens within the acceptance condition, which have not been created as other
nodes, will form the answers of the multiple choice question. The choice made by the
user will then determine whether the node is accepted or not.
e.g. weapon and illegal_substance

- When adding a token into an acceptance condition which you wish to be part of
the multiple choice answer list, the convention is to use underscores instead of 
leaving no spaces as the program will render underscores as spaces when displaying 
the answers to the user which allows for easier comprehension.

- Set the question you wish to have answered by multiple choice.

2.3 - Question Creation
------------------------------------------------------------------------------
- After creating the domain, the program will determine which base-level factors
require questions to be set. Set a question for each and then press add question.

- You can only add one question per base-level factors, repeated entry of questions
will result in the previous question being overwritten.

2.3.1 - Question Order
------------------------------------------------------------------------------
- This screen enables the user to create an order for the questions to be presented
to the user by highlighting a question and then pressing up or down to move it.

- Press DONE when this has been completed. This will bring you to the edit screen
where you can create aditional nodes, delete erroneous nodes, change the question 
order and save the domain you have created. If you do not go through the save function
all progress will be lost upon returning to the menu or exiting the program. 

- For details on saving the domain refer to 3.4.2

##############################################################################
3.0 - EXISTING DOMAIN
------------------------------------------------------------------------------
- This screen allows you to select one of the included domains: Wild Animals,
Trade Secrets, Exception to the Fourth Amendment and Noise-Induced Hearing Loss
or to import a domain you previously created and saved through this application.
This file would be saved as a '.xlsx' file.

3.1 - Edit Domain Menu
------------------------------------------------------------------------------
- The first option allows you to query a case in your chosen legal domain.

- The second option allows you to edit a case in your chosen legal domain.

- The third option allows you to visualise your chosen legal domain.

3.2 - Query Domain
------------------------------------------------------------------------------
- On this screen you can query a predefined case from the drop down menu or
query a new case by inputting a case name. Ensure the case name has no spaces
between words.

3.2.1 - Question Answering
------------------------------------------------------------------------------
- For 'Yes' or 'No' questions, answering them is mandatory. Select your answer
and then press NEXT for the next question.

- For multiple choice questions answering them is optional. If none of the answers
fit your case then leave them blank and press NEXT.

3.3 - Outcome
------------------------------------------------------------------------------
- The outcome displays the result and reasoning which led to a decision being
made.

- NEXT CASE - will allow you to query another case in the same domain.

- REPORT - will give you a more detailed report of the outcome of the case. As
detailed in 3.3.1

3.3.1 - Report
------------------------------------------------------------------------------
- This screen states how many nodes are in the domain, how many have been
accepted and a factor list with all the nodes which have been accepted.

- If you input a filename and press visualise this will create and open a png
file which shows a tree graph of the domain with the accepted nodes highlighted
green and the rejected nodes highlighted red. This shows the pathway the decision
making tool used to reach its outcome.

3.4 - Edit Domain
------------------------------------------------------------------------------
- On this screen you can select a non-leaf node which you can delete by pressing
DELETE or you can edit by pressing SEARCH.

- If you wish to edit a leaf node, you can only edit the question associated with it.
If you wish to delete a leaf node you must do this by changing any parent node's 
acceptance conditions which make reference to this node to no longer reference the node.

- For information on CHANGE QUESTION ORDER, refer to 2.3.1

- For information on CREATE NODE, refer to 2.1 or 2.2

3.4.1 - Edit non-leaf node
------------------------------------------------------------------------------
- The same rules from 2.1 or 2.2 apply for changing the name, statements, questions
and acceptance conditions.

- For a multi-node they will appear in both non-leaf and leaf lists. In the leaf list
you will be able to edit the question and in the non-leaf list you will be able to 
edit the acceptance conditions and statements.

- Pressing ADD ACCEPTANCE will add a new acceptance condition and a statement
to the screen.

- Press SUBMIT when you have made the required changes and then press DONE. Failure
to press SUBMIT will result in the changes not being saved.

3.4.2 - Save
------------------------------------------------------------------------------
- The filename must have no spaces. Once entered pressing SAVE will create
a '.xlsx' file with the data contained. When 'Done' shows this process has been
completed. To query or edit the newly created domain, refer to 3.0.

3.5 - Visualise Domain
------------------------------------------------------------------------------
- This will open a tree graph visualisation of the domain and save this image
as a png with the domain name as the filename.


