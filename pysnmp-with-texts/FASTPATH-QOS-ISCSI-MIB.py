#
# PySNMP MIB module FASTPATH-QOS-ISCSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FASTPATH-QOS-ISCSI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:12:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
fastPathQOS, = mibBuilder.importSymbols("FASTPATH-QOS-MIB", "fastPathQOS")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, ObjectIdentity, Counter32, TimeTicks, IpAddress, Counter64, MibIdentifier, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "ObjectIdentity", "Counter32", "TimeTicks", "IpAddress", "Counter64", "MibIdentifier", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Integer32")
RowStatus, DisplayString, TruthValue, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention", "DateAndTime")
fastPathIscsiFlowAcceleration = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5))
fastPathIscsiFlowAcceleration.setRevisions(('2009-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fastPathIscsiFlowAcceleration.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: fastPathIscsiFlowAcceleration.setLastUpdated('200904300000Z')
if mibBuilder.loadTexts: fastPathIscsiFlowAcceleration.setOrganization('Broadcom Corporation')
if mibBuilder.loadTexts: fastPathIscsiFlowAcceleration.setContactInfo(' Customer Support Postal: Broadcom Corporation 100 Perimeter Park Drive Suite H Morrisville, NC 27560 Tel: +1 919 865 2700')
if mibBuilder.loadTexts: fastPathIscsiFlowAcceleration.setDescription('The MIB definitions for Quality of Service - iSCSI Flow Acceleration Flex package.')
agentIscsiFlowAccelerationGlobalConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1))
agentIscsiFlowAccelerationEnable = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationEnable.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationEnable.setDescription('Enable/Disable iSCSI Flow Acceleration globally on the system.')
agentIscsiFlowAccelerationAgingTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 2592000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationAgingTimeOut.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationAgingTimeOut.setDescription('The time in seconds that should pass before session is aged out after the last frame detected for the session.')
class QosType(TextualConvention, Integer32):
    description = 'Type of QoS: VPT or DSCP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("vpt", 0), ("dscp", 1))

