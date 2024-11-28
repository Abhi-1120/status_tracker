import uvicorn
import pymongo
from typing import Dict
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

client = pymongo.MongoClient('localhost', 27017)
db = client['upswingDB']
collection = db['status']

class TimeRange(BaseModel):
    start_time: str
    end_time: str

@app.get("/status_counts", response_model=Dict[str, int])
async def get_status_count(start_time: str = Query(), end_time: str = Query()):

    try:
        start_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        end_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

        query = [
            {
                "$match": {
                    "timestamp": {
                        "$gte": start_dt,
                        "$lte": end_dt
                    }
                }
            },
            {
                "$group": {
                    "_id": "$status",
                    "count": {
                        "$sum": 1
                    }
                }
            }
        ]

        result = collection.aggregate(query)

        return {str(item["_id"]): item["count"] for item in result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid datetime format: {str(e)}")


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=5555)
