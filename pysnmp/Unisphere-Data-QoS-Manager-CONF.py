#
# PySNMP MIB module Unisphere-Data-QoS-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-QoS-Manager-CONF
# Produced by pysmi-0.3.4 at Mon Apr 29 21:25:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ModuleIdentity, NotificationType, Counter32, IpAddress, Bits, TimeTicks, ObjectIdentity, MibIdentifier, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "Counter32", "IpAddress", "Bits", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdQosTrafficClassGroupListGroup, usdQosCapabilityGroup, usdQosProfileListGroup, usdQosQueueProfileListGroup, usdQosIfAttachGroup, usdQosSchedulerProfileListGroup, usdQosQosPortTypeProfileGroup, usdQosQueueStatisticsGroup, usdQosScalarGroup, usdQosTrafficClassListGroup, usdQosProfileElementGroup = mibBuilder.importSymbols("Unisphere-Data-QoS-MIB", "usdQosTrafficClassGroupListGroup", "usdQosCapabilityGroup", "usdQosProfileListGroup", "usdQosQueueProfileListGroup", "usdQosIfAttachGroup", "usdQosSchedulerProfileListGroup", "usdQosQosPortTypeProfileGroup", "usdQosQueueStatisticsGroup", "usdQosScalarGroup", "usdQosTrafficClassListGroup", "usdQosProfileElementGroup")
usdQosManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50))
usdQosManagerAgent.setRevisions(('2001-12-06 16:09',))
if mibBuilder.loadTexts: usdQosManagerAgent.setLastUpdated('200112061609Z')
if mibBuilder.loadTexts: usdQosManagerAgent.setOrganization('Unisphere Networks, Inc.')
usdQosManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdQosManagerAgentV1 = usdQosManagerAgentV1.setProductRelease('Version 1 of the QoS Manager component of the Unisphere Routing Switch\n        SNMP agent.  This version of the QoS Manager component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdQosManagerAgentV1 = usdQosManagerAgentV1.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-QoS-Manager-CONF", usdQosManagerAgent=usdQosManagerAgent, PYSNMP_MODULE_ID=usdQosManagerAgent, usdQosManagerAgentV1=usdQosManagerAgentV1)
