from typing import List
import httpx
import formatting
from llm import query_prompt
from ollama_config import OLLAMA_CONFIG, OLLAMA_ENDPOINT


def build_prompt(sentences: List[str]) -> str:

    NEWLINE = "\n"

    prefix = [
        "The each of following phrases are descriptions about a person and their smoking status.",
        "Evaluate each of these phrases, and return a label indicating their smoking status.",
    ]
    
    suffix: List[str] = [
        "Return on of the following labels:",
        "",
        "- if the person is a smoker, return the label CURRENT_SMOKER",
        "- if the person quit smoking in the past, return the label PAST_SMOKER",
        "- if the person has never smoked, return the label NEVER_SMOKED"
    ]
    prompt_pieces: List[str] = []
    prompt_pieces.extend(prefix)
    prompt_pieces.append(NEWLINE)
    prompt_pieces.extend(sentences)
    prompt_pieces.append(NEWLINE)
    prompt_pieces.extend(suffix)
    
    prompt_text = "\n".join(prompt_pieces)

    return prompt_text


if __name__ == "__main__":
    text_to_check: List[str] = [
        "smokes 1-1/2 pkg.q/day.",
        "quit 8/1903- smoked x 14 yrs",
        "smokes 2 p.p.d.",
        # "quit in 1985   smoker for about 14-15 yrs.",
    ]
    prompt_text = build_prompt(text_to_check)
    response: None | str = query_prompt(prompt_text)

    # retval += "| Health Factor Comment        | Corrected Text                     |\n"
    # retval += "|------------------------------|------------------------------------|\n"
    # for r in results_generator:
    #     retval += f"|{r[0]}             | {r[1]} |\n"

    print(prompt_text)
    print()

    headers = ["original comment", "updated comment"]
    print()
    print(response)
