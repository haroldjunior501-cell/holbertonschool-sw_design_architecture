#!/usr/bin/env python3


class NewsSubject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer, topics=None):
        self._observers.append((observer, topics))

    def unsubscribe(self, observer):
        self._observers = [
            (o, t) for o, t in self._observers if o is not observer
        ]

    def notify(self, topic, data):
        snapshot = list(self._observers)
        for observer, topics in snapshot:
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    def update(self, topic, data):
        print("log:{}={}".format(topic, data))


class EmailObserver:
    def update(self, topic, data):
        print("email:{}={}".format(topic, data))


class SmsObserver:
    def update(self, topic, data):
        print("sms:{}={}".format(topic, data))


def main():
    subject = NewsSubject()

    subject.subscribe(LogObserver(), topics={"sports", "breaking"})
    subject.subscribe(EmailObserver())
    subject.subscribe(SmsObserver(), topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
