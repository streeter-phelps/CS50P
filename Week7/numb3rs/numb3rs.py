import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return False
    nums = ip.split(".") # just for readability for beginners
    for num in nums:
        if int(num) < 0 or int(num) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
