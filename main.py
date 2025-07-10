from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from faker import Faker

app = FastAPI(
    title="Test Data Generator API",
    description="API to generate various types of test data based on user-defined settings.",
    version="1.0.0",
)

fake = Faker()

class FieldDefinition(BaseModel):
    name: str
    type: str = Field(..., description="Supported types: 'string', 'integer', 'float', 'boolean', 'date', 'email', 'phone_number', 'address', 'text', 'uuid', 'name', 'word', 'sentence', 'paragraph'")
    min_value: Optional[int] = None
    max_value: Optional[int] = None
    max_length: Optional[int] = None

class DataGenerationSettings(BaseModel):
    num_records: int = Field(..., gt=0, le=1000, description="Number of records to generate (1-1000)")
    fields: List[FieldDefinition] = Field(..., min_items=1, description="List of field definitions for the generated data")

@app.post("/generate-data")
async def generate_test_data(settings: DataGenerationSettings):
    """
    Generates test data based on the provided settings.
    """
    generated_data = []
    for _ in range(settings.num_records):
        record = {}
        for field in settings.fields:
            try:
                if field.type == "string":
                    record[field.name] = fake.word() if not field.max_length else fake.text(max_nb_chars=field.max_length)
                elif field.type == "integer":
                    record[field.name] = fake.random_int(min=field.min_value, max=field.max_value)
                elif field.type == "float":
                    record[field.name] = fake.pyfloat(left_digits=field.max_value, right_digits=field.min_value, positive=True)
                elif field.type == "boolean":
                    record[field.name] = fake.boolean()
                elif field.type == "date":
                    record[field.name] = str(fake.date_this_century())
                elif field.type == "email":
                    record[field.name] = fake.email()
                elif field.type == "phone_number":
                    record[field.name] = fake.phone_number()
                elif field.type == "address":
                    record[field.name] = fake.address()
                elif field.type == "text":
                    record[field.name] = fake.text()
                elif field.type == "uuid":
                    record[field.name] = str(fake.uuid4())
                elif field.type == "name":
                    record[field.name] = fake.name()
                elif field.type == "word":
                    record[field.name] = fake.word()
                elif field.type == "sentence":
                    record[field.name] = fake.sentence()
                elif field.type == "paragraph":
                    record[field.name] = fake.paragraph()
                else:
                    raise ValueError(f"Unsupported field type: {field.type}")
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Error generating data for field '{field.name}': {e}")
        generated_data.append(record)
    return {"generated_data": generated_data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
