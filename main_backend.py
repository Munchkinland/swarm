from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from swarm import Swarm, Agent

app = FastAPI()
client = Swarm()

class Message(BaseModel):
    message: str

def transfer_to_agent_b():
    return agent_b

def transfer_to_agent_c():
    return agent_c

agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent that specializes in general knowledge. If the user asks about weather, transfer to Agent B. If the user asks about movies, transfer to Agent C.",
    functions=[transfer_to_agent_b, transfer_to_agent_c],
)

agent_b = Agent(
    name="Agent B",
    instructions="You are a weather specialist. Only answer questions about weather.",
)

agent_c = Agent(
    name="Agent C",
    instructions="You are a movie expert. Only answer questions about movies.",
)

@app.post("/api/swarm")
async def swarm_chat(message: Message):
    try:
        response = client.run(
            agent=agent_a,
            messages=[{"role": "user", "content": message.message}],
        )
        return {"messages": response.messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)