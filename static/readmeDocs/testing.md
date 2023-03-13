## Manual Testing

1. All links were manually tested to check that they are being rendered as Intended.

- Root Route welcome message is being shown correctly

- Users can login and log out from the app correctly


**Reviews Page:**

- reviews list is being rendered correctly

- review/id , to get a single review is being shown correctly

- if no review with that specific id is found a "Not found." message is being shown

Logged In users:

- review create fuctionality is working as intended

- if mandatory fields are left blank, errors are being shown correctly

- if user is owner by retrieving a revew by ID they can edit or delete it correctly

- if user is not the owner of a specific review, the form to edit/ delete is not being shown, as intended

Logged out users 

- can view review list correcty

- can retrieve a review by ID but can not see the form to post, edit or delete, as intended

**Comments**

Logged In users:

- can see comments list

- can retrieve a comment by id

- can place a comment to a review, edit it or delete it if they are the owner

Loggedout users:

- can see comments correctly 

- can retrieve a comment by review ID but can not edit or delete it

**Likes**

Logged In users:

- can see likes list

- can like/ unlike a review correctly


Loggedout users:

- can see likes list correctly 

- can retrieve a like by review ID but can not like, or unlike a review

**Saved Review**

Logged In users:

- can only see their own saved list, as intended

- delete a review from the saved list correctly

Log out users:

- do not have access to saved list 


**Contact Page**


Logged In users:

- only the owner can see the list of all the time they filled in the contact form 

- errors in case of incorrect or blank field are shown correctly

Logged out users:

- do not have access to contact page, as intended

**Profiles**

- profile list is being shown correctly

- profile search by ID retrieves the related profile as intended

- user can only modify their own profile info


Logged out users:

- can see profile list 

- can not perform edit functionality

Filters are retrieveing the data as intended. For now the search field will only allow a serarch by a product name/title.


Admin is able to view and perform all the necessary action by viewing, editing and deleting reviews, profiles.