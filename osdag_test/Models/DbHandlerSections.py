import sqlite3

class DbHandler(object):
    """
    DB Handler for SQLITE3

    """
    def __init__(self):
        """
        Initialzes the object.

        """
        self.db_pth = "./steel_sections.sqlite"
        self.conn_obj =  sqlite3.connect(self.db_pth)
        self.cur_ptr =  self.conn_obj.cursor()
        self.cur_ptr.execute("SELECT * FROM Angles")
        self.angles_rcrds = self.cur_ptr.fetchall()
        self.cur_ptr.execute("SELECT * FROM Beams")
        self.beams_rcrds = self.cur_ptr.fetchall()
        self.cur_ptr.execute("SELECT * FROM Channels")
        self.channels_rcrds = self.cur_ptr.fetchall()
        self.conn_obj.commit()

    def get_angles_record(self):
        """
        This function will return the angles records.

        :returns: all record from Angles tables.
        :rtype: list
        :author: Mushir

        """
        return self.angles_rcrds
    
    def get_beams_record(self):
        """
        This function will return the beams records.

        :returns: all record from Beams tables.
        :rtype: list
        :author: Mushir

        """
        return self.beams_rcrds

    def get_channels_record(self):
        """
        This function will return the channels records.

        :returns: all record from Channels tables.
        :rtype: list
        :author: Mushir

        """
        return self.channels_rcrds


if __name__ == "__main__":

   db_obj = DbHandler()
   angles_rcrd = db_obj.get_angles_record()
   beams_rcrd = db_obj.get_beams_record()
   channls_rcrd = db_obj.get_channels_record()