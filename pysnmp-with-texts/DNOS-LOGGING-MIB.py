#
# PySNMP MIB module DNOS-LOGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DNOS-LOGGING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:51:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
agentInventoryComponentIndex, = mibBuilder.importSymbols("DNOS-INVENTORY-MIB", "agentInventoryComponentIndex")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, MibIdentifier, IpAddress, ObjectIdentity, Gauge32, Unsigned32, Counter64, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibIdentifier", "IpAddress", "ObjectIdentity", "Gauge32", "Unsigned32", "Counter64", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "iso")
RowStatus, TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DateAndTime", "DisplayString")
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

fastPathLogging = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14))
fastPathLogging.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00', '2004-10-26 13:03',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathLogging.setRevisionsDescriptions(('Postal address updated.', 'Dell branding related changes.', 'Initial version.',))
if mibBuilder.loadTexts: fastPathLogging.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathLogging.setOrganization('Dell, Inc.')
if mibBuilder.loadTexts: fastPathLogging.setContactInfo('')
if mibBuilder.loadTexts: fastPathLogging.setDescription('This MIB provides objects to configure and display events logged on this system.')
agentLogConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1))
agentLogInMemoryConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1))
agentLogInMemoryAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogInMemoryAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryAdminStatus.setDescription('Administratively enable/disable the In Memory log.')
agentLogInMemoryBehavior = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wrap", 1), ("stop-on-full", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogInMemoryBehavior.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryBehavior.setDescription('Configures the behavior of the In Memory Log when it becomes full. A value of wrap(1) will cause the oldest log message to be removed, making room for the new message. A value of stop-on-full(2) will prevent any further logging.')
agentLogConsoleConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2))
agentLogConsoleAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogConsoleAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogConsoleAdminStatus.setDescription('Admin mode for console logs')
agentLogConsoleSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 2, 2), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogConsoleSeverityFilter.setStatus('current')
if mibBuilder.loadTexts: agentLogConsoleSeverityFilter.setDescription('Severity filter for console logs')
agentLogSysLogConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4))
agentLogSyslogAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogAdminStatus.setDescription('For Enabling and Disabling logging to configured syslog hosts. Setting this to disable stops logging to all syslog hosts.')
agentLogSyslogLocalPort = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogLocalPort.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogLocalPort.setDescription('This is the port on the local host from which syslog messages are sent.')
agentLogSyslogMaxHosts = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMaxHosts.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogMaxHosts.setDescription('Maximum number of hosts that can be configured for logging syslog messages.')
agentLogCliCommandsConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 5))
agentLogCliCommandsAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogCliCommandsAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogCliCommandsAdminStatus.setDescription('Administratively enable/disable the logging of the CLI Commands ')
agentLogWebConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 7))
agentLogWebAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogWebAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogWebAdminStatus.setDescription('Administratively enable/disable the logging of the Web ')
agentLogSnmpConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 8))
agentLogSnmpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSnmpAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogSnmpAdminStatus.setDescription('Administratively enable/disable the logging of the Snmp ')
agentLogAuditConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 9))
agentLogAuditAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogAuditAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogAuditAdminStatus.setDescription('Administratively enable/disable Switch Auditing ')
agentLogSyslogHostTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5), )
if mibBuilder.loadTexts: agentLogSyslogHostTable.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogHostTable.setDescription('Syslog host table containing syslog host entries.')
agentLogSyslogHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1), ).setIndexNames((0, "DNOS-LOGGING-MIB", "agentLogHostTableIndex"))
if mibBuilder.loadTexts: agentLogSyslogHostEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogHostEntry.setDescription('Syslog Host entry attributes.')
agentLogHostTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogHostTableIndex.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableIndex.setDescription('Index to syslog host entry in syslog host table.')
agentLogHostTableIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableIpAddressType.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableIpAddressType.setDescription('Syslog Host table IP Address Type.')
agentLogHostTableIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableIpAddress.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableIpAddress.setDescription('Syslog Host table IP Address. Set operation of this object can be successful only when the valid IpAddressType (Ipv4, Ipv6 or DNS) is configured and the address specified is valid for that Address type.')
agentLogHostTablePort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTablePort.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTablePort.setDescription('Syslog Host table port number.')
agentLogHostTableSeverityFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 5), AgentLogSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableSeverityFilter.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableSeverityFilter.setDescription('Configures the minimum severity that will be stored in the In Memory log.')
agentLogHostTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 5, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableRowStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogHostTableRowStatus.setDescription('Syslog Host table row status')
agentLogSyslogSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 4, 6), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogSourceInterface.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogSourceInterface.setDescription('A source-interface selection on an Interface Index (like vlan based routing interface, port based routing interface, loopback interface, tunnel interface). A non-zero value indicates ifIndex for the corresponding interface entry in the ifTable is selected. A zero value indicates the source-interface un-selection.')
agentLogStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2))
agentLogMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessagesReceived.setStatus('current')
if mibBuilder.loadTexts: agentLogMessagesReceived.setDescription('The number of messages received by the log process. This includes messages that are dropped or ignored.')
agentLogMessagesDropped = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessagesDropped.setStatus('current')
if mibBuilder.loadTexts: agentLogMessagesDropped.setDescription('The number of messages that could not be processed due to error or lack of resources.')
agentLogSyslogMessagesRelayed = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessagesRelayed.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogMessagesRelayed.setDescription('The number of messages forwarded by the syslog function to a syslog host. Messages forwarded to multiple hosts are counted once for each host.')
agentLogSyslogMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessagesIgnored.setStatus('deprecated')
if mibBuilder.loadTexts: agentLogSyslogMessagesIgnored.setDescription('The number of messages that were not processed by the syslog process because the component name or the priority level did not match any specification.')
agentLogMessageReceivedTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessageReceivedTime.setStatus('current')
if mibBuilder.loadTexts: agentLogMessageReceivedTime.setDescription('The local time when a message was last received by the log subsystem specified as the number of non-leap seconds since 00:00:00 UTC on January 1 1970.')
agentLogSyslogMessageDeliveredTime = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessageDeliveredTime.setStatus('current')
if mibBuilder.loadTexts: agentLogSyslogMessageDeliveredTime.setDescription('The local time when a message was last delivered to a syslog host specified as the number of non-leap seconds since 00:00:00 UTC on January 1 1970.')
agentLogEmailAlertConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6))
agentLogEmailAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailAdminStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailAdminStatus.setDescription('For Enabling and Disabling email alerts to SMTP server. Setting this to disable stops emailing to SMTP servers.')
agentLogEmailfromAddr = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailfromAddr.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailfromAddr.setDescription('Email from Address')
agentLogEmaillogDuration = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmaillogDuration.setStatus('current')
if mibBuilder.loadTexts: agentLogEmaillogDuration.setDescription('This duration in minutes determines how frequently the non critical messages are sent to the SMTP server.')
agentLogEmailUrgentSeverity = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 4), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailUrgentSeverity.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailUrgentSeverity.setDescription('This is the severity level for the critical log messages')
agentLogEmailNonUrgentSeverity = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 5), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailNonUrgentSeverity.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailNonUrgentSeverity.setDescription('This is the severity level for the non critical log messages.')
agentLogEmailTrapsSeverity = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 6), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailTrapsSeverity.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailTrapsSeverity.setDescription('This is the severity level for Trap messages.')
agentLogEmailToAddrTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7), )
if mibBuilder.loadTexts: agentLogEmailToAddrTable.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddrTable.setDescription('The (conceptual) table listing the destination email address and the message type.')
agentLogEmailToAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7, 1), ).setIndexNames((0, "DNOS-LOGGING-MIB", "agentLogEmailToAddrMessageType"), (0, "DNOS-LOGGING-MIB", "agentLogEmailToAddr"))
if mibBuilder.loadTexts: agentLogEmailToAddrEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddrEntry.setDescription('An entry (conceptual row) in the agentLogEmailtoAddrTable. This entry shows what kind of messages go to the given destination email addresses.')
agentLogEmailToAddrMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("critical", 1), ("non-critical", 2))))
if mibBuilder.loadTexts: agentLogEmailToAddrMessageType.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddrMessageType.setDescription('Log message Type')
agentLogEmailToAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7, 1, 2), DisplayString())
if mibBuilder.loadTexts: agentLogEmailToAddr.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddr.setDescription('Email Sender Address')
agentLogEmailToAddrEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailToAddrEntryStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailToAddrEntryStatus.setDescription('This is to create or delete the entry')
agentLogEmailSubjectTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8), )
if mibBuilder.loadTexts: agentLogEmailSubjectTable.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubjectTable.setDescription('The (conceptual) table listing the subject of the email and the message type.')
agentLogEmailSubjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8, 1), ).setIndexNames((0, "DNOS-LOGGING-MIB", "agentLogEmailSubjectMessageType"))
if mibBuilder.loadTexts: agentLogEmailSubjectEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubjectEntry.setDescription('An entry (conceptual row) in the agentLogEmailtoAddrTable. This entry shows what kind of subject to be used for the given message type.')
agentLogEmailSubjectMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("critical", 1), ("non-critical", 2))))
if mibBuilder.loadTexts: agentLogEmailSubjectMessageType.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubjectMessageType.setDescription('Log message Type')
agentLogEmailSubject = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailSubject.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubject.setDescription('Email Subject. When this object is set to empty-string, it resets to factory default string.')
agentLogEmailSubjectEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailSubjectEntryStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSubjectEntryStatus.setDescription('This is to create or delete the entry')
agentLogEmailMailServerTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9), )
if mibBuilder.loadTexts: agentLogEmailMailServerTable.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailMailServerTable.setDescription('The (conceptual) table listing the mail servers')
agentLogEmailMailServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1), ).setIndexNames((0, "DNOS-LOGGING-MIB", "agentLogEmailSmtpAddrType"), (0, "DNOS-LOGGING-MIB", "agentLogEmailSmtpAddr"))
if mibBuilder.loadTexts: agentLogEmailMailServerEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailMailServerEntry.setDescription('An entry (conceptual row) in the agentLogEmailMailServerTable. This entry shows the conmfiguration for mail server.')
agentLogEmailSmtpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 1), InetAddressType())
if mibBuilder.loadTexts: agentLogEmailSmtpAddrType.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSmtpAddrType.setDescription('Email SMTP Address type')
agentLogEmailSmtpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 2), InetAddress())
if mibBuilder.loadTexts: agentLogEmailSmtpAddr.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSmtpAddr.setDescription('SMTP server Address')
agentLogEmailSmtpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 3), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailSmtpPort.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSmtpPort.setDescription('SMTP Port number. When this object is set to 0, it resets to factory default port number.')
agentLogEmailSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("tlsv1", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailSecurity.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSecurity.setDescription('This is the authentication mechanism that should be used.')
agentLogEmailloginID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailloginID.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailloginID.setDescription('This user id is used while the switch/router is being authenticated by the SMTP server.The user ID should be minimum of 1 charcter to maximum of 16 characters.')
agentLogEmailPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailPassword.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailPassword.setDescription('This password is used while the switch/router is being authenticated by the SMTP server.The password should be minimum of 1 character to maximum of 16 characters.')
agentLogEmailEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 1, 6, 9, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailEntryStatus.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailEntryStatus.setDescription('This is to create or delete the entry')
agentLogEmailAlertStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7))
agentLogEmailStatsemailsSentCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsemailsSentCount.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailStatsemailsSentCount.setDescription('This is the count to show the no of emails sent so far.')
agentLogEmailStatsemailsFailureCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsemailsFailureCount.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailStatsemailsFailureCount.setDescription('This is the count to show the no of emails failures happened so far...')
agentLogEmailStatsTimeSinceLastEmailSent = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsTimeSinceLastEmailSent.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailStatsTimeSinceLastEmailSent.setDescription('This is the number of seconds since the last email was sent.')
agentLogEmailStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 2, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailStatsClear.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailStatsClear.setDescription('This is to clear the email alert stats.')
agentLogInMemoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3))
agentLogInMemoryLogCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogInMemoryLogCount.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryLogCount.setDescription('The count of valid entries in the in-memory log.')
agentLogInMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2), )
if mibBuilder.loadTexts: agentLogInMemoryTable.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryTable.setDescription('The in-memory log table containing sequence of in-memory log entries.')
agentLogInMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1), ).setIndexNames((0, "DNOS-LOGGING-MIB", "agentLogInMemoryMsgIndex"))
if mibBuilder.loadTexts: agentLogInMemoryEntry.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryEntry.setDescription('An individual message entry in in-memory log table.')
agentLogInMemoryMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogInMemoryMsgIndex.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryMsgIndex.setDescription('The index to message entry in the in-memory log table.')
agentLogInMemoryMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogInMemoryMsgText.setStatus('current')
if mibBuilder.loadTexts: agentLogInMemoryMsgText.setDescription('Message text info for inmemory logged messages.')
agentLogTrapsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 5))
agentLogEmailAlertTrapsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 5, 1))
agentLogEmailSendFailed = NotificationType((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 14, 5, 1, 1)).setObjects(("DNOS-LOGGING-MIB", "agentLogEmailStatsemailsFailureCount"))
if mibBuilder.loadTexts: agentLogEmailSendFailed.setStatus('current')
if mibBuilder.loadTexts: agentLogEmailSendFailed.setDescription('When ever a mail sending to the SMTP server is failed, this trap is sent with a count of how many times the connection to the SMTP server is failed so far.')
mibBuilder.exportSymbols("DNOS-LOGGING-MIB", agentLogSyslogSourceInterface=agentLogSyslogSourceInterface, agentLogEmailToAddrEntryStatus=agentLogEmailToAddrEntryStatus, agentLogAuditAdminStatus=agentLogAuditAdminStatus, agentLogEmailStatsClear=agentLogEmailStatsClear, agentLogInMemoryTable=agentLogInMemoryTable, agentLogHostTableIndex=agentLogHostTableIndex, agentLogSyslogHostEntry=agentLogSyslogHostEntry, agentLogMessageReceivedTime=agentLogMessageReceivedTime, agentLogWebConfigGroup=agentLogWebConfigGroup, agentLogConfigGroup=agentLogConfigGroup, agentLogEmailSubjectEntryStatus=agentLogEmailSubjectEntryStatus, agentLogEmailUrgentSeverity=agentLogEmailUrgentSeverity, agentLogSyslogMessagesIgnored=agentLogSyslogMessagesIgnored, agentLogEmailSubjectEntry=agentLogEmailSubjectEntry, agentLogSyslogMessagesRelayed=agentLogSyslogMessagesRelayed, agentLogInMemoryLogCount=agentLogInMemoryLogCount, agentLogInMemoryMsgText=agentLogInMemoryMsgText, agentLogEmailStatsemailsFailureCount=agentLogEmailStatsemailsFailureCount, agentLogEmailTrapsSeverity=agentLogEmailTrapsSeverity, agentLogEmailToAddrTable=agentLogEmailToAddrTable, agentLogConsoleAdminStatus=agentLogConsoleAdminStatus, agentLogEmailSmtpAddr=agentLogEmailSmtpAddr, agentLogSyslogLocalPort=agentLogSyslogLocalPort, agentLogSnmpAdminStatus=agentLogSnmpAdminStatus, agentLogEmailAlertConfigGroup=agentLogEmailAlertConfigGroup, agentLogSyslogHostTable=agentLogSyslogHostTable, agentLogEmailMailServerEntry=agentLogEmailMailServerEntry, agentLogCliCommandsConfigGroup=agentLogCliCommandsConfigGroup, PYSNMP_MODULE_ID=fastPathLogging, agentLogInMemoryAdminStatus=agentLogInMemoryAdminStatus, agentLogEmailEntryStatus=agentLogEmailEntryStatus, agentLogEmailToAddrEntry=agentLogEmailToAddrEntry, agentLogEmailSendFailed=agentLogEmailSendFailed, AgentLogFacility=AgentLogFacility, agentLogEmailSubjectTable=agentLogEmailSubjectTable, agentLogEmailToAddr=agentLogEmailToAddr, agentLogEmailSubjectMessageType=agentLogEmailSubjectMessageType, agentLogSyslogMaxHosts=agentLogSyslogMaxHosts, agentLogSnmpConfigGroup=agentLogSnmpConfigGroup, agentLogSysLogConfigGroup=agentLogSysLogConfigGroup, agentLogSyslogMessageDeliveredTime=agentLogSyslogMessageDeliveredTime, agentLogInMemoryBehavior=agentLogInMemoryBehavior, agentLogEmailNonUrgentSeverity=agentLogEmailNonUrgentSeverity, agentLogInMemoryMsgIndex=agentLogInMemoryMsgIndex, agentLogMessagesReceived=agentLogMessagesReceived, agentLogEmaillogDuration=agentLogEmaillogDuration, agentLogStatisticsGroup=agentLogStatisticsGroup, agentLogConsoleConfigGroup=agentLogConsoleConfigGroup, agentLogCliCommandsAdminStatus=agentLogCliCommandsAdminStatus, agentLogMessagesDropped=agentLogMessagesDropped, agentLogEmailSecurity=agentLogEmailSecurity, agentLogWebAdminStatus=agentLogWebAdminStatus, agentLogEmailToAddrMessageType=agentLogEmailToAddrMessageType, agentLogHostTableSeverityFilter=agentLogHostTableSeverityFilter, agentLogConsoleSeverityFilter=agentLogConsoleSeverityFilter, agentLogHostTableIpAddressType=agentLogHostTableIpAddressType, agentLogSyslogAdminStatus=agentLogSyslogAdminStatus, agentLogEmailfromAddr=agentLogEmailfromAddr, agentLogEmailAlertTrapsGroup=agentLogEmailAlertTrapsGroup, agentLogEmailSmtpAddrType=agentLogEmailSmtpAddrType, agentLogInMemoryGroup=agentLogInMemoryGroup, agentLogHostTablePort=agentLogHostTablePort, agentLogEmailSubject=agentLogEmailSubject, agentLogEmailPassword=agentLogEmailPassword, agentLogHostTableRowStatus=agentLogHostTableRowStatus, agentLogEmailStatsemailsSentCount=agentLogEmailStatsemailsSentCount, agentLogEmailMailServerTable=agentLogEmailMailServerTable, fastPathLogging=fastPathLogging, agentLogEmailSmtpPort=agentLogEmailSmtpPort, agentLogEmailStatsTimeSinceLastEmailSent=agentLogEmailStatsTimeSinceLastEmailSent, AgentLogSeverity=AgentLogSeverity, agentLogTrapsGroup=agentLogTrapsGroup, agentLogInMemoryEntry=agentLogInMemoryEntry, agentLogEmailloginID=agentLogEmailloginID, agentLogInMemoryConfigGroup=agentLogInMemoryConfigGroup, agentLogEmailAlertStatsGroup=agentLogEmailAlertStatsGroup, agentLogAuditConfigGroup=agentLogAuditConfigGroup, agentLogHostTableIpAddress=agentLogHostTableIpAddress, agentLogEmailAdminStatus=agentLogEmailAdminStatus)
