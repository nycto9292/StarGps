from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import gps


class GPSApp(App):

    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.label = Label(text="GPS Ready")

        button = Button(
            text="Get Location",
            size_hint=(1, 0.3)
        )

        button.bind(on_press=self.start_gps)

        self.layout.add_widget(self.label)
        self.layout.add_widget(button)

        return self.layout

    def start_gps(self, instance):
        self.label.text = "Finding location..."

        try:
            gps.configure(
                on_location=self.on_location,
                on_status=self.on_status
            )

            gps.start(
                minTime=1000,
                minDistance=1
            )

        except NotImplementedError:
            self.label.text = "GPS is not available on this device"

    def on_location(self, **kwargs):
        latitude = kwargs.get("lat")
        longitude = kwargs.get("lon")

        self.label.text = (
            f"Latitude: {latitude}\n"
            f"Longitude: {longitude}"
        )

    def on_status(self, stype, status):
        print(stype, status)


GPSApp().run()
