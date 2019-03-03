## Acquried from: https://gist.github.com/jasdumas/53b0cbfbb8af3e435dafb833357fd67f

try:
    from html import escape
except ImportError:
    from cgi import escape
import os
from string import Template
import sys
import platform
import socket
from datetime import datetime


output_template = Template('''<!DOCTYPE html>
<html>
<head>
    <title>pyinfo()</title>
    <meta name="robots" content="noindex,nofollow,noarchive,nosnippet">
    <style>
        body{width: 700px; margin: 10px auto; font:12px sans-serif;}
        table{border-collapse:collapse; width:100%;}
        td,th{border:1px solid #999999; padding: 3px}
        .e{width:35%;background-color:#ffffcc;font-weight:bold;color:#000}
        .h{background:url('http://python.org/images/header-bg2.png') repeat-x;}
        .v{background:#f2f2f2;}
        img{float:right;border:0;}
    </style>
    </head>
<body>
    <table><tr class="h"><td>
        <img src="http://python.org/images/python-logo.gif">
        <h1 class="p">Python $py_version</h1>
    </td></tr></table>
    $output
</body>
</html>
''')


def make_table(title, data):
    return '<h2>{}</h2><table>{}</table><br>'.format(title, ''.join(
        '<tr><td class="e">{}</td><td class="v">{}</td></tr>'.format(*row) for row in data
    ))


def pyinfo(data=None, allow_import=True, template=output_template, make_table_fn=make_table):
    """
    @param data: None or a list of additional (key, values) to include in report,
        like [('Application version', '2.1')]
    @param allow_import: allow importing (many) new modules or not, defaults to True
    @return: complete rendered html
    """
    _process_out = lambda out: '' if not out else make_table_fn(*out)
    output = ''
    output += _process_out(section_server_info(data))
    output += _process_out(section_system())
    output += _process_out(section_py_internals())
    output += _process_out(section_os_internals())
    output += _process_out(section_environ())
    if allow_import:
        output += _process_out(section_compression())
    output += _process_out(section_ldap(allow_import))
    output += _process_out(section_socket())
    if allow_import:
        output += _process_out(section_multimedia())
    output += _process_out(section_packages())

    if template is None:
        return output
    return template.substitute(output=output, py_version=platform.python_version())


def imported(module):
    """ returns 'enabled' if a module is imported, '-' if it isn't"""
    try:
        if module not in sys.modules:
            __import__(module)
        return 'enabled'
    except:
        return '-'


def section_system():
    data = []
    if hasattr(sys, 'subversion'):
        data.append(('Python Subversion', ', '.join(x for x in sys.subversion if x)))
    if platform.dist()[0] != '' and platform.dist()[1] != '':
        data.append(('OS Version', '%s %s (%s %s)' % (
                    platform.system(), platform.release(), platform.dist()[0].capitalize(), platform.dist()[1])))
    else:
        data.append(('OS Version', '%s %s' % (platform.system(), platform.release())))
    if hasattr(sys, 'executable'):
        data.append(('Executable', sys.executable))
    data.append(('Build Date', platform.python_build()[1]))
    data.append(('Compiler', platform.python_compiler()))
    if hasattr(sys, 'api_version'):
        data.append(('Python API', sys.api_version))
    return 'System', data


def section_server_info(data):
    data = list(data) if data else []
    data.append(('Hostname', socket.gethostname()))
    try:
        data.append(('IP Address', socket.gethostbyname(socket.gethostname())))
    except:
        pass
    data.append(('Local time', str(datetime.now())))
    data.append(('UTC time', str(datetime.utcnow())))
    return 'Server Info', data


def section_py_internals():
    data = []
    if hasattr(sys, 'builtin_module_names'):
        data.append(('Built-in Modules', ', '.join(sys.builtin_module_names)))
    data.append(('Byte Order', sys.byteorder + ' endian'))
    if hasattr(sys, 'getcheckinterval'):
        data.append(('Check Interval', sys.getcheckinterval()))
    if hasattr(sys, 'getfilesystemencoding'):
        data.append(('File System Encoding', sys.getfilesystemencoding()))
    data.append(('Maximum Integer Size', str(sys.maxsize) + ' (%s)' % str(hex(sys.maxsize)).upper().replace("X", "x")))
    if hasattr(sys, 'getrecursionlimit'):
        data.append(('Maximum Recursion Depth', sys.getrecursionlimit()))
    if hasattr(sys, 'tracebacklimit'):
        data.append(('Maximum Traceback Limit', sys.tracebacklimit))
    else:
        data.append(('Maximum Traceback Limit', '1000'))
    data.append(('Maximum Unicode Code Point', sys.maxunicode))
    return 'Python Internals', data


