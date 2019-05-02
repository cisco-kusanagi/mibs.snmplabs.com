#
# PySNMP MIB module CISCO-LEC-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LEC-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:04:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
VlanIndex, = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
lecConfigEntry, = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "lecConfigEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, MibIdentifier, Counter64, Integer32, IpAddress, ObjectIdentity, Unsigned32, NotificationType, Counter32, Bits, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "MibIdentifier", "Counter64", "Integer32", "IpAddress", "ObjectIdentity", "Unsigned32", "NotificationType", "Counter32", "Bits", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLecExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 77))
ciscoLecExtMIB.setRevisions(('1997-05-09 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLecExtMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLecExtMIB.setLastUpdated('9705091230Z')
if mibBuilder.loadTexts: ciscoLecExtMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLecExtMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoLecExtMIB.setDescription("This MIB module is a Cisco extension to the ATM Forum's LANE Client MIB.")
ciscoLecExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 1))
cLecExtVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1))
cLecToVlanTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1), )
if mibBuilder.loadTexts: cLecToVlanTable.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanTable.setDescription('An extension to the lecConfig table in the LAN-EMULATION-CLIENT-MIB that identifies which VLAN a LEC is associated with.')
cLecToVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1), )
lecConfigEntry.registerAugmentions(("CISCO-LEC-EXT-MIB", "cLecToVlanEntry"))
cLecToVlanEntry.setIndexNames(*lecConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cLecToVlanEntry.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanEntry.setDescription(' Each entry in this table shows the correlation between a LAN Emulation client and the VLAN that it extends.')
cLecToVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 77, 1, 1, 1, 1, 1), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLecToVlanId.setStatus('current')
if mibBuilder.loadTexts: cLecToVlanId.setDescription(' The VLAN ID of the VLAN to which the specified LEC is attributed.')
ciscoLecExtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 2))
ciscoLecExtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 2, 0))
ciscoLecExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3))
ciscoLecExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1))
ciscoLecExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2))
ciscoLecExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 1, 1)).setObjects(("CISCO-LEC-EXT-MIB", "ciscoLecExtVlanMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecExtMIBCompliance = ciscoLecExtMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoLecExtMIBCompliance.setDescription('This module should be implemented by all Cisco devices supporting ATM LAN Emulation Clients.')
ciscoLecExtVlanMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 77, 3, 2, 1)).setObjects(("CISCO-LEC-EXT-MIB", "cLecToVlanId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecExtVlanMIBGroup = ciscoLecExtVlanMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLecExtVlanMIBGroup.setDescription('A collection of objects related to identifying a LANE Client associated VLAN information.')
mibBuilder.exportSymbols("CISCO-LEC-EXT-MIB", ciscoLecExtMIBGroups=ciscoLecExtMIBGroups, ciscoLecExtMIB=ciscoLecExtMIB, ciscoLecExtMIBNotificationPrefix=ciscoLecExtMIBNotificationPrefix, ciscoLecExtMIBCompliance=ciscoLecExtMIBCompliance, cLecToVlanTable=cLecToVlanTable, ciscoLecExtMIBNotifications=ciscoLecExtMIBNotifications, ciscoLecExtMIBConformance=ciscoLecExtMIBConformance, ciscoLecExtVlanMIBGroup=ciscoLecExtVlanMIBGroup, cLecToVlanEntry=cLecToVlanEntry, ciscoLecExtMIBObjects=ciscoLecExtMIBObjects, cLecToVlanId=cLecToVlanId, PYSNMP_MODULE_ID=ciscoLecExtMIB, ciscoLecExtMIBCompliances=ciscoLecExtMIBCompliances, cLecExtVlan=cLecExtVlan)
