import subprocess

prefix = """
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runners.MethodSorters;

@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class MyTest {

    public static boolean debug = false;

    @Test
    public void test4() throws Throwable {
      Account account1 = new Account((int) 'a');
"""

lines = [
    "boolean boolean3 = account1.Borrow((int) '#');",
    "boolean boolean5 = account1.Repay((int) '#');",
    "boolean boolean7 = account1.Borrow((int) (short) 10);",
    "java.lang.Class<?> wildcardClass8 = account1.getClass();",
    "boolean boolean10 = account1.Borrow((int) '4');",
    "boolean boolean12 = account1.Send(0);",
    "java.lang.Class<?> wildcardClass13 = account1.getClass();",
    "boolean boolean15 = account1.Receive(0);",
    "boolean boolean17 = account1.Borrow((int) '4');",
    "boolean boolean19 = account1.Borrow(1);",
    "boolean boolean21 = account1.Borrow(100);",
    "boolean boolean23 = account1.Borrow((int) (short) 100);",
]

suffix = "\n}}"


def compile(source):
  filename = 'MyTest'
  with open(filename + '.java', 'w') as f:
    f.write(source)

  try:
    subprocess.check_call(
        'javac -cp junit-4.13-beta-2.jar:hamcrest-core-1.3.jar:.:./target ' + filename + '.java', shell=True)

  except subprocess.CalledProcessError:
    return None

  return filename


def execute(target):
  result = subprocess.run(
      'java -cp junit-4.13-beta-2.jar:hamcrest-core-1.3.jar:.:./target org.junit.runner.JUnitCore ' + target, stdout=subprocess.PIPE, shell=True)

  output = str(result.stdout)

  if 'FAILURES!!!' in output:
    return 'fail'

  elif 'SUCCESS' in output:
    return 'success'

  else:
    return 'unknown'


def check_failure(input_lines):
  source = prefix + '\n'.join(input_lines) + suffix
  target = compile(source)

  if target:
    test_result = execute(target)
    if test_result == 'fail':
      return True

    return False


def DD(p, lines):
  length = len(lines)

  if length == 1:
    return lines

  l1 = lines[:length // 2]
  l2 = lines[length // 2:]
  p1 = p + l1
  p2 = p + l2

  if check_failure(p1):
    return DD(p, l1)

  elif check_failure(p2):
    return DD(p, l2)

  else:
    return DD(p2, l1) + DD(p1, l2)


def apply_delta_debugging(lines):
  return DD([], lines)


reduced_lines = apply_delta_debugging(lines)

source = prefix + '\n'.join(reduced_lines) + suffix
target = compile(source)

if target:
  test_result = execute(target)
  try:
    assert test_result == 'fail'

  except AssertionError:
    print('Failed to Generate Reduced Test Suite')
    exit(1)

print('Reduced Test Suite Generated: ' + target + '.java')
