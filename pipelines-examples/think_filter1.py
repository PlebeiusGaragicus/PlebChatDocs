"""
author: Yuchen Xie
website tested: https://arlow.cloud
description: Thinking and Output Tag
name: Think-and-Output Tag
version: 0.0.2
demonstration: https://www.reddit.com/r/LocalLLaMA/comments/1g3y432/recreating_gpt_o1_cot_thinking_thinking_and/ --> Version demonstrated: 0.0.1
details: Parts of code and structure taken from @projectmoon: https://openwebui.com/f/projectmoon/artificium_thinking_filter
last updated: 10/15/2024
changes made: Added thinking durations, added additional information to the headers, and added debugging statements.
IMPORTANT!!!
Requirements: 
1. Model should know "enters thinking" using the *## Thinking* output.
2. Model should understand that "***" will exit the thinking.
No need to retrain the model, simply instruction tune the model-file.
"""
# -----------------------------------------------------------------------------------------------------------------------------------------------------
"""
Sample instruction for the model:
You are a Chain of Thought (CoT) model with reinforcement learning capabilities, trained on synthetic data. Your task is to follow a structured yet engaging process when responding to questions, ensuring clear reasoning with creative step names before delivering your final solution. 
THIS IS IMPORTANT: THINKING IS REQUIRED ON ALL RESPONSES, THAT MEANS, YOU ARE REQUIRED TO THINK BEFORE EVERY RESPONSE. IT DOESN'T MATTER HOW EASY THE QUERY IS, THINK BEFORE ANSWERING. 

When asked a question, your response should be formatted as follows:

## Thinking

For every question, begin by engaging in Thinking. Break the problem down into smaller components that need to be understood or solved.

**Collecting Thoughts**

After identifying the main problem, proceed to Collecting Thoughts. Each thought should represent a distinct step toward solving the problem, and each step should have a creative, task-specific name. The steps should outline a logical plan or sequence of actions needed to reach the solution.

**Final Solution**

After synthesizing everything and providing a well-reasoned, coherent solution.

Example question:
If Johnny has 10 apples and Emily has 4, how many apples does Johnny have to give to Emily so that they have the equal amount of apples?

## Thinking

**Evaluating the task**

I’m analyzing Johnny's problem: he needs to share apples with Emily so they both have 7. This involves subtracting Johnny's apples from Emily's to equalize the count.

**Solving Johnny's equation**

OK, let me see. To help Johnny share his apples equally with Emily, I set the equation:

10 - x = 4 + x

Solving it gave:

x = 3

meaning Johnny should give 3 apples to balance things out.

***

To determine how many apples Johnny needs to give to Emily so that both have an equal number of apples, let’s break it down step by step.

1. **Initial Amounts**:
    - Johnny: 10 apples
    - Emily: 4 apples

2. **Let’s define the variable**:
    - Let 𝑥 be the number of apples Johnny gives to Emily.

3. **After the Transfer**:
    - Johnny’s apples: 10 − 𝑥
    - Emily’s apples: 4 + 𝑥

4. **Setting Up the Equation for Equality**:

   10 − 𝑥 = 4 + 𝑥

5. **Solving for 𝑥**:

   10 − 𝑥 = 4 + 𝑥  
   10 − 4 = 𝑥 + 𝑥  
   6 = 2𝑥  
   𝑥 = 3

6. **Conclusion**:
    - Johnny needs to give 3 apples to Emily.
    - After the transfer:
        - Johnny: 10 − 3 = 7 apples
        - Emily: 4 + 3 = 7 apples

Both Johnny and Emily will have 7 apples each, ensuring they have an equal number of apples.

Your responses must always follow this structured flow, using creative subtitles for each step in the thought process. Because of this, you are allowed to think as long as possible and as thorough as possible. Don't worry about the cost to run these tokens. You must use the thinking structure no matter how basic or complex the problem is. You are a CoT model! All thinking must be done in the first-person point of view. Keep in mind that you are not suppose to do the calculations inside the thinking stage, it should be in the final answer stage after the "***".
"""
#------------------------------------------------------------------------------------------------------------------------------------------------------
import re
import time
from typing import Optional, Dict, List
from pydantic import BaseModel, Field

THOUGHT_ENCLOSURE = """
<details>
<summary>Thought for {{DURATION}} seconds</summary>
{{THOUGHTS}}

</details>
"""


class Filter:
    class Valves(BaseModel):
        priority: int = Field(
            default=0, description="Priority level for the filter operations."
        )

    def __init__(self):
        self.valves = self.Valves()
        self.thinking_start_time = None

    def _parse_reply(self, reply: str) -> dict:
        # Split the reply into "thinking" and "final answer" parts
        thinking_pattern = r"## Thinking(.*?)(?=\*\*\*|$)"
        final_answer_pattern = r"\*\*\*(.*?)$"

        thinking_match = re.search(thinking_pattern, reply, re.DOTALL)
        final_match = re.search(final_answer_pattern, reply, re.DOTALL)

        thinking = thinking_match.group(1).strip() if thinking_match else None
        final_answer = final_match.group(1).strip() if final_match else None

        return {"thinking": thinking, "final": final_answer}

    def _enclose_thoughts(self, messages: List[Dict[str, str]]) -> None:
        if not messages:
            return

        reply = messages[-1]["content"]
        parsed_reply = self._parse_reply(reply)
        final_reply = ""

        # Enclose the thinking part in a collapsible section
        if parsed_reply["thinking"] is not None:
            # Calculate thinking duration
            if self.thinking_start_time is not None:
                thinking_duration = time.time() - self.thinking_start_time
                duration_str = f"{thinking_duration:.2f}"
            else:
                duration_str = "an unknown amount of"

            enclosed_thoughts = THOUGHT_ENCLOSURE.replace(
                "{{THOUGHTS}}", parsed_reply["thinking"]
            ).replace("{{DURATION}}", duration_str)
            final_reply += f"{enclosed_thoughts}\n"

        # Add the final answer
        if parsed_reply["final"] is not None:
            # Remove any HTML tags that may have been accidentally included
            cleaned_final_answer = re.sub(r"<[^>]+>", "", parsed_reply["final"])
            final_reply += f"\n{cleaned_final_answer}"

        final_reply = final_reply.strip()
        if final_reply:
            messages[-1]["content"] = final_reply

    def inlet(
        self, body: Dict[str, any], __user__: Optional[Dict[str, any]] = None
    ) -> Dict[str, any]:
        try:
            original_messages: List[Dict[str, str]] = body.get("messages", [])
            self.thinking_start_time = time.time()  # Start timing when inlet is called
            body["messages"] = original_messages
            return body
        except Exception as e:
            print(e)
            return body

    def outlet(
        self, body: Dict[str, any], __user__: Optional[Dict[str, any]] = None
    ) -> Dict[str, any]:
        try:
            original_messages: List[Dict[str, str]] = body.get("messages", [])
            self._enclose_thoughts(original_messages)
            body["messages"] = original_messages
            return body
        except Exception as e:
            print(e)
            return body
