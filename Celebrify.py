import webbrowser
import json
import requests
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button




class Celebrify(App):

    def celeb_detect(self,btn):
        uri = self.input_image.text
        url = "https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDFSg74tNyciJq3lNTs6UwB0TGMjK8sV5s"

        payload = {
            "requests": [
                {
                    "image": {
                        "source": {
                            "imageUri": uri
                        }
                    },
                    "features": [
                        {
                            "type": "LANDMARK_DETECTION",
                            "maxResults": 1
                        },
                        {
                            "type": "WEB_DETECTION",
                            "maxResults": 2
                        }
                    ]
                }
            ]
        }

        # Send API Request
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        # Stringify Response

        json_data = str(json.loads(response.text))

        start = json_data.find("label")
        trimmed = json_data[start + 9:]
        bestguess = ""
        for char in trimmed:
            if 'a' <= char <= 'z' or char == ' ' or 'A' <= char <= 'Z':
                bestguess = bestguess + char

            bestguess = bestguess.title()

            # Console Testing
            #print (json_data)
            #print (trimmed)
            #print (bestguess)
            self.result.text = bestguess

    def build(self):
        self.title = "Celebrify | Stay in the Loop"

        self.background = (1, 0, 1, 1)

        framework = GridLayout(cols=2,
                               rows=2,
                               spacing=10,
                               pading=10)

        submit_btn = Button(text="Submit Image",
                            size_hint_x=.2,
                            size_hint_y=.15,
                            background_normal='green-yellow.png',
                            background_down='green-yellow-pressed.png',
                            color=(0, 0, 0, 1),
                            )


        self.input_image = TextInput(text="",
                                     multiline=False,
                                     size_hint_y=.15)

        btn3 = Button(text="3rd",
                      size_hint_x=.1
                      )

        self.result = Label(text="4th")



        submit_btn.bind(on_press=self.celeb_detect)

        framework.add_widget(submit_btn)
        framework.add_widget(self.input_image)
        framework.add_widget(btn3)
        framework.add_widget(self.result)

        return framework

        # return GridLayout()


celebrify = Celebrify()

celebrify.run()


