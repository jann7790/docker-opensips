# opensips-docker

使用版本opensips 3.3

以 debian/bullseye docker 架設在 ubuntu18 的 vm上



## settings

須將vm 網路設定為 bridged ，否則區域網路內的裝置無法連接sips， 並勾選 replicate physical network
(使用此網路設定若vm太久沒用導致 -> a start job is running for wait for network.........)

![plot](./images/vm.jpg)





## Building the image
```
make build
```

## Running the container

    make start
    
## init database

    ip route get 8.8.8.8 | head -n +1 | tr -s " " | cut -d " " -f 7
    
先確認ip創建sip帳號時須使用此ip，執行後須輸入db密碼預設無密碼直接enter即可
    
    make init_database
    
defaul user for sip: 1000
password for user 1000: 123456
    
    
## attach container to debug or whatever
    make attach

## kill and remove container

    make kill








---


## 新版已將以下步驟併入makefile
輸入


    ip a 

查看vm ip 將其填入 advertised_address

```
socket=udp:<docker_ip>:5060   
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

    opensips-cli -x user add 1000 123456
    #Please provide the domain of the user: 輸入vm ip





---

wsl  無法使用 似乎還需要NAT traverse


