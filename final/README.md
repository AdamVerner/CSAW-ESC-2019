# Challenges

|set|number| name    | who | points |   hash  |
|---|------|---------|-----|--------|---------|
| A |  0   | lounge  |  H  |  100   | `643a6fa20b171fdf3a9e7e1975ce62892fde9cecf2056a73d85fa2d0802d3000` |
| A |  1   | closet  |  H  |  100   | `293f7b60b994512db99836ae7d5bab88b2d0089f90fcf6d51b95b374200dc20f` |
| A |  2   | cafe    |  H  |  130   | `d05235d380e913b5625d653c555de8925f249838896651a95bb35ea4e7863a5e` |
| A |  3   | stairs  | ORG |  50    | `396f4b1cdf1cc2e7680f2a8716a18c887cd489e12232e75b6810e9d5e91426c7` |
| B |  4   | mobile  |  H  |  100   | `f2f3792453040e837e7e1584e72859bfaa6b8c09d73d185be53b35886b6455c2` |
| B |  5   | dance   |  A  |  130   | `e631b32e3e493c51e5c2b22d1486d401c76ac83e3910566924bcc51b2157c837` |
| B |  6   | code    |  A  |  50    | `372ded6746e45ef7c8ad5a22c5738a4b5aa982da66bc8a426aa1cca830d05af3` |
| B |  7   | blue    |  H  |        |  `    sender does not work with this challenge :(                ` |
| C |  8   | uno     |  A  |  200   | `2e120f2237c71f18d29451c4787ac1df8285909618e2a821ee7c97d7efde246c` |
| C |  9   | game    |  A  |  150   | `a536829856d84ccd53ff8bcf534a65c5678bdbe9ce20f78407e1c987ba517e8a` |
| C |  10  | break   |  A  |  70    | `2d3448f09329f453e6f3a5403d89c061a9dabfbb9103ad6b8cc86d16345a7547` |
| C |  11  | recess  |  H  |  100   | `370815b8d8fde829f5c35f893d0b4139d61a775baa4181fcac1fffe014bde9ea` |
| D |  8   | bounce  |     |        |  return address overwrite |
| E |  12  | steel   |  A  |  100   | `5921d2ca353338c5f04c92205dc8f8bc8734f092a9e63e5f02ec106f7a7d99b4` |
| E |  13  | caeser  |  A  |  150   | `551b5cff372d310b57d39b616400461be0a1450c519a2a542f33a7af0dd565f3` |
| E |  14  | spiral  |  H  |  130   | `26ee8470c732dfc821bbe0561b446dc8086560e4e222b22e6a74e559d90a7d61` |
| E |  15  | tower   |     |        | sha256 bullshit |
| F |  17  | spire   |  AH |  150   | `f322344822257bb66542629db08bcea285411068963e30f0595847c79ef76f37` |


# sender.py

Modified utility to send challenge an


usage:
```
./sender.py ID hash
./sender.py ID send /dev/ttyACM0
```
