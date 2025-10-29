from fastmcp import FastMCP

# Create a basic server instance
mcp = FastMCP(name="MyAssistantServer")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
    instructions="""
        This server provides data analysis tools.
        Call get_average() to analyze numerical data.
    """,
)


@mcp.tool
def say_hello(name: str) -> str:
    """Returns a friendly greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
