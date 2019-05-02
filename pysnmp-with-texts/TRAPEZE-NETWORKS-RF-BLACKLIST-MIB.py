#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-BLACKLIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-RF-BLACKLIST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter32, ObjectIdentity, iso, Gauge32, Counter64, NotificationType, Bits, IpAddress, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter32", "ObjectIdentity", "iso", "Gauge32", "Counter64", "NotificationType", "Bits", "IpAddress", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzRFBlacklistMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 18))
trpzRFBlacklistMib.setRevisions(('2011-02-24 00:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzRFBlacklistMib.setRevisionsDescriptions(('v1.0.4: Initial version, for 7.5 release',))
if mibBuilder.loadTexts: trpzRFBlacklistMib.setLastUpdated('201102240014Z')
if mibBuilder.loadTexts: trpzRFBlacklistMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzRFBlacklistMib.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzRFBlacklistMib.setDescription("RF Blacklist objects for Trapeze Networks wireless switches. Copyright (c) 2009-2011 by Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzRFBlacklistedEntryType(TextualConvention, Integer32):
    description = 'Enumeration to indicate the Type of a Blacklisted Entry: configuredPermanent: The MAC address has been permanently blacklisted by administrative action; configuredDynamic: The MAC address has been temporarily blacklisted by administrative action; assocReqFlood, reassocReqFlood, disassocReqFlood, unknownDynamic: The MAC address has been automatically blacklisted by RF Detection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknownDynamic", 2), ("configuredPermanent", 3), ("configuredDynamic", 4), ("assocReqFlood", 5), ("reassocReqFlood", 6), ("disassocReqFlood", 7))

trpzRFBlacklistMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1))
trpzRFBlacklistXmtrTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2), )
if mibBuilder.loadTexts: trpzRFBlacklistXmtrTable.setStatus('current')
if mibBuilder.loadTexts: trpzRFBlacklistXmtrTable.setDescription('A table containing transmitters blacklisted by RF Detection.')
trpzRFBlacklistXmtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrMacAddress"))
if mibBuilder.loadTexts: trpzRFBlacklistXmtrEntry.setStatus('current')
if mibBuilder.loadTexts: trpzRFBlacklistXmtrEntry.setDescription('Information about a particular blacklisted transmitter.')
trpzRFBlacklistXmtrMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: trpzRFBlacklistXmtrMacAddress.setStatus('current')
if mibBuilder.loadTexts: trpzRFBlacklistXmtrMacAddress.setDescription('The MAC Address of this Blacklisted Transmitter.')
trpzRFBlacklistXmtrType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 2), TrpzRFBlacklistedEntryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzRFBlacklistXmtrType.setStatus('current')
if mibBuilder.loadTexts: trpzRFBlacklistXmtrType.setDescription('The Type of this Blacklisted Transmitter.')
trpzRFBlacklistXmtrTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzRFBlacklistXmtrTimeToLive.setStatus('current')
if mibBuilder.loadTexts: trpzRFBlacklistXmtrTimeToLive.setDescription('The remaining time in seconds until this Transmitter is removed from the RF Blacklist. For permanent entries, the value will be always zero.')
trpzRFBlacklistConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2))
trpzRFBlacklistCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 1))
trpzRFBlacklistGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 2))
trpzRFBlacklistCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzRFBlacklistCompliance = trpzRFBlacklistCompliance.setStatus('current')
if mibBuilder.loadTexts: trpzRFBlacklistCompliance.setDescription('The compliance statement for devices that implement RF Blacklist MIB. This compliance statement is for releases 7.5 and greater of AC (wireless switch) software.')
trpzRFBlacklistXmtrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrType"), ("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrTimeToLive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzRFBlacklistXmtrGroup = trpzRFBlacklistXmtrGroup.setStatus('current')
if mibBuilder.loadTexts: trpzRFBlacklistXmtrGroup.setDescription('Group of columnar objects implemented to provide Blacklisted Transmitter info in releases 7.5 and greater.')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", trpzRFBlacklistXmtrEntry=trpzRFBlacklistXmtrEntry, TrpzRFBlacklistedEntryType=TrpzRFBlacklistedEntryType, trpzRFBlacklistXmtrType=trpzRFBlacklistXmtrType, trpzRFBlacklistCompliances=trpzRFBlacklistCompliances, trpzRFBlacklistMib=trpzRFBlacklistMib, trpzRFBlacklistMibObjects=trpzRFBlacklistMibObjects, trpzRFBlacklistGroups=trpzRFBlacklistGroups, trpzRFBlacklistXmtrMacAddress=trpzRFBlacklistXmtrMacAddress, trpzRFBlacklistXmtrTimeToLive=trpzRFBlacklistXmtrTimeToLive, trpzRFBlacklistXmtrGroup=trpzRFBlacklistXmtrGroup, trpzRFBlacklistXmtrTable=trpzRFBlacklistXmtrTable, trpzRFBlacklistCompliance=trpzRFBlacklistCompliance, trpzRFBlacklistConformance=trpzRFBlacklistConformance, PYSNMP_MODULE_ID=trpzRFBlacklistMib)
