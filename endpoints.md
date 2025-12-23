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
  "split": "string",
  "workoutType": "string", // calisthinics or gym
  "daysPerWeek": "number"
  "weeks": "number"
  "startDate": "date"
}
Response: {
  "id": "string",
  "userId": "string",
  "splitType": "string",
  "workoutType": "string",
  "daysPerWeek": "number",
  "status": "string",
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
      "splitName": "string",
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
  "planForWeek": {
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
              "order": "number"
            }
          ]
        }
      ]
    }
  ,
  "createdAt": "datetime"
}
```

```
DELETE /api/v1/users/{userId}/plans/{planId}
```
---

### Workout Sessions & Tracking
```
PATCH /api/v1/users/{userId}/plans/{planId}/exercises/{exerciseId}
Request: {
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
---

## Exercise History & Progress Tracking

```
GET /api/v1/users/{userId}/exercises/{exerciseId}/history
Query: ?page=number&limit=number&startDate=date&endDate=date
Response: {
  "exerciseId": "string",
  "exerciseName": "string",
  "history": [
    {
      "date": "datetime",
      "sets": [
        {
          "setNumber": "number",
          "weight": "number",
          "reps": "number"
        }
      ],
      "maxWeight": "number",
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
      "imageUrl": "url"
      "name": "string",
      "type": "string",
      "targetMuscles": "string"[],
      "maxWeight": number // if played before
    }
  ],
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
  "imageUrl": "string",
  "tips": "string[]",
  "logs history"
}
```

```
DELETE /api/v1/admin/exercises/{exerciseId}
```
---

### Split Types Reference
```
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