#
# PySNMP MIB module RTBRICK-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/RTBRICK-SYSLOG-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:35:46 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rtbrickTraps, rtbrickModules, rtbrickSyslogNotifications = mibBuilder.importSymbols("RTBRICK-MIB", "rtbrickTraps", "rtbrickModules", "rtbrickSyslogNotifications")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, ObjectIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, NotificationType, Bits, iso, Integer32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "NotificationType", "Bits", "iso", "Integer32", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rtBrickSyslogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 50058, 104, 2))
rtBrickSyslogMIB.setRevisions(('2019-01-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rtBrickSyslogMIB.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: rtBrickSyslogMIB.setLastUpdated('201804140000Z')
if mibBuilder.loadTexts: rtBrickSyslogMIB.setOrganization('RtBrick')
if mibBuilder.loadTexts: rtBrickSyslogMIB.setContactInfo('E-mail: Stefan Lieberth <stefan@rtbrick.com>')
if mibBuilder.loadTexts: rtBrickSyslogMIB.setDescription('system_software_info')
syslogMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1))
class SyslogSeverity(TextualConvention, Integer32):
    description = 'Indicates the severity of a syslog message. NOTE: This values is the actual value the syslog daemon uses, plus 1. For example: the value for debug severity will be 8 instead of 7.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("info", 7), ("debug", 8))

syslogMsgNumber = MibScalar((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgNumber.setStatus('current')
if mibBuilder.loadTexts: syslogMsgNumber.setDescription('A unique ID representing a message in the system log.')
syslogMsgFacility = MibScalar((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgFacility.setStatus('current')
if mibBuilder.loadTexts: syslogMsgFacility.setDescription('A string representing the facility that sent the message.')
syslogMsgSeverity = MibScalar((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 3), SyslogSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgSeverity.setStatus('current')
if mibBuilder.loadTexts: syslogMsgSeverity.setDescription('The severity level of the message in the system log.')
syslogMsgText = MibScalar((1, 3, 6, 1, 4, 1, 50058, 104, 2, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: syslogMsgText.setStatus('current')
if mibBuilder.loadTexts: syslogMsgText.setDescription('The message itself as logged in the system log.')
rtbrickSyslogNotificationPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 50058, 103, 1, 0))
if mibBuilder.loadTexts: rtbrickSyslogNotificationPrefix.setStatus('current')
if mibBuilder.loadTexts: rtbrickSyslogNotificationPrefix.setDescription('All Syslog notifications are registered under this branch.')
rtbrickSyslogTrap = NotificationType((1, 3, 6, 1, 4, 1, 50058, 103, 1, 0, 1))
if mibBuilder.loadTexts: rtbrickSyslogTrap.setStatus('current')
if mibBuilder.loadTexts: rtbrickSyslogTrap.setDescription('Notification of a generated syslog message')
mibBuilder.exportSymbols("RTBRICK-SYSLOG-MIB", syslogMsgNumber=syslogMsgNumber, syslogMessage=syslogMessage, rtbrickSyslogTrap=rtbrickSyslogTrap, PYSNMP_MODULE_ID=rtBrickSyslogMIB, SyslogSeverity=SyslogSeverity, syslogMsgFacility=syslogMsgFacility, syslogMsgText=syslogMsgText, rtBrickSyslogMIB=rtBrickSyslogMIB, rtbrickSyslogNotificationPrefix=rtbrickSyslogNotificationPrefix, syslogMsgSeverity=syslogMsgSeverity)
