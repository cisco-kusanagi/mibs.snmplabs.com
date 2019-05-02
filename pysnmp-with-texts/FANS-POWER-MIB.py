#
# PySNMP MIB module FANS-POWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FANS-POWER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:11:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter32, Gauge32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Unsigned32, TimeTicks, Integer32, ObjectIdentity, Counter64, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "Gauge32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Unsigned32", "TimeTicks", "Integer32", "ObjectIdentity", "Counter64", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
class FanPosition(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("cabinet-fan-top", 1), ("trunk-fan-top", 2), ("trunk-fan-bottom", 3))

class FanStat(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("offline", 0), ("online", 1))

class FanType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("newfan", 1), ("oldfan", 2))

class PowerType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3))
    namedValues = NamedValues(("oldpower", 2), ("newpower", 3))

class PowerAvailStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("offline", 0), ("online", 1), ("null", 2))

class PowerOperStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("normal", 0), ("abnormal", 1), ("null", 2))

class NewFanStat(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("abnormal", 0), ("full-speed", 1), ("half-speed", 2), ("null", 3))

class DisplayString(OctetString):
    pass

fan = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 4998))
fanType = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 4998, 1), FanType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanType.setStatus('current')
if mibBuilder.loadTexts: fanType.setDescription('the description of fans type.')
power = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 4999))
powerType = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 4999, 1), PowerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerType.setStatus('current')
if mibBuilder.loadTexts: powerType.setDescription('the description of power type.')
fanTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 5000), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
if mibBuilder.loadTexts: fanTable.setDescription('the description of fans infomation.')
fansEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1), ).setIndexNames((0, "FANS-POWER-MIB", "FanPosition"))
if mibBuilder.loadTexts: fansEntry.setStatus('current')
if mibBuilder.loadTexts: fansEntry.setDescription('')
fansPositon = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 1), FanPosition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansPositon.setStatus('current')
if mibBuilder.loadTexts: fansPositon.setDescription('')
fansNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansNumber.setStatus('current')
if mibBuilder.loadTexts: fansNumber.setDescription('')
fansStatOfFan1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 3), FanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansStatOfFan1.setStatus('current')
if mibBuilder.loadTexts: fansStatOfFan1.setDescription('')
fansStatOfFan2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 4), FanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansStatOfFan2.setStatus('current')
if mibBuilder.loadTexts: fansStatOfFan2.setDescription('')
fansStatOfFan3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 5), FanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansStatOfFan3.setStatus('current')
if mibBuilder.loadTexts: fansStatOfFan3.setDescription('')
fansStatOfFan4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 6), FanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansStatOfFan4.setStatus('current')
if mibBuilder.loadTexts: fansStatOfFan4.setDescription('')
fansStatOfFan5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 7), FanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansStatOfFan5.setStatus('current')
if mibBuilder.loadTexts: fansStatOfFan5.setDescription('')
fansStatOfFan6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 8), FanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansStatOfFan6.setStatus('current')
if mibBuilder.loadTexts: fansStatOfFan6.setDescription('')
fansStatOfFan7 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 9), FanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansStatOfFan7.setStatus('current')
if mibBuilder.loadTexts: fansStatOfFan7.setDescription('')
fansStatOfFan8 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 5000, 1, 10), FanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fansStatOfFan8.setStatus('current')
if mibBuilder.loadTexts: fansStatOfFan8.setDescription('')
powerStatInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 5001))
powerStatACVoltage = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatACVoltage.setStatus('current')
if mibBuilder.loadTexts: powerStatACVoltage.setDescription('')
powerStatACCurrent = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatACCurrent.setStatus('current')
if mibBuilder.loadTexts: powerStatACCurrent.setDescription('')
powerStatDCVoltage = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatDCVoltage.setStatus('current')
if mibBuilder.loadTexts: powerStatDCVoltage.setDescription('')
powerStatDCCurrent = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatDCCurrent.setStatus('current')
if mibBuilder.loadTexts: powerStatDCCurrent.setDescription('')
powerStatACError = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatACError.setStatus('current')
if mibBuilder.loadTexts: powerStatACError.setDescription('')
powerStatRectifyError = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatRectifyError.setStatus('current')
if mibBuilder.loadTexts: powerStatRectifyError.setDescription('')
powerStatMod1AvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 7), PowerAvailStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatMod1AvailStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatMod1AvailStatus.setDescription('')
powerStatMod2AvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 8), PowerAvailStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatMod2AvailStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatMod2AvailStatus.setDescription('')
powerStatMod3AvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 9), PowerAvailStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatMod3AvailStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatMod3AvailStatus.setDescription('')
powerStatMod1OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 10), PowerOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatMod1OperStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatMod1OperStatus.setDescription('')
powerStatMod2OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 11), PowerOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatMod2OperStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatMod2OperStatus.setDescription('')
powerStatMod3OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5001, 12), PowerOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStatMod3OperStatus.setStatus('current')
if mibBuilder.loadTexts: powerStatMod3OperStatus.setDescription('')
newFanStatInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 5002))
newFanTopFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5002, 1), NewFanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newFanTopFanStatus.setStatus('current')
if mibBuilder.loadTexts: newFanTopFanStatus.setDescription('')
newFanBottomFanStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5002, 2), NewFanStat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newFanBottomFanStatus.setStatus('current')
if mibBuilder.loadTexts: newFanBottomFanStatus.setDescription('')
newPowerStatInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 5003))
newPowerStatMod1AvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5003, 1), PowerAvailStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newPowerStatMod1AvailStatus.setStatus('current')
if mibBuilder.loadTexts: newPowerStatMod1AvailStatus.setDescription('')
newPowerStatMod2AvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5003, 2), PowerAvailStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newPowerStatMod2AvailStatus.setStatus('current')
if mibBuilder.loadTexts: newPowerStatMod2AvailStatus.setDescription('')
newPowerStatMod3AvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5003, 3), PowerAvailStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newPowerStatMod3AvailStatus.setStatus('current')
if mibBuilder.loadTexts: newPowerStatMod3AvailStatus.setDescription('')
newPowerStatMod1OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5003, 4), PowerOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newPowerStatMod1OperStatus.setStatus('current')
if mibBuilder.loadTexts: newPowerStatMod1OperStatus.setDescription('')
newPowerStatMod2OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5003, 5), PowerOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newPowerStatMod2OperStatus.setStatus('current')
if mibBuilder.loadTexts: newPowerStatMod2OperStatus.setDescription('')
newPowerStatMod3OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 3902, 3, 5003, 6), PowerOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: newPowerStatMod3OperStatus.setStatus('current')
if mibBuilder.loadTexts: newPowerStatMod3OperStatus.setDescription('')
mibBuilder.exportSymbols("FANS-POWER-MIB", powerStatMod1AvailStatus=powerStatMod1AvailStatus, newPowerStatInfo=newPowerStatInfo, newPowerStatMod3OperStatus=newPowerStatMod3OperStatus, fansPositon=fansPositon, FanStat=FanStat, powerStatMod2OperStatus=powerStatMod2OperStatus, powerStatACCurrent=powerStatACCurrent, newFanBottomFanStatus=newFanBottomFanStatus, powerStatInfo=powerStatInfo, powerStatMod3AvailStatus=powerStatMod3AvailStatus, powerStatDCVoltage=powerStatDCVoltage, powerStatDCCurrent=powerStatDCCurrent, powerStatMod1OperStatus=powerStatMod1OperStatus, powerStatMod3OperStatus=powerStatMod3OperStatus, FanType=FanType, PowerAvailStatus=PowerAvailStatus, power=power, powerStatRectifyError=powerStatRectifyError, powerType=powerType, fansStatOfFan7=fansStatOfFan7, fansStatOfFan4=fansStatOfFan4, newPowerStatMod2OperStatus=newPowerStatMod2OperStatus, fansStatOfFan1=fansStatOfFan1, PowerType=PowerType, newPowerStatMod2AvailStatus=newPowerStatMod2AvailStatus, newFanStatInfo=newFanStatInfo, fanType=fanType, fanTable=fanTable, zte=zte, newPowerStatMod1AvailStatus=newPowerStatMod1AvailStatus, newFanTopFanStatus=newFanTopFanStatus, fansStatOfFan5=fansStatOfFan5, FanPosition=FanPosition, PowerOperStatus=PowerOperStatus, fansStatOfFan2=fansStatOfFan2, powerStatACVoltage=powerStatACVoltage, powerStatMod2AvailStatus=powerStatMod2AvailStatus, fansStatOfFan3=fansStatOfFan3, fansEntry=fansEntry, fansStatOfFan6=fansStatOfFan6, zxr10=zxr10, fansNumber=fansNumber, newPowerStatMod3AvailStatus=newPowerStatMod3AvailStatus, DisplayString=DisplayString, NewFanStat=NewFanStat, powerStatACError=powerStatACError, newPowerStatMod1OperStatus=newPowerStatMod1OperStatus, fansStatOfFan8=fansStatOfFan8, fan=fan)
