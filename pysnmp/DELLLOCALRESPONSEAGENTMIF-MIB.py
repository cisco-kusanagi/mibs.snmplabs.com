#
# PySNMP MIB module DELLLOCALRESPONSEAGENTMIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DELLLOCALRESPONSEAGENTMIF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ObjectIdentity, enterprises, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, Counter64, IpAddress, NotificationType, Bits, ModuleIdentity, iso, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "enterprises", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "Counter64", "IpAddress", "NotificationType", "Bits", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DmiInteger(Integer32):
    pass

class DmiDisplaystring(DisplayString):
    pass

class DmiDate(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(28, 28)
    fixedLength = 28

class DmiComponentIndex(Integer32):
    pass

dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
server = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10890))
localresponseagent = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10890, 3))
dmtfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1))
tComponentid = MibTable((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1), )
if mibBuilder.loadTexts: tComponentid.setStatus('mandatory')
eComponentid = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1), ).setIndexNames((0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eComponentid.setStatus('mandatory')
a1Manufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Manufacturer.setStatus('mandatory')
a1Product = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Product.setStatus('mandatory')
a1Version = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Version.setStatus('mandatory')
a1SerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1SerialNumber.setStatus('mandatory')
a1Installation = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 5), DmiDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Installation.setStatus('mandatory')
a1Verify = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("vAnErrorOccurredCheckStatusCode", 0), ("vThisComponentDoesNotExist", 1), ("vTheVerifyIsNotSupported", 2), ("vReserved", 3), ("vThisComponentExistsButTheFunctionalityI", 4), ("vThisComponentExistsButTheFunctionality1", 5), ("vThisComponentExistsAndIsNotFunctioningC", 6), ("vThisComponentExistsAndIsFunctioningCorr", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a1Verify.setStatus('mandatory')
tActionResponseTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2), )
if mibBuilder.loadTexts: tActionResponseTable.setStatus('mandatory')
eActionResponseTable = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1), ).setIndexNames((0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"), (0, "DELLLOCALRESPONSEAGENTMIF-MIB", "a2Actionname"))
if mibBuilder.loadTexts: eActionResponseTable.setStatus('mandatory')
a2Actionname = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 7, 13, 14, 160, 168, 172, 200, 202, 204, 206, 208, 210, 212, 214, 220, 225))).clone(namedValues=NamedValues(("vUnknown", 0), ("vAdaptec-HostAdapterFailed", 3), ("vAdaptec-LogicalUnitFailed", 7), ("vApc-SystemOnLowUtilityPower", 13), ("vApc-SystemOnLowBatteryPower", 14), ("vTemperatureSensorDetectedAFailure", 160), ("vFanSensorDetectedAFailure", 168), ("vVoltageSensorDetectedAFailure", 172), ("vTemperatureSensorWarningDetected", 200), ("vVoltageSensorWarningDetected", 202), ("vFanSensorWarningDetected", 204), ("vCurrentSensorDetectedAFailure", 206), ("vCurrentSensorWarningDetected", 208), ("vPowerSupplyLostRedundancyDetected", 210), ("vPowerSupplyDegradedRedundancyDetected", 212), ("vPowerSupplyDetectedAFailure", 214), ("vChassisIntrusionDetected", 220), ("vLostConnectionToDiskPod", 225)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Actionname.setStatus('mandatory')
a2Actionresponse = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 2), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2Actionresponse.setStatus('mandatory')
a2Actionexecute = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 3), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a2Actionexecute.setStatus('mandatory')
a2Actionsource = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 2, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a2Actionsource.setStatus('mandatory')
tActionCapabilities = MibTable((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3), )
if mibBuilder.loadTexts: tActionCapabilities.setStatus('mandatory')
eActionCapabilities = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3, 1), ).setIndexNames((0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eActionCapabilities.setStatus('mandatory')
a3LraCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 3, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3LraCapabilities.setStatus('mandatory')
tMiftomib = MibTable((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99), )
if mibBuilder.loadTexts: tMiftomib.setStatus('mandatory')
eMiftomib = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1), ).setIndexNames((0, "DELLLOCALRESPONSEAGENTMIF-MIB", "DmiComponentIndex"))
if mibBuilder.loadTexts: eMiftomib.setStatus('mandatory')
a99DellLocalResponseAgentMib = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99DellLocalResponseAgentMib.setStatus('mandatory')
a99MibOid = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99MibOid.setStatus('mandatory')
a99DisableTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10890, 3, 1, 99, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a99DisableTraps.setStatus('mandatory')
mibBuilder.exportSymbols("DELLLOCALRESPONSEAGENTMIF-MIB", eComponentid=eComponentid, tActionCapabilities=tActionCapabilities, tActionResponseTable=tActionResponseTable, a1SerialNumber=a1SerialNumber, dmtfGroups=dmtfGroups, dell=dell, eActionCapabilities=eActionCapabilities, localresponseagent=localresponseagent, a2Actionresponse=a2Actionresponse, a2Actionsource=a2Actionsource, a1Version=a1Version, tMiftomib=tMiftomib, a99DisableTraps=a99DisableTraps, DmiDisplaystring=DmiDisplaystring, a2Actionname=a2Actionname, DmiComponentIndex=DmiComponentIndex, tComponentid=tComponentid, server=server, a1Verify=a1Verify, DmiDate=DmiDate, a2Actionexecute=a2Actionexecute, eMiftomib=eMiftomib, a1Manufacturer=a1Manufacturer, a3LraCapabilities=a3LraCapabilities, a99DellLocalResponseAgentMib=a99DellLocalResponseAgentMib, eActionResponseTable=eActionResponseTable, a1Installation=a1Installation, a99MibOid=a99MibOid, a1Product=a1Product, DmiInteger=DmiInteger)
