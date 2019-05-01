#
# PySNMP MIB module ZYXEL-EXTERNAL-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-EXTERNAL-ALARM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:49:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Bits, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, ObjectIdentity, Counter32, Counter64, iso, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Bits", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "ObjectIdentity", "Counter32", "Counter64", "iso", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelExternalAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25))
if mibBuilder.loadTexts: zyxelExternalAlarm.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelExternalAlarm.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelExternalAlarm.setContactInfo('')
if mibBuilder.loadTexts: zyxelExternalAlarm.setDescription('The subtree for external alarm')
zyxelExternalAlarmTrapInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1))
zyxelExternalAlarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2))
zyExternalAlarmTrapAlarmId = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyExternalAlarmTrapAlarmId.setStatus('current')
if mibBuilder.loadTexts: zyExternalAlarmTrapAlarmId.setDescription('This trap displays which ID of external alarm is detected.')
zyExternalAlarmDetect = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2, 1)).setObjects(("ZYXEL-EXTERNAL-ALARM-MIB", "zyExternalAlarmTrapAlarmId"))
if mibBuilder.loadTexts: zyExternalAlarmDetect.setStatus('current')
if mibBuilder.loadTexts: zyExternalAlarmDetect.setDescription('External alarm is detected.')
mibBuilder.exportSymbols("ZYXEL-EXTERNAL-ALARM-MIB", zyxelExternalAlarmTrapInfoObjects=zyxelExternalAlarmTrapInfoObjects, PYSNMP_MODULE_ID=zyxelExternalAlarm, zyxelExternalAlarmNotifications=zyxelExternalAlarmNotifications, zyExternalAlarmTrapAlarmId=zyExternalAlarmTrapAlarmId, zyxelExternalAlarm=zyxelExternalAlarm, zyExternalAlarmDetect=zyExternalAlarmDetect)
