* create scripts to read data from
    * Apple Health (through [QS Access](ahttps://itunes.apple.com/gb/app/qs-access/id920297614)?)
    * schema:Conversation, schema:Message:
        * ***anonymize!***
        * Facebook dumps, esp. messages
        * iMessage/SMS: binary plist .ichat-files and sql-database: <https://github.com/PeterKaminski09/baskup> or shell:

        ```bash
        sqlite3 /Users/(username)/Library/Messages/chat.db
        ```

        * WhatsApp
        * (subtype schema:EmailMessage:) e-mail? emlx from OS X Mail is not cool perhaps <http://mike.laiosa.org/2009/03/01/emlx.html>
    * …
