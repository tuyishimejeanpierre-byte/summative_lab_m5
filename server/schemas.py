from marshmallow import Schema, fields, validate


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=100)
    )

    category = fields.Str(
        required=True,
        validate=validate.Length(min=2, max=50)
    )

    equipment_needed = fields.Bool(required=True)


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    notes = fields.Str(allow_none=True)


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    reps = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    sets = fields.Int(
        required=True,
        validate=validate.Range(min=1)
    )

    duration_seconds = fields.Int(
        allow_none=True,
        validate=validate.Range(min=1)
    )


class WorkoutExerciseDetailSchema(Schema):
    id = fields.Int(dump_only=True)

    exercise_id = fields.Int()
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int(allow_none=True)

    exercise = fields.Nested(
        ExerciseSchema,
        dump_only=True
    )


class WorkoutDetailSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date()
    duration_minutes = fields.Int()
    notes = fields.Str(allow_none=True)

    workout_exercises = fields.Nested(
        WorkoutExerciseDetailSchema,
        many=True,
        dump_only=True
    )
    class ExerciseDetailSchema(Schema):

        id = fields.Int(dump_only=True)
        name = fields.Str()
        category = fields.Str()
        equipment_needed = fields.Bool()

        workouts = fields.Nested(

            WorkoutSchema,
            many=True,
            dump_only=True
    )
class ExerciseDetailSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str()
    category = fields.Str()
    equipment_needed = fields.Bool()

    workouts = fields.Nested(
        WorkoutSchema,
        many=True,
        dump_only=True
    ) 