#
# PySNMP MIB module DCS3FRU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DCS3FRU-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Unsigned32, NotificationType, Bits, enterprises, Integer32, Counter64, Gauge32, TimeTicks, iso, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Unsigned32", "NotificationType", "Bits", "enterprises", "Integer32", "Counter64", "Gauge32", "TimeTicks", "iso", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
server3 = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10892))
baseboardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10892, 1))
fruGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000))
class DellObjectRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 128)

class DellUnsigned8BitRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class DellUnsigned16BitRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class DellUnsigned32BitRange(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class DellDateName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(25, 25)
    fixedLength = 25

class DellStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("ok", 3), ("nonCritical", 4), ("critical", 5), ("nonRecoverable", 6))

class DellFRUInformationState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ok", 1), ("notSupported", 2), ("notAvailable", 3), ("checksumInvalid", 4), ("corrupted", 5))

fruTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10), )
if mibBuilder.loadTexts: fruTable.setStatus('mandatory')
fruTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1), ).setIndexNames((0, "DCS3FRU-MIB", "fruChassisIndex"), (0, "DCS3FRU-MIB", "fruIndex"))
if mibBuilder.loadTexts: fruTableEntry.setStatus('mandatory')
fruChassisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 1), DellObjectRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruChassisIndex.setStatus('mandatory')
fruIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 2), DellObjectRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruIndex.setStatus('mandatory')
fruInformationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 3), DellStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruInformationStatus.setStatus('mandatory')
fruInformationState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 4), DellFRUInformationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruInformationState.setStatus('mandatory')
fruDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruDeviceName.setStatus('mandatory')
fruManufacturerName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruManufacturerName.setStatus('mandatory')
fruSerialNumberName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruSerialNumberName.setStatus('mandatory')
fruPartNumberName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruPartNumberName.setStatus('mandatory')
fruRevisionName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruRevisionName.setStatus('mandatory')
fruManufacturingDateName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 10), DellDateName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruManufacturingDateName.setStatus('mandatory')
fruAssetTagName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruAssetTagName.setStatus('mandatory')
mibBuilder.exportSymbols("DCS3FRU-MIB", DellUnsigned16BitRange=DellUnsigned16BitRange, fruManufacturerName=fruManufacturerName, dell=dell, DellDateName=DellDateName, server3=server3, fruGroup=fruGroup, fruSerialNumberName=fruSerialNumberName, DellStatus=DellStatus, fruAssetTagName=fruAssetTagName, DellObjectRange=DellObjectRange, fruTableEntry=fruTableEntry, baseboardGroup=baseboardGroup, fruInformationStatus=fruInformationStatus, fruManufacturingDateName=fruManufacturingDateName, fruInformationState=fruInformationState, fruPartNumberName=fruPartNumberName, fruIndex=fruIndex, DellUnsigned32BitRange=DellUnsigned32BitRange, fruDeviceName=fruDeviceName, fruTable=fruTable, fruChassisIndex=fruChassisIndex, DellFRUInformationState=DellFRUInformationState, DellUnsigned8BitRange=DellUnsigned8BitRange, fruRevisionName=fruRevisionName)
