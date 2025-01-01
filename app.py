from langchain_community.agent_toolkits import PlayWrightBrowserToolkit # type:ignore
from langchain_community.tools.playwright.utils import create_sync_playwright_browser # type:ignore
from langchain import hub # type:ignore
from langchain.agents import AgentExecutor, create_openai_tools_agent # type:ignore
from langchain_openai import ChatOpenAI # type:ignore
from dotenv import load_dotenv # type:ignore
import os 

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Get the prompt to use 
prompt = hub.pull("hwchase17/openai-tools-agent")


sync_browser = create_sync_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(sync_browser=sync_browser)
tools = toolkit.get_tools()

# Choose the LLM that will drive the agent
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Construct the OpenAI Tools agent
agent = create_openai_tools_agent(llm, tools, prompt)


# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

command = {
    "input": "Go to https://github.com/stevealila and list highlighted the repositories. Print out url at each step."
}

output = agent_executor.invoke(command)
print(output)