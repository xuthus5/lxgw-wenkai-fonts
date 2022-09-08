# lxgw-wenkai-fonts

> An open-source Chinese font derived from Fontworks' Klee One. 一款开源中文字体，基于 FONTWORKS 出品字体 Klee One 衍生。

> this repository store [ **LXGW WenKai / 霞鹜文楷** ] font rpm package metadata.

origin repo: [LXGW WenKai / 霞鹜文楷](https://github.com/lxgw/LxgwWenKai)

## install

fedora36+/centos8+:

```bash
dnf copr enable xuthus5/lxgw-wenkai-fonts
sudo dnf install lxgw-wenkai-fonts
```

other yum/dnf package system, such as centos7:

find rpm package from **Builds>Build ID>Result>os-release>lxgx-wenkai-fonts-$version.$release.noarch.rpm**

```bash
sudo rpm -ivh https://download.copr.fedorainfracloud.org/results/xuthus5/lxgw-wenkai-fonts/epel-7-x86_64/04816025-lxgw-wenkai-fonts/lxgw-wenkai-fonts-1.240-1.el7.noarch.rpm
```
