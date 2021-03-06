#
# PySNMP MIB module ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:19:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1PortMirroringMonitoring, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1PortMirroringMonitoring")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
sFlowFsEntry, sFlowCpEntry = mibBuilder.importSymbols("SFLOW-MIB", "sFlowFsEntry", "sFlowCpEntry")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ObjectIdentity, Counter64, NotificationType, Counter32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, iso, Unsigned32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter64", "NotificationType", "Counter32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "iso", "Unsigned32", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
alcatelIND1PortMirrorMonitoringMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1))
alcatelIND1PortMirrorMonitoringMIB.setRevisions(('2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1PortMirrorMonitoringMIB.setRevisionsDescriptions(('Addressing discrepancies with Alcatel Standard.',))
if mibBuilder.loadTexts: alcatelIND1PortMirrorMonitoringMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1PortMirrorMonitoringMIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1PortMirrorMonitoringMIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate version of this document is used with the products in question: Alcatel-Lucent, Enterprise Solutions Division (Formerly Alcatel Internetworking, Incorporated) 26801 West Agoura Road Agoura Hills, CA 91301-5122 United States Of America Telephone: North America +1 800 995 2696 Latin America +1 877 919 9526 Europe +31 23 556 0100 Asia +65 394 7933 All Other +1 818 878 4507 Electronic Mail: support@ind.alcatel.com World Wide Web: http://alcatel-lucent.com/wps/portal/enterprise File Transfer Protocol: ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1PortMirrorMonitoringMIB.setDescription('This module describes an authoritative enterprise-specific Simple Network Management Protocol (SNMP) Management Information Base (MIB): For the Birds Of Prey Product Line Port Mirroring and Monitoring for mirroring/monitoring session control The right to make changes in specification and other information contained in this document without prior notice is reserved. No liability shall be assumed for any incidental, indirect, special, or consequential damages whatsoever arising from or related to this document or the information contained herein. Vendors, end-users, and other interested parties are granted non-exclusive license to use this specification in connection with management of the products for which it is intended to be used. Copyright (C) 1995-2007 Alcatel-Lucent ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1PortMirMonMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 0))
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBNotifications.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBNotifications.setDescription('Root For Port Mirroring and Monitoring Subsystem Managed Notifications.')
alcatelIND1PortMirMonMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1))
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBObjects.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBObjects.setDescription('Branch For Port Mirroring and Monitoring Subsystem Managed Objects.')
alcatelIND1PortMirMonMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2))
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBConformance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBConformance.setDescription('Branch For Port Mirroring and Monitoring Subsystem Conformance Information.')
alcatelIND1PortMirMonMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBGroups.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBGroups.setDescription('Branch For Port Mirroring and Monitoring Subsystem Units Of Conformance.')
alcatelIND1PortMirMonMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBCompliances.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBCompliances.setDescription('Branch For Port Mirroring and Monitoring Subsystem Compliance Statements.')
mirmonMirroring = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1))
mirrorTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1), )
if mibBuilder.loadTexts: mirrorTable.setStatus('current')
if mibBuilder.loadTexts: mirrorTable.setDescription('A list of port mirroring instances.')
mirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessionNumber"))
if mibBuilder.loadTexts: mirrorEntry.setStatus('current')
if mibBuilder.loadTexts: mirrorEntry.setDescription('A port mirroring entry.')
mirrorSessionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorSessionNumber.setStatus('current')
if mibBuilder.loadTexts: mirrorSessionNumber.setDescription('Identifies a specific port mirroring instance.')
mirrorMirroredIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorMirroredIfindex.setStatus('deprecated')
if mibBuilder.loadTexts: mirrorMirroredIfindex.setDescription(' This variable is deprecated and value will be ignored. Please use mirrorSrcTable to configure mirrored ports. The physical identification number for this mirroring port instance (mirrorred port).')
mirrorMirroringIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 3), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorMirroringIfindex.setStatus('current')
if mibBuilder.loadTexts: mirrorMirroringIfindex.setDescription(' The physical identification number for this mirroring port instance (mirroring port).')
mirrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('on')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorStatus.setStatus('current')
if mibBuilder.loadTexts: mirrorStatus.setDescription('Whether mirroring is enabled or disabled for this port. Prior to enabling mirroring, or at the same time all other read write values in this table for the same row must be set to appropriate values, or defaults will be assumed.')
mirrorUnblockedVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorUnblockedVLAN.setStatus('current')
if mibBuilder.loadTexts: mirrorUnblockedVLAN.setDescription('A VLAN identifier which specifies the VLAN identifier that must remain unblocked no matter what is the output of the spanning tree algorithm.Value 0 indicates this parameter is not set')
mirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: mirrorRowStatus.setDescription('The status of this table entry. ')
mirrorDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inport", 1), ("outport", 2), ("bidirectional", 3))).clone('bidirectional')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorDirection.setStatus('deprecated')
if mibBuilder.loadTexts: mirrorDirection.setDescription(' This variable is deprecated and the value will be ignored. Please use mirrorSrcTable to set the direction of mirroring. Direction of mirroring.')
mirrorSessOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('on')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorSessOperStatus.setStatus('current')
if mibBuilder.loadTexts: mirrorSessOperStatus.setDescription('Whether mirroring session is active. ')
mirrorTaggedVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorTaggedVLAN.setStatus('current')
if mibBuilder.loadTexts: mirrorTaggedVLAN.setDescription('A VLAN identifier which specifies the VLAN identifier that must used to tag the mirrored packets going out of the MTP for remote port mirroring .Value 0 indicates this parameter is not set')
mirrorSrcTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2), )
if mibBuilder.loadTexts: mirrorSrcTable.setStatus('current')
if mibBuilder.loadTexts: mirrorSrcTable.setDescription('A list of port mirroring instances.')
mirrorSrcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessionNumber"), (0, "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcMirroredIf"))
if mibBuilder.loadTexts: mirrorSrcEntry.setStatus('current')
if mibBuilder.loadTexts: mirrorSrcEntry.setDescription('A port mirroring entry.')
mirrorSrcMirroredIf = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorSrcMirroredIf.setStatus('current')
if mibBuilder.loadTexts: mirrorSrcMirroredIf.setDescription('The physical identification number for this mirroring port instance (mirrorred port).')
mirrorSrcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('enable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorSrcStatus.setStatus('current')
if mibBuilder.loadTexts: mirrorSrcStatus.setDescription('Whether mirroring is enabled or disabled for this port. Prior to enabling mirroring, or at the same time all other read write values in this table for the same row must be set to appropriate values, or defaults will be assumed.')
mirrorSrcDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inport", 1), ("outport", 2), ("bidirectional", 3))).clone('bidirectional')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorSrcDirection.setStatus('current')
if mibBuilder.loadTexts: mirrorSrcDirection.setDescription('Direction of mirroring on the source port of this entry.')
mirrorSrcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mirrorSrcRowStatus.setStatus('current')
if mibBuilder.loadTexts: mirrorSrcRowStatus.setDescription('The status of this table entry.Row Status to control creation, modification and deletion of this entry. ')
mirrorSrcOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('on')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirrorSrcOperStatus.setStatus('current')
if mibBuilder.loadTexts: mirrorSrcOperStatus.setDescription('The mirroring operational status of this mirrored source. ')
mirmonMonitoring = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2))
monitorTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1), )
if mibBuilder.loadTexts: monitorTable.setStatus('current')
if mibBuilder.loadTexts: monitorTable.setDescription('A list of port monitoring instances.')
monitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorSessionNumber"))
if mibBuilder.loadTexts: monitorEntry.setStatus('current')
if mibBuilder.loadTexts: monitorEntry.setDescription('A port monitoring entry.')
monitorSessionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: monitorSessionNumber.setStatus('current')
if mibBuilder.loadTexts: monitorSessionNumber.setDescription('Identifies a specific port monitoring instance.')
monitorIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 2), InterfaceIndex().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorIfindex.setStatus('current')
if mibBuilder.loadTexts: monitorIfindex.setDescription('The physical identification number for this monitoring port instance.')
monitorFileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorFileStatus.setStatus('current')
if mibBuilder.loadTexts: monitorFileStatus.setDescription('The status of the file option of a monitoring port instance (default off)')
monitorFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorFileName.setStatus('current')
if mibBuilder.loadTexts: monitorFileName.setDescription('The name of the file in which the traffic will be stored (default PMONITOR.ENC).')
monitorFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorFileSize.setStatus('current')
if mibBuilder.loadTexts: monitorFileSize.setDescription('The number of 65536 ( 64K ) bytes allowed for the file. The file contains only the last monitorFileSize bytes of the current port monitoring instance (default 65536 bytes).')
monitorScreenStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorScreenStatus.setStatus('current')
if mibBuilder.loadTexts: monitorScreenStatus.setDescription('The status of the screen option of a monitoring port instance (default off)')
monitorScreenLine = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(24)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorScreenLine.setStatus('current')
if mibBuilder.loadTexts: monitorScreenLine.setDescription('The number of lines used when the screen option is activated (default 24)')
monitorTrafficType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("all", 1), ("unicast", 2), ("multicast", 3), ("broadcast", 4), ("unimulti", 5), ("unibroad", 6), ("multibroad", 7))).clone('all')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorTrafficType.setStatus('current')
if mibBuilder.loadTexts: monitorTrafficType.setDescription('The type of traffic being monitored (default all)')
monitorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("suspended", 3))).clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorStatus.setStatus('current')
if mibBuilder.loadTexts: monitorStatus.setDescription('The status of the port monitoring instance')
monitorFileOverWrite = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('on')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorFileOverWrite.setStatus('current')
if mibBuilder.loadTexts: monitorFileOverWrite.setDescription('The status of the File Over Write option of a monitoring port instance (default on)')
monitorDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inport", 1), ("outport", 2), ("bidirectional", 3))).clone('bidirectional')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorDirection.setStatus('current')
if mibBuilder.loadTexts: monitorDirection.setDescription('Direction of monitoring.')
monitorTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorTimeout.setStatus('current')
if mibBuilder.loadTexts: monitorTimeout.setDescription('The number of seconds allowed for this session before the session gets deleted. (default:forever 0 second).')
monitorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorRowStatus.setStatus('current')
if mibBuilder.loadTexts: monitorRowStatus.setDescription('The status of this table entry. Create,Delete and Modify.')
monitorCaptureType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("brief", 1), ("full", 2))).clone('brief')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: monitorCaptureType.setStatus('current')
if mibBuilder.loadTexts: monitorCaptureType.setDescription('The number of bytes per packet allowed to capture .(brief: 64 bytes, full: Entire packet).')
mirmonNotificationVars = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3))
class MirMonErrorIds(TextualConvention, Integer32):
    description = 'This data type is used to define the different type of error occured while configuring Mirroring/Monitoring.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("wrongSession", 2), ("hwQError", 3), ("swQError", 4))

