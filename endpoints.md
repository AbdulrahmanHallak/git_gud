### Authentication & User Management

```
POST /api/v1/auth/signup
Request: {
  "username": "string",
  "email": "string",
  "password": "string"
}
Response: {
  "user": { "id": "string", "username": "string", "email": "string" },
  "accessToken": "string",
  "refreshToken": "string",
  "validUntil": "datetime utc"
}
```

```
POST /api/v1/auth/login
Request: {
  "email": "string",
  "password": "string"
}
Response: {
  "user": { "id": "string", "username": "string", "email": "string" },
  "accessToken": "string",
  "refreshToken": "string",
  "validUntil": "datetime utc"
}

```

```
POST /api/v1/auth/refresh
Request: {
  "refreshToken": "string"
}
Response: {
  "accessToken": "string",
  "refreshToken": "string",
  "validUntil": "datetime utc"
}

```

```
POST /api/v1/auth/logout
Request: {
  "refreshToken": "string"
}

```

```
PUT /api/v1/users/{id}
Request: {
  "id": "number"
  "height": "number",
  "weight": "number",
  "bodyFat": "number",
  "splitType": "string",
  "workoutType": "string",
  "daysPerWeek": "number"
}
Response: {
  "id": "number",
  "email": "string",
  "height": "number",
  "weight": "number",
  "bodyFat": "number",
  "splitType": "string",
  "workoutType": "string",
  "daysPerWeek": "number",
  "updatedAt": "datetime"
}

```


```
GET /api/v1/users/{userId}
Response: {
  "id": "number",
  "username": "string",
  "email": "string",
  "height": "number",
  "weight": "number",
  "bodyFat": "number",
  "splitType": "string",
  "workoutType": "string",
  "daysPerWeek": "number",
  "role": "string",
  "createdAt": "datetime"
}

```
---

### Workout Plan Generation

```
POST /api/v1/users/{userId}/plans
Request: {
  "splitType": "string",
  "workoutType": "string",
  "daysPerWeek": "number"
}
Response: {
  "id": "string",
  "userId": "string",
  "splitType": "string",
  "workoutType": "string",
  "daysPerWeek": "number",
  "startDate": "date",
  "endDate": "date",
  "status": "string",
  "createdAt": "datetime"
}
```

```
// user have many plans (completed and only one still active)
GET /api/v1/users/{userId}/plans
Query: ?status=string&page=number&limit=number
Response: {
  "plans": [
    {
      "id": "string",
      "splitType": "string",
      "workoutType": "string",
      "daysPerWeek": "number",
      "startDate": "date",
      "endDate": "date",
      "status": "string",
      "createdAt": "datetime"
    }
  ],
  "total": "number"
}
```

```
GET /api/v1/users/{userId}/plans/{planId}
Response: {
  "id": "string",
  "userId": "string",
  "splitType": "string",
  "workoutType": "string",
  "daysPerWeek": "number",
  "startDate": "date",
  "endDate": "date",
  "status": "string",
  "weeks": [
    {
      "weekNumber": "number",
      "days": [
        {
          "dayNumber": "number",
          "dayOfWeek": "string",
          "exercises": [
            {
              "id": "string",
              "exerciseId": "string",
              "name": "string",
              "sets": "number",
              "reps": "string",
              "restSeconds": "number",
              "order": "number"
            }
          ]
        }
      ]
    }
  ],
  "createdAt": "datetime"
}
```

```
GET /api/v1/users/{userId}/plans/current/week/{weekNumber}/day/{dayNumber}
Response: {
  "planId": "string",
  "weekNumber": "number",
  "dayNumber": "number",
  "dayOfWeek": "string",
  "exercises": [
    {
      "id": "string",
      "exerciseId": "string",
      "name": "string",
      "sets": "number",
      "reps": "string",
      "restSeconds": "number",
      "targetMuscle": "string",
      "equipment": "string",
      "videoUrl": "string",
      "order": "number"
    }
  ]
}
```
```
DELETE /api/v1/users/{userId}/plans/{planId}
```
---
# statistic endpoint for maximum weight of a certain excersise
### Workout Sessions & Tracking
```
POST /api/v1/users/{userId}/sessions
Request: {
  "planId": "string",
  "weekNumber": "number",
  "dayNumber": "number"
}
Response: {
  "id": "string",
  "userId": "string",
  "planId": "string",
  "weekNumber": "number",
  "dayNumber": "number",
  "status": "string",
  "startedAt": "datetime",
  "exercises": [
    {
      "id": "string",
      "exerciseId": "string",
      "name": "string",
      "targetSets": "number",
      "targetReps": "string",
      "restSeconds": "number",
      "status": "string",
      "order": "number"
    }
  ]
}
```

