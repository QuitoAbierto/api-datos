
def colorize(text, color_code):
  return '{}{}\033[0m'.format(color_code, text)

def red(text):
  return colorize(text, "\033[31m")

def green(text):
  return colorize(text, "\033[92m")

def task_message(message):
  border = '=' * len(message)
  print(green(message))
  print(green(border))
