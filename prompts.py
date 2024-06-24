import constants

ZS_SV = f"""
    Your task is to identify the underlying value for a given piece of text from a provided list of possible values.
    - The answer must be exactly one of these possible values, using their exact wording from this list: {constants.VALUES}.
    - The answer must be given in the format of a Python list, e.g., ["be ..."] or ["have ..."].
    - Do not provide any explanation, additional text, or any value not present in the list.
    Given the text below, identify the underlying value in the specified format:
"""

ZS_MV = f"""
    Your task is to identify the underlying values for a given piece of text from a provided list of possible values.
    - The answers must be any of these possible values that you think apply, using their exact wording from this list: {constants.VALUES}.
    - If none of the values match, you may respond with 'None'.
    - The responses must be given in the format of a Python list, e.g., ["be ...", "have ..."], or ["None"] if no values apply.
    - Do not provide any explanation, additional text, or any values not present in the list.
    Given the text below, identify the underlying values in the specified format:
"""

FS_SV = f"""
    Your task is to identify the underlying value for a given piece of text from a provided list of possible values.
    - If none of the values listed are applicable, please select 'None'.
    - The answer must be exactly one of these possible values, using their exact wording from this list: {constants.VALUES}.
    - The response must be given in the format of a Python list, e.g., ["be ..."] or ["have ..."].
    - Do not provide any explanation, additional text, or any values not present in the list.

    Examples:
    - Text: "nuclear weapons help keep the peace in uncertain times"
      Value: ["Have a world at peace"]

    - Text: "anyone who commits a crime should be prosecuted"
      Value: ["Be just"]

    - Text: "sending aid to people in need is the right thing to do"
      Value: ["Be helpful"]

    Given the text below, identify the underlying value in the specified format:
"""

FS_MV = f"""
    Your task is to identify the underlying values for a given piece of text from a provided list of possible values.
    - The answers must be any of these possible values that you think apply, using their exact wording from this list: {constants.VALUES}.
    - If none of the values match, you may respond with 'None'.
    - The responses must be given in the format of a Python list, e.g., ["be ...", "have ..."], or ["None"] if no values apply.
    - Do not provide any explanation, additional text, or any values not present in the list.

    Examples:
    - Text: "nuclear weapons help keep the peace in uncertain times, but we should use them responsibly"
      Value: ["Have a world at peace", "Be responsible"]

    - Text: "anyone who commits a crime should be prosecuted. it can't be the case that some people are above the law"
      Value: ["Be just", "Have equality"]

    - Text: "sending aid to people in need is the right thing to do, regardless of who they are or where they come from"
      Value: ["Be helpful", "Have the wisdom to accept others"]

    Given the text below, identify the underlying values in the specified format:
"""

# Ask for reasoning
CT_SV_REASONING = f"""
Let's think step by step.
Your task is to identify the underlying value for a given piece of text from a provided list of possible values.
    - The answer must be exactly one of these possible values, using their exact wording from this list: {constants.VALUES}.
    - Do not choose any value not present in the list.
Given the text below, please provide your reasoning for which value you think is the underlying value:
"""

# Given reasoning, ask for prediction
CT_SV_PREDICTION = f"""
Your task is to identify the underlying value for a given piece of text from a provided list of possible values.
- The answer must be exactly one of these possible values, using their exact wording from this list: {constants.VALUES}.
- The answer should not include any additional text or explanations.
- The answer must be given in the format of a Python list, e.g., ["Be just"] or ["Have freedom of thought"].
- Only provide the value inside the Python list.
Given this reasoning, please provide which single value you think is the most applicable in the specified format:

Reasoning:
"""

# Ask for reasoning
CT_MV_REASONING = f"""
Let's think step by step.
Your task is to identify the underlying values for a given piece of text from a provided list of possible values.
    - The answer must be any of these possible values that you think apply, using their exact wording from this list: {constants.VALUES}.
    - Do not choose any values not present in the list.
Given the text below, please provide your reasoning for which values you think are underlying values:
"""

# Given reasoning, ask for prediction
CT_MV_PREDICTION = f"""
Your task is to identify the underlying values for a given piece of text from a provided list of possible values.
- The answer must be any of these possible values that you think apply, using their exact wording from this list: {constants.VALUES}.
- The answer should not include any additional text or explanations.
- The answer must be given in the format of a Python list, e.g., ["Be just", "Have equality"] or ["Have freedom of thought"].
- Only provide the values inside the Python list.
Given this reasoning, please provide which values you think are applicable in the specified format:

Reasoning:
"""