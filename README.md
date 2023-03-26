# opensips-docker

使用版本opensips 3.3

以 debian/bullseye docker 架設在 ubuntu18 的 vm上

## Building the image
```
OPENSIPS_EXTRA_MODULES=opensips-mysql-module make build
```

## Running the container

make start

## settings

須將vm 網路設定為 bridged ， 並勾選 replicate physical network


![plot](./images/vm.jpg)



輸入


    ip a 

查看vm ip 將其填入 advertised_address

```
socket=udp:<docker_ip>:5060   # CUSTOMIZE ME
#socket ip 已由 run.sh 腳本自動設置

advertised_address="<vm_ip 192.168.....>"
```


重啟opensips



    service opensips restart

開啟mysql

    service mariadb start

建立opensips資料庫
    
    opensips-cli -x database create
    #Password for admin MySQL user (root): 無密碼直接enter


建立opensips用戶

    opensips-cli -x user add 7414 7414
    #Please provide the domain of the user: 輸入vm ip





---

wsl  無法使用 似乎還需要NAT traverse


