#
# PySNMP MIB module LINK-INCIDENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LINK-INCIDENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:07:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
fcSwitch, = mibBuilder.importSymbols("Brocade-REG-MIB", "fcSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Counter32, MibIdentifier, NotificationType, Bits, Integer32, ModuleIdentity, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Counter32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "ModuleIdentity", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
linkIncidentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50))
linkIncidentMIB.setRevisions(('2003-07-11 00:00', '2012-06-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: linkIncidentMIB.setRevisionsDescriptions(('Initial revision', 'Added ficonSlot and ficonPort objects and included it in all ficon traps',))
if mibBuilder.loadTexts: linkIncidentMIB.setLastUpdated('201206040000Z')
if mibBuilder.loadTexts: linkIncidentMIB.setOrganization('Brocade Communications Systems, Inc.,')
if mibBuilder.loadTexts: linkIncidentMIB.setContactInfo('Customer Support Group Brocade Communications Systems, 1745, Technology Drive, San Jose, CA 95110 U.S.A Tel: +1-408-392-6061 Fax: +1-408-392-6656 Email: support@Brocade.COM WEB: www.brocade.com')
if mibBuilder.loadTexts: linkIncidentMIB.setDescription('The MIB module defines support for FICON in Fabos. This MIB addresses link incident and link failure data for ficon host/devices connected to a Brocade switch')
class FcPortID(TextualConvention, OctetString):
    description = 'Represents Fibre Channel Address ID, a 24-bit value unique within the address space of a Fabric.'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class RLIRLinkFailureType(TextualConvention, Integer32):
    description = 'Represents the link failure type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("bitErrorRate", 2), ("lossOfSignal", 3), ("nOSRecognized", 4), ("primitiveSequenceTimeout", 5), ("invalidSeqForPortState", 6), ("loopInitializationTimeout", 7), ("lossOfSignalInLoopInit", 8))

class LinkWwn(TextualConvention, OctetString):
    description = 'Represents the link WWN'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class PortType(TextualConvention, Integer32):
    description = 'Represents the Port Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("n-port", 1), ("nl-port", 2), ("e-port", 3))

class LinkFormat(TextualConvention, Integer32):
    description = 'Represents the frame format'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ficon", 1), ("common", 2))

class RegType(TextualConvention, Integer32):
    description = 'Represents the RNID Registration Type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conditional", 1), ("unconditional", 2))

class LIRRProtocol(TextualConvention, Integer32):
    description = 'Represents the LIRR Protocol'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fcp", 1), ("sb2", 2))

class RNIDTagType(TextualConvention, OctetString):
    description = 'Represents the value of RNID Tag in Hexa Decimal format'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RNIDFlags(TextualConvention, OctetString):
    description = "Represents the value of RNID Flag in Hexa Decimal format. It indicates if the node is valid, not valid, or not current. The ``Flag'' values also indi- cate the following: 0x00 Indicates node ID of the (storage port for RNID, switch for SwitchRNID) is valid. 0x10 Indicates node ID of the chan- nel port is valid. 0x20 Indicates the node ID of the storage port is not current. 0x30 Indicates the node ID of the channel port is not current. 0x40 Indicates the the node ID of the (storage port for RNID, switch for RLIR) is not valid. 0x50 Indicates the node ID of the channel port is not valid."
    status = 'current'
    displayHint = 'x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class RNIDType(TextualConvention, OctetString):
    description = 'Represents the value of Type Number - Displays the type number of the self describing node. It also describes the machine type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class RNIDModel(TextualConvention, OctetString):
    description = 'Represents the value of Model Number.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class RNIDManufacturer(TextualConvention, OctetString):
    description = 'Represents the Manufacturer name or code.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class RNIDManufacturerPlant(TextualConvention, OctetString):
    description = 'The manufacture plant name or code.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class RNIDSequenceNumber(TextualConvention, OctetString):
    description = 'Sequence number of the self describing node.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

class RNIDParams(TextualConvention, OctetString):
    description = "Represents the value of Param. It is the incident node parameters type in three bytes: ``0xAABBCC''. The meaning of each byte is described below: Byte AA: 0x00 Reserved 0x20 FC-SB-2 and updates. 0x40 Other FC-4s including FCP and updates. 0x60 FC-SB-2 and updates and other FC-4s including FCP and updates. 0x80 FC-4 support not specified. 0xa0 Reserved. 0xc0 Reserved. 0xe0 Vendor specific. Byte BB: 0x00 Unspecified class 0x01 Direct access storage device, if it is an storage port. Otherwise, it is not channel to channel capable. 0x02 Magnetic tape, if it is an storage port. Otherwise, if it is a reserved field for a channel port. 0x03 Input unit record, if it is an storage port. Otherwise, it is a reserved field for a channel port. 0x04 Output unit, if it is an stor- age port. Otherwise, it is a reserved field for a channel port. 0x05 Printer, if it is an storage port. Otherwise, it is a reserved field for a channel port. 0x06 Controler, if it is an storage port. Otherwise, it is a reserved field for a channel port. 0x07 Terminal - Full screen if it is an storage port. Otherwise, it is a reserved field for a channel port. 0x08 Terminal - Line mode if it is an storage port. Otherwise, it is an emulated control unit support only. 0x09 Reserved. 0x10 Switch, if it is a switch device. Otherwise, it is reserved. 0x0b 0xff Reserved. Byte CC: 0x00 If storage CU port has regis- tered with the switch. 0xID CHIPID if channel port has registered with the switch. 0xPN If switch has registered with the channel then PN represent the FL port number."
    status = 'current'
    displayHint = 'x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

ficonRNID = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2))
if mibBuilder.loadTexts: ficonRNID.setStatus('current')
if mibBuilder.loadTexts: ficonRNID.setDescription('The OID sub-tree for ficonRNID. This group contains all RNID group objects for FICON.')
nodeRNIDTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDTableNumEntries.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDTableNumEntries.setDescription('The number of entries in Request Node Identification Data (RNID) table.')
nodeRNIDTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2), )
if mibBuilder.loadTexts: nodeRNIDTable.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDTable.setDescription('A table that contains, one entry for each Ficon RNID node attached to a switch.')
nodeRNIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1), ).setIndexNames((0, "LINK-INCIDENT-MIB", "nodeRNIDIndex"))
if mibBuilder.loadTexts: nodeRNIDEntry.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDEntry.setDescription('A entry containing the RNID information for a ficon node')
nodeRNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDIndex.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDIndex.setDescription('Index into nodeRNIDTable')
nodeRNIDIncidentPortWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 2), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDIncidentPortWWN.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDIncidentPortWWN.setDescription('Port WWN for Incident port. An N-port (ficon device or host) is an incident port')
nodeRNIDPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 3), FcPortID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDPID.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDPID.setDescription('PID for an Incident port.')
nodeRNIDFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 4), RNIDFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDFlags.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDFlags.setDescription('RNID flags for an Incident port.')
nodeRNIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 5), RNIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDType.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDType.setDescription('Number associate with a node')
nodeRNIDModel = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 6), RNIDModel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDModel.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDModel.setDescription('Model number of the RNID node')
nodeRNIDManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 7), RNIDManufacturer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDManufacturer.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDManufacturer.setDescription('Identifies the manufaturer of the node.')
nodeRNIDManufacturerPlant = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 8), RNIDManufacturerPlant()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDManufacturerPlant.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDManufacturerPlant.setDescription('Identifies the manufacturer plant of the node.')
nodeRNIDSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 9), RNIDSequenceNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDSequenceNumber.setDescription('Identifies the sequence number of the node.')
nodeRNIDConnectedPortWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 10), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDConnectedPortWWN.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDConnectedPortWWN.setDescription('WWN of the connected port.')
nodeRNIDPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 11), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDPortType.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDPortType.setDescription('Port type (N, E, NL or virtual port) of the connected port.')
nodeRNIDFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 12), LinkFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDFormat.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDFormat.setDescription('Node identification data format of the connected port.')
nodeRNIDTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 13), RNIDTagType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDTag.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDTag.setDescription('Node identification tag of the connected port.')
nodeRNIDParams = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 2, 1, 14), RNIDParams()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeRNIDParams.setStatus('current')
if mibBuilder.loadTexts: nodeRNIDParams.setDescription('Node parameters of the connected port.')
switchRNIDTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDTableNumEntries.setStatus('current')
if mibBuilder.loadTexts: switchRNIDTableNumEntries.setDescription('The number of entries in RNID table which corresponds to switch.')
switchRNIDTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4), )
if mibBuilder.loadTexts: switchRNIDTable.setStatus('current')
if mibBuilder.loadTexts: switchRNIDTable.setDescription('A table that contains, one entry for each switch ficon node.')
switchRNIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1), ).setIndexNames((0, "LINK-INCIDENT-MIB", "switchRNIDIndex"))
if mibBuilder.loadTexts: switchRNIDEntry.setStatus('current')
if mibBuilder.loadTexts: switchRNIDEntry.setDescription('')
switchRNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDIndex.setStatus('current')
if mibBuilder.loadTexts: switchRNIDIndex.setDescription('Index into switchRNIDTable.')
switchRNIDSwitchWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 2), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDSwitchWWN.setStatus('current')
if mibBuilder.loadTexts: switchRNIDSwitchWWN.setDescription('WWN of the switch.')
switchRNIDFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 3), RNIDFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDFlags.setStatus('current')
if mibBuilder.loadTexts: switchRNIDFlags.setDescription('RNID flags for switch.')
switchRNIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 4), RNIDType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDType.setStatus('current')
if mibBuilder.loadTexts: switchRNIDType.setDescription('Type Number associate with a switch.')
switchRNIDModel = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 5), RNIDModel()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDModel.setStatus('current')
if mibBuilder.loadTexts: switchRNIDModel.setDescription('Model number of the RNID switch.')
switchRNIDManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 6), RNIDManufacturer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDManufacturer.setStatus('current')
if mibBuilder.loadTexts: switchRNIDManufacturer.setDescription('Identifies the manufaturer of the switch.')
switchRNIDManufacturerPlant = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 7), RNIDManufacturerPlant()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDManufacturerPlant.setStatus('current')
if mibBuilder.loadTexts: switchRNIDManufacturerPlant.setDescription('Identifies the manufacturer plant of the switch.')
switchRNIDSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 8), RNIDSequenceNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDSequenceNumber.setStatus('current')
if mibBuilder.loadTexts: switchRNIDSequenceNumber.setDescription('Identifies the sequence number of the switch.')
switchRNIDTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 9), RNIDTagType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDTag.setStatus('current')
if mibBuilder.loadTexts: switchRNIDTag.setDescription('Identification tag of the switch.')
switchRNIDParams = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 4, 1, 10), RNIDParams()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchRNIDParams.setStatus('current')
if mibBuilder.loadTexts: switchRNIDParams.setDescription('Parameters of the switch.')
nodeVfId = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeVfId.setStatus('current')
if mibBuilder.loadTexts: nodeVfId.setDescription('The Virtual fabric id of the switch. For VF unaware switches this value will be 0.')
ficonSlot = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ficonSlot.setStatus('current')
if mibBuilder.loadTexts: ficonSlot.setDescription('It indicates the slot number in the switch.')
ficonPort = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ficonPort.setStatus('current')
if mibBuilder.loadTexts: ficonPort.setDescription('It indicates the port number in the switch.')
ficonLIRR = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3))
if mibBuilder.loadTexts: ficonLIRR.setStatus('current')
if mibBuilder.loadTexts: ficonLIRR.setDescription('The OID sub-tree for ficonLIRR. This group contains all LIRR group objects for FICON.')
lIRRTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRTableNumEntries.setStatus('current')
if mibBuilder.loadTexts: lIRRTableNumEntries.setDescription('The number of entries in Link Incident Record Registration (LIRR) table')
lIRRTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2), )
if mibBuilder.loadTexts: lIRRTable.setStatus('current')
if mibBuilder.loadTexts: lIRRTable.setDescription('A table that contains, one entry for each LIRR incident for an attached FICON device.')
lIRREntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1), ).setIndexNames((0, "LINK-INCIDENT-MIB", "lIRRIndex"))
if mibBuilder.loadTexts: lIRREntry.setStatus('current')
if mibBuilder.loadTexts: lIRREntry.setDescription('An entry containing LIRR information.')
lIRRIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRIndex.setStatus('current')
if mibBuilder.loadTexts: lIRRIndex.setDescription('Index into the LIRR table.')
lIRRListenerPortWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 2), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRListenerPortWWN.setStatus('current')
if mibBuilder.loadTexts: lIRRListenerPortWWN.setDescription('WWN of the Listener port.')
lIRRListenerPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 3), FcPortID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRListenerPID.setStatus('current')
if mibBuilder.loadTexts: lIRRListenerPID.setDescription('PID for the listener port.')
lIRRRegType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 4), RegType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRRegType.setStatus('current')
if mibBuilder.loadTexts: lIRRRegType.setDescription('Registration type - conditional or unconditional.')
lIRRProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 5), LIRRProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRProtocol.setStatus('current')
if mibBuilder.loadTexts: lIRRProtocol.setDescription('Protocol type supported.')
lIRRPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 6), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRPortType.setStatus('current')
if mibBuilder.loadTexts: lIRRPortType.setDescription('Attached port type.')
lIRRFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 3, 2, 1, 7), LinkFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lIRRFormat.setStatus('current')
if mibBuilder.loadTexts: lIRRFormat.setDescription('Registration type - conditional or unconditional.')
ficonRLIR = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4))
if mibBuilder.loadTexts: ficonRLIR.setStatus('current')
if mibBuilder.loadTexts: ficonRLIR.setDescription('The OID sub-tree for ficonRLIR. This group contains all RLIR group objects for FICON.')
rLIRTableNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRTableNumEntries.setStatus('current')
if mibBuilder.loadTexts: rLIRTableNumEntries.setDescription('The number of entries in switch Registered Link Incident Report (RLIR) table')
rLIRTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2), )
if mibBuilder.loadTexts: rLIRTable.setStatus('current')
if mibBuilder.loadTexts: rLIRTable.setDescription('A table that contains, one entry for each LIRR incident for an attached FICON device.')
rLIREntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1), ).setIndexNames((0, "LINK-INCIDENT-MIB", "rLIRIndex"))
if mibBuilder.loadTexts: rLIREntry.setStatus('current')
if mibBuilder.loadTexts: rLIREntry.setDescription('An entry containing RLIR information.')
rLIRIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIndex.setStatus('current')
if mibBuilder.loadTexts: rLIRIndex.setDescription('Index into RLIR table.')
rLIRIncidentPortWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 2), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentPortWwn.setStatus('current')
if mibBuilder.loadTexts: rLIRIncidentPortWwn.setDescription('Port WWN for RLIR Incident port.')
rLIRIncidentNodeWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 3), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentNodeWwn.setStatus('current')
if mibBuilder.loadTexts: rLIRIncidentNodeWwn.setDescription('Incident node WWN.')
rLIRIncidentPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 5), PortType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentPortType.setStatus('current')
if mibBuilder.loadTexts: rLIRIncidentPortType.setDescription('RLIR Incident port type.')
rLIRIncidentPID = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 6), FcPortID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentPID.setStatus('current')
if mibBuilder.loadTexts: rLIRIncidentPID.setDescription('RLIR Incident PID.')
rLIRIncidentPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRIncidentPortNumber.setStatus('current')
if mibBuilder.loadTexts: rLIRIncidentPortNumber.setDescription('RLIR Incident port number.This is vendor specific port number.')
rLIRConnectedPortWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 8), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRConnectedPortWwn.setStatus('current')
if mibBuilder.loadTexts: rLIRConnectedPortWwn.setDescription('RLIR Connected port WWN.')
rLIRConnectedNodeWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 9), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRConnectedNodeWwn.setStatus('current')
if mibBuilder.loadTexts: rLIRConnectedNodeWwn.setDescription('RLIR Connected node WWN.')
rLIRFabricWwn = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 10), LinkWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRFabricWwn.setStatus('current')
if mibBuilder.loadTexts: rLIRFabricWwn.setDescription('RLIR Fabric Wwn.')
rLIRLinkFailureType = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 11), RLIRLinkFailureType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRLinkFailureType.setStatus('current')
if mibBuilder.loadTexts: rLIRLinkFailureType.setDescription('RLIR Link failure type.')
rLIRTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRTimeStamp.setStatus('current')
if mibBuilder.loadTexts: rLIRTimeStamp.setDescription('RLIR time stamp.')
rLIRFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 4, 2, 1, 13), LinkFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rLIRFormat.setStatus('current')
if mibBuilder.loadTexts: rLIRFormat.setDescription('RLIR Format.')
linkIncidentMIBTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21))
if mibBuilder.loadTexts: linkIncidentMIBTraps.setStatus('current')
if mibBuilder.loadTexts: linkIncidentMIBTraps.setDescription('The OID sub-tree for Link Incident trap.')
linkIncidentMIBTrapPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0))
if mibBuilder.loadTexts: linkIncidentMIBTrapPrefix.setStatus('current')
if mibBuilder.loadTexts: linkIncidentMIBTrapPrefix.setDescription('The Link Incident traps.')
linkRNIDDeviceRegistration = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 1)).setObjects(("LINK-INCIDENT-MIB", "nodeRNIDIndex"), ("LINK-INCIDENT-MIB", "nodeRNIDIncidentPortWWN"), ("LINK-INCIDENT-MIB", "nodeRNIDConnectedPortWWN"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkRNIDDeviceRegistration.setStatus('current')
if mibBuilder.loadTexts: linkRNIDDeviceRegistration.setDescription(' A device registered with the switch')
linkRNIDDeviceDeRegistration = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 2)).setObjects(("LINK-INCIDENT-MIB", "nodeRNIDIndex"), ("LINK-INCIDENT-MIB", "nodeRNIDIncidentPortWWN"), ("LINK-INCIDENT-MIB", "nodeRNIDConnectedPortWWN"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkRNIDDeviceDeRegistration.setStatus('current')
if mibBuilder.loadTexts: linkRNIDDeviceDeRegistration.setDescription(' A device de-regsitered with the switch')
linkLIRRListenerAdded = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 3)).setObjects(("LINK-INCIDENT-MIB", "lIRRListenerPortWWN"), ("LINK-INCIDENT-MIB", "lIRRListenerPID"), ("LINK-INCIDENT-MIB", "lIRRIndex"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkLIRRListenerAdded.setStatus('current')
if mibBuilder.loadTexts: linkLIRRListenerAdded.setDescription(' A listener for link failure incident is added')
linkLIRRListenerRemoved = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 4)).setObjects(("LINK-INCIDENT-MIB", "lIRRListenerPortWWN"), ("LINK-INCIDENT-MIB", "lIRRListenerPID"), ("LINK-INCIDENT-MIB", "lIRRIndex"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkLIRRListenerRemoved.setStatus('current')
if mibBuilder.loadTexts: linkLIRRListenerRemoved.setDescription(' A listener for link failure incident is removed')
linkRLIRFailureIncident = NotificationType((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 50, 21, 0, 5)).setObjects(("LINK-INCIDENT-MIB", "nodeRNIDIndex"), ("LINK-INCIDENT-MIB", "lIRRIndex"), ("LINK-INCIDENT-MIB", "rLIRIncidentPortWwn"), ("LINK-INCIDENT-MIB", "rLIRConnectedPortWwn"), ("LINK-INCIDENT-MIB", "rLIRIndex"), ("LINK-INCIDENT-MIB", "rLIRLinkFailureType"), ("LINK-INCIDENT-MIB", "lIRRListenerPID"), ("LINK-INCIDENT-MIB", "nodeVfId"), ("LINK-INCIDENT-MIB", "ficonSlot"), ("LINK-INCIDENT-MIB", "ficonPort"))
if mibBuilder.loadTexts: linkRLIRFailureIncident.setStatus('current')
if mibBuilder.loadTexts: linkRLIRFailureIncident.setDescription(' A link failure incident has occured. The value of lIRRIndex will be -2147483647 and lIRRListenerPID will be 0 (zero) , if there is no listener for incident.')
mibBuilder.exportSymbols("LINK-INCIDENT-MIB", switchRNIDSwitchWWN=switchRNIDSwitchWWN, switchRNIDEntry=switchRNIDEntry, switchRNIDTable=switchRNIDTable, RNIDManufacturerPlant=RNIDManufacturerPlant, ficonPort=ficonPort, rLIRLinkFailureType=rLIRLinkFailureType, ficonRLIR=ficonRLIR, switchRNIDParams=switchRNIDParams, switchRNIDTag=switchRNIDTag, rLIRFabricWwn=rLIRFabricWwn, RegType=RegType, linkLIRRListenerAdded=linkLIRRListenerAdded, linkRNIDDeviceDeRegistration=linkRNIDDeviceDeRegistration, nodeRNIDSequenceNumber=nodeRNIDSequenceNumber, rLIRIncidentPortType=rLIRIncidentPortType, rLIRFormat=rLIRFormat, switchRNIDManufacturer=switchRNIDManufacturer, nodeRNIDConnectedPortWWN=nodeRNIDConnectedPortWWN, nodeRNIDTableNumEntries=nodeRNIDTableNumEntries, rLIRIncidentPortNumber=rLIRIncidentPortNumber, nodeRNIDManufacturerPlant=nodeRNIDManufacturerPlant, nodeRNIDPID=nodeRNIDPID, lIRRIndex=lIRRIndex, lIRREntry=lIRREntry, rLIRIncidentPortWwn=rLIRIncidentPortWwn, LinkWwn=LinkWwn, nodeRNIDModel=nodeRNIDModel, rLIRIncidentPID=rLIRIncidentPID, PortType=PortType, lIRRRegType=lIRRRegType, nodeRNIDParams=nodeRNIDParams, nodeRNIDTable=nodeRNIDTable, RNIDType=RNIDType, rLIREntry=rLIREntry, nodeRNIDManufacturer=nodeRNIDManufacturer, nodeRNIDIndex=nodeRNIDIndex, nodeRNIDTag=nodeRNIDTag, switchRNIDTableNumEntries=switchRNIDTableNumEntries, rLIRConnectedNodeWwn=rLIRConnectedNodeWwn, switchRNIDManufacturerPlant=switchRNIDManufacturerPlant, lIRRPortType=lIRRPortType, RNIDTagType=RNIDTagType, RNIDParams=RNIDParams, nodeRNIDPortType=nodeRNIDPortType, ficonLIRR=ficonLIRR, nodeRNIDEntry=nodeRNIDEntry, nodeRNIDFlags=nodeRNIDFlags, switchRNIDModel=switchRNIDModel, lIRRTableNumEntries=lIRRTableNumEntries, rLIRTimeStamp=rLIRTimeStamp, nodeRNIDFormat=nodeRNIDFormat, lIRRFormat=lIRRFormat, lIRRListenerPID=lIRRListenerPID, nodeRNIDIncidentPortWWN=nodeRNIDIncidentPortWWN, switchRNIDSequenceNumber=switchRNIDSequenceNumber, linkIncidentMIB=linkIncidentMIB, lIRRProtocol=lIRRProtocol, linkIncidentMIBTrapPrefix=linkIncidentMIBTrapPrefix, rLIRTableNumEntries=rLIRTableNumEntries, rLIRConnectedPortWwn=rLIRConnectedPortWwn, LinkFormat=LinkFormat, RLIRLinkFailureType=RLIRLinkFailureType, switchRNIDType=switchRNIDType, rLIRIndex=rLIRIndex, switchRNIDFlags=switchRNIDFlags, nodeRNIDType=nodeRNIDType, RNIDManufacturer=RNIDManufacturer, ficonRNID=ficonRNID, RNIDSequenceNumber=RNIDSequenceNumber, ficonSlot=ficonSlot, PYSNMP_MODULE_ID=linkIncidentMIB, RNIDModel=RNIDModel, linkLIRRListenerRemoved=linkLIRRListenerRemoved, switchRNIDIndex=switchRNIDIndex, rLIRIncidentNodeWwn=rLIRIncidentNodeWwn, RNIDFlags=RNIDFlags, linkIncidentMIBTraps=linkIncidentMIBTraps, LIRRProtocol=LIRRProtocol, linkRLIRFailureIncident=linkRLIRFailureIncident, lIRRTable=lIRRTable, FcPortID=FcPortID, linkRNIDDeviceRegistration=linkRNIDDeviceRegistration, nodeVfId=nodeVfId, rLIRTable=rLIRTable, lIRRListenerPortWWN=lIRRListenerPortWWN)
