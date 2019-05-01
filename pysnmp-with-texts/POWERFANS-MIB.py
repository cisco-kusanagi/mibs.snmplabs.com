#
# PySNMP MIB module POWERFANS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POWERFANS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:41:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, iso, Counter32, enterprises, Bits, ObjectIdentity, NotificationType, MibIdentifier, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, mgmt, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "iso", "Counter32", "enterprises", "Bits", "ObjectIdentity", "NotificationType", "MibIdentifier", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "mgmt", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
if mibBuilder.loadTexts: fanTable.setDescription('the description of fans infomation ')
fanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1), ).setIndexNames((0, "POWERFANS-MIB", "fanNo"))
if mibBuilder.loadTexts: fanEntry.setStatus('current')
if mibBuilder.loadTexts: fanEntry.setDescription('A fans entry containing objects that descript the fans infomation.')
fanNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNo.setStatus('current')
if mibBuilder.loadTexts: fanNo.setDescription('The no. of the fan.')
fanStat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 2), FanStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanStat.setStatus('current')
if mibBuilder.loadTexts: fanStat.setDescription('The status of fan')
fanRotateSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanRotateSpeed.setStatus('current')
if mibBuilder.loadTexts: fanRotateSpeed.setDescription('the Rotate Speed of fan')
powerTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2), )
if mibBuilder.loadTexts: powerTable.setStatus('current')
if mibBuilder.loadTexts: powerTable.setDescription('the description of power infomation ')
powerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1), ).setIndexNames((0, "POWERFANS-MIB", "powerNo"))
if mibBuilder.loadTexts: powerEntry.setStatus('current')
if mibBuilder.loadTexts: powerEntry.setDescription('A power entry containing objects that descript the power infomation.')
powerNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerNo.setStatus('current')
if mibBuilder.loadTexts: powerNo.setDescription('The no. of the power.')
powerStat = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 2), PowerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerStat.setStatus('current')
if mibBuilder.loadTexts: powerStat.setDescription('The status of the power')
powerTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 200, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerTemperature.setStatus('current')
if mibBuilder.loadTexts: powerTemperature.setDescription('Power Temperature')
mibBuilder.exportSymbols("POWERFANS-MIB", PowerStatus=PowerStatus, DisplayString=DisplayString, fanNo=fanNo, fanEntry=fanEntry, powerEntry=powerEntry, fanStat=fanStat, powerTable=powerTable, powerTemperature=powerTemperature, powerNo=powerNo, enviorment=enviorment, zte=zte, fanRotateSpeed=fanRotateSpeed, powerStat=powerStat, FanStatus=FanStatus, zxr10=zxr10, zxr10systemconfig=zxr10systemconfig, fanTable=fanTable)
