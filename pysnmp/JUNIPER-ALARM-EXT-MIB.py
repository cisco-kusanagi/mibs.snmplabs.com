#
# PySNMP MIB module JUNIPER-ALARM-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-ALARM-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:47:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alarmClearEntry, = mibBuilder.importSymbols("ALARM-MIB", "alarmClearEntry")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
jnxMibs, jnxAlarmExtMibRoot = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs", "jnxAlarmExtMibRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Integer32, NotificationType, Gauge32, IpAddress, Bits, Counter32, MibIdentifier, TimeTicks, Counter64, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Integer32", "NotificationType", "Gauge32", "IpAddress", "Bits", "Counter32", "MibIdentifier", "TimeTicks", "Counter64", "iso", "ModuleIdentity")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
jnxAlarmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 72, 1))
if mibBuilder.loadTexts: jnxAlarmMIB.setLastUpdated('201209041502Z')
if mibBuilder.loadTexts: jnxAlarmMIB.setOrganization('Juniper Networks, Inc.')
jnxAlarmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 72, 1, 1))
jnxAlarmClearTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 72, 1, 1, 1), )
if mibBuilder.loadTexts: jnxAlarmClearTable.setStatus('current')
jnxAlarmClearEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 72, 1, 1, 1, 1), )
alarmClearEntry.registerAugmentions(("JUNIPER-ALARM-EXT-MIB", "jnxAlarmClearEntry"))
jnxAlarmClearEntry.setIndexNames(*alarmClearEntry.getIndexNames())
if mibBuilder.loadTexts: jnxAlarmClearEntry.setStatus('current')
jnxAlarmClearActiveDateAndTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 72, 1, 1, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxAlarmClearActiveDateAndTime.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-ALARM-EXT-MIB", jnxAlarmClearEntry=jnxAlarmClearEntry, PYSNMP_MODULE_ID=jnxAlarmMIB, jnxAlarmClearActiveDateAndTime=jnxAlarmClearActiveDateAndTime, jnxAlarmClearTable=jnxAlarmClearTable, jnxAlarmMIB=jnxAlarmMIB, jnxAlarmObjects=jnxAlarmObjects)
