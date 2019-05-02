#
# PySNMP MIB module Unisphere-Data-Interfaces-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-Interfaces-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:31:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ifStackGroup2, ifVHCPacketGroup, ifCounterDiscontinuityGroup, linkUpDownNotificationsGroup, ifGeneralInformationGroup, ifFixedLengthGroup, ifAlias, ifPacketGroup, ifHCFixedLengthGroup, ifStackStatus, ifHCPacketGroup = mibBuilder.importSymbols("IF-MIB", "ifStackGroup2", "ifVHCPacketGroup", "ifCounterDiscontinuityGroup", "linkUpDownNotificationsGroup", "ifGeneralInformationGroup", "ifFixedLengthGroup", "ifAlias", "ifPacketGroup", "ifHCFixedLengthGroup", "ifStackStatus", "ifHCPacketGroup")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Gauge32, ModuleIdentity, Unsigned32, Counter32, Bits, MibIdentifier, TimeTicks, ObjectIdentity, iso, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Gauge32", "ModuleIdentity", "Unsigned32", "Counter32", "Bits", "MibIdentifier", "TimeTicks", "ObjectIdentity", "iso", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdIfInvStackGroup, usdIfGroup = mibBuilder.importSymbols("Unisphere-Data-IF-MIB", "usdIfInvStackGroup", "usdIfGroup")
usdInterfacesAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20))
usdInterfacesAgent.setRevisions(('2001-04-27 14:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdInterfacesAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdInterfacesAgent.setLastUpdated('200104271424Z')
if mibBuilder.loadTexts: usdInterfacesAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdInterfacesAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdInterfacesAgent.setDescription('The agent capabilities definitions for the Interfaces component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdInterfacesAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 20, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInterfacesAgentV1 = usdInterfacesAgentV1.setProductRelease('Version 1 of the Interfaces component of the Unisphere Routing Switch\n        SNMP agent.  This version of the Interfaces component is supported in\n        the Unisphere RX 1.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdInterfacesAgentV1 = usdInterfacesAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdInterfacesAgentV1.setDescription('The MIBs supported by the SNMP agent for the Interfaces application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-Interfaces-CONF", PYSNMP_MODULE_ID=usdInterfacesAgent, usdInterfacesAgentV1=usdInterfacesAgentV1, usdInterfacesAgent=usdInterfacesAgent)
