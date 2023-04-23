# GPT Hue
This program creates an [OpenAI](https://openai.com/) [GPT](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer) powered chatbot which gives responses which control [Philips Hue](https://www.philips-hue.com/en-gb) lights using the [Hue API](https://github.com/studioimaginaire/phue). It is an experiment to see whether generative AI has the potential to make interacting with smart home devices easier.

[Video demo on YouTube](https://www.youtube.com/watch?v=sAYGKsNVn6Y).

### Installation
```commandline
pip install phue
pip install openai
```
### First run
Before first run of program,
1. Edit `BRIDGE_IP` to be the actual IP address of the Hue Hub on your home network. You can find this out using the Hue app on your phone.
2. The program requires an `openai_key.txt` file containing your [OpenAI API key](https://platform.openai.com/account/api-keys).

### The chatbot's mission
At the start of the conversation, the GPT chatbot is asked to control some Hue lights using a defined API. The chatbot is also told a list of available lights (this list is obtained automatically using the Hue API). The chatbot is also given some additional information about the user's preferences - for example that it is a good idea to turn off lights in the Living Room before watching TV.

Here is an example mission,

> Hello.
> I would like you to control the Hue light-bulbs in my house using API calls.
> I will use natural language to ask you to do something with my Hue bulbs, and you should say the Hue API commands needed to do the thing I want.
>
> Let's define an API for Hue lights as follow. To turn on a Hue light use `PUT/lights/<name>/state {"on": true}`
>
> I have lights with the following names,
> 
> Floor Lamp\
> Desk Lamp\
> Main Dining\
> Kitchen\
> Living Room
>
> I like to watch TV in the Living Room, with the lights in that room turned off. I do all of my cooking in the Kitchen.
>
> Please ensure that all of your responses are 20 words or less. 
> Please say "OK" now if you understand.


### Example conversation
**User input (or 'quit'):** 
>let's get ready for tv

**ChatGPT:**
> PUT/lights/Living Room/state {"on": false}\
> Turned off Living Room

**User input (or 'quit'):**
> tv time is over

**ChatGPT:**
> PUT/lights/Living Room/state {"on": true}\
> Turned on Living Room

### Costs
The program is currently configured to use the **gpt-3.5-turbo** model, which (at time of writing) has a [cost](https://openai.com/pricing) of $0.002 per 1,000 tokens. Note, new OpenAI accounts usually come with some token credits.
