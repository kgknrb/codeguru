#guru:v1:internal:pythonbestpractices:inline_negation_rule:1.0
def inline_negation_rule():
    if not a is b:
        print(a)
#guru:v1:internal:pythonbestpractices:exit_class_method_re_raise_exception:1.0
class Exit_class_method_re_raise_exception:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        a = 1
        b = 2
        raise
#pythonbestpractices:prefer_secrets_for_prng_for_cryptography_rule
def prefer_secrets_for_prng_for_cryptography_rule():
    # hashlib.md5.update
    # random.choice
    import random
    import hashlib
    complex_str = "abcdefghijklmnopqrstuvwkyz123456789!@#$%^&*()"
    salt = random.choice(complex_str).encode()
    hash_str = hashlib.md5()
    hash_str.update(salt)

#pythonbestpractices:cache_result_isenabledfor:1.0
def cache_result_isenabledfor(data_fetcher: DataFetcher, transformer: Transformer, exporter: DataExporter):
    import logging
    logger = logging.getLogger('adr')
    """ executes the job here in the form of fetch, transform and export steps"""
    # fetch
    fetch_df = data_fetcher.fetch()
    arr = [1, 2, 3, 4, 5]
    for i in arr:
        if logger.isEnabledFor(logging.DEBUG):
            print(i)
            logger.debug(f"total number of customer snapshots data that is fetched {fetch_df.count()}")
#pythonbestpractices:efficient_concatenation_of_immutable_objects_rule:1.0
def efficient_concatenation_of_immutable_objects_rule():
    mylist = ['first', 'second', 'third', 'other']
    result = ''
    for item in mylist:
        result += item + "\n"
    return result
#

#pythonbestpractices:avoid_terminating_processes_rule:1.0
def avoid_terminating_processes_rule():
    from multiprocessing import Process, Queue
    queue = Queue()
    """
    Spawn _invoke() as a thread, wait for finish, kill if it doesn't.  If
    process successfully exits, return namedtuple of output and status.
    """
    process = Process(target=invoke, args=(queue,))
    process.start()
    # Wait until timeout value for process to return.
    process.join(timeout)
    if process.is_alive():
        # We timed out, the process is still going.  Kill it.
        process.terminate()
        raise CommandTimedOutException("Command Timeout: {}".format(command))
    return queue.get()

def unnecessary_iteration_rule():
    items = set([1, 3, 5, 7 , 9])
    for i in items:
        # used for loop to access single item from list
        if i == 5:
            print("found item")

#pythonbestpractices:NAIVE_DATETIME_METHODS:1.0
def naive_date_time_methods():
    from datetime import datetime
    return datetime.now(tz=None)

def dateTime_methods_for_local_clocks():
    import time
    now = time.time()
    local_time = time.localtime(now)

def use_list_comprehension_instead_of_simple_for_loop_nonconformant1():
    squares = []
    for k in range(10):
        squares.append(k*2)

def hashlib_naive_hashing_not_suitable_for_passwd_non_conformant_case1():
    import hashlib
    return "md5" + hashlib.md5((password + username).encode('UTF-8')).hexdigest()


def do_not_unpack_multiple_values_in_return_rule():
    print("Testing NC case")
    return 'a', 'abc', 100, [0, 1, 2]

def ssl_best_defaults_and_certificate_validation_rule():
    import socket, ssl
    HOST, PORT = 'example.com', 443
    sock = socket.socket(socket.AF_INET)
    context = ssl.SSLContext()
    conn = context.wrap_socket(sock, server_hostname=HOST)
    try:
        conn.connect((HOST, PORT))
        handle(conn)
    finally:
        conn.close()

def avoid_complex_comprehension_non_compliant_1():
    text = [['bar','foo','fooba'],['Rome','Madrid','Houston'], ['aa','bb','cc','dd']]
    text_3 = [y.upper() for x in text if len(x) == 3 for y in x if y.startswith('f')]

def socket_close_rule():
    import socket
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 9000))
    s.listen(5)
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send(b'Thank you for connecting')
        c.close()

def redundant_Get_Method_Call():
    dict = {"A":1, "B":2}
    val = dict.get("C", None)
    return val

def dict_Get_Default_Value():
    car = {
        "brand": "bmw",
        "model": "X5",
        "year": "2021"
    }
    x = car.get("model")
    return x
