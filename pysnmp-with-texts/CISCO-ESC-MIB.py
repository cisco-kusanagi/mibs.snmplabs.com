#
# PySNMP MIB module CISCO-ESC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ESC-MIB
# Produced by pysmi-0.3.4 at Thu Aug  8 11:00:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.7.0 by user davwang4
# Using Python version 2.7.15 (default, May  1 2018, 16:44:08) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 844))
ciscoEscMIB.setRevisions(('2017-03-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEscMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEscMIB.setLastUpdated('201705020000Z')
if mibBuilder.loadTexts: ciscoEscMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEscMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: miblib@cisco.com')
if mibBuilder.loadTexts: ciscoEscMIB.setDescription('Objects relating to the Cisco Elastic Services Controller (ESC)')
escNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 0))
escMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 1))
ciscoEscMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 2))
vnfm = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1))
escStatusMessage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: escStatusMessage.setStatus('current')
if mibBuilder.loadTexts: escStatusMessage.setDescription('ESC Status Message')
escStatusCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: escStatusCode.setStatus('current')
if mibBuilder.loadTexts: escStatusCode.setDescription('ESC Status Code')
escStatusNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 844, 0, 1)).setObjects(("CISCO-ESC-MIB", "escStatusCode"), ("CISCO-ESC-MIB", "escStatusMessage"))
if mibBuilder.loadTexts: escStatusNotif.setStatus('current')
if mibBuilder.loadTexts: escStatusNotif.setDescription('ESC Status Notification')
ciscoEscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 1))
ciscoEscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2))
ciscoEscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 1, 1)).setObjects(("CISCO-ESC-MIB", "ciscoEscMIBObjectGroup"), ("CISCO-ESC-MIB", "ciscoEscMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEscMIBCompliance = ciscoEscMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoEscMIBCompliance.setDescription('This is a default module-compliance containing default object groups.')
ciscoEscMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2, 1)).setObjects(("CISCO-ESC-MIB", "escStatusCode"), ("CISCO-ESC-MIB", "escStatusMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEscMIBObjectGroup = ciscoEscMIBObjectGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEscMIBObjectGroup.setDescription('The is a test group.')
ciscoEscMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2, 2)).setObjects(("CISCO-ESC-MIB", "escStatusNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEscMIBNotificationGroup = ciscoEscMIBNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoEscMIBNotificationGroup.setDescription('The is a test group.')
mibBuilder.exportSymbols("CISCO-ESC-MIB", ciscoEscMIB=ciscoEscMIB, escNotifs=escNotifs, escStatusMessage=escStatusMessage, ciscoEscMIBCompliance=ciscoEscMIBCompliance, ciscoEscMIBGroups=ciscoEscMIBGroups, ciscoEscMIBNotificationGroup=ciscoEscMIBNotificationGroup, escStatusNotif=escStatusNotif, escStatusCode=escStatusCode, ciscoEscMIBConform=ciscoEscMIBConform, ciscoEscMIBObjectGroup=ciscoEscMIBObjectGroup, ciscoEscMIBCompliances=ciscoEscMIBCompliances, PYSNMP_MODULE_ID=ciscoEscMIB, escMIBObjects=escMIBObjects, vnfm=vnfm)
