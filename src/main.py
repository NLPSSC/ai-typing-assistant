from typing import List
import httpx
import formatting
from llm import query_prompt
from ollama_config import OLLAMA_CONFIG, OLLAMA_ENDPOINT


def build_prompt(sentences: List[str]) -> str:

    NEWLINE = "\n"

    prefix = [
        "Fix all typos and punctuation in the following text, preserving newline characters.",
        NEWLINE
    ]
    
    suffix: List[str] = [
        NEWLINE,
        "Return only the corrected text, and do not include a preamble."
    ]
    prompt_pieces: List[str] = []
    prompt_pieces.extend(prefix)
    prompt_pieces.extend(sentences)
    prompt_pieces.extend(suffix)
    
    prompt_text = "\n".join(prompt_pieces)
    print(prompt_text)
    return prompt_text


if __name__ == "__main__":
    text_to_check: List[str] = [
        "smokes 1-1/2 pkg.q/day.",
        "quit 8/1903- smoked x 14 yrs",
        # "smokes 2 p.p.d.",
        # "quit in 1985   smoker for about 14-15 yrs.",
    ]
    response: None | str = query_prompt(build_prompt(text_to_check))

    # retval += "| Health Factor Comment        | Corrected Text                     |\n"
    # retval += "|------------------------------|------------------------------------|\n"
    # for r in results_generator:
    #     retval += f"|{r[0]}             | {r[1]} |\n"

    headers = ["original comment", "updated comment"]
    print(response)
