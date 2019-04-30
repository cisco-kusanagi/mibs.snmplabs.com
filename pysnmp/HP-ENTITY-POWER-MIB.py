#
# PySNMP MIB module HP-ENTITY-POWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ENTITY-POWER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, iso, NotificationType, ObjectIdentity, Counter64, Unsigned32, Integer32, TimeTicks, Bits, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "iso", "NotificationType", "ObjectIdentity", "Counter64", "Unsigned32", "Integer32", "TimeTicks", "Bits", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpEntityPowerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71))
hpEntityPowerMIB.setRevisions(('2010-04-11 00:00',))
if mibBuilder.loadTexts: hpEntityPowerMIB.setLastUpdated('201004110000Z')
if mibBuilder.loadTexts: hpEntityPowerMIB.setOrganization('HP Networking')
hpEntPowerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1))
hpEntPowerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1), )
if mibBuilder.loadTexts: hpEntPowerTable.setStatus('current')
hpEntPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpEntPowerEntry.setStatus('current')
hpEntPowerMaxPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 1), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerMaxPowerUsage.setStatus('current')
hpEntPowerMinPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 2), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerMinPowerUsage.setStatus('current')
hpEntPowerCurrentPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 3), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerCurrentPowerUsage.setStatus('current')
hpEntPowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2))
hpEntPowerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 1))
hpEntPowerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 1, 1)).setObjects(("HP-ENTITY-POWER-MIB", "hpEntPowerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpEntPowerCompliance = hpEntPowerCompliance.setStatus('current')
hpEntPowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 2))
hpEntPowerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 2, 1)).setObjects(("HP-ENTITY-POWER-MIB", "hpEntPowerMaxPowerUsage"), ("HP-ENTITY-POWER-MIB", "hpEntPowerMinPowerUsage"), ("HP-ENTITY-POWER-MIB", "hpEntPowerCurrentPowerUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpEntPowerGroup = hpEntPowerGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ENTITY-POWER-MIB", hpEntPowerObjects=hpEntPowerObjects, hpEntPowerCompliances=hpEntPowerCompliances, hpEntPowerMinPowerUsage=hpEntPowerMinPowerUsage, hpEntPowerMaxPowerUsage=hpEntPowerMaxPowerUsage, hpEntPowerCurrentPowerUsage=hpEntPowerCurrentPowerUsage, hpEntPowerGroup=hpEntPowerGroup, hpEntPowerEntry=hpEntPowerEntry, hpEntPowerCompliance=hpEntPowerCompliance, hpEntityPowerMIB=hpEntityPowerMIB, PYSNMP_MODULE_ID=hpEntityPowerMIB, hpEntPowerConformance=hpEntPowerConformance, hpEntPowerTable=hpEntPowerTable, hpEntPowerGroups=hpEntPowerGroups)
