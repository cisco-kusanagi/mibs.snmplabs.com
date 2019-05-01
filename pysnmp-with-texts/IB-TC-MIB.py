#
# PySNMP MIB module IB-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IB-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:39:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, ObjectIdentity, experimental, MibIdentifier, Bits, IpAddress, Counter32, NotificationType, Unsigned32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "ObjectIdentity", "experimental", "MibIdentifier", "Bits", "IpAddress", "Counter32", "NotificationType", "Unsigned32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibTcMIB = ModuleIdentity((1, 3, 6, 1, 3, 117, 1))
ibTcMIB.setRevisions(('2006-06-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibTcMIB.setRevisionsDescriptions(('Initial version published as part of RFC XXXX.',))
if mibBuilder.loadTexts: ibTcMIB.setLastUpdated('200606270000Z')
if mibBuilder.loadTexts: ibTcMIB.setOrganization('IETF IP over IB (IPOIB) Working Group')
if mibBuilder.loadTexts: ibTcMIB.setContactInfo('Hal Rosenstock Postal: HNR Consulting 200 Old Harvard Road Boxboro MA 01719-1834 United States Email: hnrose@earthlink.net Email comments to the IPOIB WG Mailing List at ipoverib@ietf.org.')
if mibBuilder.loadTexts: ibTcMIB.setDescription('Copyright (C) The Internet Society (2006). The initial version of this MIB module was published in RFC XXXX; for full legal notices see the RFC itself. Supplementary information may be available on http://www.ietf.org/copyrights/ianamib.html. This MIB contains managed object definitions and textual conventions for managing InfiniBand devices that support the IP Over InfiniBand (IPOIB) protocols and procedures.')
infinibandMIB = MibIdentifier((1, 3, 6, 1, 3, 117))
class IbPort(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches and (C18-14.a1) for switch port 0, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    description = 'Identifies an InfiniBand (IB) Port. The InfiniBand Architecture (IBA) defines a maximum of 254 physical ports numbered Port 1 to Port 254. A port is the location on a Channel Adapter, IB Router, or IB Switch to which a link is connected. If a device has N ports, the physical ports are always numbered from 1 to N. The relationship between an InfiniBand port and an ifIndex is one-to-one. As such, the value of an ifIndex object instance can be directly used to identify corresponding instances of the objects defined herein as IB ports. Note: this definition does include enhanced switch port 0 but not base switch port 0. In the case of a switch with enhanced switch port 0, the ifIndex is offset by 1 from the ibPort. In all other cases, the ifIndex is identical to the ibPort.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 254)

class IbPhysPort(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    description = 'Identifies a physical InfiniBand (IB) Port. The InfiniBand Architecture (IBA) defines a maximum of 254 physical ports numbered Port 1 to Port 254. A port is the location on a Channel Adapter, IB Router, or IB Switch to which a link is connected. If a device has N ports, the ports are always numbered from 1 to N. Note: this definition does NOT include switch Port 0, which is not a physical port.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 254)

class IbPhysPortAndInvalid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    description = 'Identifies a physical IB port plus an invalid port number. The invalid port number has a value of 255. Note: this definition does NOT include switch logical Port 0, which is not a physical port.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class IbDataPort(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    description = 'Identifies a physical InfiniBand (IB) Port. The InfiniBand Architecture (IBA) defines a maximum of 254 physical ports numbered Port 1 to Port 254. A port is the location on a Channel Adapter, IB Router, or IB Switch to which a link is connected. If a device has N ports, the ports are always numbered from 1 to N. The relationship between an InfiniBand port and an ifIndex is one-to-one. As such, the value of an ifIndex object instance can be directly used to identify corresponding instances of the objects defined herein as IB data ports. Note: this definition does NOT include logical Port 0, which is reserved for IB management packets.'
    status = 'deprecated'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 254)

class IbDataPortAndInvalid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    description = 'Identifies a physical IB port plus an invalid port number. The invalid port number has a value of 255. Note: this definition does NOT include logical Port 0, which is reserved for IB management packets.'
    status = 'deprecated'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class IbVirtualLane(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 3.5.7.'
    description = 'Identifies a Virtual Lane (VL) instance on a given interface (i.e., IB port). VLs provide a mechanism for creating multiple virtual links within a physical link. IBA defines VL 0 through VL 14 for data and VL 15 exclusively for Subnet Management. The actual data VLs that a port uses are configured by the Subnet Manager. The default data VL is always VL 0.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class IbDataVirtualLane(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 3.5.7.'
    description = 'Identifies a Data Virtual Lane instance on a given interface (i.e., IB port). This TC definition excludes the management Virtual Lane (VL 15). The actual data VLs that a port uses are configured by the Subnet Manager. The default data VL is always the first VL (VL 0).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 14)

class IbDlid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 4.1.3.'
    description = 'Identifies the Destination Local Identifier (DLID). The IBA defines LID 0 as reserved and valid Local Identifier (LID) values from 1 to 65535. LID 65535 is defined as a permissive DLID. This value is stored in IBA defined bit order, that is, the high-order bit of the Local Identifier byte 0 is positioned as the high-order bit of the first byte of the integer representation.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IbUnicastLid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 4.1.3.'
    description = 'Identifies a Unicast LID. Value is stored in IBA defined bit order, that is, the high-order bit of the Local Identifier byte 0 is positioned as the high-order bit of the first byte of the integer representation.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 49151)

class IbMulticastLid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 4.1.3.'
    description = 'Identifies a Multicast LID. Value is stored in IBA defined bit order, that is, the high-order bit of the Local Identifier byte 0 is positioned as the high-order bit of the first byte of the integer representation.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(49152, 65535)

class IbGuid(TextualConvention, OctetString):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 4.1.'
    description = 'Globally Unique Identifier (GUID) is a number that uniquely identifies an IB device or component. It is a compliant IEEE-defined 64-bit extended unique identifier (EUI-64) for Host Channel Adapters (HCA), Terminal Channel Adpaters (TCA), routers, and switches. This 64-bit value is created by concatenating a 24-bit company ID value and a 40-bit extension. The IEEE Registration Authority assigns the company ID. The extension ID is assigned by the particular company. Each HCA, TCA, switch, and router as well as each endport shall be assigned an EUI-64 GUID by the manufacturer.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class IbSmaPortList(TextualConvention, OctetString):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches and (C18-14.a1) for switch port 0, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    description = 'Each bit mapping within this value specifies a port presence within the managed IB device. This definition includes bit0 as IB Port 0, the switch management port. Valid physical port mappings are from bit1 to bit254. Bit255 is invalid and MUST always be zero.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class IbSmPortList(TextualConvention, OctetString):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    description = 'Each bit mapping within this value specifies a port presence within the managed IB device. This definition includes bit0 as IB Port 0, the logical port used exclusively for management packets. Valid data port mappings are from bit1 to bit254. Bit255 is invalid and MUST always be zero.'
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class IbIpoibClientIdentifier(TextualConvention, OctetString):
    description = "The IPOIB Client Identifier uniquely identifies an IPOIB link layer address associated with the InfiniBand port. It comprises three fields. 1. Global Identifier (GID) 2. Queue Pair Number field (QPN) 3. reserved 0 1 2 3 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ |1:GID(0-7) |2:GID(8-15) |3:GID(16-23) |4:GID(24-31) | +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ |5:GID(32-39) |6:GID(40-47) |7:GID(48-55) |8:GID(56-63) | +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ |9:GID(64-71) |10:GID(72-79) |11:GID(80-87) |12:GID(88-95) | +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ |13:GID(96-103) |14:GID(104-111)|15:GID(112-119)|16:GID(120-127)| +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ |17:QPN(0-7) |18:QPN(8-15) |19:QPN(16-23) |20:(reserved) | +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ The Global Identifier field is a 16 octet field (octets 1 through 16) that is formed by the combination of the IB subnet prefix and the port's GUID. It is unique in the InfiniBand fabric. NOTE: An IPOIB interface may have more than 1 GID associated with it. The Queue Pair Number field is a 3 octet field (octets 17, 18, & 19) that identifies the destination queue pair. Note: The reserved field and the QPN field are collectively referred to as the interface-id. If an IPOIB interface has only 1 GID associated with it, the interface-id MAY contain all zeroes. The reserved field is octet 20. It is reserved for future use. These bits SHOULD be set to zero."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class IbSmSubnetPrefix(TextualConvention, OctetString):
    description = 'The 64-bit value used to identify an InfiniBand subnet.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class IbSmState(TextualConvention, Integer32):
    description = "Subnet Manager's state: notActive(0) SM is not active discovering(1) SM is discovering subnet standby(2) SM is in standby role master(3) SM is in master role."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notActive", 0), ("discovering", 1), ("standby", 2), ("master", 3))

class IbNodeType(TextualConvention, Integer32):
    description = 'Type of InfiniBand node.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("channelAdapter", 1), ("switch", 2), ("router", 3))

class IbMtu(TextualConvention, Integer32):
    description = 'The MTU size of this InfiniBand link.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("mtu256", 1), ("mtu512", 2), ("mtu1024", 3), ("mtu2048", 4), ("mtu4096", 5))

class IbPartitionKey(TextualConvention, Unsigned32):
    description = 'The 16-bit Partition Key.'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IbPartition(TextualConvention, Unsigned32):
    description = 'The 15-bit Partition Key Base (without the membership bit).'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 32767)

class IbTransportTime(TextualConvention, Unsigned32):
    description = 'The time value used to calculate the InfiniBand network delay or response. The duration of time is calculated by the following formula: delay/response = (4.096 microseconds * 2 ^ IbTransportTime).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

mibBuilder.exportSymbols("IB-TC-MIB", IbDataPort=IbDataPort, IbSmState=IbSmState, IbUnicastLid=IbUnicastLid, infinibandMIB=infinibandMIB, IbPhysPortAndInvalid=IbPhysPortAndInvalid, IbIpoibClientIdentifier=IbIpoibClientIdentifier, IbPartitionKey=IbPartitionKey, IbDlid=IbDlid, IbTransportTime=IbTransportTime, IbSmPortList=IbSmPortList, IbSmSubnetPrefix=IbSmSubnetPrefix, IbPhysPort=IbPhysPort, PYSNMP_MODULE_ID=ibTcMIB, ibTcMIB=ibTcMIB, IbMtu=IbMtu, IbGuid=IbGuid, IbDataPortAndInvalid=IbDataPortAndInvalid, IbPartition=IbPartition, IbSmaPortList=IbSmaPortList, IbMulticastLid=IbMulticastLid, IbNodeType=IbNodeType, IbVirtualLane=IbVirtualLane, IbDataVirtualLane=IbDataVirtualLane, IbPort=IbPort)
