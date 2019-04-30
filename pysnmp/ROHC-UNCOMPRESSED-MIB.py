#
# PySNMP MIB module ROHC-UNCOMPRESSED-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ROHC-UNCOMPRESSED-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
rohcChannelID, rohcContextCID = mibBuilder.importSymbols("ROHC-MIB", "rohcChannelID", "rohcContextCID")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, TimeTicks, Unsigned32, Bits, mib_2, NotificationType, ModuleIdentity, Counter64, ObjectIdentity, iso, MibIdentifier, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Unsigned32", "Bits", "mib-2", "NotificationType", "ModuleIdentity", "Counter64", "ObjectIdentity", "iso", "MibIdentifier", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rohcUncmprMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 113))
rohcUncmprMIB.setRevisions(('2004-06-03 00:00',))
if mibBuilder.loadTexts: rohcUncmprMIB.setLastUpdated('200406030000Z')
if mibBuilder.loadTexts: rohcUncmprMIB.setOrganization('IETF Robust Header Compression Working Group')
rohcUncmprObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 1))
rohcUncmprConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2))
rohcUncmprContextTable = MibTable((1, 3, 6, 1, 2, 1, 113, 1, 1), )
if mibBuilder.loadTexts: rohcUncmprContextTable.setStatus('current')
rohcUncmprContextEntry = MibTableRow((1, 3, 6, 1, 2, 1, 113, 1, 1, 1), ).setIndexNames((0, "ROHC-MIB", "rohcChannelID"), (0, "ROHC-MIB", "rohcContextCID"))
if mibBuilder.loadTexts: rohcUncmprContextEntry.setStatus('current')
rohcUncmprContextState = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("initAndRefresh", 1), ("normal", 2), ("noContext", 3), ("fullContext", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextState.setStatus('current')
rohcUncmprContextMode = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unidirectional", 1), ("bidirectional", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextMode.setStatus('current')
rohcUncmprContextACKs = MibTableColumn((1, 3, 6, 1, 2, 1, 113, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rohcUncmprContextACKs.setStatus('current')
rohcUncmprCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2, 1))
rohcUncmprGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 113, 2, 2))
rohcUncmprCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 113, 2, 1, 1)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextGroup"), ("ROHC-UNCOMPRESSED-MIB", "rohcUncmprStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprCompliance = rohcUncmprCompliance.setStatus('current')
rohcUncmprContextGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 113, 2, 2, 1)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextState"), ("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprContextGroup = rohcUncmprContextGroup.setStatus('current')
rohcUncmprStatisticsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 113, 2, 2, 2)).setObjects(("ROHC-UNCOMPRESSED-MIB", "rohcUncmprContextACKs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rohcUncmprStatisticsGroup = rohcUncmprStatisticsGroup.setStatus('current')
mibBuilder.exportSymbols("ROHC-UNCOMPRESSED-MIB", rohcUncmprContextState=rohcUncmprContextState, rohcUncmprMIB=rohcUncmprMIB, rohcUncmprConformance=rohcUncmprConformance, rohcUncmprContextEntry=rohcUncmprContextEntry, rohcUncmprContextMode=rohcUncmprContextMode, rohcUncmprStatisticsGroup=rohcUncmprStatisticsGroup, rohcUncmprObjects=rohcUncmprObjects, rohcUncmprContextACKs=rohcUncmprContextACKs, rohcUncmprCompliances=rohcUncmprCompliances, rohcUncmprCompliance=rohcUncmprCompliance, rohcUncmprContextTable=rohcUncmprContextTable, rohcUncmprContextGroup=rohcUncmprContextGroup, rohcUncmprGroups=rohcUncmprGroups, PYSNMP_MODULE_ID=rohcUncmprMIB)
