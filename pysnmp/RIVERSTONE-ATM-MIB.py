#
# PySNMP MIB module RIVERSTONE-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RIVERSTONE-ATM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:49:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
AtmVcIdentifier, AtmVpIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVcIdentifier", "AtmVpIdentifier")
dot1dTpFdbAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dTpFdbAddress")
riverstoneMibs, = mibBuilder.importSymbols("RSTONE-SMI-MIB", "riverstoneMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32, Bits, Integer32, Counter64, IpAddress, NotificationType, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32", "Bits", "Integer32", "Counter64", "IpAddress", "NotificationType", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsAtmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 5567, 2, 16))
rsAtmMib.setRevisions(('2001-01-31 00:00',))
if mibBuilder.loadTexts: rsAtmMib.setLastUpdated('200101310000Z')
if mibBuilder.loadTexts: rsAtmMib.setOrganization('Riverstone Networks, Inc')
rsAtmFdbObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1))
rsAtmFdbMacsLearned = MibScalar((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAtmFdbMacsLearned.setStatus('current')
rsAtmFdbTable = MibTable((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2), )
if mibBuilder.loadTexts: rsAtmFdbTable.setStatus('current')
rsAtmFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dTpFdbAddress"))
if mibBuilder.loadTexts: rsAtmFdbEntry.setStatus('current')
rsAtmFdbVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1, 1), AtmVpIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAtmFdbVpi.setStatus('current')
rsAtmFdbVci = MibTableColumn((1, 3, 6, 1, 4, 1, 5567, 2, 16, 1, 2, 1, 2), AtmVcIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsAtmFdbVci.setStatus('current')
rsAtmFdbConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10))
rsAtmFdbGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 1))
rsAtmFdbCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 2))
rsAtmFdbBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 1, 1)).setObjects(("RIVERSTONE-ATM-MIB", "rsAtmFdbMacsLearned"), ("RIVERSTONE-ATM-MIB", "rsAtmFdbVpi"), ("RIVERSTONE-ATM-MIB", "rsAtmFdbVci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAtmFdbBaseGroup = rsAtmFdbBaseGroup.setStatus('current')
rsAtmFdbMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5567, 2, 16, 10, 2, 1)).setObjects(("RIVERSTONE-ATM-MIB", "rsAtmFdbBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsAtmFdbMibCompliance = rsAtmFdbMibCompliance.setStatus('current')
mibBuilder.exportSymbols("RIVERSTONE-ATM-MIB", rsAtmFdbMacsLearned=rsAtmFdbMacsLearned, PYSNMP_MODULE_ID=rsAtmMib, rsAtmFdbBaseGroup=rsAtmFdbBaseGroup, rsAtmFdbVci=rsAtmFdbVci, rsAtmFdbGroups=rsAtmFdbGroups, rsAtmFdbCompliances=rsAtmFdbCompliances, rsAtmFdbMibCompliance=rsAtmFdbMibCompliance, rsAtmFdbEntry=rsAtmFdbEntry, rsAtmFdbObjects=rsAtmFdbObjects, rsAtmMib=rsAtmMib, rsAtmFdbVpi=rsAtmFdbVpi, rsAtmFdbTable=rsAtmFdbTable, rsAtmFdbConformance=rsAtmFdbConformance)