agentIscsiFlowAccelerationQosType = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 3), QosType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationQosType.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationQosType.setDescription('Current type of QoS for iSCSI packets')
agentIscsiFlowAccelerationQosVptValue = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationQosVptValue.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationQosVptValue.setDescription('The value of VPT or DSCP, depends on agentIscsiFlowAccelerationQosType, that will be assigned to each iSCSI packet. The range of VPT value is 0..7')
agentIscsiFlowAccelerationQosDscpValue = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationQosDscpValue.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationQosDscpValue.setDescription('The value of VPT or DSCP, depends on agentIscsiFlowAccelerationQosType, that will be assigned to each iSCSI packet. The range of DSCP value is 0..63')
agentIscsiFlowAccelerationQosRemark = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationQosRemark.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationQosRemark.setDescription('Whether iSCSI frames with the configured VPT or DSCP when egressing the switch.')
agentIscsiFlowAccelerationTargetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2), )
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigTable.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigTable.setDescription('The table for configuration of iSCSI target TCP port number, IP address, and name. It is indexed by agentIscsiFlowAccelerationTargetConfigTcpPort and agentIscsiFlowAccelerationTargetConfigAddr.')
agentIscsiFlowAccelerationTargetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1), ).setIndexNames((0, "FASTPATH-QOS-ISCSI-MIB", "agentIscsiFlowAccelerationTargetConfigTcpPort"), (0, "FASTPATH-QOS-ISCSI-MIB", "agentIscsiFlowAccelerationTargetConfigAddr"))
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigEntry.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigEntry.setDescription('Row in the iSCSI Target configuration table.')
agentIscsiFlowAccelerationTargetConfigTcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigTcpPort.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigTcpPort.setDescription('The TCP port of configured target.')
agentIscsiFlowAccelerationTargetConfigAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigAddr.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigAddr.setDescription('Specifies the target address. If the target address is to be ignored the address should be 0.0.0.0.')
agentIscsiFlowAccelerationTargetConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 223))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigName.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigName.setDescription('The target IQN name. This text is not used to match on network traffic. It serves as an identifying comment for administrative convenience.')
agentIscsiFlowAccelerationTargetConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigStatus.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetConfigStatus.setDescription("The status of the target. It's used to add/delete a target. active(1) - this ACL instance is active createAndGo(4) - set to this value to create an instance destroy(6) - set to this value to delete an instance")
agentIscsiFlowAccelerationSessionTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3), )
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionTable.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionTable.setDescription('A table that contains iSCSI sessions. It is indexed as assigned by system.')
agentIscsiFlowAccelerationSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1), ).setIndexNames((0, "FASTPATH-QOS-ISCSI-MIB", "agentIscsiFlowAccelerationSessionIndex"))
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionEntry.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionEntry.setDescription('An entry in the agentIscsiFlowAccelerationSessionTable.')
agentIscsiFlowAccelerationSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionIndex.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionIndex.setDescription('Numerical index of session table entry assigned by system. ')
agentIscsiFlowAccelerationTargetName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 223))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetName.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationTargetName.setDescription('The target name')
agentIscsiFlowAccelerationInitiatorName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 223))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationInitiatorName.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationInitiatorName.setDescription('The initiator name')
agentIscsiFlowAccelerationSessionISID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionISID.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionISID.setDescription('The ISID of current session.')
agentIscsiFlowAccelerationSessAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessAgingTime.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessAgingTime.setDescription('The elapsed time in seconds since the traffic was detected on any connections associated with this session.')
agentIscsiFlowAccelerationSessionUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionUpTime.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationSessionUpTime.setDescription('Time elapsed since the session was detected, in seconds.')
agentIscsiFlowAccelerationConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4), )
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionTable.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionTable.setDescription('A table that contains iSCSI connections. It is indexed as assigned by system.')
agentIscsiFlowAccelerationConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1), ).setIndexNames((0, "FASTPATH-QOS-ISCSI-MIB", "agentIscsiFlowAccelerationConnectionIndex"))
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionEntry.setDescription('An entry in the agentIscsiFlowAccelerationConnectionTable.')
agentIscsiFlowAccelerationConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionIndex.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionIndex.setDescription('Numerical index of connection table entry assigned by system. ')
agentIscsiFlowAccelerationConnectionTargetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionTargetAddr.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionTargetAddr.setDescription('The connection target address.')
agentIscsiFlowAccelerationConnectionTargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionTargetPort.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionTargetPort.setDescription('The TCP port of connection target.')
agentIscsiFlowAccelerationConnectionInitiatorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionInitiatorAddr.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionInitiatorAddr.setDescription('The connection initiator address.')
agentIscsiFlowAccelerationConnectionInitiatorPort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionInitiatorPort.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionInitiatorPort.setDescription('The TCP port of connection initiator.')
agentIscsiFlowAccelerationConnectionCID = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionCID.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionCID.setDescription('The iSCSI CID for this connection.')
agentIscsiFlowAccelerationConnectionSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 5, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionSessionIndex.setStatus('current')
if mibBuilder.loadTexts: agentIscsiFlowAccelerationConnectionSessionIndex.setDescription('The index of the session associated with this connection. Refers to the index of agentIscsiFlowAccelerationSessionIndex in agentIscsiFlowAccelerationSessionTable.')
mibBuilder.exportSymbols("FASTPATH-QOS-ISCSI-MIB", QosType=QosType, agentIscsiFlowAccelerationQosRemark=agentIscsiFlowAccelerationQosRemark, agentIscsiFlowAccelerationSessionISID=agentIscsiFlowAccelerationSessionISID, agentIscsiFlowAccelerationConnectionInitiatorAddr=agentIscsiFlowAccelerationConnectionInitiatorAddr, agentIscsiFlowAccelerationInitiatorName=agentIscsiFlowAccelerationInitiatorName, agentIscsiFlowAccelerationTargetConfigTable=agentIscsiFlowAccelerationTargetConfigTable, PYSNMP_MODULE_ID=fastPathIscsiFlowAcceleration, agentIscsiFlowAccelerationTargetConfigAddr=agentIscsiFlowAccelerationTargetConfigAddr, agentIscsiFlowAccelerationAgingTimeOut=agentIscsiFlowAccelerationAgingTimeOut, agentIscsiFlowAccelerationConnectionEntry=agentIscsiFlowAccelerationConnectionEntry, agentIscsiFlowAccelerationSessionTable=agentIscsiFlowAccelerationSessionTable, agentIscsiFlowAccelerationConnectionTargetAddr=agentIscsiFlowAccelerationConnectionTargetAddr, agentIscsiFlowAccelerationTargetConfigStatus=agentIscsiFlowAccelerationTargetConfigStatus, agentIscsiFlowAccelerationConnectionInitiatorPort=agentIscsiFlowAccelerationConnectionInitiatorPort, agentIscsiFlowAccelerationQosDscpValue=agentIscsiFlowAccelerationQosDscpValue, agentIscsiFlowAccelerationTargetName=agentIscsiFlowAccelerationTargetName, agentIscsiFlowAccelerationSessionEntry=agentIscsiFlowAccelerationSessionEntry, agentIscsiFlowAccelerationGlobalConfigGroup=agentIscsiFlowAccelerationGlobalConfigGroup, agentIscsiFlowAccelerationTargetConfigEntry=agentIscsiFlowAccelerationTargetConfigEntry, agentIscsiFlowAccelerationTargetConfigTcpPort=agentIscsiFlowAccelerationTargetConfigTcpPort, agentIscsiFlowAccelerationQosType=agentIscsiFlowAccelerationQosType, agentIscsiFlowAccelerationConnectionSessionIndex=agentIscsiFlowAccelerationConnectionSessionIndex, agentIscsiFlowAccelerationSessionUpTime=agentIscsiFlowAccelerationSessionUpTime, agentIscsiFlowAccelerationQosVptValue=agentIscsiFlowAccelerationQosVptValue, agentIscsiFlowAccelerationEnable=agentIscsiFlowAccelerationEnable, agentIscsiFlowAccelerationConnectionCID=agentIscsiFlowAccelerationConnectionCID, agentIscsiFlowAccelerationSessAgingTime=agentIscsiFlowAccelerationSessAgingTime, agentIscsiFlowAccelerationConnectionTable=agentIscsiFlowAccelerationConnectionTable, agentIscsiFlowAccelerationConnectionIndex=agentIscsiFlowAccelerationConnectionIndex, agentIscsiFlowAccelerationConnectionTargetPort=agentIscsiFlowAccelerationConnectionTargetPort, agentIscsiFlowAccelerationTargetConfigName=agentIscsiFlowAccelerationTargetConfigName, fastPathIscsiFlowAcceleration=fastPathIscsiFlowAcceleration, agentIscsiFlowAccelerationSessionIndex=agentIscsiFlowAccelerationSessionIndex)