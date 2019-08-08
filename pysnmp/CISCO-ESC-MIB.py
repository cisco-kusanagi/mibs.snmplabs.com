#
# PySNMP MIB module CISCO-ESC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ESC-MIB
# Produced by pysmi-0.3.4 at Wed Aug  7 17:20:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.7.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, Unsigned32, Counter32, IpAddress, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, NotificationType, Integer32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Unsigned32", "Counter32", "IpAddress", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "NotificationType", "Integer32", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoEscMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 844))
ciscoEscMIB.setRevisions(('2017-03-28 00:00',))
if mibBuilder.loadTexts: ciscoEscMIB.setLastUpdated('201705020000Z')
if mibBuilder.loadTexts: ciscoEscMIB.setOrganization('Cisco Systems, Inc.')
escNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 0))
escMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 1))
ciscoEscMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 2))
vnfm = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1))
escStatusMessage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: escStatusMessage.setStatus('current')
escStatusCode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 844, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: escStatusCode.setStatus('current')
escStatusNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 844, 0, 1)).setObjects(("CISCO-ESC-MIB", "escStatusCode"), ("CISCO-ESC-MIB", "escStatusMessage"))
if mibBuilder.loadTexts: escStatusNotif.setStatus('current')
ciscoEscMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 1))
ciscoEscMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2))
ciscoEscMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 1, 1)).setObjects(("CISCO-ESC-MIB", "ciscoEscMIBObjectGroup"), ("CISCO-ESC-MIB", "ciscoEscMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEscMIBCompliance = ciscoEscMIBCompliance.setStatus('current')
ciscoEscMIBObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2, 1)).setObjects(("CISCO-ESC-MIB", "escStatusCode"), ("CISCO-ESC-MIB", "escStatusMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEscMIBObjectGroup = ciscoEscMIBObjectGroup.setStatus('current')
ciscoEscMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 844, 2, 2, 2)).setObjects(("CISCO-ESC-MIB", "escStatusNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEscMIBNotificationGroup = ciscoEscMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ESC-MIB", ciscoEscMIBCompliance=ciscoEscMIBCompliance, ciscoEscMIBConform=ciscoEscMIBConform, PYSNMP_MODULE_ID=ciscoEscMIB, vnfm=vnfm, escStatusMessage=escStatusMessage, escStatusNotif=escStatusNotif, ciscoEscMIBCompliances=ciscoEscMIBCompliances, ciscoEscMIBGroups=ciscoEscMIBGroups, ciscoEscMIBObjectGroup=ciscoEscMIBObjectGroup, ciscoEscMIBNotificationGroup=ciscoEscMIBNotificationGroup, ciscoEscMIB=ciscoEscMIB, escNotifs=escNotifs, escStatusCode=escStatusCode, escMIBObjects=escMIBObjects)
