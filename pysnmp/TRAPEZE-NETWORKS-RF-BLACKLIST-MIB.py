#
# PySNMP MIB module TRAPEZE-NETWORKS-RF-BLACKLIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-RF-BLACKLIST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, Counter64, IpAddress, Bits, ModuleIdentity, ObjectIdentity, MibIdentifier, TimeTicks, Integer32, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "IpAddress", "Bits", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Integer32", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzRFBlacklistMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 18))
trpzRFBlacklistMib.setRevisions(('2011-02-24 00:14',))
if mibBuilder.loadTexts: trpzRFBlacklistMib.setLastUpdated('201102240014Z')
if mibBuilder.loadTexts: trpzRFBlacklistMib.setOrganization('Trapeze Networks')
class TrpzRFBlacklistedEntryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("unknownDynamic", 2), ("configuredPermanent", 3), ("configuredDynamic", 4), ("assocReqFlood", 5), ("reassocReqFlood", 6), ("disassocReqFlood", 7))

trpzRFBlacklistMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1))
trpzRFBlacklistXmtrTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2), )
if mibBuilder.loadTexts: trpzRFBlacklistXmtrTable.setStatus('current')
trpzRFBlacklistXmtrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrMacAddress"))
if mibBuilder.loadTexts: trpzRFBlacklistXmtrEntry.setStatus('current')
trpzRFBlacklistXmtrMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: trpzRFBlacklistXmtrMacAddress.setStatus('current')
trpzRFBlacklistXmtrType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 2), TrpzRFBlacklistedEntryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzRFBlacklistXmtrType.setStatus('current')
trpzRFBlacklistXmtrTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 18, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzRFBlacklistXmtrTimeToLive.setStatus('current')
trpzRFBlacklistConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2))
trpzRFBlacklistCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 1))
trpzRFBlacklistGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 2))
trpzRFBlacklistCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzRFBlacklistCompliance = trpzRFBlacklistCompliance.setStatus('current')
trpzRFBlacklistXmtrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 18, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrType"), ("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", "trpzRFBlacklistXmtrTimeToLive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzRFBlacklistXmtrGroup = trpzRFBlacklistXmtrGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-RF-BLACKLIST-MIB", trpzRFBlacklistMibObjects=trpzRFBlacklistMibObjects, trpzRFBlacklistXmtrTable=trpzRFBlacklistXmtrTable, trpzRFBlacklistXmtrMacAddress=trpzRFBlacklistXmtrMacAddress, TrpzRFBlacklistedEntryType=TrpzRFBlacklistedEntryType, trpzRFBlacklistMib=trpzRFBlacklistMib, trpzRFBlacklistXmtrEntry=trpzRFBlacklistXmtrEntry, trpzRFBlacklistXmtrTimeToLive=trpzRFBlacklistXmtrTimeToLive, trpzRFBlacklistGroups=trpzRFBlacklistGroups, trpzRFBlacklistCompliances=trpzRFBlacklistCompliances, PYSNMP_MODULE_ID=trpzRFBlacklistMib, trpzRFBlacklistCompliance=trpzRFBlacklistCompliance, trpzRFBlacklistXmtrGroup=trpzRFBlacklistXmtrGroup, trpzRFBlacklistConformance=trpzRFBlacklistConformance, trpzRFBlacklistXmtrType=trpzRFBlacklistXmtrType)
