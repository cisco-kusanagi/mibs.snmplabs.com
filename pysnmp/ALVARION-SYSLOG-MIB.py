#
# PySNMP MIB module ALVARION-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionNotificationEnable, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionNotificationEnable")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, iso, Bits, TimeTicks, Counter64, MibIdentifier, ModuleIdentity, Counter32, IpAddress, Unsigned32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Bits", "TimeTicks", "Counter64", "MibIdentifier", "ModuleIdentity", "Counter32", "IpAddress", "Unsigned32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alvarionSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3))
if mibBuilder.loadTexts: alvarionSyslogMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionSyslogMIB.setOrganization('Alvarion Ltd.')
alvarionSyslogMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1))
syslogConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1))
syslogMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2))
class SyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))

syslogSeverityNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 1), AlvarionNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogSeverityNotificationEnabled.setStatus('current')
syslogRegExMatchNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 2), AlvarionNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogRegExMatchNotificationEnabled.setStatus('current')
syslogSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 3), SyslogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogSeverityLevel.setStatus('current')
syslogTrapSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 4), SyslogSeverity().clone('warning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogTrapSeverityLevel.setStatus('current')
syslogMessageRegEx = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogMessageRegEx.setStatus('current')
syslogMsgNumber = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgNumber.setStatus('current')
syslogMsgFacility = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgFacility.setStatus('current')
syslogMsgSeverity = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2, 3), SyslogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgSeverity.setStatus('current')
syslogMsgText = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgText.setStatus('current')
alvarionSyslogMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 2))
alvarionSyslogMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 2, 0))
syslogSeverityNotification = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 2, 0, 1)).setObjects(("ALVARION-SYSLOG-MIB", "syslogMsgNumber"), ("ALVARION-SYSLOG-MIB", "syslogMsgFacility"), ("ALVARION-SYSLOG-MIB", "syslogMsgSeverity"), ("ALVARION-SYSLOG-MIB", "syslogMsgText"))
if mibBuilder.loadTexts: syslogSeverityNotification.setStatus('current')
syslogRegExMatchNotification = NotificationType((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 2, 0, 2)).setObjects(("ALVARION-SYSLOG-MIB", "syslogMsgNumber"), ("ALVARION-SYSLOG-MIB", "syslogMsgFacility"), ("ALVARION-SYSLOG-MIB", "syslogMsgSeverity"), ("ALVARION-SYSLOG-MIB", "syslogMsgText"))
if mibBuilder.loadTexts: syslogRegExMatchNotification.setStatus('current')
alvarionSyslogMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3))
alvarionSyslogMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 1))
alvarionSyslogMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 2))
alvarionSyslogMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 1, 1)).setObjects(("ALVARION-SYSLOG-MIB", "alvarionSyslogMIBGroup"), ("ALVARION-SYSLOG-MIB", "alvarionSyslogNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionSyslogMIBCompliance = alvarionSyslogMIBCompliance.setStatus('current')
alvarionSyslogMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 2, 1)).setObjects(("ALVARION-SYSLOG-MIB", "syslogSeverityNotificationEnabled"), ("ALVARION-SYSLOG-MIB", "syslogRegExMatchNotificationEnabled"), ("ALVARION-SYSLOG-MIB", "syslogSeverityLevel"), ("ALVARION-SYSLOG-MIB", "syslogTrapSeverityLevel"), ("ALVARION-SYSLOG-MIB", "syslogMessageRegEx"), ("ALVARION-SYSLOG-MIB", "syslogMsgNumber"), ("ALVARION-SYSLOG-MIB", "syslogMsgFacility"), ("ALVARION-SYSLOG-MIB", "syslogMsgSeverity"), ("ALVARION-SYSLOG-MIB", "syslogMsgText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionSyslogMIBGroup = alvarionSyslogMIBGroup.setStatus('current')
alvarionSyslogNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 2, 2)).setObjects(("ALVARION-SYSLOG-MIB", "syslogSeverityNotification"), ("ALVARION-SYSLOG-MIB", "syslogRegExMatchNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionSyslogNotificationGroup = alvarionSyslogNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-SYSLOG-MIB", alvarionSyslogNotificationGroup=alvarionSyslogNotificationGroup, syslogMessageRegEx=syslogMessageRegEx, alvarionSyslogMIB=alvarionSyslogMIB, syslogMsgNumber=syslogMsgNumber, alvarionSyslogMIBConformance=alvarionSyslogMIBConformance, syslogTrapSeverityLevel=syslogTrapSeverityLevel, PYSNMP_MODULE_ID=alvarionSyslogMIB, alvarionSyslogMIBNotifications=alvarionSyslogMIBNotifications, syslogMsgFacility=syslogMsgFacility, alvarionSyslogMIBGroup=alvarionSyslogMIBGroup, syslogSeverityNotificationEnabled=syslogSeverityNotificationEnabled, syslogConfig=syslogConfig, alvarionSyslogMIBGroups=alvarionSyslogMIBGroups, syslogMsgText=syslogMsgText, syslogMsgSeverity=syslogMsgSeverity, alvarionSyslogMIBCompliances=alvarionSyslogMIBCompliances, syslogSeverityLevel=syslogSeverityLevel, alvarionSyslogMIBCompliance=alvarionSyslogMIBCompliance, SyslogSeverity=SyslogSeverity, syslogMessage=syslogMessage, syslogRegExMatchNotificationEnabled=syslogRegExMatchNotificationEnabled, syslogRegExMatchNotification=syslogRegExMatchNotification, alvarionSyslogMIBObjects=alvarionSyslogMIBObjects, alvarionSyslogMIBNotificationPrefix=alvarionSyslogMIBNotificationPrefix, syslogSeverityNotification=syslogSeverityNotification)
