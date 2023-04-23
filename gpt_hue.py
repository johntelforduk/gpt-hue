from phue import Bridge
import openai

MODEL = 'gpt-3.5-turbo'
BRIDGE_IP = '192.168.1.193'


def cost_calc(num_tokens: int) -> float:
    """
    For parm number of tokens used, return cost incurred in USD.
    """
    # From, https://openai.com/pricing, gpt-3.5-turbo is $0.002 per 1000 tokens.
    return num_tokens * 0.002 / 1000


class Persona:

    def __init__(self, name: str):

        self.name = name
        self.history = []
        self.cumulative_tokens = 0

    def give_mission(self, mission: str):
        mission += '''\nPlease ensure that all of your responses are 20 words or less.
Please say "OK" now if you understand.'''
        print(self.name + ' mission...')
        print(mission)
        print('------------')
        self.update_history(role='user', content=mission)

        # 'Trick' GPT into thinking it understood us earlier in the conversation.
        self.update_history(role='assistant', content='OK.')

    def update_history(self, role: str, content: str):
        assert role in ['assistant', 'user']
        self.history.append({'role': role, 'content': content})

    def chat(self, prompt: str) -> str:
        self.update_history(role='user', content=prompt)
        completion = openai.ChatCompletion.create(model=MODEL, messages=self.history)
        self.cumulative_tokens += int(completion.usage.total_tokens)
        response = completion.choices[0].message.content

        print(self.name + ': ' + response)
        self.update_history(role='assistant', content=response)
        return response


class Lights:

    def __init__(self, bridge_ip):
        self.bridge = Bridge(bridge_ip)

        # If the app is not registered and the button is not pressed, press the button and call connect()
        # (this only needs to be run a single time)
        self.bridge.connect()

        # Get the bridge state (This returns the full dictionary that you can explore)
        bridge_state = self.bridge.get_api()

        # Make a single dictionary of all the lights and groups.
        # Key = name of individual light or group of lights, value = list of light IDs.
        self.lights = {}

        for light_id in bridge_state['lights']:
            light_name = bridge_state['lights'][light_id]['name']
            self.lights[light_name] = [light_id]

        remove_later = set()

        for group_id in bridge_state['groups']:
            group_name = bridge_state['groups'][group_id]['name']

            for candidate in self.lights:
                if group_name in candidate:
                    remove_later.add(candidate)

            self.lights[group_name] = bridge_state['groups'][group_id]['lights']

        for each_light in remove_later:
            del self.lights[each_light]

    def turn_on_or_off(self, name: str, on: bool):
        if name not in self.lights:
            print('Light not found.')
            return

        for light_id in self.lights[name]:
            self.bridge.set_light(int(light_id), 'on', on)

        if on:
            print('Turned on ' + name)
        else:
            print('Turned off ' + name)

    def describe_lights(self) -> str:
        description = '''I have lights with the following names,'''
        for name in self.lights:
            description += f'\n\t{name}'
        return description

    def interpret_response(self, response: str):
        if 'PUT' in response:
            api_command = response.split('PUT')
            api_parts = api_command[1].split('/')
            # print('response: ' + str(api_parts))
            light_name = api_parts[2]
            state = 'true' in api_parts[3]

            # print('light_name: ' + light_name)
            # print('state: ' + str(state))
            self.turn_on_or_off(light_name, state)


my_lights = Lights(BRIDGE_IP)

openai.api_key = open('openai_key.txt', 'r').read().strip('\n')
chatgpt = Persona('ChatGPT')
chatgpt.give_mission(mission='''Hello.
I would like you to control the Hue light-bulbs in my house using API calls.
I will use natural language to ask you to do something with my Hue bulbs, and you should say the Hue API commands 
needed to do the thing I want.
Let's define an API for Hue lights as follow. To turn on a Hue light use PUT/lights/<name>/state {"on": true}
''' + my_lights.describe_lights() + '''
I like to watch TV in the Living Room, with the lights in that room turned off. I do all of my cooking in the Kitchen.''')

while True:
    inp = input("User input (or 'quit'): ")
    if inp == 'quit':
        break
    resp = chatgpt.chat(prompt=inp)
    my_lights.interpret_response(resp)

print('\nTotal tokens used:', chatgpt.cumulative_tokens)
print('Cost incurred (USD):', cost_calc(chatgpt.cumulative_tokens))
