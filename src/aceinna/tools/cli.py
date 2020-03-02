import sys
import argparse

try:
    from aceinna.bootstrap.cli import CommandLine
    from aceinna.framework.constants import BAUDRATE_LIST
except:  # pylint: disable=bare-except
    print('load package from local')
    sys.path.append('./src')
    from aceinna.bootstrap.cli import CommandLine
    from aceinna.framework.constants import BAUDRATE_LIST


def receive_args():
    """parse input arguments
    """
    parser = argparse.ArgumentParser(
        description='Aceinna python driver input args command:')
    # parser.add_argument("-host", type=str, help="host type", default='web')
    # for host as web
    parser.add_argument("-p", "--port", type=int,
                        help="Webserver port")
    parser.add_argument("--device-type", type=str,
                        help="Open Device Type")
    parser.add_argument("-b", "--baudrate", type=int,
                        help="Baudrate for uart", choices=BAUDRATE_LIST)
    parser.add_argument("-c", "--com-port", type=str,
                        help="COM Port")
    parser.add_argument("--debug", type=bool,
                        help="Log debug information", default=False)
    parser.add_argument("--with-data-log", type=int,
                        help="Contains internal data log (OpenIMU only)", default=False)
    parser.add_argument("--with-raw-log", type=bool,
                        help="Contains raw data log (OpenRTK only)", default=False)
    return parser.parse_args()


def main():
    '''start'''
    input_args = receive_args()
    command_line = CommandLine(
        device_type=input_args.device_type,
        com_port=input_args.com_port,
        port=input_args.port,
        baudrate=input_args.baudrate,
        debug=input_args.debug,
        with_data_log=input_args.with_data_log
    )
    command_line.listen()


if __name__ == '__main__':
    main()
