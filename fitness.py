# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token

from langflow.load import run_flow_from_json
import requests
import os
from dotenv import load_dotenv
from  typing import Optional
import json

load_dotenv()



BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = 
FLOW_ID = 
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")


# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}

def dict_to_string(obj, level=0):
    strings = []
    indent = "  " * level  # Indentation for nested levels
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                nested_string = dict_to_string(value, level + 1)
                strings.append(f"{indent}{key}: {nested_string}")
            else:
                strings.append(f"{indent}{key}: {value}")
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            nested_string = dict_to_string(item, level + 1)
            strings.append(f"{indent}Item {idx + 1}: {nested_string}")
    else:
        strings.append(f"{indent}{obj}")

    return ", ".join(strings)

def get_macros(profile ,  goal ):
      
      TWEAKS = {
        
      
                
               
         
          
           "TextInput-NMku7": {
            "input_value": dict_to_string(profile)
          },
          "ChatInput-nwycj": {
            
            "input_value":goal
            
          }
        
       
      }
      
      #result  =    run_flow_from_json(flow="Fitness_application.json",input_value="message",fallback_to_env_vars=True,tweaks=TWEAKS)
       #result[0].outputs[0].results["text"].data["text"]

      result =  run_flow("",tweaks=TWEAKS,application_token=APPLICATION_TOKEN)
      return result

      


  



def run_flow(message: str,
             output_type: str = "chat",
             input_type: str = "chat",
             tweaks: Optional[dict]= None,
             application_token: Optional[str] = None):


     
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/Fitness"
    print("hi ",tweaks["ChatInput-nwycj"]["input_value"])

    payload = {
        "input_value": tweaks["ChatInput-nwycj"]["input_value"],
        "tweaks": tweaks["TextInput-NMku7"],
        #"input_type": input_type,
        "output_type": output_type
        

        
    }
   
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    k = response.json()
    return k["outputs"][0]["outputs"][0]["results"]['message']['data']['text']








