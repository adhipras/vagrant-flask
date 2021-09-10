# Vagrant + Flask

A [Flask](https://flask.palletsprojects.com/) app running in a [Vagrant VM](https://www.vagrantup.com/). I choose [Ansible](https://www.ansible.com/) as [Vagrant provisioner](https://www.vagrantup.com/docs/provisioning/) to install and configure everything.

## Usage

1. Start up the VM.
```sh
$ vagrant up
```

2. Once the VM is all set, execute the `curl` command.
```sh
$ curl http://10.10.10.20
```

3. The output should be similar to this:
```json
{
    "headers":
    {
        "Accept": "*/*",
        "Connection": "close",
        "Host": "0.0.0.0:5000",
        "User-Agent": "curl/7.54.0",
        "X-Forwarded-For": "10.10.10.1",
        "X-Real-Ip": "10.10.10.1"
    },
    "origin": "10.10.10.1"
}
```
