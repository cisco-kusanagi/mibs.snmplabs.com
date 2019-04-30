#
# PySNMP MIB module LINK-INCIDENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LINK-INCIDENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
fcSwitch, = mibBuilder.importSymbols("Brocade-REG-MIB", "fcSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, ModuleIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, TimeTicks, MibIdentifier, ObjectIdentity, Counter64, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "ModuleIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
linkIncidentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50))
linkIncidentMIB.setRevisions(('2003-07-11 00:00', '2012-06-04 00:00',))
if mibBuilder.loadTexts: linkIncidentMIB.setLastUpdated('201206040000Z')
if mibBuilder.loadTexts: linkIncidentMIB.setOrganization('Brocade Communications Systems, Inc.,')
class FcPortID(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class RLIRLinkFailureType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("bitErrorRate", 2), ("lossOfSignal", 3), ("nOSRecognized", 4), ("primitiveSequenceTimeout", 5), ("invalidSeqForPortState", 6), ("loopInitializationTimeout", 7), ("lossOfSignalInLoopInit", 8))

class LinkWwn(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class PortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("n-port", 1), ("nl-port", 2), ("e-port", 3))

class LinkFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ficon", 1), ("common", 2))

class RegType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conditional", 1), ("unconditional", 2))

class LIRRProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fcp", 1), ("sb2", 2))

