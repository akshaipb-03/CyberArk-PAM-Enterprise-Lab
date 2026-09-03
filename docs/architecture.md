                         SecureCorp PAM Lab

                         PAM User
                            |
                            v
                    +----------------+
                    | CyberArk Portal |
                    |     (PVWA)      |
                    +----------------+
                       |          |
                       v          v
                +----------+  +----------+
                |   CPM    |  |   PSM    |
                | Password |  | Session  |
                | Rotation |  | Recording|
                +----+-----+  +----+-----+
                     |             |
                     +------+------+
                            |
                            v
                  +-------------------+
                  |  CyberArk Vault   |
                  +-------------------+
                     |            |
                     v            v
             UNIX-ADMIN-SAFE   WIN-ADMIN-SAFE
                  |                 |
                  v                 v
             pamadmin           winadmin
                  |                 |
                  v                 v
             LINUX-SRV01        WIN-SRV01

