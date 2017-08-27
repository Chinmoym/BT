#!/usr/bin/env python
#This program calibrates the BMP085 Barometric Pressure and Temperature sensor connected to CHIP-pro
#and gives the measured temperature and pressure. 

import Adafruit_GPIO.I2C as I2C
import time
import sys
debug = 0 

i2c                      = I2C
BLAZE_I2C_BUS            = 0x1
BMP085_SLAVE_ADDR        = 0x77	# Device address of BMP085


# Operating Modes
BMP085_ULTRALOWPOWER     = 0
BMP085_STANDARD          = 1
BMP085_HIGHRES           = 2
BMP085_ULTRAHIGHRES      = 3


# BMP085 Registers
BMP085_CAL_AC1           = 0xAA  # R   Calibration data (16 bits)
BMP085_CAL_AC2           = 0xAC  # R   Calibration data (16 bits)
BMP085_CAL_AC3           = 0xAE  # R   Calibration data (16 bits)
BMP085_CAL_AC4           = 0xB0  # R   Calibration data (16 bits)
BMP085_CAL_AC5           = 0xB2  # R   Calibration data (16 bits)

BMP085_CAL_AC6           = 0xB4  # R   Calibration data (16 bits)
BMP085_CAL_B1            = 0xB6  # R   Calibration data (16 bits)
BMP085_CAL_B2            = 0xB8  # R   Calibration data (16 bits)
BMP085_CAL_MB            = 0xBA  # R   Calibration data (16 bits)
BMP085_CAL_MC            = 0xBC  # R   Calibration data (16 bits)
BMP085_CAL_MD            = 0xBE  # R   Calibration data (16 bits)
BMP085_CONTROL           = 0xF4
BMP085_TEMPDATA          = 0xF6
BMP085_PRESSUREDATA      = 0xF6

# Commands
BMP085_READTEMPCMD       = 0x2E
BMP085_READPRESSURECMD   = 0x34

REPEATED_BYTE_COMMAND    = 0x80

class BMP085(object):
    def __init__(self, mode = BMP085_STANDARD, address=BMP085_SLAVE_ADDR, busnum=BLAZE_I2C_BUS, **kwargs):
         # Check that mode is valid.

	self._mode = mode
        # Create I2C device.
        self._device = i2c.get_i2c_device(address, **kwargs)
        # Load calibration values.
        self._load_calibration()

    def _load_calibration(self):
        self.cal_AC1 = self._device.readS16BE(BMP085_CAL_AC1)   # INT16
        self.cal_AC2 = self._device.readS16BE(BMP085_CAL_AC2)   # INT16
        self.cal_AC3 = self._device.readS16BE(BMP085_CAL_AC3)   # INT16
        self.cal_AC4 = self._device.readU16BE(BMP085_CAL_AC4)   # UINT16
        self.cal_AC5 = self._device.readU16BE(BMP085_CAL_AC5)   # UINT16
        self.cal_AC6 = self._device.readU16BE(BMP085_CAL_AC6)   # UINT16
        self.cal_B1 = self._device.readS16BE(BMP085_CAL_B1)     # INT16
        self.cal_B2 = self._device.readS16BE(BMP085_CAL_B2)     # INT16
        self.cal_MB = self._device.readS16BE(BMP085_CAL_MB)     # INT16
        self.cal_MC = self._device.readS16BE(BMP085_CAL_MC)     # INT16
        self.cal_MD = self._device.readS16BE(BMP085_CAL_MD)     # INT16
        
    def _load_datasheet_calibration(self):
        # Set calibration from values in the datasheet example.  Useful for debugging the
        # temp and pressure calculation accuracy.
        self.cal_AC1 = 408
        self.cal_AC2 = -72
        self.cal_AC3 = -14383
        self.cal_AC4 = 32741
        self.cal_AC5 = 32757
        self.cal_AC6 = 23153
        self.cal_B1 = 6190
        self.cal_B2 = 4
        self.cal_MB = -32767
        self.cal_MC = -8711
        self.cal_MD = 2868


    def read_raw_temp(self) :
        """reads raw temperature i.e. ADC values"""
        self._device.write8(BMP085_CONTROL, BMP085_READTEMPCMD)
        time.sleep(0.005)  # Wait 5ms
        raw = self._device.readU16BE(BMP085_TEMPDATA)
        return raw
    	
    def read_temperature(self):
        """Gets the compensated temperature in degrees celsius."""
        UT = self.read_raw_temp()
        # Datasheet value for debugging:
        # Calculations below are taken straight from section 3.5 of the datasheet.
        X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
        X2 = (self.cal_MC << 11) // (X1 + self.cal_MD)
        B5 = X1 + X2
        temp = ((B5 + 8) >> 4) / 10.0
        return temp

    def read_raw_pressure(self):
        """Reads the raw (uncompensated) pressure level from the sensor."""
        self._device.write8(BMP085_CONTROL, BMP085_READPRESSURECMD + (self._mode << 6))
        if self._mode == BMP085_ULTRALOWPOWER:
            time.sleep(0.005)
        elif self._mode == BMP085_HIGHRES:
            time.sleep(0.014)
        elif self._mode == BMP085_ULTRAHIGHRES:
            time.sleep(0.026)
        else:
            time.sleep(0.008)
        msb = self._device.readU8(BMP085_PRESSUREDATA)
        lsb = self._device.readU8(BMP085_PRESSUREDATA+1)
        xlsb = self._device.readU8(BMP085_PRESSUREDATA+2)
        raw = ((msb << 16) + (lsb << 8) + xlsb) >> (8 - self._mode)
        return raw

    def read_pressure(self):
        """Gets the compensated pressure in Pascals."""
        UT = self.read_raw_temp()
        UP = self.read_raw_pressure()
        # Datasheet values for debugging:
        # Calculations below are taken straight from section 3.5 of the datasheet.
        # Calculate true temperature coefficient B5.
        X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
        X2 = (self.cal_MC << 11) // (X1 + self.cal_MD)
        B5 = X1 + X2
        
        # Pressure Calculations
        B6 = B5 - 4000
        X1 = (self.cal_B2 * (B6 * B6) >> 12) >> 11
        X2 = (self.cal_AC2 * B6) >> 11
        X3 = X1 + X2
        B3 = (((self.cal_AC1 * 4 + X3) << self._mode) + 2) // 4
	X1 = (self.cal_AC3 * B6) >> 13
        X2 = (self.cal_B1 * ((B6 * B6) >> 12)) >> 16
        X3 = ((X1 + X2) + 2) >> 2
        B4 = (self.cal_AC4 * (X3 + 32768)) >> 15
        B7 = (UP - B3) * (50000 >> self._mode)
        if B7 < 0x80000000:
            p = (B7 * 2) // B4
        else:
            p = (B7 // B4) * 2
        X1 = (p >> 8) * (p >> 8)
        X1 = (X1 * 3038) >> 16
        X2 = (-7357 * p) >> 16
        p = p + ((X1 + X2 + 3791) >> 4)
        return p

    info = "['BMP085','[[\"0xF4\",\"CONTROL_REG\"],[\"0x2E\",\"READ_TEMPCMD\"],[\"0x34\",\"READ_PRESSURECMD\"],[\"0xF6\",\"UT_VALUE\"],[\"0xAA:0XBF\",\"E2_PROM\"]]']"
