#
# PySNMP MIB module JUNIPER-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SONET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
jnxMibs, jnxSonetNotifications = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs", "jnxSonetNotifications")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, IpAddress, Unsigned32, Gauge32, Counter32, Counter64, iso, MibIdentifier, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "IpAddress", "Unsigned32", "Gauge32", "Counter32", "Counter64", "iso", "MibIdentifier", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
jnxSonet = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 20))
jnxSonet.setRevisions(('2002-12-12 00:00', '2002-08-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxSonet.setRevisionsDescriptions(('Added sdh-specific alarms to JnxSonetAlarmId.', 'Initial revision.',))
if mibBuilder.loadTexts: jnxSonet.setLastUpdated('200307182154Z')
if mibBuilder.loadTexts: jnxSonet.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxSonet.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxSonet.setDescription('This MIB module defines objects used for managing the sonet/sdh interfaces of Juniper products.')
class JnxSonetAlarmId(TextualConvention, Bits):
    description = 'Identifies specific sonet/sdh alarms that may exist on an interface.'
    status = 'current'
    namedValues = NamedValues(("sonetLolAlarm", 0), ("sonetPllAlarm", 1), ("sonetLofAlarm", 2), ("sonetLosAlarm", 3), ("sonetSefAlarm", 4), ("sonetLaisAlarm", 5), ("sonetPaisAlarm", 6), ("sonetLopAlarm", 7), ("sonetBerrSdAlarm", 8), ("sonetBerrSfAlarm", 9), ("sonetLrdiAlarm", 10), ("sonetPrdiAlarm", 11), ("sonetReiAlarm", 12), ("sonetUneqAlarm", 13), ("sonetPmisAlarm", 14), ("sonetLocAlarm", 15), ("sonetVaisAlarm", 16), ("sonetVlopAlarm", 17), ("sonetVrdiAlarm", 18), ("sonetVuneqAlarm", 19), ("sonetVmisAlarm", 20), ("sonetVlocAlarm", 21), ("sdhLolAlarm", 22), ("sdhPllAlarm", 23), ("sdhLofAlarm", 24), ("sdhLosAlarm", 25), ("sdhOofAlarm", 26), ("sdhMsAisAlarm", 27), ("sdhHpAisAlarm", 28), ("sdhLopAlarm", 29), ("sdhBerrSdAlarm", 30), ("sdhBerrSfAlarm", 31), ("sdhMsFerfAlarm", 32), ("sdhHpFerfAlarm", 33), ("sdhMsFebeAlarm", 34), ("sdhHpUneqAlarm", 35), ("sdhHpMisAlarm", 36), ("sdhLocAlarm", 37))

jnxSonetAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1))
jnxSonetAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1), )
if mibBuilder.loadTexts: jnxSonetAlarmTable.setStatus('current')
if mibBuilder.loadTexts: jnxSonetAlarmTable.setDescription('Information about alarms on all the sonet/sdh physical interfaces on this router.')
jnxSonetAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: jnxSonetAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: jnxSonetAlarmEntry.setDescription('Information about alarms on a sonet/sdh physical interface on this router.')
jnxSonetCurrentAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 1), JnxSonetAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetCurrentAlarms.setStatus('current')
if mibBuilder.loadTexts: jnxSonetCurrentAlarms.setDescription('This object identifies all the active sonet/sdh alarms on this interface.')
jnxSonetLastAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 2), JnxSonetAlarmId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetLastAlarmId.setStatus('current')
if mibBuilder.loadTexts: jnxSonetLastAlarmId.setDescription('The object identifies the sonet/sdh alarm that most recently was set or cleared.')
jnxSonetLastAlarmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetLastAlarmTime.setStatus('current')
if mibBuilder.loadTexts: jnxSonetLastAlarmTime.setDescription('The value of sysUpTime when the management subsystem learned of the last alarm event.')
jnxSonetLastAlarmDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetLastAlarmDate.setStatus('current')
if mibBuilder.loadTexts: jnxSonetLastAlarmDate.setDescription('The system date and time when the management subsystem learned of the last alarm event.')
jnxSonetLastAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("set", 2), ("cleared", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxSonetLastAlarmEvent.setStatus('current')
if mibBuilder.loadTexts: jnxSonetLastAlarmEvent.setDescription('This indicates whether the last alarm event set a new alarm or cleared an existing alarm.')
jnxSonetNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 6, 0))
jnxSonetAlarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 6, 0, 1)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmId"), ("JUNIPER-SONET-MIB", "jnxSonetCurrentAlarms"), ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmDate"))
if mibBuilder.loadTexts: jnxSonetAlarmSet.setStatus('current')
if mibBuilder.loadTexts: jnxSonetAlarmSet.setDescription('Notification of a recently set sonet/sdh alarm.')
jnxSonetAlarmCleared = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 6, 0, 2)).setObjects(("IF-MIB", "ifDescr"), ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmId"), ("JUNIPER-SONET-MIB", "jnxSonetCurrentAlarms"), ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmDate"))
if mibBuilder.loadTexts: jnxSonetAlarmCleared.setStatus('current')
if mibBuilder.loadTexts: jnxSonetAlarmCleared.setDescription('Notification of a recently cleared sonet/sdh alarm.')
mibBuilder.exportSymbols("JUNIPER-SONET-MIB", jnxSonetAlarmEntry=jnxSonetAlarmEntry, PYSNMP_MODULE_ID=jnxSonet, jnxSonetLastAlarmTime=jnxSonetLastAlarmTime, jnxSonetNotificationPrefix=jnxSonetNotificationPrefix, jnxSonetCurrentAlarms=jnxSonetCurrentAlarms, jnxSonetLastAlarmEvent=jnxSonetLastAlarmEvent, jnxSonetLastAlarmId=jnxSonetLastAlarmId, jnxSonetAlarmSet=jnxSonetAlarmSet, jnxSonetLastAlarmDate=jnxSonetLastAlarmDate, jnxSonetAlarms=jnxSonetAlarms, jnxSonet=jnxSonet, JnxSonetAlarmId=JnxSonetAlarmId, jnxSonetAlarmTable=jnxSonetAlarmTable, jnxSonetAlarmCleared=jnxSonetAlarmCleared)
