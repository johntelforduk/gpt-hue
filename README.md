# GPT Hue
This program creates an [OpenAI](https://openai.com/) [GPT](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer) powered chatbot which gives responses which control Philips Hue lights using the Hue API. It is an experiment to see whether generative AI has the potential to make interacting with smart home devices easier.

### Installation
```commandline
pip install phue
pip install openai
```
### First run
Before first run of program,
1. Edit `BRIDGE_IP` to be the actual IP address of the Hue Hub on your home network. You can find this out using the Hue app on your phone.
2. The program requires a `openai_key.txt` file containing your [OpenAI API key](https://platform.openai.com/account/api-keys).

### The chat-bot's mission
TODO

## Costs
The program is currently configured to use the **gpt-3.5-turbo** model, which (at time of writing) has a [cost](https://openai.com/pricing) of $0.002 per 1,000 tokens. Note, new OpenAI accounts usually come with some token credits.

### Example conversations
**User:** get ready for watching tv

**User:** tv time is over

**User:** let's cook