#
# PySNMP MIB module DAMOCLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DAMOCLES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, Integer32, MibIdentifier, IpAddress, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, ModuleIdentity, ObjectIdentity, NotificationType, NotificationType, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Integer32", "MibIdentifier", "IpAddress", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "NotificationType", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class OnOff(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("off", 1), ("on", 2))

class OutputType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("onOff", 0), ("rts", 1), ("dtr", 2))

class UnitType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("celsius", 0), ("fahrenheit", 1), ("kelvin", 2), ("percent", 3), ("volt", 4), ("miliamper", 5), ("nounit", 6), ("pulse", 7), ("switch", 8))

class InputAlarmSetup(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("inactive", 0), ("activeOff", 1), ("activeOn", 2))

class InputAlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("alarm", 2))

class SensorState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("invalid", 0), ("normal", 1), ("alarmstate", 2), ("alarm", 3))

class SensorID(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IOName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 12)

class SensorName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class SensorValue(Integer32):
    pass

class SensorString(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 10)

class SensorFlags(Integer32):
    pass

class TimeStamp(TimeTicks):
    pass

hwgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796))
charonII = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3))
damocles = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 4))
setup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99))
inpTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 4, 1), )
if mibBuilder.loadTexts: inpTable.setStatus('current')
inpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 4, 1, 1), ).setIndexNames((0, "DAMOCLES-MIB", "inpIndex"))
if mibBuilder.loadTexts: inpEntry.setStatus('current')
inpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 1, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: inpIndex.setStatus('current')
inpState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 1, 1, 2), OnOff()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpState.setStatus('current')
inpName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 1, 1, 3), IOName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpName.setStatus('current')
inpAlarmSetup = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 1, 1, 4), InputAlarmSetup()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpAlarmSetup.setStatus('current')
inpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 1, 1, 5), InputAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpAlarmState.setStatus('current')
inpCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 1, 1, 6), NonNegativeInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpCounter.setStatus('current')
outTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 4, 2), )
if mibBuilder.loadTexts: outTable.setStatus('current')
outEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 4, 2, 1), ).setIndexNames((0, "DAMOCLES-MIB", "outIndex"))
if mibBuilder.loadTexts: outEntry.setStatus('current')
outIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: outIndex.setStatus('current')
outState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 2, 1, 2), OnOff()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outState.setStatus('current')
outName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 2, 1, 3), IOName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: outName.setStatus('current')
outType = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 2, 1, 4), OutputType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: outType.setStatus('current')
sensTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3), )
if mibBuilder.loadTexts: sensTable.setStatus('current')
sensEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1), ).setIndexNames((0, "DAMOCLES-MIB", "sensIndex"))
if mibBuilder.loadTexts: sensEntry.setStatus('current')
sensIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: sensIndex.setStatus('current')
sensName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1, 2), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensName.setStatus('current')
sensState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1, 4), SensorState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensState.setStatus('current')
sensString = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1, 5), SensorString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensString.setStatus('current')
sensValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1, 6), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensValue.setStatus('current')
sensValueRaw = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1, 7), SensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensValueRaw.setStatus('current')
sensID = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1, 8), SensorID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensID.setStatus('current')
sensUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 3, 1, 9), UnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensUnit.setStatus('current')
tsAlarm = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50))
tsAlarmsPresent = MibScalar((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmsPresent.setStatus('current')
tsAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50, 2), )
if mibBuilder.loadTexts: tsAlarmTable.setStatus('current')
tsAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50, 2, 1), ).setIndexNames((0, "DAMOCLES-MIB", "tsAlarmIdx"))
if mibBuilder.loadTexts: tsAlarmEntry.setStatus('current')
tsAlarmIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: tsAlarmIdx.setStatus('current')
tsAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50, 2, 1, 2), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmId.setStatus('current')
tsAlarmDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inputStateAlarm", 1), ("temperatureOutOfRange", 2), ("maskStateAlarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmDescr.setStatus('current')
tsAlarmSensName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50, 2, 1, 4), SensorName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmSensName.setStatus('current')
tsAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 50, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsAlarmTime.setStatus('current')
sensSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1))
unitType = MibScalar((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 1), UnitType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unitType.setStatus('current')
sensSetupTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 2), )
if mibBuilder.loadTexts: sensSetupTable.setStatus('current')
sensSetupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 2, 1), ).setIndexNames((0, "DAMOCLES-MIB", "sensSetupIndex"))
if mibBuilder.loadTexts: sensSetupEntry.setStatus('current')
sensSetupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 2, 1, 1), PositiveInteger())
if mibBuilder.loadTexts: sensSetupIndex.setStatus('current')
sensSetupName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 2, 1, 2), SensorName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensSetupName.setStatus('current')
sensFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 2, 1, 5), SensorFlags()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensFlags.setStatus('current')
sensLimitMin = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 2, 1, 6), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensLimitMin.setStatus('current')
sensLimitMax = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 2, 1, 7), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensLimitMax.setStatus('current')
sensHysteresis = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 3, 4, 99, 1, 2, 1, 8), SensorValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sensHysteresis.setStatus('current')
inpChange = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 4) + (0,1)).setObjects(("DAMOCLES-MIB", "inpName"), ("DAMOCLES-MIB", "inpState"), ("DAMOCLES-MIB", "inpAlarmState"))
sensStateChanged = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 4) + (0,2)).setObjects(("DAMOCLES-MIB", "sensName"), ("DAMOCLES-MIB", "sensID"), ("DAMOCLES-MIB", "sensState"), ("DAMOCLES-MIB", "sensValue"), ("DAMOCLES-MIB", "sensUnit"))
tsTrapNewAlarm = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 4) + (0,3)).setObjects(("DAMOCLES-MIB", "tsAlarmId"), ("DAMOCLES-MIB", "tsAlarmDescr"))
tsTrapAlarmEnd = NotificationType((1, 3, 6, 1, 4, 1, 21796, 3, 4) + (0,4)).setObjects(("DAMOCLES-MIB", "tsAlarmId"), ("DAMOCLES-MIB", "tsAlarmDescr"))
mibBuilder.exportSymbols("DAMOCLES-MIB", inpName=inpName, tsAlarmSensName=tsAlarmSensName, sensState=sensState, tsTrapNewAlarm=tsTrapNewAlarm, sensLimitMin=sensLimitMin, hwgroup=hwgroup, SensorFlags=SensorFlags, sensSetupTable=sensSetupTable, InputAlarmSetup=InputAlarmSetup, InputAlarmState=InputAlarmState, outName=outName, inpCounter=inpCounter, sensTable=sensTable, inpIndex=inpIndex, OutputType=OutputType, outType=outType, TimeStamp=TimeStamp, outState=outState, sensFlags=sensFlags, PositiveInteger=PositiveInteger, sensValue=sensValue, sensSetupIndex=sensSetupIndex, SensorState=SensorState, outTable=outTable, sensID=sensID, outEntry=outEntry, SensorString=SensorString, SensorName=SensorName, inpEntry=inpEntry, SensorID=SensorID, inpAlarmSetup=inpAlarmSetup, unitType=unitType, sensIndex=sensIndex, sensString=sensString, charonII=charonII, SensorValue=SensorValue, sensName=sensName, tsAlarmDescr=tsAlarmDescr, outIndex=outIndex, tsAlarmTime=tsAlarmTime, OnOff=OnOff, sensSetup=sensSetup, sensHysteresis=sensHysteresis, setup=setup, sensStateChanged=sensStateChanged, tsTrapAlarmEnd=tsTrapAlarmEnd, tsAlarmTable=tsAlarmTable, sensUnit=sensUnit, tsAlarm=tsAlarm, inpState=inpState, tsAlarmEntry=tsAlarmEntry, tsAlarmIdx=tsAlarmIdx, sensSetupEntry=sensSetupEntry, sensEntry=sensEntry, sensLimitMax=sensLimitMax, IOName=IOName, tsAlarmId=tsAlarmId, NonNegativeInteger=NonNegativeInteger, UnitType=UnitType, sensValueRaw=sensValueRaw, inpChange=inpChange, tsAlarmsPresent=tsAlarmsPresent, sensSetupName=sensSetupName, inpAlarmState=inpAlarmState, damocles=damocles, inpTable=inpTable)
