#
# PySNMP MIB module BROCADE-VCS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BROCADE-VCS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
bcsiModules, = mibBuilder.importSymbols("Brocade-REG-MIB", "bcsiModules")
FcWwn, = mibBuilder.importSymbols("Brocade-TC", "FcWwn")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, IpAddress, Integer32, ObjectIdentity, MibIdentifier, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, iso, Gauge32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Integer32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "iso", "Gauge32", "Counter32", "NotificationType")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
brocadeVcsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6))
brocadeVcsMIB.setRevisions(('2015-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: brocadeVcsMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: brocadeVcsMIB.setLastUpdated('201504080000Z')
if mibBuilder.loadTexts: brocadeVcsMIB.setOrganization('Brocade Communications Systems Inc.')
if mibBuilder.loadTexts: brocadeVcsMIB.setContactInfo('130 Holger Way, San Jose, CA 95134 USA. Phone: +1-408-333-8000 Email: vivekk@brocade.com')
if mibBuilder.loadTexts: brocadeVcsMIB.setDescription('The MIB module for the monitoring of VCS fabrics. VCS fabrics is a proprietary technology of Brocade. A VCS fabric consists of a set of inter-connected Brocade VDX switches. These set of switches together behave like a single L2 switch to the outside world. The cluster can operate in 2 modes: fabric mode and Logical chassis mode. In fabric mode, the switches together behave like a single L2 switch - but configuration on each switch is independent of the other. In logical chassis mode, one switch in the fabric is elected as the principal switch. All configurations need to be done only from the principal switch. This is synced across to all the switches in the fabric. Thus the configuration information is the same on all the switches.')
brocadeVcsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1))
brocadeVcsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2))
class VcsConfigMode(TextualConvention, Integer32):
    description = 'The configuration mode that is in effect in the VCS fabric. local(1) - configuration is local to the switch. distributed(2) - configuration is to be done from the principal switch and will be the same across all the switches in the fabric.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("local", 1), ("distributed", 2))

class VcsOperationMode(TextualConvention, Integer32):
    description = 'The operational mode of the fabric. fabricCluster(1) - the entire set of switches in the cluster behaves like a single L2 switch to the outer world. However, configuration is local to each switch. logicalChassis(2) - in this case the fabric behaves like a single L2 switch and the configuration is driven from the principal switch and is the same across all switches in the fabric.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fabricCluster", 1), ("logicalChassis", 2))

class VcsIdentifier(TextualConvention, Unsigned32):
    description = 'A number that uniquely identifies a fabric. Two different fabrics would have different identifiers.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8192)

class VcsRbridgeId(TextualConvention, Unsigned32):
    description = 'A number that uniquely identifies a switch within a fabric.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 239)

class VcsClusterCondition(TextualConvention, Integer32):
    description = 'The state of the fabric as a whole. good(1) - indicates that all switches are in good condition and cluster is fine. degraded(2) - indicates that one or more switches are offline and cluster has degraded. error(3) - Internal error state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("good", 1), ("degraded", 2), ("error", 3))

vcsConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 1), VcsConfigMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsConfigMode.setStatus('current')
if mibBuilder.loadTexts: vcsConfigMode.setDescription('The configuration mode of this cluster that is in effect.')
vcsModeOfOperation = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 2), VcsOperationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsModeOfOperation.setStatus('current')
if mibBuilder.loadTexts: vcsModeOfOperation.setDescription('The operational mode of this cluster.')
vcsIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 3), VcsIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsIdentifier.setStatus('current')
if mibBuilder.loadTexts: vcsIdentifier.setDescription('The unique identifier of this cluster.')
vcsVirtualIpV4Address = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpV4Address.setStatus('current')
if mibBuilder.loadTexts: vcsVirtualIpV4Address.setDescription('The virtual IPv4 address of the cluster. Management stations can use this address to send requests.')
vcsVirtualIpV6Address = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpV6Address.setStatus('current')
if mibBuilder.loadTexts: vcsVirtualIpV6Address.setDescription('The virtual IPv6 address of the cluster. Management stations can use this address to send requests.')
vcsVirtualIpAssociatedRbridgeId = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 6), VcsRbridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpAssociatedRbridgeId.setStatus('current')
if mibBuilder.loadTexts: vcsVirtualIpAssociatedRbridgeId.setDescription('The rbridge-id of the switch that hosts the virtual IP address.')
vcsVirtualIpInterfaceId = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpInterfaceId.setStatus('current')
if mibBuilder.loadTexts: vcsVirtualIpInterfaceId.setDescription('The interface Id that is configured in the case of inband configuration. If it is not inband configuration, then this object will contain the value 0.')
vcsVirtualIpV4OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpV4OperStatus.setStatus('current')
if mibBuilder.loadTexts: vcsVirtualIpV4OperStatus.setDescription('The operational status of the virtual IPv4 address.')
vcsVirtualIpV6OperStatus = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsVirtualIpV6OperStatus.setStatus('current')
if mibBuilder.loadTexts: vcsVirtualIpV6OperStatus.setDescription('The operational status of the virtual IPv6 address.')
vcsNumNodesInCluster = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsNumNodesInCluster.setStatus('current')
if mibBuilder.loadTexts: vcsNumNodesInCluster.setDescription('The number of switches in the cluster that are currently online.')
vcsClusterCondition = MibScalar((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 11), VcsClusterCondition()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsClusterCondition.setStatus('current')
if mibBuilder.loadTexts: vcsClusterCondition.setDescription('The condition of the cluster as a whole.')
vcsFabricIslTable = MibTable((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12), )
if mibBuilder.loadTexts: vcsFabricIslTable.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslTable.setDescription('This table contains all the ISLs (Inter Switch Link) on the local device.')
vcsFabricIslEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1), ).setIndexNames((0, "BROCADE-VCS-MIB", "vcsFabricIslIndex"))
if mibBuilder.loadTexts: vcsFabricIslEntry.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslEntry.setDescription('Represents a single Inter Switch Link (ISL) on this switch.')
vcsFabricIslIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 1), Unsigned32())
if mibBuilder.loadTexts: vcsFabricIslIndex.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslIndex.setDescription('A unique id to distinguish this ISL from others on the local device.')
vcsFabricIslIntfName = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslIntfName.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslIntfName.setDescription('The interface name (ifName) of the interface on which the ISL is formed on this switch.')
vcsFabricIslNbrIntfName = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslNbrIntfName.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslNbrIntfName.setDescription('The interface name (ifName) of the interface on the neighboring switch for this ISL.')
vcsFabricIslNbrWWN = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 4), FcWwn()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslNbrWWN.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslNbrWWN.setDescription('The World Wide Name (WWN) of the neighboring switch for this ISL.')
vcsFabricIslNbrName = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslNbrName.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslNbrName.setDescription('The name of the neighboring switch on which this ISL is formed.')
vcsFabricIslBW = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 6), Unsigned32()).setUnits('megabytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslBW.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslBW.setDescription('The band-width of this ISL.')
vcsFabricIslIsTrunk = MibTableColumn((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 1, 12, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcsFabricIslIsTrunk.setStatus('current')
if mibBuilder.loadTexts: vcsFabricIslIsTrunk.setDescription('An indication whether this ISL is a trunk interface. A value of true(1) means it is a trunk. A value of false(2) means it is not a trunk.')
brocadeVcsConformanceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 1))
brocadeVcsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 2))
brocadeVcsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 2, 1)).setObjects(("BROCADE-VCS-MIB", "brocadeVcsObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeVcsCompliance = brocadeVcsCompliance.setStatus('current')
if mibBuilder.loadTexts: brocadeVcsCompliance.setDescription('The compliance information for this MIB.')
brocadeVcsObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1588, 3, 1, 6, 2, 1, 1)).setObjects(("BROCADE-VCS-MIB", "vcsConfigMode"), ("BROCADE-VCS-MIB", "vcsModeOfOperation"), ("BROCADE-VCS-MIB", "vcsIdentifier"), ("BROCADE-VCS-MIB", "vcsVirtualIpV4Address"), ("BROCADE-VCS-MIB", "vcsVirtualIpV6Address"), ("BROCADE-VCS-MIB", "vcsVirtualIpAssociatedRbridgeId"), ("BROCADE-VCS-MIB", "vcsVirtualIpInterfaceId"), ("BROCADE-VCS-MIB", "vcsVirtualIpV4OperStatus"), ("BROCADE-VCS-MIB", "vcsVirtualIpV6OperStatus"), ("BROCADE-VCS-MIB", "vcsNumNodesInCluster"), ("BROCADE-VCS-MIB", "vcsClusterCondition"), ("BROCADE-VCS-MIB", "vcsFabricIslIndex"), ("BROCADE-VCS-MIB", "vcsFabricIslIntfName"), ("BROCADE-VCS-MIB", "vcsFabricIslNbrIntfName"), ("BROCADE-VCS-MIB", "vcsFabricIslNbrWWN"), ("BROCADE-VCS-MIB", "vcsFabricIslNbrName"), ("BROCADE-VCS-MIB", "vcsFabricIslBW"), ("BROCADE-VCS-MIB", "vcsFabricIslIsTrunk"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    brocadeVcsObjectsGroup = brocadeVcsObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: brocadeVcsObjectsGroup.setDescription('The MIB objects related to VCS monitoring.')
mibBuilder.exportSymbols("BROCADE-VCS-MIB", vcsVirtualIpV4Address=vcsVirtualIpV4Address, vcsIdentifier=vcsIdentifier, vcsModeOfOperation=vcsModeOfOperation, brocadeVcsMIBObjects=brocadeVcsMIBObjects, vcsFabricIslBW=vcsFabricIslBW, vcsFabricIslIndex=vcsFabricIslIndex, vcsFabricIslNbrIntfName=vcsFabricIslNbrIntfName, PYSNMP_MODULE_ID=brocadeVcsMIB, VcsOperationMode=VcsOperationMode, vcsVirtualIpV6OperStatus=vcsVirtualIpV6OperStatus, brocadeVcsCompliances=brocadeVcsCompliances, VcsConfigMode=VcsConfigMode, vcsVirtualIpInterfaceId=vcsVirtualIpInterfaceId, brocadeVcsConformanceGroups=brocadeVcsConformanceGroups, vcsNumNodesInCluster=vcsNumNodesInCluster, VcsIdentifier=VcsIdentifier, brocadeVcsMIBConformance=brocadeVcsMIBConformance, vcsFabricIslIsTrunk=vcsFabricIslIsTrunk, vcsFabricIslIntfName=vcsFabricIslIntfName, vcsFabricIslNbrName=vcsFabricIslNbrName, vcsFabricIslEntry=vcsFabricIslEntry, vcsClusterCondition=vcsClusterCondition, vcsFabricIslTable=vcsFabricIslTable, brocadeVcsObjectsGroup=brocadeVcsObjectsGroup, vcsConfigMode=vcsConfigMode, vcsVirtualIpAssociatedRbridgeId=vcsVirtualIpAssociatedRbridgeId, VcsClusterCondition=VcsClusterCondition, vcsVirtualIpV4OperStatus=vcsVirtualIpV4OperStatus, vcsVirtualIpV6Address=vcsVirtualIpV6Address, vcsFabricIslNbrWWN=vcsFabricIslNbrWWN, brocadeVcsCompliance=brocadeVcsCompliance, brocadeVcsMIB=brocadeVcsMIB, VcsRbridgeId=VcsRbridgeId)
