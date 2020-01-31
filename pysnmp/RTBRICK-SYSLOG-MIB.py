#
# PySNMP MIB module RTBRICK-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/RTBRICK-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:33:01 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
rtbrickSyslogNotifications, rtbrickTraps, rtbrickModules = mibBuilder.importSymbols("RTBRICK-MIB", "rtbrickSyslogNotifications", "rtbrickTraps", "rtbrickModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Counter32, Counter64, MibIdentifier, IpAddress, TimeTicks, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "TimeTicks", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rtBrickSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 50058, 104, 2))
rtBrickSyslogMIB.setRevisions(('2019-01-04 00:00',))
if mibBuilder.loadTexts: rtBrickSyslogMIB.setLastUpdated('201804140000Z')
if mibBuilder.loadTexts: rtBrickSyslogMIB.setOrganization('RtBrick')
syslogMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1))
class SyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))

syslogMsgNumber = MibScalar((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgNumber.setStatus('current')
syslogMsgFacility = MibScalar((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgFacility.setStatus('current')
syslogMsgSeverity = MibScalar((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 3), SyslogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgSeverity.setStatus('current')
syslogMsgText = MibScalar((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgText.setStatus('current')
rtbrickSyslogNotificationPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 50058, 103, 1, 0))
if mibBuilder.loadTexts: rtbrickSyslogNotificationPrefix.setStatus('current')
rtbrickSyslogTrap = NotificationType((1, 3, 6, 1, 4, 1, 50058, 103, 1, 0, 1))
if mibBuilder.loadTexts: rtbrickSyslogTrap.setStatus('current')
mibBuilder.exportSymbols("RTBRICK-SYSLOG-MIB", SyslogSeverity=SyslogSeverity, rtbrickSyslogNotificationPrefix=rtbrickSyslogNotificationPrefix, rtbrickSyslogTrap=rtbrickSyslogTrap, syslogMsgFacility=syslogMsgFacility, rtBrickSyslogMIB=rtBrickSyslogMIB, PYSNMP_MODULE_ID=rtBrickSyslogMIB, syslogMsgText=syslogMsgText, syslogMsgSeverity=syslogMsgSeverity, syslogMsgNumber=syslogMsgNumber, syslogMessage=syslogMessage)
