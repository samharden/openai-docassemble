from docassemble.base.util import get_config
import openai
openai.api_key = get_config('openai key')

def send_to_openai(user_input):
  try:
    return openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role":"system", "content":"You are a famous chef who can create a good recipe using any ingredients. Please use the ingredients that the user gives you and write a good recipe using all of them."},
        {"role":"user", "content":user_input}
               ],
      max_tokens=4000,
      temperature=.4)
  except Exception as e:
    return e
