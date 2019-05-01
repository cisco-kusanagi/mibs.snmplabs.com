#
# PySNMP MIB module Unisphere-Data-CLI-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-CLI-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:30:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Counter64, Integer32, IpAddress, ModuleIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Unsigned32, Bits, ObjectIdentity, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Unsigned32", "Bits", "ObjectIdentity", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdCliSecurityAlertGroup, usdCliSecurityTrapGroup, usdCliGroup = mibBuilder.importSymbols("Unisphere-Data-CLI-MIB", "usdCliSecurityAlertGroup", "usdCliSecurityTrapGroup", "usdCliGroup")
usdCliAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6))
usdCliAgent.setRevisions(('2001-03-27 22:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdCliAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdCliAgent.setLastUpdated('200103272230Z')
if mibBuilder.loadTexts: usdCliAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdCliAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdCliAgent.setDescription('The agent capabilities definitions for the CLI Security Management component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdCliAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 6, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliAgentV1 = usdCliAgentV1.setProductRelease('Version 1 of the CLI Security Management component of the Unisphere\n        Routing Switch SNMP agent.  This version of the CLI Security Management\n        component is supported in the Unisphere RX 1.3 and subsequent system\n        releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCliAgentV1 = usdCliAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdCliAgentV1.setDescription('The MIB supported by the SNMP agent for the CLI Security Management application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-CLI-CONF", usdCliAgentV1=usdCliAgentV1, PYSNMP_MODULE_ID=usdCliAgent, usdCliAgent=usdCliAgent)
