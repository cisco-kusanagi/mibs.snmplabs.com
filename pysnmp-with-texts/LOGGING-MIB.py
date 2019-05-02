#
# PySNMP MIB module LOGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LOGGING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:08:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
agentInventoryComponentIndex, = mibBuilder.importSymbols("INVENTORY-MIB", "agentInventoryComponentIndex")
switch, quanta = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch", "quanta")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, MibIdentifier, Integer32, ObjectIdentity, Gauge32, Bits, iso, Counter64, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "MibIdentifier", "Integer32", "ObjectIdentity", "Gauge32", "Bits", "iso", "Counter64", "NotificationType", "Counter32")
DateAndTime, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "TextualConvention", "DisplayString")
class AgentLogFacility(TextualConvention, Integer32):
    reference = 'RFC3164 - 4.1.1: Table 1'
    description = 'Facility code used in determining the SysLog Priority value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("user", 1), ("mail", 2), ("system", 3), ("security", 4), ("syslog", 5), ("lpr", 6), ("nntp", 7), ("uucp", 8), ("cron", 9), ("auth", 10), ("ftp", 11), ("ntp", 12), ("audit", 13), ("alert", 14), ("clock", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class AgentLogSeverity(TextualConvention, Integer32):
    reference = 'RFC3164 - 4.1.1: Table 2'
    description = 'Severity code used in determining the SysLog Priority value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("informational", 6), ("debug", 7))

