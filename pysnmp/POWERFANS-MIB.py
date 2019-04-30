#
# PySNMP MIB module POWERFANS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POWERFANS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, NotificationType, Bits, mgmt, enterprises, Counter32, Unsigned32, ObjectIdentity, ModuleIdentity, MibIdentifier, NotificationType, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Bits", "mgmt", "enterprises", "Counter32", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "NotificationType", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
class FanStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("fan-online", 0), ("fan-offline", 1))

class PowerStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("power-work", 0), ("power-online", 1), ("power-offline", 2))

class DisplayString(OctetString):
    pass

zxr10systemconfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 1))
enviorment = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 200))
fanTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1), )
if mibBuilder.loadTexts: fanTable.setStatus('current')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1), ).setIndexNames((0, "POWERFANS-MIB", "fanNo"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
fanNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNo.setStatus('current')
fanStat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 2), FanStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStat.setStatus('current')
fanRotateSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanRotateSpeed.setStatus('current')
powerTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2), )
if mibBuilder.loadTexts: powerTable.setStatus('current')
powerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1), ).setIndexNames((0, "POWERFANS-MIB", "powerNo"))
if mibBuilder.loadTexts: powerEntry.setStatus('current')
powerNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerNo.setStatus('current')
powerStat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 2), PowerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStat.setStatus('current')
powerTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerTemperature.setStatus('current')
mibBuilder.exportSymbols("POWERFANS-MIB", zxr10=zxr10, fanStat=fanStat, powerTemperature=powerTemperature, FanStatus=FanStatus, fanTable=fanTable, enviorment=enviorment, zte=zte, powerTable=powerTable, fanRotateSpeed=fanRotateSpeed, powerStat=powerStat, zxr10systemconfig=zxr10systemconfig, powerEntry=powerEntry, DisplayString=DisplayString, PowerStatus=PowerStatus, powerNo=powerNo, fanEntry=fanEntry, fanNo=fanNo)
