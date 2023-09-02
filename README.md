2
# EcommerceProject-Django

EcommerceProject-Django
This repository contains the backend code for an e-commerce platform built using Django and Django Rest Framework (DRF).

Features
  1.User Authentication: Register, login, and manage user accounts.
  2.Profile Management:
  3.Address Management: Users can add multiple addresses.
  4.Phone Number Management: Each user profile contains a phone number.
  5.Revenue Tracking: Track and update revenue for individual users.

Setup & Installation
1Clone the repository
git clone https://github.com/ciscoprogrammer/EcommerceProject-Django.git
cd EcommerceProject-Django

2.Set up a virtual environment 
python -m venv myenv
source myenv/bin/activate  # Windows `myenv\Scripts\activate`

3.nstall required packages
pip install -r requirements.txt

4.Run migrations
python manage.py migrate

5.Run the development server
python manage.py runserver

API Endpoints
  User Management:
  POST /api/users/: Register a new user.
  GET /api/users/: Retrieve the list of users.
  GET /api/users/<user_id>/: Retrieve details of a specific user.
  PUT /api/users/<user_id>/: Update details of a specific user.
  DELETE /api/users/<user_id>/: Delete a specific user.
  
  Profile Management:
  GET /api/users/profiles/: Retrieve the list of user profiles.
  GET /api/users/profiles/<profile_id>/: Retrieve a specific user profile.
  POST /api/users/profiles/: Create a new user profile.
  PUT /api/users/profiles/<profile_id>/: Update a specific user profile.
  DELETE /api/users/profiles/<profile_id>/: Delete a specific user profile.
  
  Address Management:
  GET /api/users/addresses/: Retrieve the list of addresses.
  GET /api/users/addresses/<address_id>/: Retrieve a specific address.
  POST /api/users/addresses/: Add a new address for a user.
  PUT /api/users/addresses/<address_id>/: Update a specific address.
  DELETE /api/users/addresses/<address_id>/: Delete a specific address.

  
  Revenue:
  POST /api/users/<user_id>/update_revenue/: Update the revenue for a specific user.

Usage
When making requests to create a new user, address, or profile, ensure you provide the necessary JSON data in the request body. 
For detailed information about the required data for each endpoint, refer to the API documentation.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


License
This project is licensed under the MIT License.





