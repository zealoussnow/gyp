{
  'targets': [
    {
      'name': 'libevent',  # Maybe this should be called "event" so that it
                           # outputs libevent.a.
      'type': 'static_library',
      'sources': [
        'buffer.c',
        'evbuffer.c',
        'evdns.c',
        'event.c',
        'event_tagging.c',
        'evrpc.c',
        'evutil.c',
        'http.c',
        'log.c',
        'poll.c',
        'select.c',
        'signal.c',
        'strlcpy.c',
      ],
      'defines': [
        'HAVE_CONFIG_H',
      ],
      'include_dirs': [
        '.',   # libevent includes some of its own headers with #include <...>
               # instead of #include "..."
      ],
      'conditions': [
        # libevent has platform-specific implementation files.  Since its
        # native build uses autoconf, platform-specific config.h files are
        # provided and live in platform-specific directories.
        [ 'OS == "linux"', { 'sources': [ 'epoll.c', 'epoll_sub.c' ],
                             'include_dirs': [ 'linux' ] } ],
        [ 'OS == "mac"',   { 'sources': [ 'kqueue.c' ],
                             'include_dirs': [ 'mac' ] } ],
      ],
    },
  ],
}
