#
# PySNMP MIB module HWG-PWR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HWG-PWR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, ObjectIdentity, enterprises, ModuleIdentity, IpAddress, Unsigned32, MibIdentifier, Integer32, Counter64, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "ObjectIdentity", "enterprises", "ModuleIdentity", "IpAddress", "Unsigned32", "MibIdentifier", "Integer32", "Counter64", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Txt8(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 8)

class Txt16(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 16)

class SensorValue(Integer32):
    pass

class SensorID(Integer32):
    pass

class OpenClose(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("open", 0), ("close", 1))

class AlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("invalid", 0), ("normal", 1), ("alarm", 2))

hwgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 21796))
x390 = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4))
hwgpwr = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 6))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 6, 70))
meters = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1))
input = MibIdentifier((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2))
infoAddressMAC = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 6, 70, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: infoAddressMAC.setStatus('mandatory')
mtNumber = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtNumber.setStatus('mandatory')
mtTableMeters = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2), )
if mibBuilder.loadTexts: mtTableMeters.setStatus('mandatory')
mtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1), ).setIndexNames((0, "HWG-PWR-MIB", "mtIndex"))
if mibBuilder.loadTexts: mtEntry.setStatus('mandatory')
mtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtIndex.setStatus('mandatory')
mtName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 2), Txt16()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtName.setStatus('mandatory')
mtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 3), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtAddr.setStatus('mandatory')
mtSecAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtSecAddr.setStatus('mandatory')
mtValNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 2, 1, 5), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtValNumber.setStatus('mandatory')
mtvalTableValues = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3), )
if mibBuilder.loadTexts: mtvalTableValues.setStatus('mandatory')
mtvalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1), ).setIndexNames((0, "HWG-PWR-MIB", "mtvalIndex"))
if mibBuilder.loadTexts: mtvalEntry.setStatus('mandatory')
mtvalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalIndex.setStatus('mandatory')
mtvalName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 2), Txt16()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtvalName.setStatus('mandatory')
mtvalUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 3), Txt8()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtvalUnit.setStatus('mandatory')
mtvalTarif = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 4), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalTarif.setStatus('mandatory')
mtvalExp = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 5), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtvalExp.setStatus('mandatory')
mtvalMbusValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 6), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalMbusValue.setStatus('mandatory')
mtvalTxtValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 7), Txt8()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalTxtValue.setStatus('mandatory')
mtvalAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 8), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mtvalAlarmState.setStatus('mandatory')
mtvalZeroOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 1, 3, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mtvalZeroOffset.setStatus('mandatory')
inpNumber = MibScalar((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpNumber.setStatus('mandatory')
inpTable = MibTable((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2), )
if mibBuilder.loadTexts: inpTable.setStatus('mandatory')
inpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1), ).setIndexNames((0, "HWG-PWR-MIB", "inpIndex"))
if mibBuilder.loadTexts: inpEntry.setStatus('mandatory')
inpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 1), PositiveInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpIndex.setStatus('mandatory')
inpName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 2), Txt16()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: inpName.setStatus('mandatory')
inpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 3), OpenClose()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpValue.setStatus('mandatory')
inpValueName = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 4), Txt8()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpValueName.setStatus('mandatory')
inpAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 21796, 4, 6, 2, 2, 1, 5), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inpAlarmState.setStatus('mandatory')
pwrStateToAlarm = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 6) + (0,1)).setObjects(("HWG-PWR-MIB", "mtvalIndex"), ("HWG-PWR-MIB", "mtvalName"), ("HWG-PWR-MIB", "mtvalUnit"), ("HWG-PWR-MIB", "mtvalTarif"), ("HWG-PWR-MIB", "mtvalExp"), ("HWG-PWR-MIB", "mtvalValue"), ("HWG-PWR-MIB", "mtvalTxtValue"), ("HWG-PWR-MIB", "mtvalAlarmState"))
pwrStateToNormal = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 6) + (0,2)).setObjects(("HWG-PWR-MIB", "mtvalIndex"), ("HWG-PWR-MIB", "mtvalName"), ("HWG-PWR-MIB", "mtvalUnit"), ("HWG-PWR-MIB", "mtvalTarif"), ("HWG-PWR-MIB", "mtvalExp"), ("HWG-PWR-MIB", "mtvalValue"), ("HWG-PWR-MIB", "mtvalTxtValue"), ("HWG-PWR-MIB", "mtvalAlarmState"))
inContactStateToAlarm = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 6) + (0,3)).setObjects(("SNMPv2-MIB", "sysName"), ("HWG-PWR-MIB", "infoAddressMAC"), ("HWG-PWR-MIB", "inpIndex"), ("HWG-PWR-MIB", "inpName"), ("HWG-PWR-MIB", "inpValue"), ("HWG-PWR-MIB", "inpValueName"), ("HWG-PWR-MIB", "inpAlarmState"))
inContactStateToNormal = NotificationType((1, 3, 6, 1, 4, 1, 21796, 4, 6) + (0,4)).setObjects(("SNMPv2-MIB", "sysName"), ("HWG-PWR-MIB", "infoAddressMAC"), ("HWG-PWR-MIB", "inpIndex"), ("HWG-PWR-MIB", "inpName"), ("HWG-PWR-MIB", "inpValue"), ("HWG-PWR-MIB", "inpValueName"), ("HWG-PWR-MIB", "inpAlarmState"))
mibBuilder.exportSymbols("HWG-PWR-MIB", pwrStateToAlarm=pwrStateToAlarm, SensorID=SensorID, mtName=mtName, mtTableMeters=mtTableMeters, mtSecAddr=mtSecAddr, inpValueName=inpValueName, inpValue=inpValue, mtvalTarif=mtvalTarif, mtIndex=mtIndex, inpAlarmState=inpAlarmState, hwgroup=hwgroup, mtvalMbusValue=mtvalMbusValue, hwgpwr=hwgpwr, mtAddr=mtAddr, inpNumber=inpNumber, mtvalTableValues=mtvalTableValues, mtvalAlarmState=mtvalAlarmState, inpTable=inpTable, inpEntry=inpEntry, mtvalEntry=mtvalEntry, mtvalIndex=mtvalIndex, pwrStateToNormal=pwrStateToNormal, PositiveInteger=PositiveInteger, mtvalUnit=mtvalUnit, mtNumber=mtNumber, infoAddressMAC=infoAddressMAC, SensorValue=SensorValue, inContactStateToNormal=inContactStateToNormal, mtvalTxtValue=mtvalTxtValue, Txt16=Txt16, inpName=inpName, Txt8=Txt8, inContactStateToAlarm=inContactStateToAlarm, mtEntry=mtEntry, mtvalExp=mtvalExp, OpenClose=OpenClose, AlarmState=AlarmState, mtvalName=mtvalName, meters=meters, mtvalZeroOffset=mtvalZeroOffset, inpIndex=inpIndex, info=info, x390=x390, mtValNumber=mtValNumber, input=input)
