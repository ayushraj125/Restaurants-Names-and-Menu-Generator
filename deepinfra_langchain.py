#######################################
#-----USING DEEPINFRA MODEL------#
#######################################



from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os
from secret_key import deepinfrapi_key

os.environ["OPENAI_API_KEY"] = deepinfrapi_key

llm = ChatOpenAI(
    temperature=0.7,
    model="deepseek-ai/DeepSeek-R1-0528",
    openai_api_base="https://api.deepinfra.com/v1/openai"
)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest some fancy names for this. With no explanation, just return the names."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Generate 5 creative, upscale menu items that would be served at a high-end Indian restaurant called "{restaurant_name}". The items should reflect the restaurant's luxurious and elegant branding. Return only a comma-separated list of dish names."""
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine both chains sequentially
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items'],
        return_all=True,
        verbose=False
    )

    return chain({'cuisine': cuisine})

if __name__ == "__main__":
    result = generate_restaurant_name_and_items("Italian")
    print("Restaurant Name:", result['restaurant_name'])
    print("Menu Items:", result['menu_items'])
