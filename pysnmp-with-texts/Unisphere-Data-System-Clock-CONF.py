#
# PySNMP MIB module Unisphere-Data-System-Clock-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-System-Clock-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:33:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, NotificationType, Counter64, MibIdentifier, Integer32, iso, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter64", "MibIdentifier", "Integer32", "iso", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter32", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdNtpPeersGroup, usdNtpAccessGroupGroup, usdNtpServerGroup, usdNtpClientGroup, usdNtpSysClockGroup, usdSysClockDstGroup, usdSysClockTimeGroup = mibBuilder.importSymbols("Unisphere-Data-System-Clock-MIB", "usdNtpPeersGroup", "usdNtpAccessGroupGroup", "usdNtpServerGroup", "usdNtpClientGroup", "usdNtpSysClockGroup", "usdSysClockDstGroup", "usdSysClockTimeGroup")
usdSysClockAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52))
usdSysClockAgent.setRevisions(('2002-04-04 18:47',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdSysClockAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdSysClockAgent.setLastUpdated('200204041847Z')
if mibBuilder.loadTexts: usdSysClockAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdSysClockAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdSysClockAgent.setDescription('The agent capabilities definitions for the system clock component of the SNMP agent in the Unisphere Routing Switch family of products.')
usdSysClockAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 52, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSysClockAgentV1 = usdSysClockAgentV1.setProductRelease('Version 1 of the system clock component of the Unisphere Routing Switch\n        SNMP agent.  This version of the system clock component is supported in\n        the Unisphere RX 4.0 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSysClockAgentV1 = usdSysClockAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdSysClockAgentV1.setDescription('The MIB supported by the SNMP agent for the system clock application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-System-Clock-CONF", usdSysClockAgentV1=usdSysClockAgentV1, usdSysClockAgent=usdSysClockAgent, PYSNMP_MODULE_ID=usdSysClockAgent)
