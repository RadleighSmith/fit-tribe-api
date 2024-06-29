# Testing And Validation

## Contents

[Code Validation](#code-validation)

[Manual Testing](#manual-testing)

[Error Handling Tests](#error-handling-tests)

[Permissions Tests](#permissions-tests)

---



## Code Validation

### PEP8 Code Validation

PEP8 is the style guide for Python code, aiming to improve the readability and consistency of Python code. To ensure adherence to PEP8 standards, I used Code Institute's PEP8 Python Linter. This tool analyzes the code and highlights deviations from the PEP8 guidelines, such as line length, indentation, and spacing issues. Running the linter helps maintain clean, readable, and professional code. By integrating this into the development process, I ensured that all Python files in the project comply with industry-standard coding practices, enhancing overall code quality and maintainability.


**ft_api Folder**

| Filename         | PEP8 Validation Status  | Notes                      |
|------------------|---------|--------------------------------------------|
| agsi.py          | Pass    |                                            |
| permissions.py   | Pass    |                                            |
| serializers.py   | Pass    |                                            |
| settings.py      | Fail    | Please see note bellow                     |
| urls.py          | Pass    |                                            |
| views.py         | Pass    |                                            |
| wsgi.py          | Pass    |                                            |



The settings.py file contains essential configuration settings, and while most of the code complies with PEP8 guidelines, a few lines exceed the 79-character limit due to the detailed configuration of password validators. These lines were not modified to ensure the clarity and readability of the settings, despite causing PEP8 warnings for line length.

![PEP8 settings screenshot](docs/readme_images/pep8_settings_screenshot.png)

---
**blogs Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**blog_likes Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**blog_comments Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**workouts Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**workout_likes Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**workout_comments Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**profiles Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**followers Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**feed Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**groups Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |

---
**group_events Folder**

| Filename       | PEP8 Validation Status |
|----------------|------------------------|
| admin.py       | Pass                   |
| apps.py        | Pass                   |
| models.py      | Pass                   |
| serializers.py | Pass                   |
| tests.py       | Pass                   |
| urls.py        | Pass                   |
| views.py       | Pass                   |


## Manual Testing

### Authentication Endpoints

| URL                              | HTTP Request | Expected Outcome              | Result |
|----------------------------------|--------------|-------------------------------|--------|
| /api-auth/                       | GET          | DRF auth endpoints accessible | PASS   |
| /dj-rest-auth/logout/            | POST         | User logged out successfully  | PASS   |
| /dj-rest-auth/                   | GET          | Auth endpoints accessible     | PASS   |
| /dj-rest-auth/registration/      | POST         | New user created              | PASS   |

### Profile Endpoints

---

#### Profile List

| URL                  | HTTP Request | Expected Outcome                             | Result |
|----------------------|--------------|----------------------------------------------|--------|
| /profiles/           | GET          | List of all profiles with annotations        | PASS   |

#### Profile Detail

| URL                  | HTTP Request | Expected Outcome                                         | Result |
|----------------------|--------------|----------------------------------------------------------|--------|
| /profiles/{id}/      | GET          | Retrieve details of a specific profile                   | PASS   |
| /profiles/{id}/      | PUT          | Update the details of a specific profile (owner only)    | PASS   |
| /profiles/{id}/      | DELETE       | Delete the profile and associated user (owner only)      | PASS   |

#### Profile Creation (via User Creation)

| URL                              | HTTP Request | Expected Outcome                    | Result |
|----------------------------------|--------------|-------------------------------------|--------|
| /dj-rest-auth/registration/      | POST         | New user created, profile auto-generated | PASS   |

#### Joining and Leaving Groups (Profile-related)

| URL                              | HTTP Request | Expected Outcome                    | Result |
|----------------------------------|--------------|-------------------------------------|--------|
| /groups/{id}/join/               | POST         | User joined the group, profile updated | PASS   |
| /groups/{id}/leave/              | POST         | User left the group, profile updated | PASS   |

---

### Follower Endpoints

#### Follower List

| URL             | HTTP Request | Expected Outcome                                     | Result |
|-----------------|--------------|------------------------------------------------------|--------|
| /followers/     | GET          | List of all follower relationships                   | PASS   |
| /followers/     | POST         | New follower relationship created (user follows another user) | PASS   |

#### Follower Detail

| URL                    | HTTP Request | Expected Outcome                                     | Result |
|------------------------|--------------|------------------------------------------------------|--------|
| /followers/{id}/       | GET          | Retrieve details of a specific follower relationship | PASS   |
| /followers/{id}/       | DELETE       | Delete a specific follower relationship (unfollow)   | PASS   |


---

### Feed Endpoints

| URL                              | HTTP Request | Expected Outcome                                  | Result |
|----------------------------------|--------------|---------------------------------------------------|--------|
| /feed/                           | GET          | List of blog posts from followed users retrieved  | PASS   |

---

### Other Endpoints

| URL                              | HTTP Request | Expected Outcome              | Result |
|----------------------------------|--------------|-------------------------------|--------|
| /                                | GET          | Root route accessible         | PASS   |
| /admin/                          | GET          | Admin site accessible         | PASS   |

---

### Blog Endpoints

#### Blog List

| URL       | HTTP Request | Expected Outcome                    | Result |
|-----------|--------------|-------------------------------------|--------|
| /blogs/   | GET          | List of all blogs with annotations  | PASS   |
| /blogs/   | POST         | New blog created                    | PASS   |

#### Blog Detail

| URL              | HTTP Request | Expected Outcome                           | Result |
|------------------|--------------|--------------------------------------------|--------|
| /blogs/{id}/     | GET          | Retrieve details of a specific blog        | PASS   |
| /blogs/{id}/     | PUT          | Update the details of a specific blog      | PASS   |
| /blogs/{id}/     | DELETE       | Delete a specific blog                     | PASS   |


---

### Blog Like Endpoints

#### Blog Like List

| URL             | HTTP Request | Expected Outcome                              | Result |
|-----------------|--------------|-----------------------------------------------|--------|
| /blog-likes/    | GET          | List of all blog likes                        | PASS   |
| /blog-likes/    | POST         | New blog like created for the authenticated user | PASS   |

### Blog Like Detail

| URL                    | HTTP Request | Expected Outcome                           | Result |
|------------------------|--------------|--------------------------------------------|--------|
| /blog-likes/{id}/      | GET          | Retrieve details of a specific blog like   | PASS   |
| /blog-likes/{id}/      | DELETE       | Delete a specific blog like                | PASS   |

---

### Blog Comment Endpoints

#### Blog Comment List

| URL                   | HTTP Request | Expected Outcome                                      | Result |
|-----------------------|--------------|-------------------------------------------------------|--------|
| /blog-comments/       | GET          | List of all blog comments or comments for a specific blog | PASS   |
| /blog-comments/       | POST         | New blog comment created for a specific blog          | PASS   |

#### Blog Comment Detail

| URL                         | HTTP Request | Expected Outcome                              | Result |
|-----------------------------|--------------|-----------------------------------------------|--------|
| /blog-comments/{id}/        | GET          | Retrieve details of a specific blog comment   | PASS   |
| /blog-comments/{id}/        | PUT          | Update the details of a specific blog comment | PASS   |
| /blog-comments/{id}/        | DELETE       | Delete a specific blog comment                | PASS   |

---

### Workout Endpoints

#### Workout List

| URL                | HTTP Request | Expected Outcome                         | Result |
|--------------------|--------------|------------------------------------------|--------|
| /workouts/         | GET          | List of all workouts with annotations    | PASS   |
| /workouts/         | POST         | New workout created                      | PASS   |

#### Workout Detail

| URL                    | HTTP Request | Expected Outcome                         | Result |
|------------------------|--------------|------------------------------------------|--------|
| /workouts/{id}/        | GET          | Retrieve details of a specific workout   | PASS   |
| /workouts/{id}/        | PUT          | Update the details of a specific workout | PASS   |
| /workouts/{id}/        | DELETE       | Delete a specific workout                | PASS   |

---

### Workout Like Endpoints

#### Workout Like List

| URL                  | HTTP Request | Expected Outcome                                      | Result |
|----------------------|--------------|-------------------------------------------------------|--------|
| /workout-likes/      | GET          | List of all workout likes                             | PASS   |
| /workout-likes/      | POST         | New workout like created for the authenticated user   | PASS   |

#### Workout Like Detail

| URL                         | HTTP Request | Expected Outcome                                      | Result |
|-----------------------------|--------------|-------------------------------------------------------|--------|
| /workout-likes/{id}/        | GET          | Retrieve details of a specific workout like           | PASS   |
| /workout-likes/{id}/        | PUT          | Update the details of a specific workout like         | PASS   |
| /workout-likes/{id}/        | DELETE       | Delete a specific workout like                        | PASS   |

---

### Workout Comment Endpoints

#### Workout Comment List

| URL                     | HTTP Request | Expected Outcome                                      | Result |
|-------------------------|--------------|-------------------------------------------------------|--------|
| /workout-comments/      | GET          | List of all workout comments                          | PASS   |
| /workout-comments/      | POST         | New workout comment created for the authenticated user | PASS   |

#### Workout Comment Detail

| URL                                | HTTP Request | Expected Outcome                                      | Result |
|------------------------------------|--------------|-------------------------------------------------------|--------|
| /workout-comments/{id}/            | GET          | Retrieve details of a specific workout comment        | PASS   |
| /workout-comments/{id}/            | PUT          | Update the details of a specific workout comment      | PASS   |
| /workout-comments/{id}/            | DELETE       | Delete a specific workout comment                     | PASS   |


---

### Group Endpoints

#### Group List

| URL           | HTTP Request | Expected Outcome                     | Result |
|---------------|--------------|--------------------------------------|--------|
| /groups/      | GET          | List of all groups                   | PASS   |
| /groups/      | POST         | New group created (admin only)       | PASS   |

#### Group Detail

| URL                  | HTTP Request | Expected Outcome                            | Result |
|----------------------|--------------|---------------------------------------------|--------|
| /groups/{id}/        | GET          | Retrieve details of a specific group        | PASS   |
| /groups/{id}/        | PUT          | Update the details of a specific group (admin only) | PASS   |
| /groups/{id}/        | DELETE       | Delete a specific group (admin only)        | PASS   |

#### Join and Leave Group

| URL                       | HTTP Request | Expected Outcome                             | Result |
|---------------------------|--------------|----------------------------------------------|--------|
| /groups/{id}/join/        | POST         | User joins the group                         | PASS   |
| /groups/{id}/leave/       | POST         | User leaves the group                        | PASS   |

#### Membership List

| URL               | HTTP Request | Expected Outcome                               | Result |
|-------------------|--------------|------------------------------------------------|--------|
| /memberships/     | GET          | List of memberships for the current user       | PASS   |

---

### Group Event Endpoints

#### Group Event List

| URL               | HTTP Request | Expected Outcome                                       | Result |
|-------------------|--------------|--------------------------------------------------------|--------|
| /group-events/    | GET          | List of all group events or events for a specific group| PASS   |
| /group-events/    | POST         | New group event created (admin only)                   | PASS   |

#### Group Event Detail

| URL                    | HTTP Request | Expected Outcome                            | Result |
|------------------------|--------------|---------------------------------------------|--------|
| /group-events/{id}/    | GET          | Retrieve details of a specific group event  | PASS   |
| /group-events/{id}/    | PUT          | Update the details of a specific group event (admin only) | PASS   |
| /group-events/{id}/    | DELETE       | Delete a specific group event (admin only)  | PASS   |

#### Join and Leave Event

| URL                          | HTTP Request | Expected Outcome                                | Result |
|------------------------------|--------------|-------------------------------------------------|--------|
| /group-events/{id}/join/     | POST         | User joins the group event                      | PASS   |
| /group-events/{id}/leave/    | POST         | User leaves the group event                     | PASS   |

---

### Error Handling Tests

#### Authentication Endpoints

| URL                              | HTTP Request | Error Scenario                  | Expected Outcome                      | Result |
|----------------------------------|--------------|---------------------------------|---------------------------------------|--------|
| /dj-rest-auth/registration/      | POST         | Missing required fields         | 400 Bad Request, error details        | PASS   |
| /dj-rest-auth/registration/      | POST         | Invalid email format            | 400 Bad Request, error message        | PASS   |
| /dj-rest-auth/login/             | POST         | Incorrect password              | 401 Unauthorized, error message       | PASS   |
| /dj-rest-auth/logout/            | POST         | Invalid session token           | 403 Forbidden, error message          | PASS   |

#### Profile Endpoints

| URL                  | HTTP Request | Error Scenario                     | Expected Outcome                      | Result |
|----------------------|--------------|------------------------------------|---------------------------------------|--------|
| /profiles/{id}/      | GET          | Profile does not exist             | 404 Not Found, error message          | PASS   |
| /profiles/{id}/      | PUT          | Unauthorized update attempt        | 403 Forbidden, error message          | PASS   |
| /profiles/{id}/      | DELETE       | Unauthorized delete attempt        | 403 Forbidden, error message          | PASS   |

#### Follower Endpoints

| URL                    | HTTP Request | Error Scenario                        | Expected Outcome                              | Result |
|------------------------|--------------|---------------------------------------|-----------------------------------------------|--------|
| /followers/            | POST         | Duplicate follower relationship       | 400 Bad Request, "This follow relationship already exists." | PASS   |
| /followers/            | POST         | User tries to follow themselves       | 400 Bad Request, "You cannot follow yourself."| PASS   |

#### Feed Endpoints

| URL             | HTTP Request | Error Scenario                        | Expected Outcome                              | Result |
|-----------------|--------------|---------------------------------------|-----------------------------------------------|--------|
| /feed/          | GET          | Unauthorized access                   | 403 Forbidden, error message                  | PASS   |

#### Blog Endpoints

| URL              | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|------------------|--------------|------------------------------------|--------------------------------------------|--------|
| /blogs/{id}/     | GET          | Blog does not exist                | 404 Not Found, error message               | PASS   |
| /blogs/{id}/     | PUT          | Unauthorized update attempt        | 403 Forbidden, error message               | PASS   |
| /blogs/{id}/     | DELETE       | Unauthorized delete attempt        | 403 Forbidden, error message               | PASS   |

#### Blog Like Endpoints

| URL             | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|-----------------|--------------|------------------------------------|--------------------------------------------|--------|
| /blog-likes/    | POST         | Duplicate like relationship        | 400 Bad Request, "This like already exists." | PASS   |

#### Blog Comment Endpoints

| URL                  | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|----------------------|--------------|------------------------------------|--------------------------------------------|--------|
| /blog-comments/      | POST         | Missing required fields            | 400 Bad Request, error details             | PASS   |

#### Workout Endpoints

| URL                  | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|----------------------|--------------|------------------------------------|--------------------------------------------|--------|
| /workouts/{id}/      | GET          | Workout does not exist             | 404 Not Found, error message               | PASS   |
| /workouts/{id}/      | PUT          | Unauthorized update attempt        | 403 Forbidden, error message               | PASS   |
| /workouts/{id}/      | DELETE       | Unauthorized delete attempt        | 403 Forbidden, error message               | PASS   |

#### Workout Like Endpoints

| URL                  | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|----------------------|--------------|------------------------------------|--------------------------------------------|--------|
| /workout-likes/      | POST         | Duplicate like relationship        | 400 Bad Request, "This like already exists." | PASS   |

#### Workout Comment Endpoints

| URL                          | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|------------------------------|--------------|------------------------------------|--------------------------------------------|--------|
| /workout-comments/           | POST         | Missing required fields            | 400 Bad Request, error details             | PASS   |

#### Group Endpoints

| URL                  | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|----------------------|--------------|------------------------------------|--------------------------------------------|--------|
| /groups/{id}/        | GET          | Group does not exist               | 404 Not Found, error message               | PASS   |
| /groups/{id}/        | PUT          | Unauthorized update attempt        | 403 Forbidden, error message               | PASS   |
| /groups/{id}/        | DELETE       | Unauthorized delete attempt        | 403 Forbidden, error message               | PASS   |

#### Group Event Endpoints

| URL                    | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|------------------------|--------------|------------------------------------|--------------------------------------------|--------|
| /group-events/{id}/    | GET          | Group event does not exist         | 404 Not Found, error message               | PASS   |
| /group-events/{id}/    | PUT          | Unauthorized update attempt        | 403 Forbidden, error message               | PASS   |
| /group-events/{id}/    | DELETE       | Unauthorized delete attempt        | 403 Forbidden, error message               | PASS   |

#### Event Membership Endpoints

| URL                        | HTTP Request | Error Scenario                     | Expected Outcome                           | Result |
|----------------------------|--------------|------------------------------------|--------------------------------------------|--------|
| /group-events/{id}/join/   | POST         | User already joined the event      | 400 Bad Request, "Already a member of this event." | PASS   |
| /group-events/{id}/leave/  | POST         | User not a member of the event     | 400 Bad Request, "Not a member of this event." | PASS   |

---

### Permissions Tests

#### Authentication Endpoints

| URL                              | HTTP Request | Permission Scenario              | Expected Outcome                      | Result |
|----------------------------------|--------------|----------------------------------|---------------------------------------|--------|
| /dj-rest-auth/logout/            | POST         | Logged out user                  | 403 Forbidden, error message          | PASS   |
| /dj-rest-auth/registration/      | POST         | Logged in user                   | 400 Bad Request, "User already registered." | PASS   |

#### Profile Endpoints

| URL                  | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|----------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /profiles/{id}/      | PUT          | Non-owner attempting to update profile  | 403 Forbidden, error message          | PASS   |
| /profiles/{id}/      | DELETE       | Non-owner attempting to delete profile  | 403 Forbidden, error message          | PASS   |

#### Follower Endpoints

| URL                    | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|------------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /followers/{id}/       | DELETE       | Non-owner attempting to delete follower relationship | 403 Forbidden, error message          | PASS   |

#### Feed Endpoints

| URL             | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|-----------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /feed/          | GET          | Unauthenticated user                    | 403 Forbidden, error message          | PASS   |

#### Blog Endpoints

| URL              | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /blogs/{id}/     | PUT          | Non-owner attempting to update blog     | 403 Forbidden, error message          | PASS   |
| /blogs/{id}/     | DELETE       | Non-owner attempting to delete blog     | 403 Forbidden, error message          | PASS   |

#### Blog Like Endpoints

| URL                    | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|------------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /blog-likes/{id}/      | DELETE       | Non-owner attempting to delete blog like | 403 Forbidden, error message          | PASS   |

#### Blog Comment Endpoints

| URL                         | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|-----------------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /blog-comments/{id}/        | PUT          | Non-owner attempting to update comment  | 403 Forbidden, error message          | PASS   |
| /blog-comments/{id}/        | DELETE       | Non-owner attempting to delete comment  | 403 Forbidden, error message          | PASS   |

#### Workout Endpoints

| URL                    | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|------------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /workouts/{id}/        | PUT          | Non-owner attempting to update workout  | 403 Forbidden, error message          | PASS   |
| /workouts/{id}/        | DELETE       | Non-owner attempting to delete workout  | 403 Forbidden, error message          | PASS   |

#### Workout Like Endpoints

| URL                         | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|-----------------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /workout-likes/{id}/        | DELETE       | Non-owner attempting to delete workout like | 403 Forbidden, error message          | PASS   |

#### Workout Comment Endpoints

| URL                                | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|------------------------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /workout-comments/{id}/            | PUT          | Non-owner attempting to update comment  | 403 Forbidden, error message          | PASS   |
| /workout-comments/{id}/            | DELETE       | Non-owner attempting to delete comment  | 403 Forbidden, error message          | PASS   |

#### Group Endpoints

| URL                  | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|----------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /groups/             | POST         | Non-admin attempting to create group    | 403 Forbidden, error message          | PASS   |
| /groups/{id}/        | PUT          | Non-admin attempting to update group    | 403 Forbidden, error message          | PASS   |
| /groups/{id}/        | DELETE       | Non-admin attempting to delete group    | 403 Forbidden, error message          | PASS   |

#### Group Event Endpoints

| URL                    | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|------------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /group-events/         | POST         | Non-admin attempting to create event    | 403 Forbidden, error message          | PASS   |
| /group-events/{id}/    | PUT          | Non-admin attempting to update event    | 403 Forbidden, error message          | PASS   |
| /group-events/{id}/    | DELETE       | Non-admin attempting to delete event    | 403 Forbidden, error message          | PASS   |

#### Event Membership Endpoints

| URL                          | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|------------------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /group-events/{id}/join/     | POST         | Unauthenticated user                    | 403 Forbidden, error message          | PASS   |
| /group-events/{id}/leave/    | POST         | Unauthenticated user                    | 403 Forbidden, error message          | PASS   |

#### Follower Endpoints

| URL                  | HTTP Request | Permission Scenario                     | Expected Outcome                      | Result |
|----------------------|--------------|-----------------------------------------|---------------------------------------|--------|
| /followers/          | POST         | Unauthenticated user                    | 403 Forbidden, error message          | PASS   |
| /followers/{id}/     | DELETE       | Non-owner attempting to delete follower relationship | 403 Forbidden, error message          | PASS   |


[Back to Contents](#contents)