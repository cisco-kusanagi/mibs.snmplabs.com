#
# PySNMP MIB module DCS3FRU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DCS3FRU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:37:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, ObjectIdentity, Unsigned32, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Counter64, IpAddress, Gauge32, NotificationType, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "ObjectIdentity", "Unsigned32", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Counter64", "IpAddress", "Gauge32", "NotificationType", "enterprises", "ModuleIdentity")
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
if mibBuilder.loadTexts: fruTable.setDescription('2000.0010 This object defines the Field Replaceable Unit table.')
fruTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1), ).setIndexNames((0, "DCS3FRU-MIB", "fruChassisIndex"), (0, "DCS3FRU-MIB", "fruIndex"))
if mibBuilder.loadTexts: fruTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: fruTableEntry.setDescription('2000.0010.0001 This object defines the Field Replaceable Unit table entry.')
fruChassisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 1), DellObjectRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruChassisIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fruChassisIndex.setDescription('2000.0010.0001.0001 This attribute defines the index (one based) of the chassis containing the field replaceable unit.')
fruIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 2), DellObjectRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruIndex.setStatus('mandatory')
if mibBuilder.loadTexts: fruIndex.setDescription('2000.0010.0001.0002 This attribute defines the index (one based) of the field replaceable unit.')
fruInformationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 3), DellStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruInformationStatus.setStatus('mandatory')
if mibBuilder.loadTexts: fruInformationStatus.setDescription('2000.0010.0001.0003 This attribute defines the status of the field replaceable unit information.')
fruInformationState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 4), DellFRUInformationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruInformationState.setStatus('mandatory')
if mibBuilder.loadTexts: fruInformationState.setDescription('2000.0010.0001.0004 This attribute defines the state of the field replaceable unit information. Some information for the field replaceable unit may not be available if the state is other than ok(1).')
fruDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruDeviceName.setStatus('mandatory')
if mibBuilder.loadTexts: fruDeviceName.setDescription('2000.0010.0001.0005 This attribute defines the device name of the field replaceable unit.')
fruManufacturerName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruManufacturerName.setStatus('mandatory')
if mibBuilder.loadTexts: fruManufacturerName.setDescription('2000.0010.0001.0006 This attribute defines the manufacturer of the field replaceable unit.')
fruSerialNumberName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruSerialNumberName.setStatus('mandatory')
if mibBuilder.loadTexts: fruSerialNumberName.setDescription('2000.0010.0001.0007 This attribute defines the serial number of the field replaceable unit.')
fruPartNumberName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruPartNumberName.setStatus('mandatory')
if mibBuilder.loadTexts: fruPartNumberName.setDescription('2000.0010.0001.0008 This attribute defines the part number of the field replaceable unit.')
fruRevisionName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruRevisionName.setStatus('mandatory')
if mibBuilder.loadTexts: fruRevisionName.setDescription('2000.0010.0001.0009 This attribute defines the revision of the field replaceable unit.')
fruManufacturingDateName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 10), DellDateName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruManufacturingDateName.setStatus('mandatory')
if mibBuilder.loadTexts: fruManufacturingDateName.setDescription('2000.0010.0001.0010 This attribute defines the manufacturing date of the of the field replaceable unit.')
fruAssetTagName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10892, 1, 2000, 10, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fruAssetTagName.setStatus('mandatory')
if mibBuilder.loadTexts: fruAssetTagName.setDescription('2000.0010.0001.0011 This attribute defines the asset tag of the field replaceable unit.')
mibBuilder.exportSymbols("DCS3FRU-MIB", DellStatus=DellStatus, dell=dell, fruAssetTagName=fruAssetTagName, DellUnsigned32BitRange=DellUnsigned32BitRange, fruPartNumberName=fruPartNumberName, fruGroup=fruGroup, baseboardGroup=baseboardGroup, fruSerialNumberName=fruSerialNumberName, fruTableEntry=fruTableEntry, fruChassisIndex=fruChassisIndex, fruManufacturerName=fruManufacturerName, DellFRUInformationState=DellFRUInformationState, fruManufacturingDateName=fruManufacturingDateName, fruDeviceName=fruDeviceName, fruInformationState=fruInformationState, DellUnsigned8BitRange=DellUnsigned8BitRange, fruTable=fruTable, DellObjectRange=DellObjectRange, DellDateName=DellDateName, DellUnsigned16BitRange=DellUnsigned16BitRange, server3=server3, fruIndex=fruIndex, fruRevisionName=fruRevisionName, fruInformationStatus=fruInformationStatus)
