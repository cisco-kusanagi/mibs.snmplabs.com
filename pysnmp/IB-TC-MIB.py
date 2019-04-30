#
# PySNMP MIB module IB-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IB-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:22:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, Bits, Counter64, IpAddress, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Integer32, Unsigned32, TimeTicks, experimental, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Bits", "Counter64", "IpAddress", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Integer32", "Unsigned32", "TimeTicks", "experimental", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibTcMIB = ModuleIdentity((1, 3, 6, 1, 3, 117, 1))
ibTcMIB.setRevisions(('2006-06-27 00:00',))
if mibBuilder.loadTexts: ibTcMIB.setLastUpdated('200606270000Z')
if mibBuilder.loadTexts: ibTcMIB.setOrganization('IETF IP over IB (IPOIB) Working Group')
infinibandMIB = MibIdentifier((1, 3, 6, 1, 3, 117))
class IbPort(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches and (C18-14.a1) for switch port 0, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 254)

class IbPhysPort(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 254)

class IbPhysPortAndInvalid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class IbDataPort(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    status = 'deprecated'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 254)

class IbDataPortAndInvalid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    status = 'deprecated'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class IbVirtualLane(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 3.5.7.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 15)

class IbDataVirtualLane(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 3.5.7.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 14)

class IbDlid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 4.1.3.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IbUnicastLid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 4.1.3.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 49151)

class IbMulticastLid(TextualConvention, Unsigned32):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 4.1.3.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(49152, 65535)

class IbGuid(TextualConvention, OctetString):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 4.1.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class IbSmaPortList(TextualConvention, OctetString):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches and (C18-14.a1) for switch port 0, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class IbSmPortList(TextualConvention, OctetString):
    reference = 'InfiniBand Architecture Release 1.2 Vol. 1. [IBTAARCH] Section 18.2.4.1 (C18-10.a1) for switches, Section 17.2.1.3 (C17-7.a1) for Channel Adapters, and Section 19.2.4.2 for routers.'
    status = 'deprecated'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class IbIpoibClientIdentifier(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class IbSmSubnetPrefix(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class IbSmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notActive", 0), ("discovering", 1), ("standby", 2), ("master", 3))

class IbNodeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("channelAdapter", 1), ("switch", 2), ("router", 3))

class IbMtu(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("mtu256", 1), ("mtu512", 2), ("mtu1024", 3), ("mtu2048", 4), ("mtu4096", 5))

class IbPartitionKey(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class IbPartition(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 32767)

class IbTransportTime(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 31)

mibBuilder.exportSymbols("IB-TC-MIB", IbSmSubnetPrefix=IbSmSubnetPrefix, IbPhysPort=IbPhysPort, IbTransportTime=IbTransportTime, IbIpoibClientIdentifier=IbIpoibClientIdentifier, IbUnicastLid=IbUnicastLid, IbSmPortList=IbSmPortList, IbMulticastLid=IbMulticastLid, ibTcMIB=ibTcMIB, IbSmState=IbSmState, PYSNMP_MODULE_ID=ibTcMIB, IbDlid=IbDlid, IbGuid=IbGuid, IbPort=IbPort, IbDataPort=IbDataPort, IbDataPortAndInvalid=IbDataPortAndInvalid, IbVirtualLane=IbVirtualLane, IbNodeType=IbNodeType, IbMtu=IbMtu, infinibandMIB=infinibandMIB, IbDataVirtualLane=IbDataVirtualLane, IbPartition=IbPartition, IbPhysPortAndInvalid=IbPhysPortAndInvalid, IbSmaPortList=IbSmaPortList, IbPartitionKey=IbPartitionKey)
