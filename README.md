# GPT Hue
This program creates an [OpenAI](https://openai.com/) [GPT](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer) powered chatbot which gives responses which control [Philips Hue](https://www.philips-hue.com/en-gb) lights using the [Hue API](https://github.com/studioimaginaire/phue). It is an experiment to see whether generative AI has the potential to make interacting with smart home devices easier.

It uses the recently released [function calling](https://openai.com/blog/function-calling-and-other-api-updates) capability in the Chat Completions API. For a great description of how this capability works, I recommend this [video](https://youtu.be/0lOSvOoF2to).

### Example conversation
**"turn on lights where we eat"**

> Turned on Main Dining

**"that's too bright"**

> Main Dining set to 39% brightness

**"still too bright"**

> Main Dining set to 19% brightness

**"turn them off"**

> Turned off Main Dining

### Setup
The program requires an [OpenAI API key](https://platform.openai.com/account/api-keys).

You also need to find out the IP address of the Hue Hub on your home network. You can find this out using the Hue app on your phone.

Before running the program, create a `.env` file containing the following key/values,
```commandline
# OpenAI
OPEN_AI_KEY=<your OpenAI API key>
OPEN_AI_MODEL="gpt-3.5-turbo-0613"

# Philips Hue
BRIDGE_IP=<IP address of your Hue Hub>
```

### Install & run
To install the packages one-by-one,
```commandline
pip install python-dotenv
pip install phue
pip install openai
```
Alternatively, use this command,
```commandline
pip install -r requirements.txt
```
Before the first run of the program, press the button on your Hue bridge (this is needed on the first run only).

Finally, run the program with `python gpt_hue.py`

### Costs
The program is currently configured to use the **gpt-3.5-turbo** model, which (at time of writing) has a [cost](https://openai.com/pricing) of $0.002 per 1,000 tokens. Note, new OpenAI accounts usually come with some token credits.
