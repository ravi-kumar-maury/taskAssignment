
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

**Response:**
{
    "id": 3,
    "name": "rk",
    "email": "r@gmail.com",
    "mobile": "9956217474"
}


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

**Response:**
{
    "id": 3,
    "name": "coding1",
    "description": "complete it",
    "created_at": "2024-10-22T05:30:06.003383Z",
    "task_type": "coding1",
    "completed_at": null,
    "status": "pending",
    "users": []
}


#### 3. Assign a Task to Users

Endpoint: `POST /tasks/assign/<task_id>/`

Description: Assigns a task to one or multiple users.

**Request:**

curl --location 'http://localhost:8000/api/tasks/assign/2/' \
--header 'Content-Type: application/json' \
--data '{
    "user_ids" : [1, 2]
}'

**Response:**
{
    "id": 2,
    "name": "coding1",
    "description": "complete it",
    "created_at": "2024-10-22T05:30:06.003383Z",
    "task_type": "coding1",
    "completed_at": null,
    "status": "pending",
    "users": [
        1,
        2
    ]
}


#### 4. Get Tasks for a Specific User

Endpoint: GET /users/<user_id>/tasks/

Description: Fetches all tasks assigned to a particular user.

**Request:**


curl --location 'http://localhost:8000/api/users/2/tasks/'

**Response:**

[
    {
        "id": 2,
        "name": "coding1",
        "description": "complete it",
        "created_at": "2024-10-21T18:11:52.690189Z",
        "task_type": "coding1",
        "completed_at": null,
        "status": "pending",
        "users": [
            1,
            2
        ]
    },
    {
        "id": 3,
        "name": "coding1",
        "description": "complete it",
        "created_at": "2024-10-22T05:30:06.003383Z",
        "task_type": "coding1",
        "completed_at": null,
        "status": "pending",
        "users": [
            1,
        ]
    }
]


### Summary:
Create User: POST /user/create/

Create Task: POST /tasks/create/

Assign Task: PUT /tasks/assign/<task_id>/

Get User Tasks: GET /users/<user_id>/tasks/


#### Instructions on Setting Up and Running the Project

1. **Clone the Repository:**
  ```
  git clone https://github.com/ravi-kumar-maury/taskAssignmentBackend.git
  cd taskAssignmentBackend
  ```

2. **Create a Virtual Environment:**
  ```
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

3. **Install Dependencies:**
  ```
  pip install -r requirements.txt
  ```

4. **Run Migrations:**
  ```
  python manage.py migrate
  ```

5. **Start the Development Server:**
  ```
  python manage.py runserver
  ```

6. **Access the API:**
  Use postman and run curl of api endpoints from point 1 to 4 in API ENDPOINTS section.

7. **Run Tests:**
  ```
  python manage.py test
  ```