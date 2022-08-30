(ui-testing)=

# UI testing

Provides the [IceWM](http://www.icewm.org/) window manager, the [TightVNC](http://tightvnc.com/) remote desktop software,  and the [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/products/) browser. This allows you to
e.g. set up UI testing using [Selenium](http://docs.seleniumhq.org/).

## Components

- [x11-wm/icewm](https://packages.gentoo.org/package/x11-wm/icewm)
- [net-misc/tightvnc](https://packages.gentoo.org/package/net-misc/tightvnc)
- [www-client/firefox-bin](https://packages.gentoo.org/package/www-client/firefox-bin)

## Default setup

We only install the software packages but do not change their default
configuration.

## Configuration

All tools can be configured individually with dotfiles in the user’s home
directory.

If you need help with the configuration concepts and syntax, please consult the
respective tool's online documentation:

- [Mozilla Firefox online help](https://support.mozilla.org/en-US/products/firefox)
- [IceWM online manual](http://www.icewm.org/manual/)
- [TightVNC online documentation](http://www.tightvnc.com/docs.php)

## Interaction

Interaction with the tools highly depends on your use case. To give you an idea
of how the tools can be used, here is an example how to start Mozilla Firefox
and access it remotely via VNC:

First, we configure VNC (only has to be done once):

```shell-session
# Create a configuration directory in your home
abittner@test04 ~ $ mkdir ~/.vnc

# Set a password for VNC remote access:
abittner@test04 ~ $ vncpasswd
Using password file /home/abittner/.vnc/passwd
Password:
Verify:
Would you like to enter a view-only password (y/n)? y
Password:
Verify:
```

Now we can start the VNC server:

```shell-session
abittner@test04 ~ $ vncserver -geometry 1024x768 -localhost :1

New 'X' desktop is test04:1

Starting applications specified in /home/abittner/.vnc/xstartup
Log file is /home/abittner/.vnc/test04:1.log
```

This starts a VNC server on Display :1 (TCP 5901) using a screen resolution of
1024x768. Further, we only want to listen on localhost for security reasons. We
will later use SSH port forwarding to connect to the remote desktop.

:::{warning}
We strongly recommend using the {command}`-localhost` option when starting
VNC. There are a lot of known security issues in VNC and you should not make
it accessible to the outside world.
:::

Now that VNC is running, we can start Mozilla Firefox:

```shell-session
abittner@test04 ~$ DISPLAY=:1 firefox-bin
```

On our client machine, we initiate a SSH connection that tunnels the VNC port:

```shell-session
abittner@zapp ~$ ssh -L 5901:localhost:5901 test04.gocept.net
```

We can now use any remote desktop software that support VNC to view our Firefox.
To do so, connect to {command}`localhost:1` or {command}`localhost:5901`,
respectively.
