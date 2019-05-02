#
# PySNMP MIB module BAY-STACK-ECMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-ECMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, NotificationType, Bits, TimeTicks, IpAddress, Counter32, Gauge32, Counter64, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "NotificationType", "Bits", "TimeTicks", "IpAddress", "Counter32", "Gauge32", "Counter64", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackEcmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 15))
bayStackEcmpMib.setRevisions(('2012-06-01 00:00', '2005-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackEcmpMib.setRevisionsDescriptions(('v2: Added new value 4 (bgp) for bsEcmpConfigRoutingProtocol', 'v1: Initial version.',))
if mibBuilder.loadTexts: bayStackEcmpMib.setLastUpdated('201206010000Z')
if mibBuilder.loadTexts: bayStackEcmpMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: bayStackEcmpMib.setContactInfo('Nortel Networks')
if mibBuilder.loadTexts: bayStackEcmpMib.setDescription("Nortel Networks ECMP MIB Copyright 2005 Nortel Networks, Inc. All rights reserved. This Nortel Networks SNMP Management Information Base Specification embodies Nortel Networks' confidential and proprietary intellectual property. Nortel Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
bsEcmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 0))
bsEcmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 1))
bsEcmpScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 1))
bsEcmpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2), )
if mibBuilder.loadTexts: bsEcmpConfigTable.setStatus('current')
if mibBuilder.loadTexts: bsEcmpConfigTable.setDescription('Extensions to the ospfIfTable from RFC 2787.')
bsEcmpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1), ).setIndexNames((0, "BAY-STACK-ECMP-MIB", "bsEcmpConfigRoutingProtocol"))
if mibBuilder.loadTexts: bsEcmpConfigEntry.setStatus('current')
if mibBuilder.loadTexts: bsEcmpConfigEntry.setDescription('A set of objects that augments the ospfIfTable. There will be an entry in this table for each entry in the ospfIfTable.')
bsEcmpConfigRoutingProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("static", 1), ("rip", 2), ("ospf", 3), ("bgp", 4))))
if mibBuilder.loadTexts: bsEcmpConfigRoutingProtocol.setStatus('current')
if mibBuilder.loadTexts: bsEcmpConfigRoutingProtocol.setDescription('Specifies the protocols that are supported by ECMP: static, RIP, OSPF, BGP')
bsEcmpConfigMaxPath = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 15, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEcmpConfigMaxPath.setStatus('current')
if mibBuilder.loadTexts: bsEcmpConfigMaxPath.setDescription('Specifies the number of ECMP paths allowed for routes of the given protocol')
mibBuilder.exportSymbols("BAY-STACK-ECMP-MIB", bsEcmpNotifications=bsEcmpNotifications, bsEcmpConfigRoutingProtocol=bsEcmpConfigRoutingProtocol, bayStackEcmpMib=bayStackEcmpMib, bsEcmpScalars=bsEcmpScalars, bsEcmpConfigMaxPath=bsEcmpConfigMaxPath, bsEcmpConfigEntry=bsEcmpConfigEntry, bsEcmpConfigTable=bsEcmpConfigTable, bsEcmpObjects=bsEcmpObjects, PYSNMP_MODULE_ID=bayStackEcmpMib)
