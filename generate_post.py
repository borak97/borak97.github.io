import openai
import os
from datetime import date

openai.api_key = os.getenv("OPENAI_API_KEY")

topic = f"تدوينة تقنية عربية بتاريخ {date.today().isoformat()}"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "اكتب تدوينة قصيرة ومفيدة باللغة العربية."},
        {"role": "user", "content": topic}
    ]
)

output = response['choices'][0]['message']['content']

os.makedirs("posts", exist_ok=True)
with open(f"posts/{date.today().isoformat()}.md", "w", encoding='utf-8') as f:
    f.write(output)
