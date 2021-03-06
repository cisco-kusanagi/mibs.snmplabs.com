#
# PySNMP MIB module MARVELL-rldot1q-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-rldot1q-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, dot1qTpFdbEntry, dot1qStaticUnicastEntry = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "dot1qTpFdbEntry", "dot1qStaticUnicastEntry")
rlpBridgeMIBObjects, = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rlpBridgeMIBObjects")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, Integer32, Bits, IpAddress, Unsigned32, Counter32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Integer32", "Bits", "IpAddress", "Unsigned32", "Counter32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "TimeTicks", "Gauge32")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
rlq_bridge_mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 57, 8)).setLabel("rlq-bridge-mib")
rlq_bridge_mib.setRevisions(('2008-11-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlq_bridge_mib.setRevisionsDescriptions(('The private MIB module definition for dot1q MIBs.',))
if mibBuilder.loadTexts: rlq_bridge_mib.setLastUpdated('200811250000Z')
if mibBuilder.loadTexts: rlq_bridge_mib.setOrganization('MARVELL Semiconductor, Inc.')
if mibBuilder.loadTexts: rlq_bridge_mib.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlq_bridge_mib.setDescription('<description>')
rldot1q = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 57, 8))
rldot1qStaticUnicastTable = MibTable((1, 3, 6, 1, 4, 1, 89, 57, 8, 1), )
if mibBuilder.loadTexts: rldot1qStaticUnicastTable.setStatus('current')
if mibBuilder.loadTexts: rldot1qStaticUnicastTable.setDescription('An augmentation to dot1qStaticUnicastTable')
rldot1qStaticUnicastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 57, 8, 1, 1), )
dot1qStaticUnicastEntry.registerAugmentions(("MARVELL-rldot1q-MIB", "rldot1qStaticUnicastEntry"))
rldot1qStaticUnicastEntry.setIndexNames(*dot1qStaticUnicastEntry.getIndexNames())
if mibBuilder.loadTexts: rldot1qStaticUnicastEntry.setStatus('current')
if mibBuilder.loadTexts: rldot1qStaticUnicastEntry.setDescription('An augmentation to dot1qStaticUnicastEntry')
rldot1qStaticUnicastAddressOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 57, 8, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("learned", 2))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rldot1qStaticUnicastAddressOwner.setStatus('current')
if mibBuilder.loadTexts: rldot1qStaticUnicastAddressOwner.setDescription('The learned status of this entry: static(1) - address has added by user. learned(2)- address has added by device.')
rldot1qTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 89, 57, 8, 2), )
if mibBuilder.loadTexts: rldot1qTpFdbTable.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbTable.setDescription('An augmentation to dot1qTpFdbTable')
rldot1qTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 57, 8, 2, 1), )
dot1qTpFdbEntry.registerAugmentions(("MARVELL-rldot1q-MIB", "rldot1qTpFdbEntry"))
rldot1qTpFdbEntry.setIndexNames(*dot1qTpFdbEntry.getIndexNames())
if mibBuilder.loadTexts: rldot1qTpFdbEntry.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbEntry.setDescription('An augmentation to dot1qTpFdbEntry')
rldot1qTpFdbSubStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 57, 8, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("dynamic-static", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rldot1qTpFdbSubStatus.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbSubStatus.setDescription('The sub status of this entry. The meanings of the values are: none(1) - non of the following. dynamic-static(2) - the value of the corresponding instance of dot1qTpFdbPort was learned dynamically in SW but kept as static address in HW.')
rldot1qTpFdbCountTable = MibTable((1, 3, 6, 1, 4, 1, 89, 57, 8, 3), )
if mibBuilder.loadTexts: rldot1qTpFdbCountTable.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbCountTable.setDescription('Counters for FDB table. Per VLAN, port and type.')
rldot1qTpFdbCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 57, 8, 3, 1), ).setIndexNames((0, "MARVELL-rldot1q-MIB", "rldot1qTpFdbCountVlanTag"), (0, "MARVELL-rldot1q-MIB", "rldot1qTpFdbCountPort"), (0, "MARVELL-rldot1q-MIB", "rldot1qTpFdbCountType"))
if mibBuilder.loadTexts: rldot1qTpFdbCountEntry.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbCountEntry.setDescription('Count the number of MAC address for a specific VLAN, port and type.')
rldot1qTpFdbCountVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 57, 8, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rldot1qTpFdbCountVlanTag.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbCountVlanTag.setDescription('Vlan Tag. Zero means all vlans')
rldot1qTpFdbCountPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 57, 8, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rldot1qTpFdbCountPort.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbCountPort.setDescription('Port. Zero means all ports')
rldot1qTpFdbCountType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 57, 8, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rldot1qTpFdbCountType.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbCountType.setDescription('Type of the address: TODO ')
rldot1qTpFdbCountCount = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 57, 8, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rldot1qTpFdbCountCount.setStatus('current')
if mibBuilder.loadTexts: rldot1qTpFdbCountCount.setDescription('Number of address per selected vlan, port and type.')
mibBuilder.exportSymbols("MARVELL-rldot1q-MIB", rldot1qTpFdbSubStatus=rldot1qTpFdbSubStatus, rldot1qStaticUnicastAddressOwner=rldot1qStaticUnicastAddressOwner, rldot1qStaticUnicastEntry=rldot1qStaticUnicastEntry, rldot1qStaticUnicastTable=rldot1qStaticUnicastTable, rldot1qTpFdbCountType=rldot1qTpFdbCountType, rldot1qTpFdbEntry=rldot1qTpFdbEntry, rldot1qTpFdbCountPort=rldot1qTpFdbCountPort, rldot1qTpFdbCountVlanTag=rldot1qTpFdbCountVlanTag, rlq_bridge_mib=rlq_bridge_mib, rldot1q=rldot1q, rldot1qTpFdbTable=rldot1qTpFdbTable, rldot1qTpFdbCountEntry=rldot1qTpFdbCountEntry, PYSNMP_MODULE_ID=rlq_bridge_mib, rldot1qTpFdbCountCount=rldot1qTpFdbCountCount, rldot1qTpFdbCountTable=rldot1qTpFdbCountTable)
