#
# PySNMP MIB module HP-ICF-JUMBO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-JUMBO-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
hpicfObjectModules, = mibBuilder.importSymbols("HP-ICF-OID", "hpicfObjectModules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, Counter32, Gauge32, IpAddress, NotificationType, Unsigned32, MibIdentifier, ModuleIdentity, Counter64, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Gauge32", "IpAddress", "NotificationType", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter64", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfJumboMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13))
hpicfJumboMIB.setRevisions(('2004-08-22 10:30',))
if mibBuilder.loadTexts: hpicfJumboMIB.setLastUpdated('200408221030Z')
if mibBuilder.loadTexts: hpicfJumboMIB.setOrganization('HP Networking')
hpicfJumboObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1))
hpJumboStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1))
hpJumboStatsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1), )
if mibBuilder.loadTexts: hpJumboStatsTable.setStatus('current')
hpJumboStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1), ).setIndexNames((0, "HP-ICF-JUMBO-MIB", "hpJumboStatsIndex"))
if mibBuilder.loadTexts: hpJumboStatsEntry.setStatus('current')
hpJumboStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpJumboStatsIndex.setStatus('current')
hpJumboStatsPkts1523to2047Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpJumboStatsPkts1523to2047Octets.setStatus('current')
hpJumboStatsPkts2048to4095Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpJumboStatsPkts2048to4095Octets.setStatus('current')
hpJumboStatsPkts4096to9216Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpJumboStatsPkts4096to9216Octets.setStatus('current')
hpicfJumboConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2))
hpicfJumboGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 1))
hpicfJumboCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 2))
hpicfJumboStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 1, 1)).setObjects(("HP-ICF-JUMBO-MIB", "hpJumboStatsIndex"), ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts1523to2047Octets"), ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts2048to4095Octets"), ("HP-ICF-JUMBO-MIB", "hpJumboStatsPkts4096to9216Octets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJumboStatsGroup = hpicfJumboStatsGroup.setStatus('current')
hpicfJumboCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13, 2, 2, 1)).setObjects(("HP-ICF-JUMBO-MIB", "hpicfJumboStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfJumboCompliance = hpicfJumboCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-JUMBO-MIB", hpicfJumboConformance=hpicfJumboConformance, hpJumboStatsPkts1523to2047Octets=hpJumboStatsPkts1523to2047Octets, hpicfJumboObjects=hpicfJumboObjects, hpJumboStatsPkts4096to9216Octets=hpJumboStatsPkts4096to9216Octets, PYSNMP_MODULE_ID=hpicfJumboMIB, hpJumboStatsTable=hpJumboStatsTable, hpJumboStatsIndex=hpJumboStatsIndex, hpJumboStatsPkts2048to4095Octets=hpJumboStatsPkts2048to4095Octets, hpJumboStatsEntry=hpJumboStatsEntry, hpicfJumboGroups=hpicfJumboGroups, hpicfJumboCompliances=hpicfJumboCompliances, hpicfJumboCompliance=hpicfJumboCompliance, hpicfJumboStatsGroup=hpicfJumboStatsGroup, hpJumboStats=hpJumboStats, hpicfJumboMIB=hpicfJumboMIB)
