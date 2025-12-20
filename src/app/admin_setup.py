from fastapi import FastAPI
from sqladmin import Admin, ModelView
from .db import engine
import src.app.models as all_models


def create_model_view(model):
    class DynamicModelView(ModelView, model=model):
        pass

    return DynamicModelView


def init_admin(app: FastAPI):
    admin = Admin(app, engine)

    models = [
        all_models.Biometric,
        all_models.ExerciseMuscleTarget,
        all_models.Exercise,
        all_models.MusclePartSplitDay,
        all_models.MusclePart,
        all_models.Muscle,
        all_models.MuscleMusclePart,
        all_models.PlanExercise,
        all_models.Plan,
        all_models.SplitDay,
        all_models.Split,
        all_models.User,
        all_models.WorkoutLog,
    ]

    for model in models:
        view_class = create_model_view(model)
        admin.add_view(view_class)

    return admin
