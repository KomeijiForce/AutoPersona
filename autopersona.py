import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

class AutoPersona:
    
    def __init__(self, model_id = f"KomeijiForce/Meta-Llama-3-8B-AutoPersona-Chinese"):

        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.float16, device_map={"":0})

    def fill_in_template(self, character, passage):

        return f'''# 角色
{character}

# 内容
{passage}

# 指令

将以上内容如实地转化为关于“{character}”人设的顺畅的中文陈述句，如果不包含任何有用的信息，回复“无用信息。”

# 人设

'''

    def auto_persona(self, character, passage):

        text = self.fill_in_template(character, passage)

        input_ids = self.tokenizer(text, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**input_ids, max_new_tokens=256)
        generated = self.tokenizer.decode(outputs[0])
        return generated.replace(text, "").replace("<|begin_of_text|>", "").replace("<|end_of_text|>", "")