```
PATCH /api/v1/users/{userId}/plan/{planId}/exercises/{exerciseId}
Request: {
  "status": "string",
  "sets": [
    {
      "setNumber": "number",
      "weight": "number",
      "reps": "number"
    }
  ]
}
Response: {
  "id": "string",
  "exerciseId": "string",
  "name": "string",
  "status": "string",
  "sets": [
    {
      "setNumber": "number",
      "weight": "number",
      "reps": "number",
      "completedAt": "datetime"
    }
  ],
  "updatedAt": "datetime"
}
```

```
PATCH /api/v1/users/{userId}/sessions/{sessionId}/rest
Request: {
  "durationSec": "number",
  "exerciseId": "string"
}
Response: {
  "success": "boolean",
  "restLogged": "boolean"
}
```
```
### Exercise History & Progress Tracking
GET /api/v1/users/{userId}/exercises/{exerciseId}/history
Query: ?page=number&limit=number&startDate=date&endDate=date
Response: {
  "exerciseId": "string",
  "exerciseName": "string",
  "history": [
    {+++
      "date": "datetime",
      "sets": [
        {
          "setNumber": "number",
          "weight": "number",
          "reps": "number"
        }
      ],
      "maxWeight": "number",
      "totalVolume": "number"
    }
  ],
  "total": "number"
}
```

```
GET /api/v1/users/{userId}/exercises/{exerciseId}/progress
Response: {
  "exerciseId": "string",
  "exerciseName": "string",
  "firstRecorded": "date",
  "lastRecorded": "date",
  "totalSessions": "number",
  "progression": [
    {
      "date": "date",
      "maxWeight": "number",
      "avgWeight": "number",
      "totalVolume": "number",
      "avgReps": "number"
    }
  ],
  "personalRecords": {
    "maxWeight": "number",
    "maxVolume": "number",
    "maxReps": "number"
  }
}
```
---

### Exercises Catalog

```
GET /api/v1/exercises
Query: ?type=string&targetMuscle=string&equipment=string&difficulty=string&page=number&limit=number&search=string
Response: {
  "exercises": [
    {
      "id": "string",
      "name": "string",
      "type": "string",
      "targetMuscle": [
        "muscle" : "string"
      ],
      "equipment": "string",
    }
  ],
  "maxweight" : "number"
  "total": "number",
  "page": "number",
  "limit": "number"
}
```
```
GET /api/v1/exercises/{exerciseId}
Response: {
  "id": "string",
  "name": "string",
  "type": "string",
  "targetMuscle": "string",
  "equipment": "string",
  "difficulty": "string",
  "description": "string",
  "instructions": "string[]",
  "videoUrl": "string",
  "histor" : [
    #we add list of history
  ]
  "imageUrl": "string",
  "tips": "string[]",
  "createdAt": "datetime",
  "updatedAt": "datetime"
}
```
---
### Meal Suggestions & Nutrition
```
GET /api/v1/users/{userId}/mealplan
Query: ?mealsPerDay=number
Response: {
  "userId": "string",
  "date": "date",
  "mealsPerDay": "number",
  "nutritionTargets": {
    "calories": "number",
    "protein": "number",
    "carbs": "number",
    "fats": "number"
  },
  "meals": [
    {
      "id": "string",
      "name": "string",
      "mealNumber": "number",
      "mealType": "string",
      "calories": "number",
      "protein": "number",
      "carbs": "number",
      "fats": "number",
      "ingredients": "string[]",
      "instructions": "string"
    }
  ],
  "totals": {
    "calories": "number",
    "protein": "number",
    "carbs": "number",
    "fats": "number"
  }
}
```

```
POST /api/v1/users/{userId}/mealplan
Request: {
  "mealsPerDay": "number",
  "dietaryPreferences": "string[]",
  "excludeIngredients": "string[]"
}
Response: {
  "userId": "string",
  "date": "date",
  "mealsPerDay": "number",
  "nutritionTargets": {
    "calories": "number",
    "protein": "number",
    "carbs": "number",
    "fats": "number"
  },
  "meals": [
    {
      "id": "string",
      "name": "string",
      "mealNumber": "number",
      "mealType": "string",
      "calories": "number",
      "protein": "number",
      "carbs": "number",
      "fats": "number"
    }
  ]
}
```

