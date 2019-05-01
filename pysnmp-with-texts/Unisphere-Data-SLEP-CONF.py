#
# PySNMP MIB module Unisphere-Data-SLEP-CONF (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-SLEP-CONF
# Produced by pysmi-0.3.4 at Wed May  1 15:32:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Bits, Counter64, IpAddress, MibIdentifier, Counter32, ModuleIdentity, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Bits", "Counter64", "IpAddress", "MibIdentifier", "Counter32", "ModuleIdentity", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataAgents, = mibBuilder.importSymbols("Unisphere-Data-Agents", "usDataAgents")
usdSlepGroup, = mibBuilder.importSymbols("Unisphere-Data-SLEP-MIB", "usdSlepGroup")
usdSlepAgent = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38))
usdSlepAgent.setRevisions(('2001-03-30 14:15',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: usdSlepAgent.setRevisionsDescriptions(('The initial release of this management information module.',))
if mibBuilder.loadTexts: usdSlepAgent.setLastUpdated('200103301415Z')
if mibBuilder.loadTexts: usdSlepAgent.setOrganization('Unisphere Networks, Inc.')
if mibBuilder.loadTexts: usdSlepAgent.setContactInfo(' Unisphere Networks, Inc. Postal: 10 Technology Park Drive Westford, MA 01886 USA Tel: +1 978 589 5800 E-mail: mib@UnisphereNetworks.com')
if mibBuilder.loadTexts: usdSlepAgent.setDescription('The agent capabilities definitions for the Serial Line Encapsulation Protocol (SLEP) component of the SNMP agent in the Unisphere Data Routing Switch family of products.')
usdSlepAgentV1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 4874, 5, 2, 38, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSlepAgentV1 = usdSlepAgentV1.setProductRelease('Version 1 of the SLEP component of the Unisphere Routing Switch SNMP\n        agent.  This version of the SLEP component is supported in the Unisphere\n        RX 1.3 and subsequent system releases.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdSlepAgentV1 = usdSlepAgentV1.setStatus('current')
if mibBuilder.loadTexts: usdSlepAgentV1.setDescription('The MIB supported by the SNMP agent for the SLEP application in the Unisphere Routing Switch.')
mibBuilder.exportSymbols("Unisphere-Data-SLEP-CONF", usdSlepAgentV1=usdSlepAgentV1, usdSlepAgent=usdSlepAgent, PYSNMP_MODULE_ID=usdSlepAgent)
