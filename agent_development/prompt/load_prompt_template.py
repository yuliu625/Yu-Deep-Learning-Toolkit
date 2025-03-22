
def load_prompt_template(prompt_template_path: str) -> str:
    with open(prompt_template_path, 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    return prompt_template


if __name__ == '__main__':
    eg_prompt_template = load_prompt_template(
        r"D:\document\code\paper\World-of-Six\game\prompts\participant_prompts\system_prompts\game_description_prompt_1"
    )

    print(eg_prompt_template)
    print(type(eg_prompt_template))
