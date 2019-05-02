#
# PySNMP MIB module CISCO-DEVICE-EXCEPTION-REPORTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DEVICE-EXCEPTION-REPORTING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, Integer32, Counter64, iso, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Unsigned32, Bits, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Integer32", "Counter64", "iso", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Unsigned32", "Bits", "ObjectIdentity", "TimeTicks")
TextualConvention, TruthValue, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "TimeStamp")
ciscoDevExcepReportMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 224))
if mibBuilder.loadTexts: ciscoDevExcepReportMIB.setLastUpdated('200108140000Z')
if mibBuilder.loadTexts: ciscoDevExcepReportMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDevExcepReportMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-crm@cisco.com')
if mibBuilder.loadTexts: ciscoDevExcepReportMIB.setDescription('This mib defines the SNMP objects to report exceptions to north-bound NMS. The devices implementing this MIB monitor the status of hardware and software services, and report any exceptions regarding these components. These hardware and software services could belong to the monitoring devices or other managed devices. An exception is something abnormal that the system administrators should pay attention to. The criteria for what is an exception could vary by system and should be defined by the system administrators. Certain NM devices or applications may have pre-defined exceptions. This MIB does not try to define exceptions. But rather it defines SNMP objects for devices to use SNMP notification as an exception reporting mechanism. Exceptions may be pre-defined or defined through other device management interface such as CLI, GUI, or HTTP.')
ciscoDevExcepReportMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 224, 1))
cderExceptionData = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1))
cderMaxExceptionRecords = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cderMaxExceptionRecords.setStatus('current')
if mibBuilder.loadTexts: cderMaxExceptionRecords.setDescription('The maximun number of records to keep in cderExceptionTable. New records will replace the old records on a first-in-first-out basis. A value of 0 indicates no history will be retained.')
cderNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cderNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: cderNotificationEnabled.setDescription('Enable or disable exception notification via SNMP.')
cderNotificationsSent = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderNotificationsSent.setStatus('current')
if mibBuilder.loadTexts: cderNotificationsSent.setDescription('The number of cderMonitoredExceptionEvent events. If a NMS is receiving notifications, it can periodically poll this object to find out if any notifications were missed. In that case it could poll cderExceptionTable to find out missing exceptions.')
cderNotificationsDropped = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderNotificationsDropped.setStatus('current')
if mibBuilder.loadTexts: cderNotificationsDropped.setDescription('The number of notifications dropped from the cderExceptionTable table. If the difference between two consecutive polls of this object is greater than cderMaxExceptionRecords, then it indicates the NMS will not be able to find missing exceptions. The solution is to either poll the cderExceptionTable more frequently or increase the size of the cderExceptionTable by setting cderMaxExceptionRecords.')
cderExceptionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5), )
if mibBuilder.loadTexts: cderExceptionTable.setStatus('current')
if mibBuilder.loadTexts: cderExceptionTable.setDescription('This table keeps an history of exceptions found.')
cderExceptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1), ).setIndexNames((0, "CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepTableIndex"))
if mibBuilder.loadTexts: cderExceptionEntry.setStatus('current')
if mibBuilder.loadTexts: cderExceptionEntry.setDescription('An entry containing information about an exception.')
cderExcepTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cderExcepTableIndex.setStatus('current')
if mibBuilder.loadTexts: cderExcepTableIndex.setDescription('An monotonically increasing number for the sole purpose of indexing entries. When it reaches maximum value, the agent sets it back to 1.')
cderExcepId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderExcepId.setStatus('current')
if mibBuilder.loadTexts: cderExcepId.setDescription('Identification for this exception. This object should uniquely identify the exception.')
cderExcepHostAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 3), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderExcepHostAddressType.setStatus('current')
if mibBuilder.loadTexts: cderExcepHostAddressType.setDescription('Represents the type of address stored in cderExcepHostAddress.')
cderExcepHostAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderExcepHostAddress.setStatus('current')
if mibBuilder.loadTexts: cderExcepHostAddress.setDescription('Host device address where the exception happened.')
cderExcepPriorityDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderExcepPriorityDescription.setStatus('current')
if mibBuilder.loadTexts: cderExcepPriorityDescription.setDescription('A string that tells the system administrator about the priority of this exception. This string is provided to the snmp agent by the reporting service(s) which could be any services or applications on the device. The receiving NMS of this object should understand the string in order to utilize this object.')
cderExcepTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderExcepTime.setStatus('current')
if mibBuilder.loadTexts: cderExcepTime.setDescription('Timestamp when the exception happened.')
cderExcepData = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderExcepData.setStatus('current')
if mibBuilder.loadTexts: cderExcepData.setDescription('More information about the exception that the reporting service(s) want to convey to the NMS. The receiving NMS should understand the meaning of this object value in order to use it.')
cderExcepReportedBy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cderExcepReportedBy.setStatus('current')
if mibBuilder.loadTexts: cderExcepReportedBy.setDescription('Name of the reporting service, or process, or other component of the device that reports this exception.')
cderMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 224, 2))
cderMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 224, 2, 0))
cderMonitoredExceptionEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 224, 2, 0, 1)).setObjects(("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepId"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepHostAddressType"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepHostAddress"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepPriorityDescription"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepTime"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepData"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepReportedBy"))
if mibBuilder.loadTexts: cderMonitoredExceptionEvent.setStatus('current')
if mibBuilder.loadTexts: cderMonitoredExceptionEvent.setDescription('This notification is sent when an exception is detected on the managed device. This notification can be enabled or disabled via cderNotificationEnable.')
ciscoDEReportMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 224, 3))
ciscoDEReportMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 1))
ciscoDEReportMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 2))
ciscoDEReportMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 1, 1)).setObjects(("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "ciscoDERExceptionDataGroup"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "ciscoDERExceptionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDEReportMIBCompliance = ciscoDEReportMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDEReportMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO-DEVICE-EXCEPTION-REPORTING-MIB.')
ciscoDERExceptionDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 2, 1)).setObjects(("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderMaxExceptionRecords"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderNotificationEnabled"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderNotificationsSent"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderNotificationsDropped"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepId"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepHostAddressType"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepHostAddress"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepPriorityDescription"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepTime"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepData"), ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepReportedBy"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDERExceptionDataGroup = ciscoDERExceptionDataGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDERExceptionDataGroup.setDescription('A collection of objects that enable the exception notification for monitored exceptions of network elements.')
ciscoDERExceptionGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 2, 2)).setObjects(("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderMonitoredExceptionEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDERExceptionGroup = ciscoDERExceptionGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDERExceptionGroup.setDescription('A collection of the monitored exception events.')
mibBuilder.exportSymbols("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", cderNotificationsSent=cderNotificationsSent, ciscoDERExceptionGroup=ciscoDERExceptionGroup, cderExceptionData=cderExceptionData, ciscoDevExcepReportMIB=ciscoDevExcepReportMIB, ciscoDevExcepReportMIBObjects=ciscoDevExcepReportMIBObjects, ciscoDERExceptionDataGroup=ciscoDERExceptionDataGroup, cderExcepTime=cderExcepTime, cderNotificationEnabled=cderNotificationEnabled, ciscoDEReportMIBCompliances=ciscoDEReportMIBCompliances, cderExcepHostAddress=cderExcepHostAddress, PYSNMP_MODULE_ID=ciscoDevExcepReportMIB, ciscoDEReportMIBConformance=ciscoDEReportMIBConformance, ciscoDEReportMIBCompliance=ciscoDEReportMIBCompliance, cderExceptionTable=cderExceptionTable, cderMaxExceptionRecords=cderMaxExceptionRecords, cderExcepReportedBy=cderExcepReportedBy, cderExceptionEntry=cderExceptionEntry, cderMIBNotifPrefix=cderMIBNotifPrefix, ciscoDEReportMIBGroups=ciscoDEReportMIBGroups, cderExcepHostAddressType=cderExcepHostAddressType, cderExcepId=cderExcepId, cderExcepPriorityDescription=cderExcepPriorityDescription, cderExcepData=cderExcepData, cderMIBNotifications=cderMIBNotifications, cderExcepTableIndex=cderExcepTableIndex, cderNotificationsDropped=cderNotificationsDropped, cderMonitoredExceptionEvent=cderMonitoredExceptionEvent)
