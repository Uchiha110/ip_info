import sqlite3


def write_person_db_func(response):
    with sqlite3.connect("person_db.db") as con:
        cur = con.cursor()

        cur.execute(
            "INSERT OR IGNORE INTO `persons` (`query`, `status`, `continent`, `continentCode`, `country`, `countryCode`, `region`, `regionName`, `city`, `district`, `zip`, `lat`, `lon`, `timezone`, `offset`, `currency`, `isp`, `org`, `as`, `asname`, `mobile`, `proxy`, `hosting`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                response.get('query'),
                response.get('status'),
                response.get('continent'),
                response.get('continentCode'),
                response.get('country'),
                response.get('countryCode'),
                response.get('region'),
                response.get('regionName'),
                response.get('city'),
                response.get('district'),
                response.get('zip'),
                response.get('lat'),
                response.get('lon'),
                response.get('timezone'),
                response.get('offset'),
                response.get('currency'),
                response.get('isp'),
                response.get('org'),
                response.get('as'),
                response.get('asname'),
                response.get('mobile'),
                response.get('proxy'),
                response.get('hosting')
            ))
        con.commit()

    print("Record saved successfully!")
