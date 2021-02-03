# terminal-password-manager
A simple password manager for terminal.


## how to use
To add pwd-manager to the linux terminal, modify the .bash_aliases file in your home folder (if you don't have it, you'll need to create it) add the line:

    alias pwd-manager: 'python3 /path/to/the/passwd_manager.py'
and save the file.
now, to use pwd-manager, all you need to do is open a new terminal and type
    
    pwd-manager [parameter] 'name-to-the-site'
parameters:

    -p: return your password
    -u: return your user name
    -e: return your email address
    -n: to add a new account

### exemple

image you want your password from facebook. what you need to do is type:

    pwd-manager -p facebook
and your password will be on the clipboard.
