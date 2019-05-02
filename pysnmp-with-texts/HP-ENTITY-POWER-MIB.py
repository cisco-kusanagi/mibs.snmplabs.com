#
# PySNMP MIB module HP-ENTITY-POWER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ENTITY-POWER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:33:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, Bits, Unsigned32, ModuleIdentity, TimeTicks, Counter32, ObjectIdentity, IpAddress, NotificationType, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "Bits", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "ObjectIdentity", "IpAddress", "NotificationType", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpEntityPowerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71))
hpEntityPowerMIB.setRevisions(('2010-04-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpEntityPowerMIB.setRevisionsDescriptions(('Initial version of this MIB',))
if mibBuilder.loadTexts: hpEntityPowerMIB.setLastUpdated('201004110000Z')
if mibBuilder.loadTexts: hpEntityPowerMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpEntityPowerMIB.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA - 95747.')
if mibBuilder.loadTexts: hpEntityPowerMIB.setDescription('This MIB defines HP proprietary objects that can be used to set the power status of physical entities and report power usage statistics.')
hpEntPowerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1))
hpEntPowerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1), )
if mibBuilder.loadTexts: hpEntPowerTable.setStatus('current')
if mibBuilder.loadTexts: hpEntPowerTable.setDescription('A table of information about the power status of entities. This is a sparse augment of the entPhysicalTable. Entries appear in this table for values of entPhysicalClass [RFC4133] that in this implementation are able to report any of the power state or status stored in this table.')
hpEntPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpEntPowerEntry.setStatus('current')
if mibBuilder.loadTexts: hpEntPowerEntry.setDescription('Power related information about this physical entity.')
hpEntPowerMaxPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 1), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerMaxPowerUsage.setStatus('current')
if mibBuilder.loadTexts: hpEntPowerMaxPowerUsage.setDescription('This MIB object returns the maximum power usage of this entity. This would typically correspond to the maximum power rating of the entity.')
hpEntPowerMinPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 2), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerMinPowerUsage.setStatus('current')
if mibBuilder.loadTexts: hpEntPowerMinPowerUsage.setDescription('This MIB object returns the minimum power usage of this entity. This is applicable only to those entities that can be administratively set to function in a low power state.')
hpEntPowerCurrentPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 1, 1, 1, 3), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpEntPowerCurrentPowerUsage.setStatus('current')
if mibBuilder.loadTexts: hpEntPowerCurrentPowerUsage.setDescription('This MIB object returns the current power usage of this entity. For entities that cannot be set to function in a low power mode, the value returned by this object would be the same as that of entPowerMaxPowerUsage. For entities that are set to function in a low power mode, the value returned would be the same as that of entPowerMinPowerUsage.')
hpEntPowerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2))
hpEntPowerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 1))
hpEntPowerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 1, 1)).setObjects(("HP-ENTITY-POWER-MIB", "hpEntPowerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpEntPowerCompliance = hpEntPowerCompliance.setStatus('current')
if mibBuilder.loadTexts: hpEntPowerCompliance.setDescription('The compliance statement for systems supporting the HP Entity Power MIB.')
hpEntPowerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 2))
hpEntPowerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71, 2, 2, 1)).setObjects(("HP-ENTITY-POWER-MIB", "hpEntPowerMaxPowerUsage"), ("HP-ENTITY-POWER-MIB", "hpEntPowerMinPowerUsage"), ("HP-ENTITY-POWER-MIB", "hpEntPowerCurrentPowerUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpEntPowerGroup = hpEntPowerGroup.setStatus('current')
if mibBuilder.loadTexts: hpEntPowerGroup.setDescription('HP proprietary Entity Power group.')
mibBuilder.exportSymbols("HP-ENTITY-POWER-MIB", hpEntPowerMinPowerUsage=hpEntPowerMinPowerUsage, hpEntPowerGroup=hpEntPowerGroup, hpEntityPowerMIB=hpEntityPowerMIB, hpEntPowerConformance=hpEntPowerConformance, hpEntPowerCompliance=hpEntPowerCompliance, hpEntPowerGroups=hpEntPowerGroups, PYSNMP_MODULE_ID=hpEntityPowerMIB, hpEntPowerTable=hpEntPowerTable, hpEntPowerObjects=hpEntPowerObjects, hpEntPowerCurrentPowerUsage=hpEntPowerCurrentPowerUsage, hpEntPowerCompliances=hpEntPowerCompliances, hpEntPowerMaxPowerUsage=hpEntPowerMaxPowerUsage, hpEntPowerEntry=hpEntPowerEntry)
