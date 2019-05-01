#
# PySNMP MIB module ADTRAN-ATLAS-550-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADTRAN-ATLAS-550-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:14:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, Counter64, Counter32, ObjectIdentity, MibIdentifier, NotificationType, Unsigned32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ModuleIdentity, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Counter64", "Counter32", "ObjectIdentity", "MibIdentifier", "NotificationType", "Unsigned32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ModuleIdentity", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adtran = MibIdentifier((1, 3, 6, 1, 4, 1, 664))
adMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2))
adATLAS550mg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219))
adATLAS550Fpnl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219, 1))
adATLAS550FpnlSysLeds = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1))
adATLAS550FpnlPow = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("syson", 1), ("sysoff", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlPow.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlPow.setDescription('This variable indicates if the unit is powererd on or off. The various Power LED states are: Number State Status 1 ON GREEN 2 OFF OFF')
adATLAS550FpnlSys = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("sysok", 1), ("syserr", 2), ("syswarn", 3), ("sysflashupdate", 4), ("sysflasherror", 5), ("sysoff", 6), ("greenslow", 7), ("yellowslow", 8), ("yellowfast", 9), ("redslow", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlSys.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlSys.setDescription('This variable indicates the status of the System LED. When the System LED changes state, this variable also changes state. The various system LED states are: Number State Status 1 OK Green 2 Error Red 3 Warning Yellow 4 Flash Update Green Fast 5 Flash Error Red Fast 6 Off Off 7 Green Slow Green Slow -- Currently not used, but possible in future 8 Yellow Slow Yellow Slow 9 Yellow Fast Yellow Fast 10 Red Slow Red Slow')
adATLAS550FpnlEth = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("etheron", 1), ("etheroff", 2), ("etherflashslow", 3), ("etherflashfast", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlEth.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlEth.setDescription('This variable indicates if the ethernet module is active. If the unit is not recieving data through a valid ethernet connection, the LED is on. If data is being recieved the LED will occasionally flash. If no ethernet connection is established the LED is off. The various Ethernet LED states are: Number State Status 1 ON GREEN 2 OFF OFF 3 Data is passing Green Slow 3 Green Fast Green Fast')
adATLAS550FpnlRem = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("remon", 1), ("remoff", 2), ("remflashslow", 3), ("remflashfast", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlRem.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlRem.setDescription('This variable indicates if someone is connected to the Atlas 550 using a telnet session. The various Remote LED states are: Number State Status 1 ON YELLOW 2 OFF OFF 3 Flash Slow Yellow Slow 4 Flash Fast Yellow Fast')
adATLAS550FpnlNtwkLeds = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2))
adATLAS550FpnlNwTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1), )
if mibBuilder.loadTexts: adATLAS550FpnlNwTable.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlNwTable.setDescription('The Network LED table.')
adATLAS550FpnlNwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1), ).setIndexNames((0, "ADTRAN-ATLAS-550-MIB", "adATLAS550FpnlNwIndex"))
if mibBuilder.loadTexts: adATLAS550FpnlNwEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlNwEntry.setDescription('An entry in the Network Led table.')
adATLAS550FpnlNwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlNwIndex.setDescription('This variable indicates which network slots are active on the ATLAS 550.')
adATLAS550FpnlNwOK = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nwokon", 1), ("nwokflashslow", 2), ("nwokflashfast", 3), ("nwokoff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwOK.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlNwOK.setDescription('This variable indicates the status of the network inteface. The choices for this variable are Number State Status 1 OK Green 2 Flash slow Flash Green Slow 3 Flash Fast Flash green fast 4 OFF OFF')
adATLAS550FpnlNwTest = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("teston", 1), ("testflashslow", 2), ("testflashfast", 3), ("testoff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwTest.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlNwTest.setDescription('This variable indicates if a loopback, test pattern, or self-test is running on the network inteface. The choices for this variable are Number State Status 1 ON Yellow 2 Flash SLOW Flash yellow slow 3 Flash Fast Flash yellow fast 4 OFF OFF')
adATLAS550FpnlNwError = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("erroron", 1), ("errorflashslow", 2), ("errorflashfast", 3), ("erroroff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwError.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlNwError.setDescription('This variable indicates an alarm condition has been detected on the network inteface. The choices for this variable are Number State Status 1 Error Red 2 Flash Slow Flash Red Slow 3 Flash Fast Flash Red Fast 3 No error OFF')
adATLAS550FpnlNwAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("alarmon", 1), ("alarmflashslow", 2), ("alarmflashfast", 3), ("alarmoff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlNwAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlNwAlarm.setDescription('This variable indicates an alarm condition has been detected on the network inteface. The choices for this variable are Number State Status 1 Alarm RED 2 Flash Slow Flash Red Slow 3 Flash Fast Flash Red Fast 4 no Alarms OFF')
adATLAS550FpnlModLeds = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3))
adATLAS550FpnlModNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlModNumber.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlModNumber.setDescription('This variable indicates the number of module slots that are located on the Atlas Product.')
adATLAS550FpnlMLTable = MibTable((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2), )
if mibBuilder.loadTexts: adATLAS550FpnlMLTable.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlMLTable.setDescription('The Module LED Table.')
adATLAS550FpnlMLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1), ).setIndexNames((0, "ADTRAN-ATLAS-550-MIB", "adATLAS550FpnlMLIndex"))
if mibBuilder.loadTexts: adATLAS550FpnlMLEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlMLEntry.setDescription('An entry in the Module LED Table.')
adATLAS550FpnlMLIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlMLIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlMLIndex.setDescription('This variable indicates the available slots.')
adATLAS550FpnlMLStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("mlstatusok", 1), ("mlstatuswarn", 2), ("mlstatuserr", 3), ("mlstatusflashslowgreen", 4), ("mlstatusflashfastgreen", 5), ("mlstatusflashslowyellow", 6), ("mlstatusflashfastyellow", 7), ("mlstatusflashslowred", 8), ("mlstatusflashfastred", 9), ("mlstatusoff", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlMLStatus.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlMLStatus.setDescription('This variable indicates the status of the card located in the slot determined by the MLIndex variable. The choices for this variable are Number State Status 1 OK Green 2 Warn Yellow 3 Error Red 4 One module is offline or invalid flash Flash Slow Green 5 Both modules are offline or invalid flah Flash Fast Green 6 Flash Slow Yellow Flash Slow Yellow 7 Flash Fast Yellow Flash Fast Yellow 8 One module is not ready Flash Slow Red 9 One module has not response Flash Fast Red 10 Off Off')
adATLAS550FpnlMLOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("mlonlineon", 1), ("mlonlineflashslow", 2), ("mlonlineflashfast", 3), ("mlonlineoff", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlMLOnline.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlMLOnline.setDescription('This variable indicates whether the card located in the slot determined by the MLIndex is online or offline. The choices for this variable are Number State Status 1 Online Green 2 Invalid flash memory Flashing Slow Green 3 only one module has active connection Flashing fast Green 4 Offline Off')
adATLAS550FpnlMLTest = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 2, 219, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mlteston", 1), ("mltestflash", 2), ("mltestoff", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adATLAS550FpnlMLTest.setStatus('mandatory')
if mibBuilder.loadTexts: adATLAS550FpnlMLTest.setDescription('This variable indicates whether the card located in the slot determined by the MLIndex is in a test mode or not. The choices for this variable are Number State Status 1 Test in Progress Yellow 2 Flashing Flashing Yellow 3 Off Off')
adATLAS550ExtAlarmActive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 219) + (0,21900))
if mibBuilder.loadTexts: adATLAS550ExtAlarmActive.setDescription('This trap indicates that an external alarm has been activated via the short circuiting of pins on the RELAY MON connector located on the rear panel of the Atlas 550.')
adATLAS550ExtAlarmInactive = NotificationType((1, 3, 6, 1, 4, 1, 664, 2, 219) + (0,21901))
if mibBuilder.loadTexts: adATLAS550ExtAlarmInactive.setDescription('This trap indicates that an external alarm has been deactivated via the open circuiting of pins on the RELAY MON connector located on the rear panel of the Atlas 550.')
mibBuilder.exportSymbols("ADTRAN-ATLAS-550-MIB", adATLAS550FpnlPow=adATLAS550FpnlPow, adATLAS550FpnlModNumber=adATLAS550FpnlModNumber, adATLAS550Fpnl=adATLAS550Fpnl, adATLAS550ExtAlarmInactive=adATLAS550ExtAlarmInactive, adMgmt=adMgmt, adATLAS550FpnlNtwkLeds=adATLAS550FpnlNtwkLeds, adATLAS550FpnlSys=adATLAS550FpnlSys, adATLAS550FpnlNwEntry=adATLAS550FpnlNwEntry, adATLAS550FpnlNwIndex=adATLAS550FpnlNwIndex, adATLAS550FpnlNwTable=adATLAS550FpnlNwTable, adATLAS550mg=adATLAS550mg, adATLAS550FpnlMLIndex=adATLAS550FpnlMLIndex, adATLAS550FpnlSysLeds=adATLAS550FpnlSysLeds, adATLAS550FpnlRem=adATLAS550FpnlRem, adATLAS550FpnlMLEntry=adATLAS550FpnlMLEntry, adATLAS550FpnlMLOnline=adATLAS550FpnlMLOnline, adATLAS550FpnlEth=adATLAS550FpnlEth, adATLAS550ExtAlarmActive=adATLAS550ExtAlarmActive, adATLAS550FpnlNwOK=adATLAS550FpnlNwOK, adtran=adtran, adATLAS550FpnlNwTest=adATLAS550FpnlNwTest, adATLAS550FpnlModLeds=adATLAS550FpnlModLeds, adATLAS550FpnlMLTest=adATLAS550FpnlMLTest, adATLAS550FpnlMLTable=adATLAS550FpnlMLTable, adATLAS550FpnlMLStatus=adATLAS550FpnlMLStatus, adATLAS550FpnlNwAlarm=adATLAS550FpnlNwAlarm, adATLAS550FpnlNwError=adATLAS550FpnlNwError)