def section_os_internals():
    data = []
    if hasattr(os, 'getcwd'):
        data.append(('Current Working Directory', os.getcwd()))
    if hasattr(os, 'getegid'):
        data.append(('Effective Group ID', os.getegid()))
    if hasattr(os, 'geteuid'):
        data.append(('Effective User ID', os.geteuid()))
    if hasattr(os, 'getgid'):
        data.append(('Group ID', os.getgid()))
    if hasattr(os, 'getgroups'):
        data.append(('Group Membership', ', '.join(map(str, os.getgroups()))))
    if hasattr(os, 'linesep'):
        data.append(('Line Seperator', repr(os.linesep)[1:-1]))
    if hasattr(os, 'getloadavg'):
        data.append(('Load Average', ', '.join(str(round(x, 2)) for x in os.getloadavg())))
    if hasattr(os, 'pathsep'):
        data.append(('Path Seperator', os.pathsep))
    try:
        if hasattr(os, 'getpid') and hasattr(os, 'getppid'):
            data.append(('Process ID', ('%s (parent: %s)' % (os.getpid(), os.getppid()))))
    except:
        pass
    if hasattr(os, 'getuid'):
        data.append(('User ID', os.getuid()))
    return 'OS Internals', data


def section_environ():
    envvars = list(os.environ.keys())
    envvars.sort()
    data = []
    for envvar in envvars:
        data.append((envvar, escape(str(os.environ[envvar]))))
    return 'Environment', data


def section_compression():
    return ('Compression and archiving', [
        ('SQLite3', imported('sqlite3')),
        ('Bzip2 Support', imported('bz2')),
        ('Gzip Support', imported('gzip')),
        ('Tar Support', imported('tarfile')),
        ('Zip Support', imported('zipfile')),
        ('Zlib Support', imported('zlib'))
    ])


def section_ldap(allow_import):
    try:
        if allow_import:
            import ldap
        else:
            ldap = sys.modules['ldap']
    except (KeyError, ImportError):
        return ''
    return ('LDAP support', [
        ('Python-LDAP Version', ldap.__version__),
        ('API Version', ldap.API_VERSION),
        ('Default Protocol Version', ldap.VERSION),
        ('Minimum Protocol Version', ldap.VERSION_MIN),
        ('Maximum Protocol Version', ldap.VERSION_MAX),
        ('SASL Support (Cyrus-SASL)', ldap.SASL_AVAIL),
        ('TLS Support (OpenSSL)', ldap.TLS_AVAIL),
        ('Vendor Version', ldap.VENDOR_VERSION)
    ])


def section_socket():
    return ('Socket', [
        ('Hostname (fqdn)', socket.gethostbyaddr(socket.gethostname())[0]),
        ('IPv6 Support', getattr(socket, 'has_ipv6', False)),
        ('SSL Support', hasattr(socket, 'ssl')),
    ])


def section_multimedia():
    return ('Multimedia support', [
        ('AIFF Support', imported('aifc')),
        ('Color System Conversion', imported('colorsys')),
        ('curses Support', imported('curses')),
        ('IFF Chunk Support', imported('chunk')),
        ('Image Header Support', imported('imghdr')),
        ('OSS Audio Device Support', imported('ossaudiodev')),
        ('Raw Audio Support', imported('audioop')),
        ('SGI RGB Support', imported('rgbimg')),
        ('Sound Header Support', imported('sndhdr')),
        ('Sun Audio Device Support', imported('sunaudiodev')),
        ('Sun AU Support', imported('sunau')), ('Wave Support', imported('wave'))])


def section_packages():
    data = []
    try:
        import pkg_resources
    except:
        return ''
    for pkg in pkg_resources.working_set:
        assert isinstance(pkg, pkg_resources.Distribution)
        data.append((pkg.project_name, pkg.version if pkg.has_version() else '[uknown]'))
    return 'Installed Modules (Site Packages)', sorted(data, key=lambda a: a[0].lower())


if __name__ == '__main__':
    def _text_table(title, data):
        return '===== {}\n{}\n\n'.format(title, '\n'.join(
            '{:30} {}'.format(*row) for row in data
        ))
    print(pyinfo(template=None, make_table_fn=_text_table))