mirmonPrimarySlot = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirmonPrimarySlot.setStatus('current')
if mibBuilder.loadTexts: mirmonPrimarySlot.setDescription('Slot of mirrored or monitored interface.')
mirmonPrimaryPort = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirmonPrimaryPort.setStatus('current')
if mibBuilder.loadTexts: mirmonPrimaryPort.setDescription('Port of mirrored or monitored interface.')
mirroringSlot = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirroringSlot.setStatus('current')
if mibBuilder.loadTexts: mirroringSlot.setDescription('Slot of mirroring interface.')
mirroringPort = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirroringPort.setStatus('current')
if mibBuilder.loadTexts: mirroringPort.setDescription('Port of mirroring interface.')
mirMonSession = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirMonSession.setStatus('current')
if mibBuilder.loadTexts: mirMonSession.setDescription('The Mirroring session number.')
mirMonError = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 6), MirMonErrorIds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirMonError.setStatus('current')
if mibBuilder.loadTexts: mirMonError.setDescription('The Error returned by the NI which failed to configure Mirroring/Monitoring')
mirMonErrorNi = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mirMonErrorNi.setStatus('current')
if mibBuilder.loadTexts: mirMonErrorNi.setDescription('The NI slot number. ')
mirrorConfigError = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 0, 1)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimarySlot"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimaryPort"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringSlot"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringPort"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonErrorNi"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonError"))
if mibBuilder.loadTexts: mirrorConfigError.setStatus('current')
if mibBuilder.loadTexts: mirrorConfigError.setDescription('The Mirroring Configuration failed on NI. This trap is sent when any NI fails to configure mirroring. Due to this error, port mirroring session will be terminated.')
monitorFileWritten = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 0, 2)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimarySlot"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimaryPort"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileName"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileSize"))
if mibBuilder.loadTexts: monitorFileWritten.setStatus('current')
if mibBuilder.loadTexts: monitorFileWritten.setDescription('A File Written Trap is sent when the amount of data requested by the user has been written by the port monitoring instance.')
mirrorUnlikeNi = NotificationType((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 0, 3)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimarySlot"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimaryPort"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringSlot"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringPort"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonErrorNi"))
if mibBuilder.loadTexts: mirrorUnlikeNi.setStatus('current')
if mibBuilder.loadTexts: mirrorUnlikeNi.setDescription(' The Mirroring Configuration is deleted due to the swapping of different NI board type. Port Mirroring session which was active on a slot,cannot continue with the insertion of different NI type in the same slot. ')
mirmonSFlowObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4))
alasFlowFsTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 1), )
if mibBuilder.loadTexts: alasFlowFsTable.setStatus('current')
if mibBuilder.loadTexts: alasFlowFsTable.setDescription('A table of the flow samplers within a device.')
alasFlowFsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 1, 1), )
sFlowFsEntry.registerAugmentions(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowFsEntry"))
alasFlowFsEntry.setIndexNames(*sFlowFsEntry.getIndexNames())
if mibBuilder.loadTexts: alasFlowFsEntry.setStatus('current')
if mibBuilder.loadTexts: alasFlowFsEntry.setDescription('Attributes of a flow sampler.')
alasFlowFsDeleteEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("delete", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alasFlowFsDeleteEntry.setStatus('current')
if mibBuilder.loadTexts: alasFlowFsDeleteEntry.setDescription('The object is used to delete entries in the sFlowFsTable. Only value 6 is supported.')
alasFlowCpTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 2), )
if mibBuilder.loadTexts: alasFlowCpTable.setStatus('current')
if mibBuilder.loadTexts: alasFlowCpTable.setDescription('A table of the flow samplers within a device.')
alasFlowCpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 2, 1), )
sFlowCpEntry.registerAugmentions(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowCpEntry"))
alasFlowCpEntry.setIndexNames(*sFlowCpEntry.getIndexNames())
if mibBuilder.loadTexts: alasFlowCpEntry.setStatus('current')
if mibBuilder.loadTexts: alasFlowCpEntry.setDescription('Attributes of a flow sampler.')
alasFlowCpDeleteEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("delete", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alasFlowCpDeleteEntry.setStatus('current')
if mibBuilder.loadTexts: alasFlowCpDeleteEntry.setDescription('The object is used to delete entries in the sFlowCpTable. Only value 6 is supported.')
alasFlowAgentConfigType = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("default", 1), ("user", 2))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alasFlowAgentConfigType.setStatus('current')
if mibBuilder.loadTexts: alasFlowAgentConfigType.setDescription('The Agent Config Information 1 -- Default 2 -- sFlow Interface IP Specified by User')
alasFlowAgentAddressType = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 4), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alasFlowAgentAddressType.setStatus('current')
if mibBuilder.loadTexts: alasFlowAgentAddressType.setDescription('The address type of the address associated with this agent. Only ipv4 and ipv6 types are supported.')
alasFlowAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 1, 4, 5), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alasFlowAgentAddress.setStatus('current')
if mibBuilder.loadTexts: alasFlowAgentAddress.setDescription('The IP address associated with this agent. In the case of a multi-homed agent, this should be the loopback address of the agent. The sFlowAgent address must provide SNMP connectivity to the agent. The address should be an invariant that does not change as interfaces are reconfigured, enabled, disabled, added or removed. A manager should be able to use the sFlowAgentAddress as a unique key that will identify this agent over extended periods of time so that a history can be maintained.')
alcatelIND1PortMirMonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "portMirroringGroup"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "portMonitoringGroup"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "portNotificationVarsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1PortMirMonMIBCompliance = alcatelIND1PortMirMonMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1PortMirMonMIBCompliance.setDescription('Compliance statement for Port Mirroring and Monitoring.')
portMirroringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessionNumber"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorMirroredIfindex"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorMirroringIfindex"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorUnblockedVLAN"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorRowStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorDirection"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessOperStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcMirroredIf"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcDirection"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcRowStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSrcOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portMirroringGroup = portMirroringGroup.setStatus('current')
if mibBuilder.loadTexts: portMirroringGroup.setDescription('Collection of objects for management of Port Mirroring.')
portMonitoringGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorSessionNumber"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorIfindex"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileName"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileSize"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorScreenStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorScreenLine"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorTrafficType"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileOverWrite"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorDirection"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorTimeout"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorRowStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorCaptureType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portMonitoringGroup = portMonitoringGroup.setStatus('current')
if mibBuilder.loadTexts: portMonitoringGroup.setDescription('Collection of objects for management of Port Monitoring.')
portNotificationVarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimarySlot"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirmonPrimaryPort"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringSlot"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirroringPort"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonSession"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonError"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirMonErrorNi"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portNotificationVarsGroup = portNotificationVarsGroup.setStatus('current')
if mibBuilder.loadTexts: portNotificationVarsGroup.setDescription('Collection of objects which appear only in notifications.')
mirmonTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorConfigError"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorUnlikeNi"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "monitorFileWritten"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mirmonTrapsGroup = mirmonTrapsGroup.setStatus('current')
if mibBuilder.loadTexts: mirmonTrapsGroup.setDescription('Collection of Traps for port mirroring and monitoring.')
sFlowAgentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 5)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowAgentAddress"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowAgentAddressType"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowAgentConfigType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sFlowAgentGroup = sFlowAgentGroup.setStatus('current')
if mibBuilder.loadTexts: sFlowAgentGroup.setDescription('Collection of objects for sFlow agent configuration.')
portMirrorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 6)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessionNumber"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorMirroredIfindex"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorMirroringIfindex"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorUnblockedVLAN"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorRowStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorDirection"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorSessOperStatus"), ("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "mirrorTaggedVLAN"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portMirrorGroup = portMirrorGroup.setStatus('current')
if mibBuilder.loadTexts: portMirrorGroup.setDescription('Collection of objects for Mirror configuration.')
portSFlowCpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 7)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowCpDeleteEntry"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portSFlowCpGroup = portSFlowCpGroup.setStatus('current')
if mibBuilder.loadTexts: portSFlowCpGroup.setDescription('Collection of objects for sFlow Cp configuration.')
portSFlowFsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 19, 1, 2, 1, 8)).setObjects(("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", "alasFlowFsDeleteEntry"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    portSFlowFsGroup = portSFlowFsGroup.setStatus('current')
if mibBuilder.loadTexts: portSFlowFsGroup.setDescription('Collection of objects for sFlow Fs configuration.')
mibBuilder.exportSymbols("ALCATEL-IND1-PORT-MIRRORING-MONITORING-MIB", portNotificationVarsGroup=portNotificationVarsGroup, mirrorUnblockedVLAN=mirrorUnblockedVLAN, monitorSessionNumber=monitorSessionNumber, monitorFileSize=monitorFileSize, MirMonErrorIds=MirMonErrorIds, mirrorSessionNumber=mirrorSessionNumber, portMonitoringGroup=portMonitoringGroup, mirmonPrimaryPort=mirmonPrimaryPort, mirrorSrcMirroredIf=mirrorSrcMirroredIf, mirrorTaggedVLAN=mirrorTaggedVLAN, monitorIfindex=monitorIfindex, mirrorSrcRowStatus=mirrorSrcRowStatus, mirrorConfigError=mirrorConfigError, alasFlowAgentAddress=alasFlowAgentAddress, alasFlowAgentAddressType=alasFlowAgentAddressType, mirmonNotificationVars=mirmonNotificationVars, monitorFileStatus=monitorFileStatus, alasFlowAgentConfigType=alasFlowAgentConfigType, mirrorMirroredIfindex=mirrorMirroredIfindex, portMirrorGroup=portMirrorGroup, mirrorSrcTable=mirrorSrcTable, monitorRowStatus=monitorRowStatus, mirrorEntry=mirrorEntry, mirrorUnlikeNi=mirrorUnlikeNi, mirrorRowStatus=mirrorRowStatus, mirrorSrcOperStatus=mirrorSrcOperStatus, alasFlowCpTable=alasFlowCpTable, mirrorSrcDirection=mirrorSrcDirection, alcatelIND1PortMirMonMIBCompliances=alcatelIND1PortMirMonMIBCompliances, monitorDirection=monitorDirection, mirrorSrcStatus=mirrorSrcStatus, monitorTable=monitorTable, PYSNMP_MODULE_ID=alcatelIND1PortMirrorMonitoringMIB, monitorCaptureType=monitorCaptureType, monitorTrafficType=monitorTrafficType, monitorFileWritten=monitorFileWritten, monitorFileName=monitorFileName, mirroringSlot=mirroringSlot, mirmonSFlowObjects=mirmonSFlowObjects, mirrorTable=mirrorTable, mirmonPrimarySlot=mirmonPrimarySlot, mirMonErrorNi=mirMonErrorNi, alasFlowFsDeleteEntry=alasFlowFsDeleteEntry, alcatelIND1PortMirMonMIBCompliance=alcatelIND1PortMirMonMIBCompliance, mirroringPort=mirroringPort, alasFlowCpEntry=alasFlowCpEntry, sFlowAgentGroup=sFlowAgentGroup, alcatelIND1PortMirMonMIBObjects=alcatelIND1PortMirMonMIBObjects, monitorStatus=monitorStatus, mirmonTrapsGroup=mirmonTrapsGroup, portSFlowFsGroup=portSFlowFsGroup, alcatelIND1PortMirMonMIBNotifications=alcatelIND1PortMirMonMIBNotifications, mirrorSrcEntry=mirrorSrcEntry, alcatelIND1PortMirMonMIBGroups=alcatelIND1PortMirMonMIBGroups, mirMonError=mirMonError, alasFlowFsTable=alasFlowFsTable, mirmonMirroring=mirmonMirroring, mirMonSession=mirMonSession, alasFlowFsEntry=alasFlowFsEntry, portMirroringGroup=portMirroringGroup, mirmonMonitoring=mirmonMonitoring, monitorFileOverWrite=monitorFileOverWrite, alcatelIND1PortMirrorMonitoringMIB=alcatelIND1PortMirrorMonitoringMIB, monitorScreenStatus=monitorScreenStatus, alasFlowCpDeleteEntry=alasFlowCpDeleteEntry, portSFlowCpGroup=portSFlowCpGroup, mirrorSessOperStatus=mirrorSessOperStatus, mirrorMirroringIfindex=mirrorMirroringIfindex, mirrorStatus=mirrorStatus, monitorTimeout=monitorTimeout, monitorScreenLine=monitorScreenLine, alcatelIND1PortMirMonMIBConformance=alcatelIND1PortMirMonMIBConformance, monitorEntry=monitorEntry, mirrorDirection=mirrorDirection)
