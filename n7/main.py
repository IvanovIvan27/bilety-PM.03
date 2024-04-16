class ZTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def from_seconds(total_seconds):
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return ZTime(hours, minutes, seconds)


class Runner:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __str__(self):
        return f"{self.name}: {self.time}"


def main():
    runners = [
        Runner("Alice", ZTime(0, 3, 45)),
        Runner("Bob", ZTime(0, 4, 5)),
        Runner("Charlie", ZTime(0, 3, 55)),
    ]

    # Sort runners by time
    runners.sort(key=lambda x: x.time.to_seconds())

    # Print the table
    print("Results of the 1000-meter race:")
    print(f"{'Name'} {'Time'}")
    for runner in runners:
        print(f"{runner.name} {runner.time}")


if __name__ == "__main__":
    main()
