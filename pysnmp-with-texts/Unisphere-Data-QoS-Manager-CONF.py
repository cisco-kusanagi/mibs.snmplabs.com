#
# PySNMP MIB module Unisphere-Data-QoS-Manager-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-QoS-Manager-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Bits, ObjectIdentity, Integer32, NotificationType, TimeTicks, MibIdentifier, Gauge32, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Bits", "ObjectIdentity", "Integer32", "NotificationType", "TimeTicks", "MibIdentifier", "Gauge32", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdQosIfAttachGroup, usdQosQosPortTypeProfileGroup, usdQosQueueProfileListGroup, usdQosScalarGroup, usdQosQueueStatisticsGroup, usdQosTrafficClassListGroup, usdQosProfileElementGroup, usdQosTrafficClassGroupListGroup, usdQosSchedulerProfileListGroup, usdQosProfileListGroup, usdQosCapabilityGroup = mibBuilder.importSymbols("Unisphere-Data-QoS-MIB", "usdQosIfAttachGroup", "usdQosQosPortTypeProfileGroup", "usdQosQueueProfileListGroup", "usdQosScalarGroup", "usdQosQueueStatisticsGroup", "usdQosTrafficClassListGroup", "usdQosProfileElementGroup", "usdQosTrafficClassGroupListGroup", "usdQosSchedulerProfileListGroup", "usdQosProfileListGroup", "usdQosCapabilityGroup")
usdQosManagerAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50))
usdQosManagerAgent.setRevisions(('2001-12-06 16:09',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdQosManagerAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdQosManagerAgent.setLastUpdated('200112061609Z')
if mibBuilder.loadTexts: usdQosManagerAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdQosManagerAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdQosManagerAgent.setDescription('The agent capabilities definitions for the Quality of Service (QoS) Manager component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdQosManagerAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 50, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdQosManagerAgentV1 = usdQosManagerAgentV1.setProductRelease('Version 1 of the QoS Manager component of the Unisphere Routing Switch\n        SNMP agent.  This version of the QoS Manager component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdQosManagerAgentV1 = usdQosManagerAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdQosManagerAgentV1.setDescription('The MIB supported by the SNMP agent for the QoS Manager application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-QoS-Manager-CONF", usdQosManagerAgent=usdQosManagerAgent, usdQosManagerAgentV1=usdQosManagerAgentV1, PYSNMP_MODULE_ID=usdQosManagerAgent)
