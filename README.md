# StudyBuddyProject API

Welcome to the StudyBuddyProject API. This API allows users to manage study groups, sessions, messages, and memberships. Below is a description of the available routes and their respective functionalities.

## Authentication

This API uses basic authentication.

## API Endpoints

### Authentication

- **Login**  
  `POST /login/`  
  Authenticate and login a user.

- **Logout**  
  `POST /logout/`  
  Logout a user.

### Membership

- **List Memberships**  
  `GET /membership/`  
  Retrieve a list of all memberships.

- **Create Membership**  
  `POST /membership/`  
  Create a new membership.

- **Update Membership**  
  `PUT /membership/`  
  Update an existing membership.

- **Delete Membership**  
  `DELETE /membership/`  
  Delete a membership.

- **Retrieve Membership by ID**  
  `GET /membership/{id}/`  
  Retrieve a specific membership by its ID.

### Messages

- **List Messages**  
  `GET /message/`  
  Retrieve a list of all messages.

- **Create Message**  
  `POST /message/`  
  Create a new message.

- **Update Message**  
  `PUT /message/`  
  Update an existing message.

- **Delete Message**  
  `DELETE /message/`  
  Delete a message.

- **Retrieve Message by ID**  
  `GET /message/{id}/`  
  Retrieve a specific message by its ID.

- **List Messages by Study Group**  
  `GET /messageST/`  
  Retrieve a list of messages filtered by study group.

### Registration

- **Register User**  
  `POST /registration/`  
  Register a new user.

### Session

- **List Sessions**  
  `GET /session/`  
  Retrieve a list of all sessions.

- **Create Session**  
  `POST /session/`  
  Create a new session.

- **Update Session**  
  `PUT /session/`  
  Update an existing session.

- **Delete Session**  
  `DELETE /session/`  
  Delete a session.

- **Retrieve Session by ID**  
  `GET /session/{id}/`  
  Retrieve a specific session by its ID.

- **List Sessions by Study Group**  
  `GET /studysessionST/`  
  Retrieve a list of sessions filtered by study group.

### Study Group

- **List Study Groups**  
  `GET /studygroup/`  
  Retrieve a list of all study groups.

- **Create Study Group**  
  `POST /studygroup/`  
  Create a new study group.

- **Update Study Group**  
  `PUT /studygroup/`  
  Update an existing study group.

- **Delete Study Group**  
  `DELETE /studygroup/`  
  Delete a study group.

- **Retrieve Study Group by ID**  
  `GET /studygroup/{id}/`  
  Retrieve a specific study group by its ID.

### Subject

- **List Subjects**  
  `GET /subject/`  
  Retrieve a list of all subjects.

- **Create Subject**  
  `POST /subject/`  
  Create a new subject.

- **Update Subject**  
  `PUT /subject/`  
  Update an existing subject.

- **Delete Subject**  
  `DELETE /subject/`  
  Delete a subject.

- **Retrieve Subject by ID**  
  `GET /subject/{id}/`  
  Retrieve a specific subject by its ID.

## License

This project is licensed under the BSD License.

## Contact

For any questions or issues, feel free to reach out to us at [contact@yourapi.local](mailto:contact@yourapi.local).

