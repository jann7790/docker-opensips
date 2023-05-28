# opensips and http interface 

使用版本opensips 3.3

架設在 ubuntu18 vm 的 docker上





## settings

須將vm 網路設定為 bridged ，否則區域網路內的裝置無法連接sips， 並勾選 replicate physical network
(使用此網路設定若vm太久沒用不知為何導致 -> a start job is running for wait for network.........)


使用HOST-only 無法連接dns


目前使用NAT 測試用

![plot](./images/vm.jpg)






## Build and run the image

  make




