#
# PySNMP MIB module NTWS-AP-UNCONFIGURED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-AP-UNCONFIGURED-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NtwsApSerialNum, = mibBuilder.importSymbols("NTWS-AP-TC", "NtwsApSerialNum")
NtwsPhysPortNumber, = mibBuilder.importSymbols("NTWS-BASIC-TC", "NtwsPhysPortNumber")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Counter32, NotificationType, Gauge32, MibIdentifier, Unsigned32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "Unsigned32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "IpAddress", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntwsApUnconfiguredMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15))
ntwsApUnconfiguredMib.setRevisions(('2008-11-14 00:04',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setRevisionsDescriptions(('v1.0.4: Initial version',))
if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setLastUpdated('200811140004Z')
if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsApUnconfiguredMib.setDescription("Unconfigured/orphan APs info for Nortel Networks wireless switches. AP = Access Point; AC = Access Controller (wireless switch), the device that runs a SNMP Agent implementing this MIB. Orphan AP = an AP currently detected by this AC but not managed by any AC. Copyright 2008 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsApUnconfiguredOrphanReason(TextualConvention, Integer32):
    description = "Enumeration of the reasons why an AP could be unconfigured/orphan: no-configuration: the AC has no configuration corresponding to that AP; ap-license-exceeded: AP license capacity exceeded; controller-behind-nat: the AC is behind NAT, and cannot suggest another AC for that AP to attach to (the first AC does not know what the AP's view of the public IP address of the other AC is); ap-model-mismatch: AP model does not match configuration; no-macs: the AC must allocate MAC address for that AP but no MAC is available."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("no-configuration", 2), ("ap-license-exceeded", 3), ("controller-behind-nat", 4), ("ap-model-mismatch", 5), ("no-macs", 6))

ntwsApUnconfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1))
ntwsApUnconfOrphanTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2), )
if mibBuilder.loadTexts: ntwsApUnconfOrphanTable.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanTable.setDescription("A table describing all the APs currently detected by this AC but not managed by any AC. Such APs are reported as ''unconfigured'' or ''orphan'' in other management interfaces of the AC (CLI, Web etc).")
ntwsApUnconfOrphanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1), ).setIndexNames((0, "NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanApSerialNum"))
if mibBuilder.loadTexts: ntwsApUnconfOrphanEntry.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanEntry.setDescription('Information about a particular orphan AP detected by this AC.')
ntwsApUnconfOrphanApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 1), NtwsApSerialNum())
if mibBuilder.loadTexts: ntwsApUnconfOrphanApSerialNum.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanApSerialNum.setDescription('The Serial Number of this orphan AP.')
ntwsApUnconfOrphanApModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanApModelName.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanApModelName.setDescription('The Model name of this orphan AP.')
ntwsApUnconfOrphanIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanIpAddress.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanIpAddress.setDescription('The IPv4 Address of this orphan AP.')
ntwsApUnconfOrphanPhysPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 6), NtwsPhysPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanPhysPortNum.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanPhysPortNum.setDescription('The Number of the Physical Port on which this orphan AP was detected by the AC (usually the uplink port going to other switches/routers connecting this AP to the network).')
ntwsApUnconfOrphanVLANName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanVLANName.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanVLANName.setDescription('Identifies the VLAN containing this orphan AP. This is the VLAN Name as configured on this AC (another AC might have a different name corresponding to same VLAN tag used in the network).')
ntwsApUnconfOrphanReason = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 1, 2, 1, 8), NtwsApUnconfiguredOrphanReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApUnconfOrphanReason.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanReason.setDescription('The reason why this AP is orphan.')
ntwsApUnconfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2))
ntwsApUnconfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 1))
ntwsApUnconfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 2))
ntwsApUnconfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 1, 1)).setObjects(("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApUnconfCompliance = ntwsApUnconfCompliance.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfCompliance.setDescription('The compliance statement for devices that implement AP Unconfigured MIB.')
ntwsApUnconfOrphanBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 15, 2, 2, 1)).setObjects(("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanApModelName"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanIpAddress"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanPhysPortNum"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanVLANName"), ("NTWS-AP-UNCONFIGURED-MIB", "ntwsApUnconfOrphanReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApUnconfOrphanBasicGroup = ntwsApUnconfOrphanBasicGroup.setStatus('current')
if mibBuilder.loadTexts: ntwsApUnconfOrphanBasicGroup.setDescription('Mandatory group of objects implemented to provide info about Orphan APs.')
mibBuilder.exportSymbols("NTWS-AP-UNCONFIGURED-MIB", ntwsApUnconfCompliance=ntwsApUnconfCompliance, ntwsApUnconfConformance=ntwsApUnconfConformance, ntwsApUnconfOrphanApSerialNum=ntwsApUnconfOrphanApSerialNum, PYSNMP_MODULE_ID=ntwsApUnconfiguredMib, ntwsApUnconfOrphanApModelName=ntwsApUnconfOrphanApModelName, ntwsApUnconfOrphanVLANName=ntwsApUnconfOrphanVLANName, ntwsApUnconfOrphanTable=ntwsApUnconfOrphanTable, ntwsApUnconfCompliances=ntwsApUnconfCompliances, ntwsApUnconfGroups=ntwsApUnconfGroups, ntwsApUnconfOrphanReason=ntwsApUnconfOrphanReason, ntwsApUnconfOrphanIpAddress=ntwsApUnconfOrphanIpAddress, ntwsApUnconfOrphanBasicGroup=ntwsApUnconfOrphanBasicGroup, ntwsApUnconfiguredMib=ntwsApUnconfiguredMib, ntwsApUnconfOrphanEntry=ntwsApUnconfOrphanEntry, NtwsApUnconfiguredOrphanReason=NtwsApUnconfiguredOrphanReason, ntwsApUnconfOrphanPhysPortNum=ntwsApUnconfOrphanPhysPortNum, ntwsApUnconfMibObjects=ntwsApUnconfMibObjects)
