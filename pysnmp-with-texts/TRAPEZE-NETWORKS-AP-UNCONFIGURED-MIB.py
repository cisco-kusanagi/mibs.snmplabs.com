#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, iso, Integer32, Gauge32, ModuleIdentity, Unsigned32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Integer32", "Gauge32", "ModuleIdentity", "Unsigned32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "MibIdentifier", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
TrpzApSerialNum, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApSerialNum")
TrpzPhysPortNumber, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-BASIC-TC", "TrpzPhysPortNumber")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzApUnconfiguredMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 15))
trpzApUnconfiguredMib.setRevisions(('2011-06-15 00:11', '2008-11-14 00:04',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzApUnconfiguredMib.setRevisionsDescriptions(('v1.1.1: Revised for 7.5 release', 'v1.0.4: Initial version, for 7.1 release',))
if mibBuilder.loadTexts: trpzApUnconfiguredMib.setLastUpdated('201106150011Z')
if mibBuilder.loadTexts: trpzApUnconfiguredMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzApUnconfiguredMib.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzApUnconfiguredMib.setDescription("Unconfigured/orphan APs info for Trapeze Networks wireless switches. AP = Access Point; AC = Access Controller (wireless switch), the device that runs a SNMP Agent implementing this MIB. Orphan AP = an AP currently detected by this AC but not managed by any AC. Copyright 2008-2011 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzApUnconfiguredOrphanReason(TextualConvention, Integer32):
    description = "Enumeration of the reasons why an AP could be unconfigured/orphan: no-configuration: the AC has no configuration corresponding to that AP; ap-license-exceeded: AP license capacity exceeded; controller-behind-nat: the AC is behind NAT, and cannot suggest another AC for that AP to attach to (the first AC does not know what the AP's view of the public IP address of the other AC is); ap-model-mismatch: AP model does not match configuration; no-macs: the AC must allocate MAC address for that AP but no MAC is available."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("no-configuration", 2), ("ap-license-exceeded", 3), ("controller-behind-nat", 4), ("ap-model-mismatch", 5), ("no-macs", 6))

trpzApUnconfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1))
trpzApUnconfOrphanTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2), )
if mibBuilder.loadTexts: trpzApUnconfOrphanTable.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanTable.setDescription("A table describing all the APs currently detected by this AC but not managed by any AC. Such APs are reported as ''unconfigured'' or ''orphan'' in other management interfaces of the AC (CLI, Web etc).")
trpzApUnconfOrphanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApSerialNum"))
if mibBuilder.loadTexts: trpzApUnconfOrphanEntry.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanEntry.setDescription('Information about a particular orphan AP detected by this AC.')
trpzApUnconfOrphanApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 1), TrpzApSerialNum())
if mibBuilder.loadTexts: trpzApUnconfOrphanApSerialNum.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanApSerialNum.setDescription('The Serial Number of this orphan AP.')
trpzApUnconfOrphanApModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanApModelName.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanApModelName.setDescription('The Model name of this orphan AP.')
trpzApUnconfOrphanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanIpAddress.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanIpAddress.setDescription('The IPv4 Address of this orphan AP.')
trpzApUnconfOrphanPhysPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 6), TrpzPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanPhysPortNum.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanPhysPortNum.setDescription('The Number of the Physical Port on which this orphan AP was detected by the AC (usually the uplink port going to other switches/routers connecting this AP to the network).')
trpzApUnconfOrphanVLANName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanVLANName.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanVLANName.setDescription('Identifies the VLAN containing this orphan AP. This is the VLAN Name as configured on this AC (another AC might have a different name corresponding to same VLAN tag used in the network).')
trpzApUnconfOrphanReason = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 15, 1, 2, 1, 8), TrpzApUnconfiguredOrphanReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApUnconfOrphanReason.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanReason.setDescription('The reason why this AP is orphan.')
trpzApUnconfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2))
trpzApUnconfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1))
trpzApUnconfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2))
trpzApUnconfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApUnconfCompliance = trpzApUnconfCompliance.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfCompliance.setDescription('The compliance statement for devices that implement AP Unconfigured MIB.')
trpzApUnconfOrphanBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 15, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanApModelName"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanIpAddress"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanPhysPortNum"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanVLANName"), ("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", "trpzApUnconfOrphanReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApUnconfOrphanBasicGroup = trpzApUnconfOrphanBasicGroup.setStatus('current')
if mibBuilder.loadTexts: trpzApUnconfOrphanBasicGroup.setDescription('Mandatory group of objects implemented to provide info about Orphan APs.')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-UNCONFIGURED-MIB", trpzApUnconfOrphanApModelName=trpzApUnconfOrphanApModelName, trpzApUnconfOrphanTable=trpzApUnconfOrphanTable, trpzApUnconfOrphanVLANName=trpzApUnconfOrphanVLANName, trpzApUnconfOrphanReason=trpzApUnconfOrphanReason, trpzApUnconfOrphanBasicGroup=trpzApUnconfOrphanBasicGroup, trpzApUnconfOrphanEntry=trpzApUnconfOrphanEntry, trpzApUnconfGroups=trpzApUnconfGroups, PYSNMP_MODULE_ID=trpzApUnconfiguredMib, trpzApUnconfOrphanIpAddress=trpzApUnconfOrphanIpAddress, trpzApUnconfCompliance=trpzApUnconfCompliance, TrpzApUnconfiguredOrphanReason=TrpzApUnconfiguredOrphanReason, trpzApUnconfConformance=trpzApUnconfConformance, trpzApUnconfOrphanPhysPortNum=trpzApUnconfOrphanPhysPortNum, trpzApUnconfMibObjects=trpzApUnconfMibObjects, trpzApUnconfCompliances=trpzApUnconfCompliances, trpzApUnconfiguredMib=trpzApUnconfiguredMib, trpzApUnconfOrphanApSerialNum=trpzApUnconfOrphanApSerialNum)