logging = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 14))
if mibBuilder.loadTexts: logging.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: logging.setOrganization('Quanta Computer Inc.')
if mibBuilder.loadTexts: logging.setContactInfo(' Customer Support Postal: Quanta Computer Inc. 4, Wen Ming 1 St., Kuei Shan Hsiang, Tao Yuan Shien, Taiwan, R.O.C. Tel: +886 3 328 0050 E-Mail: strong.chen@quantatw.com')
if mibBuilder.loadTexts: logging.setDescription('This MIB provides objects to configure and display events logged on this system.')
agentLogConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1))
agentLogInMemoryConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 1))
agentLogInMemoryAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogInMemoryAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryAdminStatus.setDescription('Administratively enable/disable the In Memory log.')
agentLogInMemoryBehavior = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wrap", 1), ("stop-on-full", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogInMemoryBehavior.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryBehavior.setDescription('Configures the behavior of the In Memory Log when it becomes full. A value of wrap(1) will cause the oldest log message to be removed, making room for the new message. A value of stop-on-full(2) will prevent any further logging.')
agentLogConsoleConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 2))
agentLogConsoleAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogConsoleAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogConsoleAdminStatus.setDescription('Admin mode for console logs')
agentLogConsoleSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 2, 2), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogConsoleSeverityFilter.setStatus('current')
if mibBuilder.loadTexts: agentLogConsoleSeverityFilter.setDescription('Severity filter for console logs')
agentLogSysLogConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4))
agentLogSyslogAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogAdminStatus.setDescription('For Enabling and Disabling logging to configured syslog hosts. Setting this to disable stops logging to all syslog hosts.')
agentLogSyslogLocalPort = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogLocalPort.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogLocalPort.setDescription('This is the port on the local host from which syslog messages are sent.')
agentLogSyslogMaxHosts = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMaxHosts.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogMaxHosts.setDescription('Maximum number of hosts that can be configured for logging syslog messages.')
agentLogCliCommandsConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 5))
agentLogCliCommandsAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogCliCommandsAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogCliCommandsAdminStatus.setDescription('Administratively enable/disable the logging of the CLI Commands ')
agentLogTerminalConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 6))
agentLogTerminalAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogTerminalAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogTerminalAdminStatus.setDescription('Admin mode for terminal logs')
agentLogTerminalSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 6, 2), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogTerminalSeverityFilter.setStatus('current')
if mibBuilder.loadTexts: agentLogTerminalSeverityFilter.setDescription('Severity filter for terminal logs')
agentLogSyslogHostTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 5), )
if mibBuilder.loadTexts: agentLogSyslogHostTable.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogHostTable.setDescription('Syslog host table containing syslog host entries.')
agentLogSyslogHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 5, 1), ).setIndexNames((0, "LOGGING-MIB", "agentLogHostTableIndex"))
if mibBuilder.loadTexts: agentLogSyslogHostEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogHostEntry.setDescription('Syslog Host entry attributes.')
agentLogHostTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogHostTableIndex.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableIndex.setDescription('Index to syslog host entry in syslog host table.')
agentLogHostTableIpAddressOrHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 5, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableIpAddressOrHostName.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableIpAddressOrHostName.setDescription('Syslog Host table IP Address.')
agentLogHostTableType = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 16, 17))).clone(namedValues=NamedValues(("unknown", 0), ("ipv4", 1), ("ipv6", 2), ("dns", 16), ("dnsv6", 17)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableType.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableType.setDescription('Syslog Host table Type.')
agentLogHostTablePort = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTablePort.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTablePort.setDescription('Syslog Host table port number.')
agentLogHostTableSeverityFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 5, 1, 5), AgentLogSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableSeverityFilter.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableSeverityFilter.setDescription('Configures the minimum severity that will be stored in the In Memory log.')
agentLogHostTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 5, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableRowStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableRowStatus.setDescription('Syslog Host table row status')
agentLogSyslogSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 6), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogSourceInterface.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogSourceInterface.setDescription('A source-interface selection on an Interface Index (like vlan based routing interface, port based routing interface, loopback interface, tunnel interface). A non-zero value indicates ifIndex for the corresponding interface entry in the ifTable is selected. A zero value indicates the source-interface un-selection.')
agentLogSyslogFacility = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 4, 7), AgentLogFacility()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogFacility.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogFacility.setDescription('This is the facility which is sent in syslog messages.')
agentLogStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2))
agentLogMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessagesReceived.setStatus('current')
if mibBuilder.loadTexts: agentLogMessagesReceived.setDescription('The number of messages received by the log process. This includes messages that are dropped or ignored.')
agentLogMessagesDropped = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessagesDropped.setStatus('current')
if mibBuilder.loadTexts: agentLogMessagesDropped.setDescription('The number of messages that could not be processed due to error or lack of resources.')
agentLogSyslogMessagesRelayed = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessagesRelayed.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogMessagesRelayed.setDescription('The number of messages forwarded by the syslog function to a syslog host. Messages forwarded to multiple hosts are counted once for each host.')
agentLogSyslogMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessagesIgnored.setStatus('deprecated')
if mibBuilder.loadTexts: agentLogSyslogMessagesIgnored.setDescription('The number of messages that were not processed by the syslog process because the component name or the priority level did not match any specification.')
agentLogMessageReceivedTime = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessageReceivedTime.setStatus('current')
if mibBuilder.loadTexts: agentLogMessageReceivedTime.setDescription('The local time when a message was last received by the log subsystem specified as the number of non-leap seconds since 00:00:00 UTC on January 1 1970.')
agentLogSyslogMessageDeliveredTime = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessageDeliveredTime.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogMessageDeliveredTime.setDescription('The local time when a message was last delivered to a syslog host specified as the number of non-leap seconds since 00:00:00 UTC on January 1 1970.')
agentLogEmailAlertConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10))
agentLogEmailAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailAdminStatus.setDescription('For Enabling and Disabling email alerts to SMTP server. Setting this to disable stops emailing to SMTP servers.')
agentLogEmailfromAddr = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailfromAddr.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailfromAddr.setDescription('Sender Email Address. Maximum length is 255')
agentLogEmaillogDuration = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmaillogDuration.setStatus('current')
if mibBuilder.loadTexts: agentLogEmaillogDuration.setDescription('This duration in minutes determines how frequently the non critical messages are sent to the SMTP server.')
agentLogEmailUrgentSeverity = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 4), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailUrgentSeverity.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailUrgentSeverity.setDescription('This is the severity level for the critical log messages')
agentLogEmailNonUrgentSeverity = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 5), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailNonUrgentSeverity.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailNonUrgentSeverity.setDescription('This is the severity level for the non critical log messages.')
agentLogEmailUrgentAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailUrgentAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailUrgentAdminStatus.setDescription('For Enabling and Disabling email urgent alerts to SMTP server. Setting this to disable stops urgent emailing to SMTP servers.')
agentLogEmailNonUrgentAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailNonUrgentAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailNonUrgentAdminStatus.setDescription('For Enabling and Disabling email non-urgent alerts to SMTP server. Setting this to disable stops non-urgent emailing to SMTP servers.')
agentLogEmailTrapsSeverity = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 6), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailTrapsSeverity.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailTrapsSeverity.setDescription('This is the severity level for Trap messages.')
agentLogEmailToAddrTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 7), )
if mibBuilder.loadTexts: agentLogEmailToAddrTable.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddrTable.setDescription('The (conceptual) table listing the destination email address and the message type.')
agentLogEmailToAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 7, 1), ).setIndexNames((0, "LOGGING-MIB", "agentLogEmailToAddrMessageType"), (0, "LOGGING-MIB", "agentLogEmailToAddr"))
if mibBuilder.loadTexts: agentLogEmailToAddrEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddrEntry.setDescription('An entry (conceptual row) in the agentLogEmailtoAddrTable. This entry shows what kind of messages go to the given destination email addresses.')
agentLogEmailToAddrMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("critical", 1), ("non-critical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailToAddrMessageType.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddrMessageType.setDescription('Log message Type')
agentLogEmailToAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailToAddr.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddr.setDescription('Recipient Email Address. Maximum length is 255')
agentLogEmailToAddrEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailToAddrEntryStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddrEntryStatus.setDescription('This is to create or delete the entry')
agentLogEmailSubjectTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 8), )
if mibBuilder.loadTexts: agentLogEmailSubjectTable.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubjectTable.setDescription('The (conceptual) table listing the subject of the email and the message type.')
agentLogEmailSubjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 8, 1), ).setIndexNames((0, "LOGGING-MIB", "agentLogEmailSubjectMessageType"))
if mibBuilder.loadTexts: agentLogEmailSubjectEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubjectEntry.setDescription('An entry (conceptual row) in the agentLogEmailtoAddrTable. This entry shows what kind of subject to be used for the given message type.')
agentLogEmailSubjectMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("critical", 1), ("non-critical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailSubjectMessageType.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubjectMessageType.setDescription('Log message Type')
agentLogEmailSubject = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 8, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailSubject.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubject.setDescription('Email Subject. Maximum length is 255. When this object is set to empty-string, it resets to factory default string.')
agentLogEmailSubjectEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailSubjectEntryStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubjectEntryStatus.setDescription('This is to create or delete the entry')
agentLogEmailMailServerTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9), )
if mibBuilder.loadTexts: agentLogEmailMailServerTable.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailMailServerTable.setDescription('The (conceptual) table listing the mail servers')
agentLogEmailMailServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9, 1), ).setIndexNames((0, "LOGGING-MIB", "agentLogEmailSmtpAddrType"), (0, "LOGGING-MIB", "agentLogEmailSmtpAddr"))
if mibBuilder.loadTexts: agentLogEmailMailServerEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailMailServerEntry.setDescription('An entry (conceptual row) in the agentLogEmailMailServerTable. This entry shows the conmfiguration for mail server.')
agentLogEmailSmtpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailSmtpAddrType.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSmtpAddrType.setDescription('Email SMTP Address type')
agentLogEmailSmtpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailSmtpAddr.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSmtpAddr.setDescription('SMTP server Address')
agentLogEmailSmtpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9, 1, 3), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailSmtpPort.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSmtpPort.setDescription('SMTP Port number. When this object is set to 0, it resets to factory default port number.')
agentLogEmailSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("tlsv1", 2), ("starttls", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailSecurity.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSecurity.setDescription('This is the authentication mechanism that should be used. Well known port for none security is 25, sslv3/tlsv1 is 465, and starttls is 587 or 25.')
agentLogEmailloginID = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailloginID.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailloginID.setDescription('This user id is used while the switch/router is being authenticated by the SMTP server.The user ID should be minimum of 1 charcter to maximum of 32 characters.')
agentLogEmailPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailPassword.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailPassword.setDescription('This password is used while the switch/router is being authenticated by the SMTP server.The password should be minimum of 1 character to maximum of 32 characters.')
agentLogEmailEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 1, 10, 9, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailEntryStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailEntryStatus.setDescription('This is to create or delete the entry')
agentLogEmailAlertStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 7))
agentLogEmailStatsemailsSentCount = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsemailsSentCount.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailStatsemailsSentCount.setDescription('This is the count to show the no of emails sent so far.')
agentLogEmailStatsemailsFailureCount = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsemailsFailureCount.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailStatsemailsFailureCount.setDescription('This is the count to show the no of emails failures happened so far...')
agentLogEmailStatsTimeSinceLastEmailSent = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 7, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsTimeSinceLastEmailSent.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailStatsTimeSinceLastEmailSent.setDescription('This is the number of seconds since the last email was sent.')
agentLogEmailStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 2, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailStatsClear.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailStatsClear.setDescription('This is to clear the email alert stats.')
agentLogInMemoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 3))
agentLogInMemoryLogCount = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 14, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogInMemoryLogCount.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryLogCount.setDescription('The count of valid entries in the in-memory log.')
agentLogInMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 14, 3, 2), )
if mibBuilder.loadTexts: agentLogInMemoryTable.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryTable.setDescription('The in-memory log table containing sequence of in-memory log entries.')
agentLogInMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 14, 3, 2, 1), ).setIndexNames((0, "LOGGING-MIB", "agentLogInMemoryMsgIndex"))
if mibBuilder.loadTexts: agentLogInMemoryEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryEntry.setDescription('An individual message entry in in-memory log table.')
agentLogInMemoryMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogInMemoryMsgIndex.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryMsgIndex.setDescription('The index to message entry in the in-memory log table.')
agentLogInMemoryMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 14, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogInMemoryMsgText.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryMsgText.setDescription('Message text info for inmemory logged messages.')
agentLogTrapsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 5))
agentLogEmailAlertTrapsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 14, 5, 1))
agentLogEmailSendFailed = NotificationType((1, 3, 6, 1, 4, 1, 7244, 2, 14, 5, 1, 1)).setObjects(("LOGGING-MIB", "agentLogEmailStatsemailsFailureCount"))
if mibBuilder.loadTexts: agentLogEmailSendFailed.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSendFailed.setDescription('When ever a mail sending to the SMTP server is failed, this trap is sent with a count of how many times the connection to the SMTP server is failed so far.')
mibBuilder.exportSymbols("LOGGING-MIB", agentLogHostTableIndex=agentLogHostTableIndex, agentLogSyslogMessagesRelayed=agentLogSyslogMessagesRelayed, agentLogMessageReceivedTime=agentLogMessageReceivedTime, agentLogTerminalConfigGroup=agentLogTerminalConfigGroup, agentLogEmailStatsemailsSentCount=agentLogEmailStatsemailsSentCount, agentLogSyslogLocalPort=agentLogSyslogLocalPort, agentLogCliCommandsAdminStatus=agentLogCliCommandsAdminStatus, agentLogEmailUrgentSeverity=agentLogEmailUrgentSeverity, agentLogEmailPassword=agentLogEmailPassword, agentLogHostTableRowStatus=agentLogHostTableRowStatus, AgentLogFacility=AgentLogFacility, agentLogEmailMailServerTable=agentLogEmailMailServerTable, agentLogEmailAlertTrapsGroup=agentLogEmailAlertTrapsGroup, agentLogHostTableType=agentLogHostTableType, agentLogMessagesReceived=agentLogMessagesReceived, agentLogConsoleConfigGroup=agentLogConsoleConfigGroup, agentLogEmailNonUrgentAdminStatus=agentLogEmailNonUrgentAdminStatus, agentLogEmailUrgentAdminStatus=agentLogEmailUrgentAdminStatus, agentLogEmailToAddrTable=agentLogEmailToAddrTable, logging=logging, agentLogEmailSmtpAddr=agentLogEmailSmtpAddr, agentLogEmailAdminStatus=agentLogEmailAdminStatus, agentLogEmailAlertStatsGroup=agentLogEmailAlertStatsGroup, agentLogEmailSubjectEntry=agentLogEmailSubjectEntry, agentLogHostTableSeverityFilter=agentLogHostTableSeverityFilter, agentLogEmailloginID=agentLogEmailloginID, agentLogCliCommandsConfigGroup=agentLogCliCommandsConfigGroup, agentLogHostTableIpAddressOrHostName=agentLogHostTableIpAddressOrHostName, agentLogConfigGroup=agentLogConfigGroup, agentLogEmailToAddrEntry=agentLogEmailToAddrEntry, agentLogMessagesDropped=agentLogMessagesDropped, agentLogEmailToAddr=agentLogEmailToAddr, agentLogSysLogConfigGroup=agentLogSysLogConfigGroup, agentLogEmailToAddrMessageType=agentLogEmailToAddrMessageType, AgentLogSeverity=AgentLogSeverity, agentLogStatisticsGroup=agentLogStatisticsGroup, agentLogEmailSubject=agentLogEmailSubject, agentLogConsoleAdminStatus=agentLogConsoleAdminStatus, agentLogEmailMailServerEntry=agentLogEmailMailServerEntry, agentLogSyslogMessageDeliveredTime=agentLogSyslogMessageDeliveredTime, agentLogSyslogAdminStatus=agentLogSyslogAdminStatus, agentLogEmailStatsemailsFailureCount=agentLogEmailStatsemailsFailureCount, agentLogTerminalAdminStatus=agentLogTerminalAdminStatus, agentLogEmailSubjectEntryStatus=agentLogEmailSubjectEntryStatus, agentLogEmailSmtpAddrType=agentLogEmailSmtpAddrType, agentLogEmailSendFailed=agentLogEmailSendFailed, agentLogSyslogMaxHosts=agentLogSyslogMaxHosts, agentLogInMemoryBehavior=agentLogInMemoryBehavior, agentLogConsoleSeverityFilter=agentLogConsoleSeverityFilter, agentLogInMemoryMsgIndex=agentLogInMemoryMsgIndex, agentLogSyslogFacility=agentLogSyslogFacility, agentLogEmailStatsTimeSinceLastEmailSent=agentLogEmailStatsTimeSinceLastEmailSent, agentLogInMemoryAdminStatus=agentLogInMemoryAdminStatus, agentLogTrapsGroup=agentLogTrapsGroup, agentLogEmailSubjectTable=agentLogEmailSubjectTable, agentLogEmailSubjectMessageType=agentLogEmailSubjectMessageType, agentLogEmailEntryStatus=agentLogEmailEntryStatus, agentLogHostTablePort=agentLogHostTablePort, agentLogEmaillogDuration=agentLogEmaillogDuration, agentLogEmailToAddrEntryStatus=agentLogEmailToAddrEntryStatus, agentLogInMemoryConfigGroup=agentLogInMemoryConfigGroup, agentLogEmailSecurity=agentLogEmailSecurity, agentLogInMemoryEntry=agentLogInMemoryEntry, agentLogEmailNonUrgentSeverity=agentLogEmailNonUrgentSeverity, agentLogSyslogHostEntry=agentLogSyslogHostEntry, agentLogEmailfromAddr=agentLogEmailfromAddr, agentLogSyslogSourceInterface=agentLogSyslogSourceInterface, PYSNMP_MODULE_ID=logging, agentLogSyslogHostTable=agentLogSyslogHostTable, agentLogInMemoryGroup=agentLogInMemoryGroup, agentLogEmailStatsClear=agentLogEmailStatsClear, agentLogTerminalSeverityFilter=agentLogTerminalSeverityFilter, agentLogSyslogMessagesIgnored=agentLogSyslogMessagesIgnored, agentLogEmailTrapsSeverity=agentLogEmailTrapsSeverity, agentLogEmailSmtpPort=agentLogEmailSmtpPort, agentLogEmailAlertConfigGroup=agentLogEmailAlertConfigGroup, agentLogInMemoryMsgText=agentLogInMemoryMsgText, agentLogInMemoryLogCount=agentLogInMemoryLogCount, agentLogInMemoryTable=agentLogInMemoryTable)