class RNIDTagType(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RNIDFlags(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class RNIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class RNIDModel(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class RNIDManufacturer(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class RNIDManufacturerPlant(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RNIDSequenceNumber(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

class RNIDParams(TextualConvention, OctetString):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

ficonRNID = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2))
if mibBuilder.loadTexts: ficonRNID.setStatus('current')
nodeRNIDTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDTableNumEntries.setStatus('current')
nodeRNIDTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2), )
if mibBuilder.loadTexts: nodeRNIDTable.setStatus('current')
nodeRNIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1), ).setIndexNames((0, "LINK-INCIDENT-MIB", "nodeRNIDIndex"))
if mibBuilder.loadTexts: nodeRNIDEntry.setStatus('current')
nodeRNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDIndex.setStatus('current')
nodeRNIDIncidentPortWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 2), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDIncidentPortWWN.setStatus('current')
nodeRNIDPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 3), FcPortID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDPID.setStatus('current')
nodeRNIDFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 4), RNIDFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDFlags.setStatus('current')
nodeRNIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 5), RNIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDType.setStatus('current')
nodeRNIDModel = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 6), RNIDModel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDModel.setStatus('current')
nodeRNIDManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 7), RNIDManufacturer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDManufacturer.setStatus('current')
nodeRNIDManufacturerPlant = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 8), RNIDManufacturerPlant()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDManufacturerPlant.setStatus('current')
nodeRNIDSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 9), RNIDSequenceNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDSequenceNumber.setStatus('current')
nodeRNIDConnectedPortWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 10), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDConnectedPortWWN.setStatus('current')
nodeRNIDPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 11), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDPortType.setStatus('current')
nodeRNIDFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 12), LinkFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDFormat.setStatus('current')
nodeRNIDTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 13), RNIDTagType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDTag.setStatus('current')
nodeRNIDParams = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 14), RNIDParams()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDParams.setStatus('current')
switchRNIDTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDTableNumEntries.setStatus('current')
switchRNIDTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4), )
if mibBuilder.loadTexts: switchRNIDTable.setStatus('current')
switchRNIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1), ).setIndexNames((0, "LINK-INCIDENT-MIB", "switchRNIDIndex"))
if mibBuilder.loadTexts: switchRNIDEntry.setStatus('current')
switchRNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDIndex.setStatus('current')
switchRNIDSwitchWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 2), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDSwitchWWN.setStatus('current')
switchRNIDFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 3), RNIDFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDFlags.setStatus('current')
switchRNIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 4), RNIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDType.setStatus('current')
switchRNIDModel = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 5), RNIDModel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDModel.setStatus('current')
switchRNIDManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 6), RNIDManufacturer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDManufacturer.setStatus('current')
switchRNIDManufacturerPlant = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 7), RNIDManufacturerPlant()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDManufacturerPlant.setStatus('current')
switchRNIDSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 8), RNIDSequenceNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDSequenceNumber.setStatus('current')
switchRNIDTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 9), RNIDTagType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDTag.setStatus('current')
switchRNIDParams = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 10), RNIDParams()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDParams.setStatus('current')
nodeVfId = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeVfId.setStatus('current')
ficonSlot = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ficonSlot.setStatus('current')
ficonPort = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ficonPort.setStatus('current')
ficonLIRR = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3))
if mibBuilder.loadTexts: ficonLIRR.setStatus('current')
lIRRTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRTableNumEntries.setStatus('current')
lIRRTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2), )
if mibBuilder.loadTexts: lIRRTable.setStatus('current')
lIRREntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1), ).setIndexNames((0, "LINK-INCIDENT-MIB", "lIRRIndex"))
if mibBuilder.loadTexts: lIRREntry.setStatus('current')
lIRRIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRIndex.setStatus('current')
lIRRListenerPortWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 2), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRListenerPortWWN.setStatus('current')
lIRRListenerPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 3), FcPortID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRListenerPID.setStatus('current')
lIRRRegType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 4), RegType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRRegType.setStatus('current')
lIRRProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 5), LIRRProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRProtocol.setStatus('current')
lIRRPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 6), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRPortType.setStatus('current')
lIRRFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 7), LinkFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRFormat.setStatus('current')
ficonRLIR = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4))
if mibBuilder.loadTexts: ficonRLIR.setStatus('current')
rLIRTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRTableNumEntries.setStatus('current')
rLIRTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2), )
if mibBuilder.loadTexts: rLIRTable.setStatus('current')
rLIREntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1), ).setIndexNames((0, "LINK-INCIDENT-MIB", "rLIRIndex"))
if mibBuilder.loadTexts: rLIREntry.setStatus('current')
rLIRIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIndex.setStatus('current')
rLIRIncidentPortWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 2), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentPortWwn.setStatus('current')
rLIRIncidentNodeWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 3), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentNodeWwn.setStatus('current')
rLIRIncidentPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 5), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentPortType.setStatus('current')
rLIRIncidentPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 6), FcPortID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentPID.setStatus('current')
rLIRIncidentPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentPortNumber.setStatus('current')
rLIRConnectedPortWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 8), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRConnectedPortWwn.setStatus('current')
rLIRConnectedNodeWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 9), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRConnectedNodeWwn.setStatus('current')
rLIRFabricWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 10), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRFabricWwn.setStatus('current')
rLIRLinkFailureType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 11), RLIRLinkFailureType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRLinkFailureType.setStatus('current')
rLIRTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRTimeStamp.setStatus('current')
rLIRFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 13), LinkFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRFormat.setStatus('current')
linkIncidentMIBTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21))
if mibBuilder.loadTexts: linkIncidentMIBTraps.setStatus('current')
linkIncidentMIBTrapPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0))
if mibBuilder.loadTexts: linkIncidentMIBTrapPrefix.setStatus('current')
linkRNIDDeviceRegistration = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 1)).setObjects(("LINK-INCIDENT-MIB", "nodeRNIDIndex"), ("LINK-INCIDENT-MIB", "nodeRNIDIncidentPortWWN"), ("LINK-INCIDENT-MIB", "nodeRNIDConnectedPortWWN"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkRNIDDeviceRegistration.setStatus('current')
linkRNIDDeviceDeRegistration = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 2)).setObjects(("LINK-INCIDENT-MIB", "nodeRNIDIndex"), ("LINK-INCIDENT-MIB", "nodeRNIDIncidentPortWWN"), ("LINK-INCIDENT-MIB", "nodeRNIDConnectedPortWWN"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkRNIDDeviceDeRegistration.setStatus('current')
linkLIRRListenerAdded = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 3)).setObjects(("LINK-INCIDENT-MIB", "lIRRListenerPortWWN"), ("LINK-INCIDENT-MIB", "lIRRListenerPID"), ("LINK-INCIDENT-MIB", "lIRRIndex"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkLIRRListenerAdded.setStatus('current')
linkLIRRListenerRemoved = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 4)).setObjects(("LINK-INCIDENT-MIB", "lIRRListenerPortWWN"), ("LINK-INCIDENT-MIB", "lIRRListenerPID"), ("LINK-INCIDENT-MIB", "lIRRIndex"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkLIRRListenerRemoved.setStatus('current')
linkRLIRFailureIncident = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 5)).setObjects(("LINK-INCIDENT-MIB", "nodeRNIDIndex"), ("LINK-INCIDENT-MIB", "lIRRIndex"), ("LINK-INCIDENT-MIB", "rLIRIncidentPortWwn"), ("LINK-INCIDENT-MIB", "rLIRConnectedPortWwn"), ("LINK-INCIDENT-MIB", "rLIRIndex"), ("LINK-INCIDENT-MIB", "rLIRLinkFailureType"), ("LINK-INCIDENT-MIB", "lIRRListenerPID"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkRLIRFailureIncident.setStatus('current')
mibBuilder.exportSymbols("LINK-INCIDENT-MIB", PortType=PortType, rLIRConnectedPortWwn=rLIRConnectedPortWwn, ficonRNID=ficonRNID, linkRNIDDeviceRegistration=linkRNIDDeviceRegistration, lIRRTableNumEntries=lIRRTableNumEntries, nodeRNIDTag=nodeRNIDTag, lIRRListenerPortWWN=lIRRListenerPortWWN, nodeRNIDModel=nodeRNIDModel, switchRNIDManufacturer=switchRNIDManufacturer, switchRNIDTableNumEntries=switchRNIDTableNumEntries, nodeRNIDTableNumEntries=nodeRNIDTableNumEntries, linkRNIDDeviceDeRegistration=linkRNIDDeviceDeRegistration, RegType=RegType, nodeRNIDSequenceNumber=nodeRNIDSequenceNumber, nodeRNIDFlags=nodeRNIDFlags, linkLIRRListenerRemoved=linkLIRRListenerRemoved, ficonRLIR=ficonRLIR, lIRRRegType=lIRRRegType, rLIRIndex=rLIRIndex, lIRRFormat=lIRRFormat, RNIDFlags=RNIDFlags, nodeRNIDFormat=nodeRNIDFormat, RLIRLinkFailureType=RLIRLinkFailureType, switchRNIDSwitchWWN=switchRNIDSwitchWWN, lIRRListenerPID=lIRRListenerPID, rLIRConnectedNodeWwn=rLIRConnectedNodeWwn, linkIncidentMIBTraps=linkIncidentMIBTraps, switchRNIDIndex=switchRNIDIndex, switchRNIDFlags=switchRNIDFlags, RNIDManufacturerPlant=RNIDManufacturerPlant, switchRNIDEntry=switchRNIDEntry, switchRNIDParams=switchRNIDParams, lIRRTable=lIRRTable, switchRNIDModel=switchRNIDModel, RNIDModel=RNIDModel, rLIRIncidentNodeWwn=rLIRIncidentNodeWwn, nodeRNIDPID=nodeRNIDPID, LIRRProtocol=LIRRProtocol, rLIRFabricWwn=rLIRFabricWwn, LinkWwn=LinkWwn, lIRRProtocol=lIRRProtocol, nodeRNIDTable=nodeRNIDTable, nodeRNIDPortType=nodeRNIDPortType, lIRREntry=lIRREntry, rLIRIncidentPortType=rLIRIncidentPortType, nodeVfId=nodeVfId, rLIREntry=rLIREntry, nodeRNIDManufacturer=nodeRNIDManufacturer, linkLIRRListenerAdded=linkLIRRListenerAdded, switchRNIDType=switchRNIDType, switchRNIDTable=switchRNIDTable, switchRNIDTag=switchRNIDTag, ficonSlot=ficonSlot, rLIRIncidentPortWwn=rLIRIncidentPortWwn, rLIRTableNumEntries=rLIRTableNumEntries, ficonPort=ficonPort, RNIDManufacturer=RNIDManufacturer, RNIDSequenceNumber=RNIDSequenceNumber, RNIDParams=RNIDParams, rLIRTable=rLIRTable, PYSNMP_MODULE_ID=linkIncidentMIB, nodeRNIDManufacturerPlant=nodeRNIDManufacturerPlant, RNIDType=RNIDType, rLIRFormat=rLIRFormat, LinkFormat=LinkFormat, nodeRNIDParams=nodeRNIDParams, ficonLIRR=ficonLIRR, rLIRIncidentPID=rLIRIncidentPID, linkIncidentMIBTrapPrefix=linkIncidentMIBTrapPrefix, nodeRNIDEntry=nodeRNIDEntry, rLIRIncidentPortNumber=rLIRIncidentPortNumber, lIRRIndex=lIRRIndex, linkRLIRFailureIncident=linkRLIRFailureIncident, FcPortID=FcPortID, nodeRNIDIncidentPortWWN=nodeRNIDIncidentPortWWN, rLIRLinkFailureType=rLIRLinkFailureType, RNIDTagType=RNIDTagType, lIRRPortType=lIRRPortType, nodeRNIDConnectedPortWWN=nodeRNIDConnectedPortWWN, switchRNIDSequenceNumber=switchRNIDSequenceNumber, switchRNIDManufacturerPlant=switchRNIDManufacturerPlant, linkIncidentMIB=linkIncidentMIB, rLIRTimeStamp=rLIRTimeStamp, nodeRNIDType=nodeRNIDType, nodeRNIDIndex=nodeRNIDIndex)
