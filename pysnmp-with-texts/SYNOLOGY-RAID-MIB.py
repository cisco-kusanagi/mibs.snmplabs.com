#
# PySNMP MIB module SYNOLOGY-RAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SYNOLOGY-RAID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:14:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, ModuleIdentity, Unsigned32, enterprises, Gauge32, Counter64, NotificationType, TimeTicks, IpAddress, Counter32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "ModuleIdentity", "Unsigned32", "enterprises", "Gauge32", "Counter64", "NotificationType", "TimeTicks", "IpAddress", "Counter32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
synoRaid = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 3))
synoRaid.setRevisions(('2013-09-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: synoRaid.setRevisionsDescriptions(('Second draft.',))
if mibBuilder.loadTexts: synoRaid.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: synoRaid.setOrganization('www.synology.com')
if mibBuilder.loadTexts: synoRaid.setContactInfo('postal: Jay Pan email: jaypan@synology.com')
if mibBuilder.loadTexts: synoRaid.setDescription('Characteristics of the raid information')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
raidTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 3, 1), )
if mibBuilder.loadTexts: raidTable.setStatus('current')
if mibBuilder.loadTexts: raidTable.setDescription('Synology raid table')
raidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1), ).setIndexNames((0, "SYNOLOGY-RAID-MIB", "raidIndex"))
if mibBuilder.loadTexts: raidEntry.setStatus('current')
if mibBuilder.loadTexts: raidEntry.setDescription('For all raid entry')
raidIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: raidIndex.setStatus('current')
if mibBuilder.loadTexts: raidIndex.setDescription('The index of raid table')
raidName = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidName.setStatus('current')
if mibBuilder.loadTexts: raidName.setDescription('Synology raid name The name of each raid will be showed here. ')
raidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raidStatus.setStatus('current')
if mibBuilder.loadTexts: raidStatus.setDescription('Synology Raid status Each meanings of status represented describe below. Normal(1): The raid functions normally. Degrade(11): Degrade happens when a tolerable failure of disk(s) occurs. Crashed(12): Raid has crashed and just uses for read-only operation. Note: Other status will be showed when creating or deleting raids, including below status, Repairing(2), Migrating(3), Expanding(4), Deleting(5), Creating(6), RaidSyncing(7), RaidParityChecking(8), RaidAssembling(9) and Canceling(10). ')
raidConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2))
raidCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2, 1))
raidGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 3, 2, 2))
raidCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 3, 2, 1, 1)).setObjects(("SYNOLOGY-RAID-MIB", "raidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidCompliance = raidCompliance.setStatus('current')
if mibBuilder.loadTexts: raidCompliance.setDescription('The compliance statement for synoRaid entities which implement the SYNOLOGY RAID MIB.')
raidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 3, 2, 2, 1)).setObjects(("SYNOLOGY-RAID-MIB", "raidName"), ("SYNOLOGY-RAID-MIB", "raidStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    raidGroup = raidGroup.setStatus('current')
if mibBuilder.loadTexts: raidGroup.setDescription('A collection of objects providing basic instrumentation and control of an synology raid entity.')
mibBuilder.exportSymbols("SYNOLOGY-RAID-MIB", raidCompliances=raidCompliances, raidName=raidName, raidEntry=raidEntry, PYSNMP_MODULE_ID=synoRaid, synology=synology, raidStatus=raidStatus, raidConformance=raidConformance, synoRaid=synoRaid, raidGroups=raidGroups, raidIndex=raidIndex, raidCompliance=raidCompliance, raidGroup=raidGroup, raidTable=raidTable)
