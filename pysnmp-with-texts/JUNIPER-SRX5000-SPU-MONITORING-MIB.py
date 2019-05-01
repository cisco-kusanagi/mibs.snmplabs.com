#
# PySNMP MIB module JUNIPER-SRX5000-SPU-MONITORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SRX5000-SPU-MONITORING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
jnxJsSPUMonitoringRoot, = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsSPUMonitoringRoot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, MibIdentifier, NotificationType, Bits, ModuleIdentity, TimeTicks, Counter32, ObjectIdentity, Gauge32, IpAddress, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "MibIdentifier", "NotificationType", "Bits", "ModuleIdentity", "TimeTicks", "Counter32", "ObjectIdentity", "Gauge32", "IpAddress", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxJsSPUMonitoringMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1))
jnxJsSPUMonitoringMIB.setRevisions(('2012-07-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxJsSPUMonitoringMIB.setRevisionsDescriptions(('add MIB for session counters of IPv4 and IPv6 respectively.',))
if mibBuilder.loadTexts: jnxJsSPUMonitoringMIB.setLastUpdated('201003250000Z')
if mibBuilder.loadTexts: jnxJsSPUMonitoringMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxJsSPUMonitoringMIB.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxJsSPUMonitoringMIB.setDescription("This is Juniper Networks' implementation of enterprise specific MIB for SRX5000 SPU monitoring.")
jnxJsSPUMonitoringObjectsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1), )
if mibBuilder.loadTexts: jnxJsSPUMonitoringObjectsTable.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringObjectsTable.setDescription('This table exposes SPUs utilization statistics.')
jnxJsSPUMonitoringObjectsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1), ).setIndexNames((0, "JUNIPER-SRX5000-SPU-MONITORING-MIB", "jnxJsSPUMonitoringIndex"))
if mibBuilder.loadTexts: jnxJsSPUMonitoringObjectsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringObjectsEntry.setDescription('Each entry collects CPU/Memory utilization for a SPU.')
jnxJsSPUMonitoringIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxJsSPUMonitoringIndex.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringIndex.setDescription("SPU's overall index in platform.")
jnxJsSPUMonitoringFPCIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringFPCIndex.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringFPCIndex.setDescription('Which FPC SPU is on.')
jnxJsSPUMonitoringSPUIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringSPUIndex.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringSPUIndex.setDescription("SPU'Index inside the FPC.")
jnxJsSPUMonitoringCPUUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 4), Unsigned32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringCPUUsage.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringCPUUsage.setDescription('Current SPU(CPU) Utilization in percentage.')
jnxJsSPUMonitoringMemoryUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 5), Unsigned32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringMemoryUsage.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringMemoryUsage.setDescription('Current memory usage of SPU(CPU) in percentage.')
jnxJsSPUMonitoringCurrentFlowSession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringCurrentFlowSession.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringCurrentFlowSession.setDescription('Current flow session number of SPU.')
jnxJsSPUMonitoringMaxFlowSession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringMaxFlowSession.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringMaxFlowSession.setDescription('Max flow session number of SPU.')
jnxJsSPUMonitoringCurrentCPSession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringCurrentCPSession.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringCurrentCPSession.setDescription('Current CP session number of SPU.')
jnxJsSPUMonitoringMaxCPSession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringMaxCPSession.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringMaxCPSession.setDescription('Max CP session number of SPU.')
jnxJsSPUMonitoringNodeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringNodeIndex.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringNodeIndex.setDescription('This attribute is used to identify a chassis. A chassis can be configured in a single or cluster mode. When it is in a cluster mode, the chassis can be denote as a cluster node.')
jnxJsSPUMonitoringNodeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringNodeDescr.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringNodeDescr.setDescription('This attribute is used to describe the chassis/cluster node information. Chassis can be configured as a single, or cluster node. When it is cluster mode, the chassis can be denoted as a cluster node.')
jnxJsSPUMonitoringFlowSessIPv4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringFlowSessIPv4.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringFlowSessIPv4.setDescription('Current IPv4 flow session number of SPU.')
jnxJsSPUMonitoringFlowSessIPv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringFlowSessIPv6.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringFlowSessIPv6.setDescription('Current IPv6 flow session number of SPU.')
jnxJsSPUMonitoringCPSessIPv4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringCPSessIPv4.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringCPSessIPv4.setDescription('Current IPv4 CP session number of SPU.')
jnxJsSPUMonitoringCPSessIPv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringCPSessIPv6.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringCPSessIPv6.setDescription('Current IPv6 CP session number of SPU.')
jnxJsSPUMonitoringCurrentTotalSession = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringCurrentTotalSession.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringCurrentTotalSession.setDescription('System level total session in use.')
jnxJsSPUMonitoringMaxTotalSession = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringMaxTotalSession.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringMaxTotalSession.setDescription('System level max session possible.')
jnxSPUClusterObjectsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4), )
if mibBuilder.loadTexts: jnxSPUClusterObjectsTable.setStatus('current')
if mibBuilder.loadTexts: jnxSPUClusterObjectsTable.setDescription('This table exposes SPU monitoring objects in HA cluster.')
jnxSPUClusterObjectsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1), ).setIndexNames((0, "JUNIPER-SRX5000-SPU-MONITORING-MIB", "jnxJsClusterMonitoringNodeIndex"))
if mibBuilder.loadTexts: jnxSPUClusterObjectsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxSPUClusterObjectsEntry.setDescription('Each entry collects SPU monitoring contents in HA cluster.')
jnxJsClusterMonitoringNodeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxJsClusterMonitoringNodeIndex.setStatus('current')
if mibBuilder.loadTexts: jnxJsClusterMonitoringNodeIndex.setDescription('This attribute is used to identify a chassis. A chassis can be configured in a single or cluster mode. When it is in a cluster mode, the chassis can be denote as a cluster node.')
jnxJsClusterMonitoringNodeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsClusterMonitoringNodeDescr.setStatus('current')
if mibBuilder.loadTexts: jnxJsClusterMonitoringNodeDescr.setDescription('This attribute is used to describe the chassis/cluster node information. Chassis can be configured as a single, or cluster node. When it is cluster mode, the chassis can be denoted as a cluster node.')
jnxJsNodeCurrentTotalSession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNodeCurrentTotalSession.setStatus('current')
if mibBuilder.loadTexts: jnxJsNodeCurrentTotalSession.setDescription('Node total session in use.')
jnxJsNodeMaxTotalSession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNodeMaxTotalSession.setStatus('current')
if mibBuilder.loadTexts: jnxJsNodeMaxTotalSession.setDescription('Node max session possible.')
jnxJsNodeSessionCreationPerSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 5), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNodeSessionCreationPerSecond.setStatus('current')
if mibBuilder.loadTexts: jnxJsNodeSessionCreationPerSecond.setDescription('Node average session created in last 96 seconds.')
jnxJsNodeSessCreationPerSecIPv4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 6), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNodeSessCreationPerSecIPv4.setStatus('current')
if mibBuilder.loadTexts: jnxJsNodeSessCreationPerSecIPv4.setDescription('Node average IPv4 session created in last 96 seconds.')
jnxJsNodeSessCreationPerSecIPv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 7), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNodeSessCreationPerSecIPv6.setStatus('current')
if mibBuilder.loadTexts: jnxJsNodeSessCreationPerSecIPv6.setDescription('Node average IPv6 session created in last 96 seconds.')
jnxJsNodeCurrentTotalSessIPv4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNodeCurrentTotalSessIPv4.setStatus('current')
if mibBuilder.loadTexts: jnxJsNodeCurrentTotalSessIPv4.setDescription('Node total IPv4 session in use.')
jnxJsNodeCurrentTotalSessIPv6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsNodeCurrentTotalSessIPv6.setStatus('current')
if mibBuilder.loadTexts: jnxJsNodeCurrentTotalSessIPv6.setDescription('Node total IPv6 session in use.')
jnxJsSPUMonitoringTotalSessIPv4 = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringTotalSessIPv4.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringTotalSessIPv4.setDescription('System level total IPv4 session in use.')
jnxJsSPUMonitoringTotalSessIPv6 = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsSPUMonitoringTotalSessIPv6.setStatus('current')
if mibBuilder.loadTexts: jnxJsSPUMonitoringTotalSessIPv6.setDescription('System level total IPv6 session in use.')
mibBuilder.exportSymbols("JUNIPER-SRX5000-SPU-MONITORING-MIB", PYSNMP_MODULE_ID=jnxJsSPUMonitoringMIB, jnxSPUClusterObjectsTable=jnxSPUClusterObjectsTable, jnxJsNodeCurrentTotalSession=jnxJsNodeCurrentTotalSession, jnxJsSPUMonitoringMaxTotalSession=jnxJsSPUMonitoringMaxTotalSession, jnxJsNodeMaxTotalSession=jnxJsNodeMaxTotalSession, jnxJsClusterMonitoringNodeIndex=jnxJsClusterMonitoringNodeIndex, jnxJsSPUMonitoringCurrentCPSession=jnxJsSPUMonitoringCurrentCPSession, jnxJsSPUMonitoringNodeDescr=jnxJsSPUMonitoringNodeDescr, jnxJsNodeCurrentTotalSessIPv4=jnxJsNodeCurrentTotalSessIPv4, jnxJsSPUMonitoringNodeIndex=jnxJsSPUMonitoringNodeIndex, jnxJsSPUMonitoringCurrentTotalSession=jnxJsSPUMonitoringCurrentTotalSession, jnxJsSPUMonitoringObjectsEntry=jnxJsSPUMonitoringObjectsEntry, jnxJsSPUMonitoringFlowSessIPv6=jnxJsSPUMonitoringFlowSessIPv6, jnxJsSPUMonitoringMemoryUsage=jnxJsSPUMonitoringMemoryUsage, jnxJsNodeCurrentTotalSessIPv6=jnxJsNodeCurrentTotalSessIPv6, jnxJsSPUMonitoringFlowSessIPv4=jnxJsSPUMonitoringFlowSessIPv4, jnxJsSPUMonitoringIndex=jnxJsSPUMonitoringIndex, jnxJsClusterMonitoringNodeDescr=jnxJsClusterMonitoringNodeDescr, jnxJsNodeSessionCreationPerSecond=jnxJsNodeSessionCreationPerSecond, jnxJsSPUMonitoringTotalSessIPv6=jnxJsSPUMonitoringTotalSessIPv6, jnxJsSPUMonitoringFPCIndex=jnxJsSPUMonitoringFPCIndex, jnxJsSPUMonitoringMaxFlowSession=jnxJsSPUMonitoringMaxFlowSession, jnxSPUClusterObjectsEntry=jnxSPUClusterObjectsEntry, jnxJsNodeSessCreationPerSecIPv6=jnxJsNodeSessCreationPerSecIPv6, jnxJsSPUMonitoringCPSessIPv6=jnxJsSPUMonitoringCPSessIPv6, jnxJsSPUMonitoringTotalSessIPv4=jnxJsSPUMonitoringTotalSessIPv4, jnxJsSPUMonitoringSPUIndex=jnxJsSPUMonitoringSPUIndex, jnxJsNodeSessCreationPerSecIPv4=jnxJsNodeSessCreationPerSecIPv4, jnxJsSPUMonitoringObjectsTable=jnxJsSPUMonitoringObjectsTable, jnxJsSPUMonitoringCPUUsage=jnxJsSPUMonitoringCPUUsage, jnxJsSPUMonitoringMIB=jnxJsSPUMonitoringMIB, jnxJsSPUMonitoringCurrentFlowSession=jnxJsSPUMonitoringCurrentFlowSession, jnxJsSPUMonitoringMaxCPSession=jnxJsSPUMonitoringMaxCPSession, jnxJsSPUMonitoringCPSessIPv4=jnxJsSPUMonitoringCPSessIPv4)