```
GET /api/v1/users/{userId}/nutrition/targets
Response: {
  "userId": "string",
  "bmr": "number",
  "tdee": "number",
  "targetCalories": "number",
  "targetProtein": "number",
  "targetCarbs": "number",
  "targetFats": "number",
  "calculatedFrom": {
    "height": "number",
    "weight": "number",
    "bodyFat": "number",
    "activityLevel": "string"
  }
}
```

```
POST /api/v1/users/{userId}/meals/log
Request: {
  "mealId": "string",
  "date": "date",
  "mealType": "string"
}
Response: {
  "id": "string",
  "userId": "string",
  "mealId": "string",
  "date": "date",
  "mealType": "string",
  "loggedAt": "datetime"
}
```

```
GET /api/v1/users/{userId}/meals/logged
Query: ?startDate=date&endDate=date&page=number&limit=number
Response: {
  "logs": [
    {
      "id": "string",
      "mealId": "string",
      "mealName": "string",
      "date": "date",
      "mealType": "string",
      "calories": "number",
      "protein": "number",
      "loggedAt": "datetime"
    }
  ],
  "total": "number"
}
```

```
GET /api/v1/meals
Query: ?page=number&limit=number&search=string&minProtein=number&maxCalories=number&dietaryPreferences=string
Response: {
  "meals": [
    {
      "id": "string",
      "name": "string",
      "mealType": "string",
      "calories": "number",
      "protein": "number",
      "carbs": "number",
      "fats": "number",
      "prepTime": "number",
      "difficulty": "string"
    }
  ],
  "total": "number",
  "page": "number",
  "limit": "number"
}
```

```
GET /api/v1/meals/{mealId}
Response: {
  "id": "string",
  "name": "string",
  "mealType": "string",
  "calories": "number",
  "protein": "number",
  "carbs": "number",
  "fats": "number",
  "ingredients": [
    {
      "name": "string",
      "amount": "string",
      "unit": "string"
    }
  ],
  "instructions": "string[]",
  "prepTime": "number",
  "cookTime": "number",
  "servings": "number",
  "difficulty": "string",
  "imageUrl": "string",
  "tags": "string[]"
}
```

```
POST /api/v1/admin/meals
Request: {
  "name": "string",
  "mealType": "string",
  "calories": "number",
  "protein": "number",
  "carbs": "number",
  "fats": "number",
  "ingredients": [
    {
      "name": "string",
      "amount": "string",
      "unit": "string"
    }
  ],
  "instructions": "string[]",
  "prepTime": "number",
  "cookTime": "number",
  "servings": "number",
  "difficulty": "string",
  "imageUrl": "string",
  "tags": "string[]"
}
Response: {
  "id": "string",
  "name": "string",
  "calories": "number",
  "protein": "number",
  "createdAt": "datetime"
}
```

```
PUT /api/v1/admin/meals/{mealId}
Request: {
  "name": "string",
  "mealType": "string",
  "calories": "number",
  "protein": "number",
  "carbs": "number",
  "fats": "number",
  "ingredients": [
    {
      "name": "string",
      "amount": "string",
      "unit": "string"
    }
  ],
  "instructions": "string[]",
  "prepTime": "number",
  "cookTime": "number",
  "servings": "number",
  "difficulty": "string",
  "imageUrl": "string",
  "tags": "string[]"
}
Response: {
  "id": "string",
  "name": "string",
  "updatedAt": "datetime"
}
```

```
DELETE /api/v1/admin/meals/{mealId}
```

---

```
### Split Types Reference
GET /api/v1/splits
Response: {
  "splits": [
    {
      "id": "string",
      "name": "string",
      "code": "string",
      "description": "string",
      "recommendedDaysPerWeek": "number",
      "trainingStyle": "string"
    }
  ]
}
```
```
GET /api/v1/splits/{splitId}
Response: {
  "id": "string",
  "name": "string",
  "code": "string",
  "description": "string",
  "recommendedDaysPerWeek": "number",
  "trainingStyle": "string",
  "dayBreakdown": [
    {
      "day": "number",
      "focus": "string",
      "muscleGroups": "string[]"
    }
  ]
}
```