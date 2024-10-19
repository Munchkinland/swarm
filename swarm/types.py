from openai.types.chat import ChatCompletionMessage
from openai.types.chat.chat_completion_message_tool_call import (
    ChatCompletionMessageToolCall,
    Function,
)
from typing import List, Callable, Union, Optional

# Third-party imports
from pydantic import BaseModel

AgentFunction = Callable[[], Union[str, "Agent", dict]]


class Agent(BaseModel):
    """
    Represents an agent in the system. Each agent can have functions,
    tool choices, and provide instructions for behavior.

    Attributes:
        name (str): Name of the agent.
        model (str): The model used by the agent (e.g., GPT-3.5-turbo).
        instructions (Union[str, Callable[[], str]]): Instructions to guide the agent's behavior.
        functions (List[AgentFunction]): A list of functions the agent can use.
        tool_choice (str): The specific tool the agent may prefer using.
        parallel_tool_calls (bool): Indicates if the agent can call tools in parallel.
    """
    name: str = "Agent"
    model: str = "gpt-3.5-turbo"  # Updated model to gpt-3.5-turbo
    instructions: Union[str, Callable[[], str]] = "You are a helpful agent."
    functions: List[AgentFunction] = []
    tool_choice: str = None
    parallel_tool_calls: bool = True


class Response(BaseModel):
    """
    Represents the response generated during a conversation or process.

    Attributes:
        messages (List): The list of messages involved in the response.
        agent (Optional[Agent]): The agent that participated in the response.
        context_variables (dict): Contextual data updated during the process.
    """
    messages: List = []
    agent: Optional[Agent] = None
    context_variables: dict = {}


class Result(BaseModel):
    """
    Encapsulates the possible return values for an agent function.

    Attributes:
        value (str): The result value as a string.
        agent (Optional[Agent]): The agent instance, if applicable.
        context_variables (dict): A dictionary of context variables.
    """
    value: str = ""
    agent: Optional[Agent] = None
    context_variables: dict = {}
