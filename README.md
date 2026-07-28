# Flask SQLAlchemy Workout API

## Description

This project is a Flask REST API for managing workouts and exercises. The API uses Flask-SQLAlchemy for database management, Flask-Migrate for database migrations, and Marshmallow for serialization, deserialization, and schema validation.

The application allows users to:

* View all workouts
* View a single workout and its associated exercises
* Create workouts
* Delete workouts
* View all exercises
* View a single exercise and its associated workouts
* Create exercises
* Delete exercises
* Add exercises to workouts with reps, sets, and duration information

## Technologies

* Python 3.8
* Flask 2.2.2
* Flask-SQLAlchemy 3.0.3
* Flask-Migrate 3.1.0
* Marshmallow 3.20.1
* SQLite
* Pipenv

## Installation

Clone the repository and move into the project directory:

```bash
git clone <your-github-repository-url>
cd summative_lab_m5
```

Install the project dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

## Database Setup

Move into the server directory:

```bash
cd server
```

Initialize the database migration system if necessary:

```bash
pipenv run flask --app app:app db init
```

Create a migration:

```bash
pipenv run flask --app app:app db migrate -m "create workout database tables"
```

Apply the migration:

```bash
pipenv run flask --app app:app db upgrade
```

## Seed the Database

To create starter data for exercises, workouts, and workout exercises, run:

```bash
pipenv run python seed.py
```

The seed script clears existing data and creates new sample records.

## Running the Application

From the `server` directory, run:

```bash
pipenv run python app.py
```

The API will run at:

```text
http://127.0.0.1:5555
```

## API Endpoints

### Workouts

#### GET `/workouts`

Returns all workouts.

#### GET `/workouts/<id>`

Returns one workout and its associated exercises.

#### POST `/workouts`

Creates a new workout.

Example request:

```json
{
  "date": "2026-07-28",
  "duration_minutes": 45,
  "notes": "Upper body workout"
}
```

#### DELETE `/workouts/<id>`

Deletes a workout and its associated workout-exercise records.

### Exercises

#### GET `/exercises`

Returns all exercises.

#### GET `/exercises/<id>`

Returns one exercise and its associated workouts.

#### POST `/exercises`

Creates a new exercise.

Example request:

```json
{
  "name": "Deadlift",
  "category": "Strength",
  "equipment_needed": true
}
```

#### DELETE `/exercises/<id>`

Deletes an exercise and its associated workout-exercise records.

### Workout Exercises

#### POST `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises`

Adds an exercise to a workout.

Example request:

```json
{
  "reps": 10,
  "sets": 3,
  "duration_seconds": 30
}
```

## Validations and Constraints

The application includes validation at multiple levels.

### Table Constraints

Examples include:

* Required fields use `nullable=False`
* Exercise names are unique
* Workout and exercise foreign keys cannot be null
* Reps and sets cannot be null

### Model Validations

The models validate:

* Exercise names cannot be blank
* Workout duration must be greater than zero
* Reps must be greater than zero
* Sets must be greater than zero
* Exercise duration must be greater than zero when provided

### Schema Validations

Marshmallow validates:

* Exercise name length
* Exercise category length
* Workout duration
* Reps
* Sets
* Duration in seconds

Invalid data is rejected before it is saved to the database.

## Relationships

The application uses the following relationships:

* A Workout has many WorkoutExercises
* An Exercise has many WorkoutExercises
* A WorkoutExercise belongs to a Workout
* A WorkoutExercise belongs to an Exercise
* A Workout has many Exercises through WorkoutExercises
* An Exercise has many Workouts through WorkoutExercises

## Project Structure

```text
summative_lab_m5/
├── README.md
├── Pipfile
├── Pipfile.lock
├── .gitignore
└── server/
    ├── app.py
    ├── models.py
    ├── schemas.py
    ├── seed.py
    └── migrations/
```

## Author

Created as a Flask SQLAlchemy backend summative project.
