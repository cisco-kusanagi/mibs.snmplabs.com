#
# PySNMP MIB module ZYXEL-EXTERNAL-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-EXTERNAL-ALARM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, TimeTicks, MibIdentifier, Gauge32, iso, Integer32, ObjectIdentity, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "TimeTicks", "MibIdentifier", "Gauge32", "iso", "Integer32", "ObjectIdentity", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelExternalAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25))
if mibBuilder.loadTexts: zyxelExternalAlarm.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelExternalAlarm.setOrganization('Enterprise Solution ZyXEL')
zyxelExternalAlarmTrapInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1))
zyxelExternalAlarmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2))
zyExternalAlarmTrapAlarmId = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyExternalAlarmTrapAlarmId.setStatus('current')
zyExternalAlarmDetect = NotificationType((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 25, 2, 1)).setObjects(("ZYXEL-EXTERNAL-ALARM-MIB", "zyExternalAlarmTrapAlarmId"))
if mibBuilder.loadTexts: zyExternalAlarmDetect.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-EXTERNAL-ALARM-MIB", zyxelExternalAlarmNotifications=zyxelExternalAlarmNotifications, zyxelExternalAlarmTrapInfoObjects=zyxelExternalAlarmTrapInfoObjects, zyExternalAlarmDetect=zyExternalAlarmDetect, zyxelExternalAlarm=zyxelExternalAlarm, zyExternalAlarmTrapAlarmId=zyExternalAlarmTrapAlarmId, PYSNMP_MODULE_ID=zyxelExternalAlarm)
