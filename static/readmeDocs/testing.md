## Manual Testing

1. All links were manually tested to check that teyr are being rendered as Intended.

- Root Route welcome message is being shown correctly
- Users can login and log out from the app correctly


**Reviews Page:**

- reviews list is being rendered correctly
- review:id , to get a single review is being shown correctly
- if no review with that specific id is found a "Not found." message is being shown

Logged In users:

- review create fuctionality is working as intended

- if mandatory fields are left blank, errors are being shown correctly

- if user is owner by retrieving a revew by ID they can edit or delete it correctly

- if user is not the owner of a specifi review, the form to edit/ delete is not being shown, as intended

Logged out users 

- can view review list correcty
- can retrieve a review by ID but can not see the form to post, edit or delete 

**Comments**

Logged In users:
- can see comments list
- can retrieve a comment by id
- can place a comment, edit it or delete it

Log out users:
- can see comments correctly 
- can retrieve a comment by review ID but not place edit or delete it

**Likes**

Logged In users:
 can see likes list
- can like/ unlike a review correctly


Log out users:
- can see likes list correctly 
- can retrieve a like by review ID but can like, or unlike a review

**Saved Review**

Logged In users:
- can see saved reviews list only if their owns
- delete a review from the saved list correctly
Log out users:
- do not have access to saved list 


**Contact Page**


Logged In users:

- only the owner can see the list of all the time they filled in the contact form 
- errors in case or incorrect on blank fields are shown correctly
Logged out users:
- do not have access to contact page, as intended

** Profiles**

- profile list is being shown correctly
- profile search by ID retrieves the related profile as intended
- user can only modify their own profile data


Logged out users:
- can see profile list 
- can not permorm crud functionality

Search filters are retrieveing the data as intended. For now the search field will only allow a serarch by a product name/title.


Admin is able to view and perform all the necessary action by viewing, editing and deleting reviews, profiles.