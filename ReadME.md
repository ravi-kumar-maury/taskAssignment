
### API Endpoints

#### 1. Create a User
**Endpoint:** `POST /user/create/`

**Description:** Allows the creation of a new user with a name, email, and mobile number.

**Request:**

curl --location 'http://localhost:8000/api/user/create/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name" : "rk",
    "email": "r@gmail.com",
    "mobile": "9956217474"
}'

#### 2. Create a Task
Endpoint: `POST /tasks/create/`

##### Description: Allows the creation of a new task with a name, description, task type, and an optional list of users.

**Request:**

curl --location 'http://localhost:8000/api/tasks/create/' \
--header 'Content-Type: application/json' \
--data '{
  "name": "coding1",
  "description": "complete it",
  "task_type":"coding1",
  "users": []
}'

#### 3. Assign a Task to Users

Endpoint: `POST /tasks/assign/<task_id>/`

Description: Assigns a task to one or multiple users.

**Request:**

curl --location 'http://localhost:8000/api/tasks/assign/2/' \
--header 'Content-Type: application/json' \
--data '{
    "user_ids" : [1, 2]
}'

#### 4. Get Tasks for a Specific User

Endpoint: GET /users/<user_id>/tasks/

Description: Fetches all tasks assigned to a particular user.

**Request:**


curl --location 'http://localhost:8000/api/users/2/tasks/'

### Summary:
Create User: POST /user/create/
Create Task: POST /tasks/create/
Assign Task: PUT /tasks/assign/<task_id>/
Get User Tasks: GET /users/<user_id>/tasks/